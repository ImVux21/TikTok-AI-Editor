"""Make a pitch-preserving 1.2x narration track before CapCut import.

Use only when the CapCut draft path cannot confirm pitch-preserving speed. The
new file must be imported at normal speed; this command never edits its input.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from pathlib import Path


RATE = 1.2


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def probe_duration(ffprobe: str, path: Path) -> float:
    completed = subprocess.run(
        [ffprobe, "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        capture_output=True, text=True, check=True,
    )
    return float(completed.stdout.strip())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="Reviewed original narration audio")
    parser.add_argument("--output", type=Path, required=True, help="New .m4a file for CapCut import")
    parser.add_argument("--ffmpeg", default=shutil.which("ffmpeg") or "ffmpeg")
    parser.add_argument("--ffprobe", default=shutil.which("ffprobe") or "ffprobe")
    args = parser.parse_args()

    source, target = args.input.resolve(), args.output.resolve()
    meta = target.with_suffix(target.suffix + ".speed.json")
    if not source.is_file():
        parser.error(f"Input is missing: {source}")
    if source == target:
        parser.error("Output must differ from input")
    if target.suffix.lower() != ".m4a":
        parser.error("Output must be an .m4a file")
    if target.exists() or meta.exists():
        parser.error("Output or its metadata already exists; choose a fresh filename")
    if source.with_suffix(source.suffix + ".speed.json").exists():
        parser.error("Input already has speed metadata; refusing to speed it twice")
    try:
        source_duration = probe_duration(args.ffprobe, source)
        target.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run([
            args.ffmpeg, "-hide_banner", "-loglevel", "error", "-n", "-i", str(source),
            "-vn", "-af", f"atempo={RATE}", "-c:a", "aac", "-b:a", "192k", str(target),
        ], check=True)
        target_duration = probe_duration(args.ffprobe, target)
    except (FileNotFoundError, subprocess.CalledProcessError, ValueError) as exc:
        if target.exists():
            target.unlink()
        parser.error(f"Audio processing failed: {exc}")

    expected = source_duration / RATE
    if abs(target_duration - expected) > max(0.15, expected * 0.02):
        target.unlink()
        parser.error("Output duration does not match 1.2x playback within tolerance")
    metadata = {
        "source": str(source), "source_sha256": sha256(source),
        "output": str(target), "output_sha256": sha256(target),
        "source_duration_seconds": source_duration,
        "output_duration_seconds": target_duration,
        "target_speed": RATE, "applied_speed": RATE,
        "method": "ffmpeg_atempo_pitch_preserving",
        "capcut_import_speed": 1.0,
        "listening_qa": "pending",
        "caption_alignment": "pending_on_this_output",
    }
    meta.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Created {target}\nMetadata {meta}\nImport in CapCut at speed 1.0 and listen before use.")


if __name__ == "__main__":
    main()
