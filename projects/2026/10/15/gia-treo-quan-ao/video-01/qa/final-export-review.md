# Final export QA — release gate

## Verdict: FIX REQUIRED (do not release this export)

The exact export fails visual continuity at **00:04.625–00:06.125**. At this cut, the picture changes to a different plain beige/white wall with a visible electrical outlet and no reference room's distinctive two-tone wall edge. The room differs from `input/background-replaced-rack.png` and the supplied background photo. Replace this 1.5-second shot with a reviewed interval that preserves the approved room, then render and submit the new exact export for QA. Other reviewed portions are visually usable, but this defect blocks release.

## File and coverage

- Exact file: `projects/2026/10/15/gia-treo-quan-ao/video-01/output/final_video.mp4`
- SHA-256: `699BD1645372C1E1AB5CEF05CBB4573915FB1FBE4E766A5A14E97645907ABDE8`
- Probe: H.264, 720×1280, 24 fps, 240 frames, 10.000 seconds; AAC stereo 48 kHz.
- QA phase: started 2026-10-15 14:07:27 +07:00; completed 2026-10-15 14:10:35 +07:00.
- Compared with source EDL `scripts/hook-edit-plan-20261015.md`, edit notes `scripts/final-edit-notes.md`, `output/subtitles-final.srt`, the approved product/background references and source clip QA reports.
- Exhaustive frame coverage: six sequential contact sheets contain frames 0–239, 40 frames each at source cadence 24 fps (`qa/final-contact-sheets/frames-000-039.png` through `frames-200-239.png`). All 240 frames were reviewed. Decoded frame-hash check: 240 unique frames, 0 exact duplicate frames; no freeze/still interval found.
- Reviewed cut boundaries at frames 74/75 (3.083/3.125s), 110/111 (4.583/4.625s), and 146/147 (6.083/6.125s), plus first/last frames and 7.5/9.5s. Full-resolution extracts are in `qa/final-frame-*.png`.

## Timeline findings

| Final time | Review |
|---|---|
| 00:00.000–00:03.125 | Stable product overview in the approved room. Text “Ủa, một giá mà treo được hai tầng luôn á?” is legible, stays above the rails and reflects the visible two-rail rack. Circular shop mark covers the lower-right Flow sparkle. Pass. |
| 00:03.125–00:04.625 | Hard cut to product/clothing detail. Product identity remains recognizable; caption “Thanh trên, thanh dưới—” is above the product. Pass, though the scale change is abrupt. |
| **00:04.625–00:06.125** | **Fail:** close shot shows a different plain wall, a room corner and an electrical outlet; the required two-tone wall/floor setting is absent. This is a conspicuous background continuity break. Replace this shot. |
| 00:06.125–00:10.000 | Returns to the reference room; rack remains recognizable, hanger/clothing demonstration is coherent in the reviewed frames, and the CTA appears above the product. Several garments are shown, but the narration makes no load/capacity claim. Pass. |

No obvious rack deformation, extra limbs, or fused/floating hand was identified in the exhaustive visual scan. The product remains black with two parallel rails and side hooks. No caption or branding overlay obscures the product or hand action. Hard cuts occur at 3.125, 4.625 and 6.125 seconds; there are no transition effects. The cut at 4.625 itself is clean, but its source shot's different room is not acceptable.

## Captions, branding and safe area

- Burned-in captions visually match the provided SRT wording and are centered near the top. At full-frame review they are legible and clear of the rack's top rail/hand action, including at the two-line opening and final CTA. The CTA concludes at 8.841s; the remaining end hold has no caption.
- The overlay is a circular crop of the supplied shop-branding art, about 68 px diameter, center approximately (600,1158) on the 720×1280 frame. It remains steady across cuts and covers the raw Flow sparkle at lower-right without covering the rack or hands. It is recognizable as the shop mark at the reviewed phone-size scale. This review did not render TikTok's live interface overlay.
- Product staging includes multiple garments in the final payoff. This is acceptable under the current edit direction because the narration/caption does not state a tested load or capacity.

## Audio gate

The export contains a continuous AAC stereo track. `scripts/final-edit-notes.md` records that the full `output/attempt08-flow-audio.m4a` audio is used under the edit and that speech from attempts 03/04 is excluded. The coordinator reports CapCut audio-only ASR matched the locked script and the user approved the attempt08 voice preview. I could not listen to the final export at normal speed in this reviewer runtime, so exact final speech, intelligibility, voice consistency and Adam selector status remain **not independently ear-verified**. Keep audio confirmation with the coordinator; no independent listen pass is claimed.

## Required action

Replace the 4.625–6.125s different-room shot with an already QA-approved interval in the exact target room, export a new MP4, and rerun final QA against that exact file and hash. The current SHA is rejected for release.
