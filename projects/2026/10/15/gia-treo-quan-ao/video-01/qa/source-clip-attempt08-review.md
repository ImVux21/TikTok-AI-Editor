# Visual QA — Flow attempt 08

## Disposition

**Conditional PASS for two trimmed visual ranges only. Reject the untrimmed clip.** Safe ranges: **00:00.00–00:03.15 (out exclusive)** and **00:05.80–00:10.00**. The middle section makes the rack appear to rotate without a person or visible camera move, and adds an overhead ceiling with recessed lights that is absent from the exact replacement plate. Keep only the two stable front/three-quarter views; do not use frames 3.15–5.80. These ranges show the same black two-rail rack and exact room/floor treatment, with no visible hands, garments, or product deformation. Avoid claims about tested load/capacity.

The selected intervals contain 75 frames (0–74) and 101 frames (139–239), respectively, **176/240 source frames total**. They are suitable as separate short product shots; make a clean cut between them. The full source contains small camera/framing drift in the stable ranges, so these are video footage, not a substituted still image. The isolated middle is rejected.

## Source and review record

- Exact reviewed file: `projects/2026/10/15/gia-treo-quan-ao/video-01/output/scene-01-flow-attempt-08.mp4`
- Download source: `C:\Users\vuodo\Downloads\Daily_vlog_video_production_script_20261015134747.mp4`
- SHA-256: `6DD43145E02849FEE8837422EF7046EBC32A3E738264A1D3A72D41C65D20AD3E` (matches coordinator-provided digest)
- Media: H.264, 720×1280, 24 fps, 240 frames, 10.005 sec; AAC stereo, 48 kHz.
- Compared with `input/background-replaced-rack.png` and `input/product-photo-2.jpg`.
- QA phase: started 2026-10-15 ~13:43 +07:00; completed 2026-10-15 13:52:14 +07:00. (The start is approximate; this report began immediately after the coordinator handoff.)
- Method: generated six sequential contact sheets covering frame indices 0–239, 40 frames per sheet at 24 fps; reviewed all sheets and full-resolution frames at 0.2, 2.8, 3.2, 3.6, 4.5, 5.5, 5.8, 6.0, 8.0 and 9.9 seconds. Contact sheets: `qa/contact-sheets-attempt08/frames-000-039.png` through `frames-200-239.png`; full-resolution extracts are adjacent in `qa/`.
- This is exhaustive source-frame visual coverage. Continuous-speed playback/audio listening was not available in this reviewer runtime; do not treat audio as personally verified here.

## Findings by timeline

| Time | Finding | Severity / disposition |
|---|---|---|
| 00:00–03:15 | Stable front view; rack geometry and room match the replacement plate. Four side hooks, paired rails/uprights, center braces and feet remain coherent. No people or hands enter. | Pass as an opening/detail shot. |
| ~03:15–03:60 | Rack angle changes from near frontal to strong three-quarter view while the room/background remains fixed; no person or contact explains the movement. At 3.6s, two recessed ceiling lights and a visible ceiling plane appear above the wall. These are absent from the reference plate. | Hard visual/continuity defect. Reject this section. |
| 03:60–~05:50 | Three-quarter rack view holds; geometry remains recognizable, but the unexplained rack rotation and ceiling/light invention persist. | Reject. |
| ~05:50–05:80 | Framing returns toward the frontal view and ceiling artifacts disappear; boundary uncertain at source-frame granularity, so use conservative in-point 5.80s. | Transition excluded. |
| 05:80–10:00 | Stable frontal view returns; room and rack align with the reference, no visible product deformation or anatomy issue. | Pass as a separate shot. |

- Plant/props: none in the reviewed clip.
- Product: black two-rail freestanding rack; no clear silhouette, proportion, hook-count or base-foot defect in the accepted ranges. No garments are shown, so footage does not demonstrate hanging capacity.
- Hands/anatomy: no visible hands or people in any reviewed frame; no anatomy defect.
- Watermark: small translucent Gemini/Flow sparkle at lower-right, approximately **x=574–625, y=1138–1178 px** on 720×1280 (about 52×41 px). It persists through the clip and does not cover the rack; note position for the editor's approved shop-logo mask.
- Audio: AAC track is present. The coordinator reports the user approved the attempt08 voice preview; I could not listen to this clip in the QA runtime, so dialogue/script match, intelligibility and actual Adam selection are not independently confirmed here. Treat the user's preview approval as their stated preference, not as reviewer audio verification.

## Handoff

Coordinator/post may use only **00:00.00–00:03.15** and **00:05.80–00:10.00**, as separate shots. Exclude the middle 3.15–5.80s. Contact sheets establish complete frame coverage; do not use the untrimmed source as a single uninterrupted shot.
