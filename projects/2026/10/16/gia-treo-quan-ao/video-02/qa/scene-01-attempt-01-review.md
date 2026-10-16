# Scene 01 Flow clip QA — attempt 01

- Exact file: `input/scene-01-attempt-01.mp4`
- Verified SHA-256: `68BFDCBC86221403D6F8FD3DB7A6E50F166B446445C31C454740DDEE53E7A96E`.
- Source: 720 × 1280, 24 fps, 8.000 s, 192 video frames (indices 0–191).
- References: `input/product-photo-2.jpg`, `input/background-photo-1.jpg`, approved start frame `storyboard/scene-01-v01-raw.png`.
- Frame coverage: every decoded source frame, indices 0–191, reviewed in chronological 24 fps contact sheets `qa/scene-01-frames/sheet-01.jpg` through `sheet-08.jpg`, 24 frames per sheet. Full-resolution decoded frames 0, 48, 96, 144, 191 separately checked.
- Continuous full-clip playback: coordinator played this exact MP4 in @Browser for longer than its 8-second duration and observed a stable rack through a complete cycle, with screenshots at the start and later in the loop. The independent QA reviewer inspected every source frame. These two observations together cover continuous playback and exhaustive frame review; the playback observation is explicitly coordinator-witnessed, not an independent second playback.

## Findings

| Time | Evidence | Severity | Disposition |
|---|---|---|---|
| 0.000–7.958 s | Every source frame shows one black staggered double-rail clothing rack with four upright posts, four side-hook positions, two mid-height side braces, and paired floor feet/lower rails. No extra or missing visible structural member at contact-sheet scale; inspected five full-resolution frames agree with product reference. Camera makes a slow push-in. Coordinator's full-cycle playback also found the rack stable. | None observed | Pass. |
| 0.000–7.958 s | Zero visible people, hands, or fingers in all 192 reviewed frames. | None observed | No anatomy issue observed. |
| 0.000–7.958 s | Tan-over-pale irregular wall, white baseboard, and warm plank floor persist. Old rack and props from room photo remain absent as required. | None observed | Background preliminarily acceptable. |
| 0.000–7.958 s | White diamond Flow/Gemini watermark visible over floor near lower-right foot. Approximate bounding region x=575–626, y=1105–1190 in 720 × 1280 frame, varying slightly with animation; center near (601, 1150). It does not cover the product. | Overlay required later | Do not reject raw clip solely for watermark. Measure precisely again during edit and apply user-supplied circular shop-brand mask; verify final export. |
| 0.000–8.000 s | AAC stereo audio stream exists. FFmpeg `silencedetect` at −35 dB reports one silence interval covering the entire 8.000 s. There is no material sound to listen to in this raw clip; narration will be supplied separately. | None observed | Pass for absence of unintended Flow dialogue. |

## Decision

**PASS for this exact raw source clip.** All 192 source frames were reviewed by QA, and the coordinator witnessed complete continuous playback of the exact file. No product-identity, anatomy, or background defect was found. The raw watermark is recorded for the later circular shop-brand overlay. This pass does not approve any other clip, edited draft, narration track, or final export.
