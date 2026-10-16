"""Assemble one configured short-form video from project.json with FFmpeg."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


def filter_path(path: Path) -> str:
    """Escape a filesystem path for FFmpeg's subtitles/ASS filter argument."""
    value = path.resolve().as_posix()
    return value.replace("\\", "\\\\").replace(":", r"\:").replace("'", r"\'")


def resolve_asset(value: str, project_root: Path, workspace_root: Path) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    local = project_root / path
    if local.is_file():
        return local
    shared = workspace_root / path
    return shared if shared.is_file() else local


def frame_pair(segment: dict, key: str) -> tuple[int, int] | None:
    if key not in segment:
        return None
    bounds = segment[key]
    if (not isinstance(bounds, list) or len(bounds) != 2
            or any(isinstance(v, bool) or not isinstance(v, int) for v in bounds)
            or bounds[0] < 0 or bounds[1] <= bounds[0]):
        raise ValueError(f"Invalid {key} frame interval")
    return bounds[0], bounds[1]


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the configured short-form video.")
    parser.add_argument("--project", type=Path, required=True, help="Path to the selected video's project.json")
    parser.add_argument("--output", type=Path, help="Optional output path, relative to the project unless absolute")
    parser.add_argument("--ffmpeg", help="FFmpeg executable; defaults to PATH or FFMPEG_BINARY")
    parser.add_argument("--no-captions", action="store_true", help="Do not burn the configured ASS captions.")
    args = parser.parse_args()

    project_file = args.project.resolve()
    root = project_file.parent
    workspace_root = next((p for p in project_file.parents if (p / "workflow").is_dir()), root)
    config = json.loads(project_file.read_text(encoding="utf-8-sig"))
    timeline = config["timeline"]
    segments = timeline["segments"]
    if not segments:
        parser.error("project.json must contain at least one timeline segment")

    voiceover = config.get("assets", {}).get("voiceover") or timeline.get("voiceover_source")
    if not voiceover:
        parser.error("project.json must name assets.voiceover or timeline.voiceover_source")
    branding = config.get("branding") or timeline.get("shop_branding")
    if branding and branding.get("shape") != "circle":
        parser.error("branding.shape must be circle")

    output_value = str(args.output) if args.output else config["output"]["video"]
    output_video = Path(output_value)
    if not output_video.is_absolute():
        output_video = root / output_video
    output_video.parent.mkdir(parents=True, exist_ok=True)
    captions_value = config["output"].get("captions_ass")
    captions = resolve_asset(captions_value, root, workspace_root) if captions_value else None

    fmt = config.get("format", {})
    width, height = int(fmt.get("width", 720)), int(fmt.get("height", 1280))
    fps = float(fmt.get("fps", 24))
    if width <= 0 or height <= 0 or fps <= 0:
        parser.error("format width, height, and fps must be positive")
    inputs = [resolve_asset(s.get("source") or s.get("file"), root, workspace_root) for s in segments]
    voice_path = resolve_asset(voiceover, root, workspace_root)
    brand_source = (branding.get("source") or branding.get("source_image")) if branding else None
    if branding and not brand_source:
        parser.error("branding needs source or source_image")
    brand_path = resolve_asset(brand_source, root, workspace_root) if brand_source else None
    for path in [*inputs, voice_path, *([brand_path] if brand_path else [])]:
        if not path.is_file():
            parser.error(f"Missing input file: {path}")
    if output_video.resolve() in {p.resolve() for p in [*inputs, voice_path, *([brand_path] if brand_path else [])]}:
        parser.error("Output video path must differ from all input assets")

    try:
        source_frames = [frame_pair(s, "source_frames") for s in segments]
        timeline_frames = [frame_pair(s, "timeline_frames") for s in segments]
    except ValueError as exc:
        parser.error(str(exc))
    source_intervals: list[tuple[float, float]] = []
    timeline_intervals: list[tuple[float, float]] = []
    expected_start = 0.0
    for segment, source_pair, timeline_pair in zip(segments, source_frames, timeline_frames):
        source_fps = float(segment.get("source_fps", timeline.get("source_fps", fps)))
        if source_fps <= 0:
            parser.error("source_fps must be positive")
        if source_pair:
            source_start, source_length = source_pair[0] / source_fps, (source_pair[1] - source_pair[0]) / source_fps
        else:
            source_start = float(segment.get("source_start", 0))
            source_length = float(segment.get("source_duration", float(segment.get("duration", 0)) * float(segment.get("playback_rate", 1.0))))
            if source_start < 0 or source_length <= 0:
                parser.error("Legacy segments need nonnegative source_start and positive source_duration or duration")
        source_intervals.append((source_start, source_length))
        if timeline_pair:
            start, length = timeline_pair[0] / fps, (timeline_pair[1] - timeline_pair[0]) / fps
        else:
            start, length = float(segment.get("timeline_start", expected_start)), float(segment.get("duration", source_length / float(segment.get("playback_rate", 1.0))))
        if length <= 0 or abs(start - expected_start) > 1e-6:
            parser.error("Timeline segments must be contiguous and ordered")
        playback_rate = float(segment.get("playback_rate", 1.0))
        if playback_rate <= 0 or abs(source_length / playback_rate - length) > 0.5 / fps:
            parser.error("Segment source length, playback_rate, and timeline length disagree")
        timeline_intervals.append((start, length))
        expected_start = start + length
    duration = float(timeline.get("voiceover_duration") or expected_start)
    if abs(duration - expected_start) > 0.5 / fps:
        parser.error("voiceover_duration must match the contiguous visual timeline")
    if not args.no_captions and captions_value and not captions.is_file():
        parser.error(f"Configured captions file is missing: {captions}")

    ffmpeg = args.ffmpeg or shutil.which("ffmpeg")
    if not ffmpeg:
        parser.error("FFmpeg was not found. Add it to PATH or pass --ffmpeg.")
    command = [ffmpeg, "-hide_banner", "-y", "-loglevel", "warning"]
    for path in inputs:
        command.extend(["-i", str(path)])
    command.extend(["-i", str(voice_path)])
    if brand_path:
        command.extend(["-loop", "1", "-framerate", str(fps), "-i", str(brand_path)])

    filters: list[str] = []
    for index, (segment, (start, source_length)) in enumerate(zip(segments, source_intervals)):
        playback_rate = float(segment.get("playback_rate", 1.0))
        if playback_rate <= 0:
            parser.error("timeline playback_rate must be greater than zero")
        retime = f",setpts=PTS/{playback_rate}" if playback_rate != 1.0 else ""
        trim = (f"trim=start_frame={source_frames[index][0]}:end_frame={source_frames[index][1]}"
                if source_frames[index] else f"trim=start={start}:duration={source_length}")
        filters.append(
            f"[{index}:v]{trim},setpts=PTS-STARTPTS{retime},"
            f"scale={width}:{height}:force_original_aspect_ratio=increase,crop={width}:{height},"
            f"fps={fps},setsar=1[v{index}]"
        )
    concat_inputs = "".join(f"[v{i}]" for i in range(len(segments)))
    filters.append(f"{concat_inputs}concat=n={len(segments)}:v=1:a=0[vbase]")
    if not args.no_captions and captions and captions.is_file():
        filters.append(f"[vbase]ass='{filter_path(captions)}'[vcomposed]")
    else:
        filters.append("[vbase]null[vcomposed]")

    audio_index = len(inputs)
    if branding:
        diameter = int(branding["diameter_px"])
        inset = int(branding.get("mask_inset_px", 0))
        if "center_px" in branding:
            center_x, center_y = map(int, branding["center_px"])
            x, y = center_x - diameter // 2, center_y - diameter // 2
        else:
            x, y = int(branding["x"]), int(branding["y"])
        if diameter < 1 or inset < 0 or inset * 2 >= diameter:
            parser.error("Invalid circular branding diameter or mask inset")
        if x < 0 or y < 0 or x + diameter > width or y + diameter > height:
            parser.error("Circular branding must fit within the video frame")
        center, radius = (diameter - 1) / 2, (diameter - 1) / 2 - inset
        alpha = f"if(lte((X-{center})*(X-{center})+(Y-{center})*(Y-{center}),{radius}*{radius}),255,0)"
        logo_index = audio_index + 1
        filters.extend([
            f"[{logo_index}:v]scale={diameter}:{diameter},format=rgba,split[brandbase][brandmasksrc]",
            f"[brandmasksrc]format=gray,geq=lum='{alpha}'[brandmask]",
            "[brandbase][brandmask]alphamerge[brandlogo]",
            f"[vcomposed][brandlogo]overlay={x}:{y}:format=auto:shortest=1[vout]",
        ])
    else:
        filters.append("[vcomposed]null[vout]")
    filters.append(f"[{audio_index}:a]atrim=duration={duration},asetpts=PTS-STARTPTS[aout]")
    command.extend([
        "-filter_complex", ";".join(filters), "-map", "[vout]", "-map", "[aout]", "-t", str(duration),
        "-c:v", "libx264", "-crf", "19", "-preset", "fast", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(output_video),
    ])
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as exc:
        return exc.returncode or 1
    print(f"Created {output_video}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
