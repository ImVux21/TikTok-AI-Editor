# Flow prompts — video 03

**Title:** Bộ bát hoa Diệp Hồng — Veo 3.1 Quality — video 03  
**Newly written prefixes:** scene-01.prefix.txt, scene-02.prefix.txt, scene-03.prefix.txt  
**One locked base template for every scene:** `workflow/assets/daily-vlog-mode.txt`  
**SHA-256:** `4F5AE6490436166A745F99F9ECC8E8BF6C387E3F018891BD98747109D5996A11`  
**Settings:** Veo 3.1 Quality · Frames · 9:16 · 8 seconds each · 1 output per scene. Current Flow configuration is 720p; upscale only at final export to 1080×1920. The output is not native 1080p generation.

The three clips cover the 24-second edit continuously: scene 1 = 0:00–0:08, scene 2 = 0:08–0:16, scene 3 = 0:16–0:24. Every scene carries the exact same unchanged DAILY VLOG base prompt after its own newly written prefix. Scene 1 uses the before and after keyframes to make the planned reveal at the scene cut. Scenes 2 and 3 use the approved after image as both first and last frame, so the camera can move for detail/context and return to the same table composition at each boundary. Do not describe these AI reenactments as real customer footage or personal product experience.

## Image slots and source QA

| Scene | First frame | Last frame | Supplemental references |
|---|---|---|---|
| 1 | `input/table-before-ai.png` | `input/table-after-ai.png` | None. Quality Frames does not support Ingredients/References-to-Video. Product and user-table references below are for human QA only. |
| 2 | `input/table-after-ai.png` | `input/table-after-ai.png` | None. |
| 3 | `input/table-after-ai.png` | `input/table-after-ai.png` | None. |

Human QA identity sources only: `input/product-reference-ui-source.jpg` (product appearance; the file includes screenshot UI) and `input/user-table-product-reference.png` (user's meal-table photo). Compare generated tableware against those sources during visual QA. Neither is an extra Veo reference slot.

## Continuity and prohibitions

- The table, woven placemat, chairs, curtains, flowers, food dishes and tableware stay in the positions shown by the keyframes. Motion is camera-only; no hands enter or handle ceramics.
- Preserve the visible set's exact white ceramic bodies, scalloped outlines, blue-gray rims and leaf/floral pattern. No plain bowls, invented handled bowls, altered rim colors, duplicated/missing ceramics or changing motifs.
- Keep the same wood-grain dining table and warm window light. Food remains exactly as represented in `table-after-ai.png`; add no dishes, utensils, chopsticks, food, flowers, napkins, logos, labels, UI or text.
- No dialogue, music, captions, voice-over, claims, price, review, fake TikTok interface or brand logo. Voice and text overlays are post-production.
- The AI before/after images are visual anchors, not proof of real use. Inspect all rendered frames, especially frame interpolation and close-up product details, before editing.

## Files

- Scene prefixes: `scene-01.prefix.txt` through `scene-03.prefix.txt` (newly written).
- Full Flow prompts: `scene-01.full.txt` through `scene-03.full.txt` (each prefix followed by the identical locked base template).
- Profile: `video-profile.json`.
