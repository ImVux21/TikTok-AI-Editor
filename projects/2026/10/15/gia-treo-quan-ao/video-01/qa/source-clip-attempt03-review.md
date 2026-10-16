# Source clip review — attempt 03

## Disposition

**REJECT / HOLD — do not pass this source to editing yet.** The opening 1.1 s retains part of the old plant/pot from the original room photo, which is absent from `input/background-replaced-rack.png` and was explicitly excluded in the locked script/prompt. It vanishes at the first wide reveal, creating a visible continuity error. The final ~0.3 s also cuts away from the locked wide ending to a hand-held clothing close-up. Recommend a video replacement that removes the plant in every shot and ends on a clear moving wide view. Do not cover the opening with a still or freeze.

## Exact reviewed source and settings

- File: `output/scene-01-flow-attempt-03.mp4`
- Downloaded: 2026-10-15 10:41:50 +07:00 (coordinator record)
- Flow model/settings: Omni 1.1 Flash, 9:16, 720p, 10 s; one clip; reference order: `input/background-replaced-rack.png`, then product image.
- Scene/editor identifier: `f642a966-d7f5-4664-b51b-b3115d3d7e5a`; distinct per-render generation ID was not exposed.
- References: `input/background-photo-1.jpg`, `input/background-replaced-rack.png`, `input/product-photo-2.jpg`; script `scripts/script.md`.
- Probe: H.264, 720×1280, 24/1 fps, 240 frames, 10.000 s; AAC stereo 48 kHz, 10.005 s.

## Coverage and playback limitations

- Decoded and visually checked **240/240 frames at 24 fps** in ten ordered contact sheets, one second per sheet: `qa/contact-sheets-attempt03/second-00.png` through `second-09.png`. Focused hand sheets are in `qa/hands-detail-attempt03/`.
- I could not play the clip continuously in this subagent runtime or listen to it. `ffplay` is installed but there is no accessible playback surface/audio stream to the reviewer; no local Whisper/whisper-cli speech recognizer is installed. The AAC track exists, but actual dialogue, intelligibility, language, repetitions, alignment and voice consistency are **unverified**. Do not treat the locked script/prompt as proof of what was spoken. No ElevenLabs tools used. Adam selector was not exposed to this reviewer; the prompt requests Adam-style voice, so exact preset selection remains unverified.
- The frame-by-frame visual review is complete; continuous normal-speed watch and audio gate remain open for the coordinator.

## Findings

| Time | Finding and evidence | Severity | Disposition |
|---|---|---|---|
| 00:00–~00:01.1 | Green leaves and the rim/body of a potted plant remain at the lower-left edge while the rack is shown close. The replacement plate has no plant; it is visible in the original background photo on the shelf. It disappears at the cut to the wide room reveal. This breaks the requested removal and continuity. | Major | **Reject; replace with a new video clip.** |
| ~00:01.1–00:09.7 | Main wide shots preserve the distinctive two-tone wall with rough paint boundary and wood plank floor. The former shelving, boxes and shoes are absent. | Pass for main-room match | Keep as positive evidence; opening still fails. |
| 00:00–00:10 | Black rack appearance broadly matches the product/replacement references: two offset rail frames, black finish, uprights, braces, side hooks and curved feet. No extra frame or obvious shape/colour mutation seen in the source-rate scan. | Pass for product identity | No product-identity defect observed. |
| ~00:00–00:01.1; ~00:03.5–00:04.8; ~00:09.7–00:10 | One visible hand at a time places/adjusts a hanger or garment. No extra/duplicated/floating hand, fused hand, or clearly malformed anatomy observed in inspected frames. Hands are partly occluded by hangers/clothes in several frames, limiting finger counts there. | No clear anatomy defect | Contact/action still needs normal-speed playback. |
| ~00:06–00:09.7 | Wide views show roughly 8–10 garments concentrated on one rail, exceeding the script's “a few lightweight garments” staging and potentially implying unverified capacity. No load test is shown. | Moderate | Reduce to a few items in replacement clip. |
| ~00:09.7–00:10 | Final frames cut from the wide product view to a side close-up with a hand on a garment; product is cropped and the ending does not match the locked clear wide payoff. | Moderate | Fix ending in replacement clip; do not conceal with a still. |
| 00:00–00:10 | White Gemini/Flow sparkle watermark appears at lower right throughout; no other generated text/badge observed. At 8.0 s, estimated bbox x≈573–626, y≈1133–1178 px on 720×1280 (about 53×45 px), center≈(600,1155). Position is stable in the contact sheets. | Record only | Do not reject solely for watermark. Final draft/export still needs the exact circular shop-brand image mask and its own watermark/overlay review. |

## Phase log

- Review started: 2026-10-15 10:42 +07:00 (immediately after handoff).
- Contact sheets and full frame scan completed: 2026-10-15 10:47 +07:00.
- Review disposition recorded: 2026-10-15 10:48 +07:00.
- unresolved: continuous playback and listening/audio verification; coordinator to review in Flow player.
