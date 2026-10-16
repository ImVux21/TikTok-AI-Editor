# Visual QA — Flow attempt 06

**Visual disposition: PASS.** This is the first reviewed attempt that preserves the supplied replacement-room plate, keeps the rack clear and empty, and remains full-frame throughout. The audio gate remains open because this reviewer could not listen to the file.

## Run record

- QA review started: 2026-10-15 11:18:46 +07:00
- QA review completed: 2026-10-15 11:20:10 +07:00
- Exact reviewed file: `projects/2026/10/15/gia-treo-quan-ao/video-01/output/scene-01-flow-attempt-06.mp4`
- Original download filename was not supplied in handoff.
- Flow configuration from coordinator: Omni 1.1 Flash, Video > Frames, 9:16, 720p, 10 seconds, one output; same `input/background-replaced-rack.png` used for first and last frame.
- Submitted approx. 11:15:20 +07:00; downloaded 11:17:47 +07:00. Render+download elapsed approx. 147 seconds; no separate render-completion time is available.
- Media probe: 720×1280, 24 fps, 240 frames, 10.000 seconds video (container/audio duration 10.005 seconds), 3,959,530 bytes. Audio stream is AAC stereo at 48 kHz.
- References compared: `input/background-replaced-rack.png` and `input/product-photo-2.jpg`.
- Visual coverage: all 240 source frames reviewed, represented in ten one-second contact sheets at 24 fps: `contact-sheets-attempt06/second-00.png` through `second-09.png`.
- Full-clip playback/audio listening: not available in this runtime. Narration, dialogue quality, match to locked Vietnamese script, voice consistency, and Adam selector/preset remain unverified. Coordinator must listen to the entire clip before editing and record whether Adam was selectable or only requested as a style.

## Findings

| Time | Severity | Finding | Disposition |
|---|---|---|---|
| 0.0–10.0s | Pass | The distinctive rough, jagged two-tone wall boundary, pale lower wall, warm plank floor, wall-floor junction, shadows, and room perspective match the supplied replacement plate. Room remains coherent throughout the frame scan. | Pass |
| 0.0–10.0s | Pass | Black double-offset rack remains recognizable and consistent with the product reference: both rails, uprights, side hooks, lower braces, and feet remain present. No obvious morphing, duplicated product, or deformation observed. | Pass |
| 0.0–10.0s | Pass | The full rack stays inside frame, including top rails/hooks and both feet. It is legible at phone size. The rack remains empty; no garments, hangers, people, hands, plants, shelves, or other introduced props were seen. | Pass |
| 0.0–10.0s | Informational | Framing has restrained, subtle drift while retaining the same room/rack setup; no disruptive cut or crop observed. Every decoded frame has a distinct frame hash (240/240). | Pass; no still interval identified. |
| approx. 0.0–10.0s | Informational | Small white four-point Flow/Gemini sparkle watermark is visible in the lower-right over the floor. Approximate bounds on 720×1280: x=575–615, y=1132–1172 (about 40×40 px). It does not obscure the product. | Do not reject raw Flow clip solely for watermark; handle in edit and inspect final export. |

## Audio and voice gate

AAC audio is present, but I could not listen to it here. I do not certify the narration, intelligibility, Vietnamese wording/pronunciation, voice consistency, or exact match to approved Flow speech. The voice selector and Adam availability were not inspected by this reviewer. Keep the audio gate open until coordinator playback confirms the entire speech and notes whether Adam was selectable or only requested as a style.

## Supporting artifacts

- Exhaustive contact sheets: `contact-sheets-attempt06/second-00.png` … `second-09.png`
- Spot frames: `frame-05s-attempt06.png`, `frame-09_9s-attempt06.png`
- Watermark crop: `watermark-crop-attempt06.png`
- All-frame hashes: `framehashes-attempt06.csv`
