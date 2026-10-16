# Professional edit handoff — 2026-10-15

## Corrected export v2 (current candidate)

`output/final_video-v2.mp4`; SHA-256 `2B9603EBAC4DBD9E6883DE7CDB25398163A9BE23D80022B5B0C9B142DE35D4D3`; 4,348,001 bytes; 10.000 s; 240 video frames; H.264 720×1280 at 24 fps; AAC stereo 48 kHz. The original `output/final_video.mp4` is preserved as the rejected v1 for traceability.

Final QA rejected v1 because attempt04 frames [0,36), used at final frames [111,147) or 4.625–6.125 s, show a plain beige/white room corner and electrical outlet inconsistent with the supplied background. V2 replaces only those 36 frames with QA-approved attempt08 frames [140,176), source 5.833–7.333 s. New EDL: attempt08 [0,75), attempt03 [108,144), attempt08 [140,176), attempt04 [87,180). All source out points are exclusive. The voice, caption timing/text/style, logo, 10-second duration, and clean cuts remain unchanged. `output/subtitles-final.srt` applies to v2 without modification.

Inspected frames immediately on both sides of the revised cuts at 4.58, 4.67, 6.04 and 6.17 s. The shot now returns from a rack detail to the full empty two-rail rack in the correct two-tone room, then cuts to the hanging action. Full export QA remains required; v2 has been handed to the coordinator for that gate.

Export: `output/final_video.mp4`; SHA-256 `699BD1645372C1E1AB5CEF05CBB4573915FB1FBE4E766A5A14E97645907ABDE8`; 4,156,767 bytes; 10.000 s; 240 video frames; H.264 720×1280 at 24 fps; AAC stereo 48 kHz. This is a local export, not a CapCut cloud draft.

The visual EDL is unchanged from `scripts/hook-edit-plan-20261015.md`: attempt08 frames [0,75), attempt03 [108,144), attempt04 [0,36), attempt04 [87,180). All transitions are clean hard cuts, 0 frame effect duration. All intervals were previously QA-approved. No stills or freeze frames are inserted. The full `output/attempt08-flow-audio.m4a` track is continuous beneath all four visual cuts; source dialogue from attempt03/04 is excluded.

Rebuilt the export from the original source clips to replace the oversized baseline captions. The hook has a two-line caption above the top rail; subsequent phrases have one line each. The final CTA phrase is divided into two timed captions. Caption content follows the supplied CapCut ASR phrase record in `output/subtitles-hook-baseline-v3.srt`; output SRT is `output/subtitles-final.srt`. Style is white Arial 42 px, dark outline, centered at 80 px from top; this keeps the rack and hands visible. Opening title says only what the voice says and what the video visibly shows: one rack with two rails. The rack is shown empty first, then in close detail, then with garments at the end.

The Flow watermark is covered with a circular 68 px crop of the exact `workflow/assets/shop-branding.png`, centered at (600,1158), top-left (566,1124), stable through cuts. Renderer: `scripts/render_final.py`; generated logo `output/shop-brand-circle-68.png`; subtitle master `output/final-captions.ass`.

Spot-checked final frames at 0.5, 7.5 and 9.5 seconds. Final full-frame normal-speed QA, transition-by-transition inspection, and independent ear verification of the audio remain with `affiliate_visual_qa`/coordinator. Source voice was approved by the user in Flow preview; exact named Adam voice preset is unverified. Do not publish until final QA passes.
