"""Prepare an offline ElevenLabs narration plan from a creative plan JSON.

This module never calls an API or generates audio. It preserves tagged raw text
for ElevenLabs V3 while producing deterministic clean subtitle text and V2 text.
"""

from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path
from typing import Any, Sequence


VOICE_ID = "pNInz6obpgDQGcFmaJgB"
VOICE_NAME = "Adam - Dominant,Firm"
MODELS = ("eleven_v3", "eleven_multilingual_v2")
FINAL_SCENE_ENDING = re.compile(r"(?:Dứt lẹ|Dứt)!$", re.IGNORECASE)


def strip_square_tags(text: str) -> str:
    """Remove balanced, non-nested square-bracket tag spans from text."""
    output: list[str] = []
    tag_content: list[str] = []
    inside_tag = False

    for character in text:
        if character == "[":
            if inside_tag:
                raise ValueError("square tags must not be nested")
            inside_tag = True
            tag_content = []
        elif character == "]":
            if not inside_tag:
                raise ValueError("closing square bracket has no opening tag")
            if not "".join(tag_content).strip():
                raise ValueError("square tags must not be empty")
            inside_tag = False
            tag_content = []
        elif inside_tag:
            tag_content.append(character)
        else:
            output.append(character)

    if inside_tag:
        raise ValueError("square tag is missing its closing bracket")
    return "".join(output)


def clean_subtitle_text(raw_text: str) -> str:
    """Remove V3 tags and collapse whitespace deterministically for captions."""
    return re.sub(r"\s+", " ", strip_square_tags(raw_text)).strip()


def _validate_scene_text(scene_id: str, raw_text: str) -> str:
    if not isinstance(raw_text, str):
        raise ValueError(f"scene {scene_id!r}: voice text must be a string")
    if any(character.isdigit() for character in raw_text):
        raise ValueError(f"scene {scene_id!r}: voice text must not contain digits")
    try:
        clean_text = clean_subtitle_text(raw_text)
    except ValueError as exc:
        raise ValueError(f"scene {scene_id!r}: {exc}") from exc
    if not clean_text or not any(character.isalpha() for character in clean_text):
        raise ValueError(f"scene {scene_id!r}: clean speech must be nonempty")
    return clean_text


def build_voice_plan(plan: dict[str, Any], model: str) -> dict[str, Any]:
    """Validate and convert a creative plan to a deterministic voice plan."""
    if model not in MODELS:
        raise ValueError(f"model must be one of: {', '.join(MODELS)}")
    scenes = plan.get("scenes")
    if not isinstance(scenes, list) or not scenes:
        raise ValueError("creative plan must contain a nonempty scenes array")

    output_scenes: list[dict[str, str]] = []
    seen_ids: set[str] = set()
    for index, scene in enumerate(scenes):
        if not isinstance(scene, dict):
            raise ValueError(f"scene at index {index} must be an object")
        scene_id_value = scene.get("id")
        if not isinstance(scene_id_value, str) or not scene_id_value.strip():
            raise ValueError(f"scene at index {index} must have a nonempty string id")
        scene_id = scene_id_value.strip()
        if scene_id in seen_ids:
            raise ValueError(f"scene id {scene_id!r} is duplicated")
        seen_ids.add(scene_id)

        source_field = "voiceTextRaw" if "voiceTextRaw" in scene else "voiceText"
        raw_text = scene.get(source_field)
        if not isinstance(raw_text, str):
            raise ValueError(
                f"scene {scene_id!r} must have string voiceTextRaw or legacy voiceText"
            )
        clean_text = _validate_scene_text(scene_id, raw_text)
        tts_text = raw_text if model == "eleven_v3" else clean_text
        output_scenes.append(
            {
                "id": scene_id,
                "sourceField": source_field,
                "voiceTextRaw": raw_text,
                "cleanSubtitleText": clean_text,
                "ttsText": tts_text,
            }
        )

    final_clean_text = output_scenes[-1]["cleanSubtitleText"]
    if not FINAL_SCENE_ENDING.search(final_clean_text):
        raise ValueError("final clean scene must end with 'Dứt!' or 'Dứt lẹ!'")

    full_narration = " ".join(scene["ttsText"].strip() for scene in output_scenes)
    return {
        "model": model,
        "voice_id": VOICE_ID,
        "voice_name": VOICE_NAME,
        "voice_access_verified": False,
        "audio_generated": False,
        "target_speed": 1.2,
        "speed_user_confirmed": True,
        "source_generation_speed": None,
        "source_generation_speed_status": "not_explicitly_configured_by_model_schema",
        "speed_application_stage": "capcut_audio",
        "speed_application_status": "unverified_pending_audio_generation",
        "postprocess": {
            "playback_rate": 1.2,
            "preserve_pitch": True,
            "apply_once": True,
            "status": "planned_not_applied",
        },
        "audio_listening_status": "not_generated",
        "caption_timing_status": "pending_final_audio_alignment",
        "scenes": output_scenes,
        "fullNarration": full_narration,
    }


