# Scene 02 Flow clip QA — attempt 01

- Exact file: `input/scene-02-attempt-01.mp4`
- Verified SHA-256: `D3CD8344CFBEA4137ECC8F18224A46B6AB7646607A4D31B805B3C895C5031B02`
- Flow edit ID: `c2081ca3-dae7-40ee-a929-e0bc5055e28b`
- Source: 720 × 1280, 24 fps, 8.000 s, 192 frames, indices 0–191.
- References: `input/product-photo-2.jpg`, `input/background-photo-1.jpg`, QA-passed `storyboard/scene-02-v01.png`.
- Frame coverage: every decoded source frame 0–191 in chronological 24 fps contact sheets `qa/scene-02-frames/sheet-01.jpg` through `sheet-08.jpg`, 24 frames each. Full-resolution decoded frames 0, 48, 96, 144, 191 separately reviewed.
- Continuous playback: coordinator witnessed this exact scene-02 clip play in Flow from 00:00 through a loop past 00:08, observing 00:06:08, 00:07:00 and then 00:02:00 after the loop. Independent QA reviewed all 192 source frames. Playback provenance is coordinator-witnessed.

## Findings

| Time | Evidence | Severity | Disposition |
|---|---|---|---|
| 0.000–7.958 s | One black staggered double-rail rack remains in every frame, with four uprights, side hooks, two mid-height side braces, paired floor feet and lower rails. No extra, missing or fused visible product part in the 192-frame scan. A slow camera move shifts the view toward the room's right side while keeping feet grounded. | None observed | Pass. |
| 0.000–7.958 s | Zero people, hands or fingers in every reviewed frame. | None observed | No anatomy issue. |
| ~4.000–7.958 s | Tan/pale irregular wall boundary, white baseboard and warm plank floor persist. A right wall corner gradually enters as the camera moves. The original room photo does not show beyond its right edge, so the corner is unverified but does not contradict visible source geometry or introduce a prop. No old rack or props reappear. | Minor continuity uncertainty; no material defect | Pass for source clip; preserve the restrained camera move and check cut continuity against scene 01 in final edit. Do not make claims about unseen room layout. |
| 0.000–7.958 s | White diamond Flow/Gemini watermark over floor, lower right, approximate box x=578–629, y=1120–1195 at 720 × 1280. It does not overlap the rack but must be masked with the exact user-provided circular shop brand in edited output. | Overlay required later | Keep raw clip; reject an edited/exported version if watermark exposed or cover is oversized/drifting. |
| 0.000–8.000 s | AAC stereo audio stream is present but FFmpeg `silencedetect` at −35 dB reports silence from 0 to 8.000 s. | None observed | No material Flow speech detected; separate narration must be verified later. |

## Decision

**PASS for this exact raw source clip.** The coordinator witnessed continuous full-cycle playback; QA reviewed all 192 source frames and found no product-identity, anatomy, or material background defect. The newly revealed corner is an unverified but plausible extension beyond the source photo, recorded for edit continuity. Watermark treatment, approved narration, assembled video and final export each require separate QA.
