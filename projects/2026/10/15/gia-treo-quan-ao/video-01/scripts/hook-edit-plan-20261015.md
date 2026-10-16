# Baseline assembly plan — hook / video-01

**Current baseline:** `output/hook-baseline-v3.mp4` — 10.00 s, 9:16, 720×1280 at 24 fps. This is an initial post-production baseline for `pro_video_editor`, not a final release. Only QA-approved moving intervals are used; full attempt 08 speech audio is preserved.

## Exact source EDL

All source out points are exclusive. Final sequence is 240 frames exactly at 24 fps.

| Order | Source file | Source in–out | Frames | Final timeline | Purpose / QA basis |
|---|---|---:|---:|---:|---|
| 1 | `output/scene-01-flow-attempt-08.mp4` | 0.000–3.125s | 75 | 0.000–3.125s | Clean front view of empty product; opens with a truthful two-rail hook. QA pass [0.00, 3.15). Source SHA-256 `6DD43145E02849FEE8837422EF7046EBC32A3E738264A1D3A72D41C65D20AD3E`. |
| 2 | `output/scene-01-flow-attempt-03.mp4` | 4.500–6.000s | 36 | 3.125–4.625s | Close insert on side hook/rail detail. QA pass [1.25, 6.00). Source SHA-256 `587376AE1B8F3B60CF457C97F9BE6D242B123C7556940B2D4B4159D5923DA3F4`. |
| 3 | `output/scene-01-flow-attempt-04.mp4` | 0.000–1.500s | 36 | 4.625–6.125s | Moving hanger/product close-up; QA pass [0.00, 3.50). Source SHA-256 `FD67F267927E98C086FAD6F02378A75A027019B09FCEF2CA21673781FB46401B`. |
| 4 | `output/scene-01-flow-attempt-04.mp4` | 3.625–7.500s | 93 | 6.125–10.000s | Moving hanging scene and full product with clothes for the payoff/CTA. QA pass [3.60, 7.50), end before the ceiling appears at 7.75s. |

Attempt 08 intervals [3.15, 5.80) are omitted because the rack/background movement is defective. Attempt 03 material outside [1.25, 6.00) and attempt 04 material outside the two approved windows are omitted. Visual audio from attempts 03/04 is not included. The cut order transitions from the empty product overview to detail, hand action, then the clothed full-rack payoff. No stills or freeze frames are used.

## Audio and caption evidence

- Backbone: full attempt 08 AAC audio, source `output/scene-01-flow-attempt-08.mp4`, 0.000–10.000s. Audio-only ASR handoff: `output/attempt08-flow-audio.m4a` (copied AAC stream, 10.00s, no video; 163,103 bytes). CapCut ASR resource supplied by coordinator: VID `v10b9eg5000cdb87ilfog65s6kmlij5g`.
- Coordinator reports the user approved the attempt 08 voice preview. ASR transcript matches the locked dialogue. This is ASR evidence, **not an independent ear verification** in this assembly runtime; exact Adam selector/preset is not confirmed in the available record.
- Phrase-level ASR intervals and captions (also in `output/subtitles-hook-baseline-v3.srt`):
  - 0.000–2.440s — “Ủa, một giá mà treo được hai tầng luôn á?”
  - 2.440–3.721s — “Thanh trên, thanh dưới—”
  - 3.758–5.201s — “chia đồ ra là thấy ngay.”
  - 5.638–8.841s — “Có nhiều phân loại đó, chọn đúng mẫu trong giỏ nha!”
- These captions are burned into the baseline from phrase-level ASR timing. They are not word-level captions and remain subject to the professional editor's audio review. Caption cues are centered near the top (y=145 px) to avoid covering the hands/product mid-frame; final QA should check against TikTok UI and safe areas. No music was added.

## Shop-brand mask and placement

- Exact source: `workflow/assets/shop-branding.png` (SHA-256 `1C2842957DC74712462734DB6A0DF466FE8F2628A804820A854291154823D090`). The centered logo crop uses source rectangle x=227, y=0, 800×800, then a circular alpha mask.
- Compared candidate diameters 56, 64 and 68 pixels at the 720×1280 composition (phone-size preview scaled to 360×640). Selected **68 px**: shop name is clearest at this size while covering the measured Flow sparkle (about x=574–625, y=1138–1178) with an 8 px margin. Circle center is (600,1158); top-left (566,1124), aligned consistently across all cuts.
- The circle sits over the floor in the lower-right; reviewed output samples show it does not cover the rack or hand action. Final QA should still review it at phone display size with platform UI enabled.

## Output and remaining handoff items

- Baseline: `output/hook-baseline-v3.mp4` (H.264 video, AAC audio, 720×1280, 24 fps, 10.000s; 8,085,946 bytes).
- ASR transcript is not an ear-verification. Coordinator/`pro_video_editor` should listen to the full audio, confirm pronunciation/timing and preset status, then adjust captions if the spoken words differ. Exact Adam preset remains unverified.
- `pro_video_editor` receives this baseline and EDL for pacing/transition refinement. Final export and release QA remain outstanding.