def clean_alignment(
    characters: Sequence[str],
    character_start_times_seconds: Sequence[float],
    character_end_times_seconds: Sequence[float],
) -> dict[str, Any]:
    """Remove bracket-tag spans from aligned character tokens without retiming.

    Token timestamps are copied unchanged, so gaps around removed tags remain
    intact. The three input arrays must have equal lengths.
    """
    if not (
        len(characters)
        == len(character_start_times_seconds)
        == len(character_end_times_seconds)
    ):
        raise ValueError("alignment character and timestamp arrays must have equal lengths")

    kept_characters: list[str] = []
    kept_starts: list[float] = []
    kept_ends: list[float] = []
    inside_tag = False
    tag_content: list[str] = []

    for index, (token, start, end) in enumerate(
        zip(characters, character_start_times_seconds, character_end_times_seconds)
    ):
        if not isinstance(token, str):
            raise ValueError(f"alignment token at index {index} must be a string")
        if len(token) != 1:
            raise ValueError(
                f"alignment token at index {index} must be one character for accurate timing"
            )
        if isinstance(start, bool) or not isinstance(start, (int, float)) or not math.isfinite(start):
            raise ValueError(f"alignment start time at index {index} must be finite numeric data")
        if isinstance(end, bool) or not isinstance(end, (int, float)) or not math.isfinite(end):
            raise ValueError(f"alignment end time at index {index} must be finite numeric data")
        if start < 0 or end < start:
            raise ValueError(f"alignment timestamps at index {index} are invalid")

        kept_token: list[str] = []
        for character in token:
            if character == "[":
                if inside_tag:
                    raise ValueError("alignment square tags must not be nested")
                inside_tag = True
                tag_content = []
            elif character == "]":
                if not inside_tag:
                    raise ValueError("alignment closing bracket has no opening tag")
                if not "".join(tag_content).strip():
                    raise ValueError("alignment square tags must not be empty")
                inside_tag = False
                tag_content = []
            elif inside_tag:
                tag_content.append(character)
            else:
                kept_token.append(character)

        if kept_token:
            kept_characters.append("".join(kept_token))
            kept_starts.append(start)
            kept_ends.append(end)

    if inside_tag:
        raise ValueError("alignment square tag is missing its closing bracket")
    return {
        "characters": kept_characters,
        "character_start_times_seconds": kept_starts,
        "character_end_times_seconds": kept_ends,
        "text": "".join(kept_characters),
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate and prepare an offline narration plan; does not generate audio."
    )
    parser.add_argument("--plan", required=True, type=Path, help="Creative plan JSON")
    parser.add_argument("--output", required=True, type=Path, help="Voice plan JSON to write")
    parser.add_argument("--model", choices=MODELS, default="eleven_v3")
    args = parser.parse_args()

    try:
        if args.output.resolve() == args.plan.resolve():
            raise ValueError("output must not overwrite the input plan")
        plan = json.loads(args.plan.read_text(encoding="utf-8-sig"))
        if not isinstance(plan, dict):
            raise ValueError("creative plan root must be a JSON object")
        voice_plan = build_voice_plan(plan, args.model)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(
            json.dumps(voice_plan, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        parser.error(str(exc))
    print(f"Prepared narration plan at {args.output}; audio_generated=false")


if __name__ == "__main__":
    main()
