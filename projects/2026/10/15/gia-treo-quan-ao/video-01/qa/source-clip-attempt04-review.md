# Visual QA — Flow attempt 04

**Disposition: REJECT.** This clip has two material brief failures: the garment count exceeds the requested 2–3, and it does not hold a full-rack ending over 8.8–10.0s. A new clip is required; do not use this attempt in the edit.

## Run record

- QA review started: 2026-10-15 10:59 +07:00 (approx.; review session began after coordinator handoff)
- QA review completed: 2026-10-15 11:02 +07:00
- Exact reviewed file: `projects/2026/10/15/gia-treo-quan-ao/video-01/output/scene-01-flow-attempt-04.mp4`
- Download filename: `Filming_daily_vlog_product_scene_20261015105751.mp4`
- Flow configuration supplied by coordinator: Omni 1.1 Flash, 9:16, 720p, 10 seconds; reference order `input/background-replaced-rack.png`, then `input/product-photo-2.jpg`.
- Flow generation request to completed download: 277 seconds (coordinator-reported). No distinct per-render generation ID was exposed.
- Media probe: 720×1280, 24 fps, 240 frames, 10.000 seconds video; AAC stereo audio, 48 kHz, 10.005 seconds.
- Reference/script checks: `input/background-photo-1.jpg`, `input/background-replaced-rack.png`, `input/product-photo-2.jpg`, and locked `scripts/script.md`.
- Visual coverage: complete clip reviewed as a 10-second contact sheet with every source frame represented (24 frames/second × 10 seconds = all 240 frames). Sheets: `contact-sheets-attempt04/second-00.png` through `second-09.png`. Full-resolution spot frames are `frame-05s-attempt04.png` and `frame-09_9s-attempt04.png`.
- Continuous playback/audio listening: unavailable in this review runtime. AAC is present, but dialogue, intelligibility, approved narration match, voice consistency, and whether an Adam selector was available remain unverified. The coordinator must listen to the full Flow clip and confirm the voice selection before any edit.

## Findings

| Time | Severity | Finding | Disposition |
|---|---|---|---|
| 0.0–10.0s | Pass | No potted plant is visible. The room retains the reference's two-tone wall edge and wood floor. | Pass |
| 0.0–10.0s | Pass | Rack remains a black, two-level/double-offset garment rack consistent in broad silhouette with the product reference; side hooks remain visible. No obvious rack morphing or product deformation is seen in the 240-frame scan. | Pass |
| approx. 4.0–6.8s; 7.0–9.6s | **Major** | The scene builds to a rack holding roughly 7–8 garments, visibly beyond the requested 2–3 garments and the locked staging brief. Count is approximate because garments overlap, but clearly exceeds three. | **Reject; regenerate with explicit 2–3 garments total.** |
| approx. 9.7–10.0s | **Major** | The shot cuts from the wide rack to a close product/hanger view with a black shirt entering from the left. It does not preserve a full-rack composition for 8.8–10.0s; at 9.9s only the cropped rack and shirt are visible. | **Reject; regenerate or revise shot timing so the full rack stays visible for the complete 8.8–10.0s ending.** |
| approx. 0.0–0.8s and 3.6–6.8s | Pass (visual scan) | One hand is visible at a time placing/adjusting hangers. No extra, fused, duplicated, or floating hand is apparent in the frame scan. Fingers are partly occluded by hangers/clothing, so detailed finger anatomy is not fully assessable; no visible anatomy defect identified. | Pass, with this visibility limit noted. |
| approx. 3.6s–10.0s | Informational | Small white four-point Flow/Gemini watermark appears near lower-right. On the reviewed close-up it is about x=575–598, y=1129–1154 in the 720×1280 frame (roughly 23×25 px); the time window is approximate from the frame scan. It does not obscure the product. | Do not reject solely for raw-generation watermark; remove/cover appropriately in final edit and inspect export. |

## Voice/audio gate

Audio stream is present, but I could not play or listen to the clip in this runtime. No claim is made about dialogue, Vietnamese pronunciation, exact narration, Adam preset selection, or speech quality. The Flow voice selector has not been verified by this reviewer. Keep the audio gate open until the coordinator confirms the entire audio against the locked script and records whether Adam was selectable or only requested as a style. Do not use this clip for editing until the audio gate is resolved and a clip passes visual QA.

## Supporting artifacts

- Exhaustive contact sheets: `contact-sheets-attempt04/second-00.png` … `second-09.png`
- Spot frames: `frame-05s-attempt04.png`, `frame-09_9s-attempt04.png`
- Watermark crop artifact: `watermark-crop-attempt04.png` (crop does not contain the mark; bbox above was measured on the full-resolution spot frame)
