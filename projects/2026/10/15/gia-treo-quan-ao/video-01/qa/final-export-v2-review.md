# Final export v2 QA — release gate

## Verdict

**PASS for delivery of the local MP4.** Visual QA passes, and the coordinator confirmed the exported AAC is continuous audio from the user-approved attempt08 asset. The previous v1 background mismatch is fixed: v2 uses the approved attempt08 rack-in-room frames [140,176) for final timeline 4.625–6.125s. The replacement shot matches the two-tone wall and wood floor; no outlet or alternate room is visible. No blocker remains for delivering this local file. Independent ear-quality review and confirmation of the named Adam preset remain unverified; those do not block local MP4 delivery.

## Exact reviewed asset and full coverage

- File: `projects/2026/10/15/gia-treo-quan-ao/video-01/output/final_video-v2.mp4`
- SHA-256: `2B9603EBAC4DBD9E6883DE7CDB25398163A9BE23D80022B5B0C9B142DE35D4D3`
- Probe: H.264 720×1280, 24 fps, 240 frames, 10.000 seconds; AAC stereo, 48 kHz.
- QA phase: started approximately 2026-10-15 14:11 +07:00; completed 2026-10-15 14:17:21 +07:00.
- Compared with updated `scripts/final-edit-notes.md`, `scripts/hook-edit-plan-20261015.md`, `output/subtitles-final.srt`, approved source QA intervals, and the exact product/background references.
- All 240/240 frames reviewed in six sequential 40-frame contact sheets at source cadence: `qa/final-v2-contact-sheets/frames-000-039.png` through `frames-200-239.png`. First/last frames, 7.5/9.5s and both sides of every cut were inspected full resolution at 3.083/3.125, 4.583/4.625, and 6.083/6.125 seconds. Images are saved as `qa/final-v2-frame-*.png`.
- Decoded frame hash check: 240 unique frames; 0 exact duplicates. No freeze/still intervals.

## Timeline and transitions

| Time | Finding |
|---|---|
| 00:00–03.125 | Approved empty-rack overview in exact two-tone room. Opening title is legible above the rails and matches visible two-rail design. Shop logo remains in lower-right safe floor area. Pass. |
| 03.125–04.625 | Cut to approved product/clothing detail; rack remains recognizable and room matches. Caption is clear above product. Pass. |
| 04.625–06.125 | Corrected cut to approved empty-rack shot; same two-tone wall and wood plank floor, no outlet/alternate room. This resolves v1's defect. Caption “chia đồ ra là thấy ngay.” stays above the rack. Pass. |
| 06.125–10.000 | Cut to approved hanging demonstration and final wide payoff. Product geometry remains recognizable, hand/hanger action appears coherent, and CTA stays clear above the product. Several garments are displayed, but there is no capacity/load claim. Pass. |

All three are clean hard cuts with no effects. The shifts in scale are noticeable but fit the detail-to-overview demonstration and do not cause product or room identity changes. No visible plant, extraneous props, product deformation, or clear hand-anatomy issue was found. Product remains the black double-rail freestanding rack with side hooks.

## Captions and branding

- Burned-in captions match the supplied SRT wording and timing on visual review. The two-line hook and later lines are readable at phone-size preview, remain above the rails/hands, and do not cover the CTA/product. The CTA ends at 8.841s; the final hold is uncaptained.
- The shop logo is a circular crop of the provided branding image, approximately 68 px diameter centered at (600,1158) in 720×1280. It is stable through the cuts, recognizable at the reviewed phone-size preview, covers the Flow sparkle, and does not overlap rack/hands/captions. TikTok's live interface overlay was not rendered for this review.

## Audio and remaining release check

- AAC stereo audio spans the full 10-second export. The updated edit notes identify the continuous attempt08 audio as the backbone; dialogue from attempts03/04 is excluded. Coordinator-reported CapCut audio-only ASR matches the locked script, and the user approved the attempt08 voice preview.
- Coordinator provenance check decoded the v2 AAC and `output/attempt08-flow-audio.m4a` to mono 16 kHz PCM: both produced 160,085 samples (10.0053125s), with zero-lag Pearson correlation 0.9998. Together with the user-approved source preview and coordinator-reported CapCut audio-only ASR matching the intended dialogue, this confirms continuous approved-source speech after AAC re-encode.\n- I could not listen to the v2 export at normal speed in this runtime. Independent ear-quality review (pronunciation/intelligibility) and exact named Adam preset selection remain unverified. No blocker remains for delivery of the local MP4; this report does not authorize posting.

