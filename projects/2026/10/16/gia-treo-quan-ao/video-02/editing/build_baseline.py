"""Build the incremental CapCut STDraft from explicitly approved clips."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = Path(r"C:/Users/vuodo/.codex/plugins/cache/CapCut/CapCut/0.2.1/skills/capcut-stdraft-builder/scripts")
sys.path.insert(0, str(SKILL))
from apply_materials import apply_audio, apply_video
from apply_captions import apply_captions

VIDEO1 = "v10b9eg5000cdb8tdofog65k7ofcs2kg"
VIDEO2 = "v10b9eg5000cdb8tdovog65tru1s9rl0"
VOICE = "v10b9eg5000cdb8tdpfog65kkiluo8n0"

draft = {"version": "0.1.0", "segments": [{"id": "draft", "type": "DRAFT", "attributes": {"width": 720, "height": 1280, "ratio_type": "custom"}}]}
first = apply_video(draft, source=f"vid://{VIDEO1}", start_ms=0, duration_ms=3256, source_start_ms=0, volume=0)
second = apply_video(first["draft"], source=f"vid://{VIDEO2}", start_ms=3256, duration_ms=3336, source_start_ms=0, volume=0)
voice = apply_audio(second["draft"], meta_type="SOUND", source=f"vid://{VOICE}", start_ms=0, duration_ms=9211, volume=1)
timing = json.loads((ROOT / "scripts/captions-timed.json").read_text(encoding="utf-8"))
utterances = [{"text": cue["text"], "start_time": cue["start_ms"], "end_time": cue["end_ms"]}
              for cue in timing["cues"] if cue["end_ms"] <= 6592]
captions = apply_captions(
    voice["draft"], [{"vid": VOICE, "utterances": utterances}],
    bindings={VOICE: voice["added_segment_ids"]},
    text_style={"font": "vimo://7317175475195875841", "font_size": 6,
                "alignment": 1, "text_color": "#FFFFFFFF", "border_color": "#000000FF",
                "border_width": 2},
    layout={"position_x": 0, "position_y": -0.62, "scale_x": 1, "scale_y": 1},
)
out = ROOT / "editing/baseline-incremental.json"
out.write_text(json.dumps(captions["draft"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"path": str(out), "segments": len(captions["draft"]["segments"]),
                  "check": captions["check_result"], "warnings": captions["warnings"],
                  "video_ids": [first["added_segment_ids"][0], second["added_segment_ids"][0]],
                  "audio_id": voice["added_segment_ids"][0],
                  "caption_ids": captions["added_segment_ids"]}, ensure_ascii=False))
