# Visual QA — Flow attempt 05

**Disposition: REJECT.** The full-rack staging and zero-prop plan pass visually, but the requested room background does not: the clip loses the distinctive irregular two-tone wall boundary that is prominent in the supplied replacement plate. Do not use this clip in the edit.

## Run record

- QA review started: 2026-10-15 11:06:40 +07:00
- QA review completed: 2026-10-15 11:09:18 +07:00
- Exact reviewed file: `projects/2026/10/15/gia-treo-quan-ao/video-01/output/scene-01-flow-attempt-05.mp4`
- Original download name: `Filming_daily_vlog_product_scene_20261015110558.mp4`
- Flow configuration from project record: Omni 1.1 Flash, 9:16, 720p, 10 seconds, one output; ordered references `input/background-replaced-rack.png` then `input/product-photo-2.jpg`.
- Submitted: 2026-10-15 11:04:01 +07:00; download complete: 11:05:58 +07:00. Elapsed submission-to-download: 117 seconds (1m57s). This combines render and download; no separate render-completion time is available.
- Media probe: 720×1280, 24 fps, 240 frames, 10.000 seconds video; AAC stereo, 48 kHz, 10.005 seconds.
- Visual coverage: every source frame represented and reviewed in ten contact sheets, 24 frames per second (240/240 total): `contact-sheets-attempt05/second-00.png` through `second-09.png`.
- Closing motion check: all 60 frames from 7.5–10.0s have distinct frame hashes, supporting continuous motion rather than a frozen still.
- Continuous clip playback/audio listening: unavailable in this runtime. Audio stream exists, but narration wording, intelligibility, pronunciation, consistency, and match to approved Flow audio are unverified. No Adam voice selector was inspected; exact preset selection remains unverified. Coordinator must listen to the complete clip and check the Flow voice selector before editing.

## Findings

| Time | Severity | Finding | Disposition |
|---|---|---|---|
| 0.0–10.0s | **Major** | Background mismatch throughout. The supplied `background-replaced-rack.png` has a distinctive rough, jagged boundary between a warm brown upper wall and pale lower wall. That boundary is absent in every frame; the generated clip shows a mostly uniform pale gray wall. The wood floor and room-like setting remain, but the exact requested room plate is not preserved. | **Reject; regenerate with stronger fixed-background preservation or use an edit/composite that keeps the supplied room.** |
| 0.0–10.0s | Pass | Rack stays empty; no garments, hangers, people, hands, arms, plants, shelves, or added decor are visible. | Pass |
| 0.0–10.0s | Pass | Full rack, both upper rails, side hooks, lower braces, and both feet remain inside frame in the contact-sheet scan. Product is legible at phone-sized framing. No obvious identity change, morph, or product deformation observed. | Pass |
| 7.5–10.0s | Pass | Closing shot holds the full rack continuously, with visible surrounding wall/floor and both feet. No cut or crop in the requested closing interval. All 60 closing frames differ by hash; motion is subtle but present. | Pass |
| approx. 2.8–3.0s; 6.5–7.0s | Informational | Several clean changes in camera angle/distance create the requested multi-beat view. The rack remains fully framed through the changes. Framing is repetitive and movement is restrained, but product readability is good and no required beat crops the rack. | Pass |
| 0.0–10.0s | Informational | Small white four-point sparkle watermark is visible at lower-right over the floor. Approximate box: x=575–615, y=1133–1173 in 720×1280; visible across the examined sheets and clearly in `frame-09s-attempt05.png`. It does not cover the product. | Do not reject raw Flow clip solely for watermark; ensure final edit handles it and inspect final export. |

## Voice/audio gate

AAC audio is present, but this reviewer could not listen to the clip in the available runtime. Dialogue, Vietnamese speech quality, exact script match, voice consistency, and Adam preset selection are not verified. Flow selector availability remains unknown to this reviewer. Keep the audio gate open until the coordinator listens to the entire clip and records whether Adam was selectable or only requested as a style.

## Supporting artifacts

- Exhaustive contact sheets: `contact-sheets-attempt05/second-00.png` … `second-09.png`
- Closing frames: `frame-09s-attempt05.png`, `frame-09_9s-attempt05.png`
- Watermark crop: `watermark-crop-attempt05.png`
- Closing frame hashes: `ending-framehashes-attempt05.csv`
- Decoded video: 240 source frames total; each contact sheet covers one second at 24 fps.
