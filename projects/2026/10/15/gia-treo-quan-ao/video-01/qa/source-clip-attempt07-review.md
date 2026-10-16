# Visual QA — Flow attempt 07

**Visual disposition: REJECT.** The rack remains identifiable and is fully visible, but the ending reveals a ceiling with two recessed lights that does not exist in either supplied room reference. This is a visible invented background detail and breaks room continuity.

## Run record

- QA started: 2026-10-15 11:43:45 +07:00
- QA completed: 2026-10-15 11:47:02 +07:00
- Exact reviewed file: `projects/2026/10/15/gia-treo-quan-ao/video-01/output/scene-01-flow-attempt-07.mp4`
- SHA-256: `A7C37FD9499571CF7D51F78AC5F4C71EE4D1D64D228F39FFA98A13748B7CBDFA`
- Probe: 1080×1920, 24 fps, 240 frames, 10.000 seconds, 6,852,148 bytes.
- Review method and coverage: created ten one-second 4×6 contact sheets from source-rate decoding, 24 frames per second, and reviewed all 240/240 frames. Also inspected full-resolution frames at 0.2s, 1.2s, 2.2s, 7.5s, 8.6s and 9.8s. Sheets are in `contact-sheets-attempt07/second-00.png` … `second-09.png`; spot frames in the same QA directory.
- References: `input/background-replaced-rack.png` and `input/product-photo-2.jpg`.
- Handoff's render/download elapsed-time record remains in `project.json`; this reviewer did not independently time that phase.
- Continuous normal-speed playback was not available in this review runtime. The complete source-rate frame set was inspected. Audio/dialogue/voice selection were not evaluated here.

## Findings

| Time | Severity | Finding | Disposition |
|---|---|---|---|
| approx. 7.5–10.0s | **Major** | The camera framing lifts enough to reveal a ceiling plane with two circular recessed fixtures. Neither supplied room image shows this ceiling or these fixtures. This is a clear generated addition to the requested background, visible in the final frames and repeatedly in the 8–10s sheet. | **Reject; regenerate while keeping the supplied room background fixed and excluding ceiling/lighting additions.** |
| 0.0–10.0s | Pass | The rough two-tone wall boundary, pale lower wall, baseboard, and warm plank floor are otherwise retained. No plant, furniture, garment, hanger, person, hand, or additional product appears. No visible generated text or captions. | Pass |
| 0.0–10.0s | Pass | The black two-rail rack remains recognizable against `product-photo-2.jpg`, with both rails, side hooks, uprights, lower braces, and feet present. It stays fully within frame in the scanned frames; no obvious part duplication or deformation observed. | Pass |
| approx. 0.0–1.2s | Informational | Opening is front-on and comparatively static, then transitions to oblique framing. Full rack is visible and readable. | Pass |
| approx. 8.0–10.0s | Informational | Ending keeps the whole rack and both feet visible. Ceiling/fixtures enter the top of frame, which causes the background failure above. | Reject overall |
| approx. 0.0–10.0s | Informational | White four-point Flow/Gemini sparkle watermark is visible near the lower-right over the floor. Approximate bounds in 1080×1920: x=885–945, y=1705–1765 (about 60×60 px); clearly visible in `watermark-crop-attempt07.png`. It does not obscure the rack. No separate flicker/brand overlay was observed. | Do not reject raw Flow clip solely for the watermark; inspect its handling in the final export. |

## Supporting artifacts

- Contact sheets: `contact-sheets-attempt07/second-00.png` … `second-09.png`
- Full-resolution spot frames: `frame-0_2s-attempt07.png`, `frame-1_2s-attempt07.png`, `frame-2_2s-attempt07.png`, `frame-7_5s-attempt07.png`, `frame-8_6s-attempt07.png`, `frame-9_8s-attempt07.png`
- Watermark crop: `watermark-crop-attempt07.png`
