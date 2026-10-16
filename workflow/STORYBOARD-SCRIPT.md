# Storyboard-first scripts

Use this guidance when the user wants to approve storyboard frames before Flow generation.

## Before Flow

1. Lock the whole-video story, scene order, exact Vietnamese dialogue, and one source template for every Flow scene.
2. Prepare **1–3 distinct, complete 9:16 storyboard frames** compositing the product into the user-approved background. Each frame represents a key moment or scene. Do not make a collage, contact sheet, or multi-panel layout; do not generate the Flow clips yet.
3. Review each frame against the product and background references. Check the whole visible product, count bars/hooks/legs, preserve proportions, color, geometry, room layout and light direction. Do not invent a rear view, hidden joints, shelves, accessories, packaging, logos, or features absent from the references/listing. Make clear when an image depicts generated staging rather than a real installation or testimonial.
4. Show the frames for review and revise any inaccurate frame. A separate manual approval is not a required gate unless the user asks to select frames; after storyboard QA passes, the coordinator may proceed to scene-specific Flow prompts within the user's existing authorization. Keep product/background continuity and dialogue consistent across every scene.

## Script and edit planning

- A 10-second Flow generation is one scene, not the whole story. A 3-scene outline can guide a longer edit; keep each generated scene within the selected model's supported duration.
- **18–24 seconds is an editorial starting point, not a TikTok optimum or a performance claim.** Change duration to fit the idea, dialogue and reviewed footage.
- Give each scene one visible purpose: hook, useful demonstration/payoff, or CTA. Narration should describe only supported facts and visible action. Avoid invented personal experience, unverified dimensions, price, load capacity, setup claims or results.
- Plan the cut on a continuing motion or matching composition. Carry the same voice, room ambience and music bed through cuts; avoid duplicating speech or covering important product details with captions.
- For this user's current production, use the explicitly selected ElevenLabs V3 voice workflow and CapCut assembly. Follow [ADAM_V3_PROMPT_SPEC.md](ADAM_V3_PROMPT_SPEC.md) for voice direction and formatting. Treat Adam and the supplied playful Vietnamese manner (“mấy dợ”, “mấy ní”) as the requested style; verify the selected voice is available before claiming success. Do not substitute a different provider/model without direction.
- Keep `voiceTextRaw` separate from `cleanSubtitleText`. V3 raw text may contain deliberate English audio tags; strip tags from captions while preserving the same spoken words and punctuation. Write all numbers spoken aloud as Vietnamese words, never digits; do not put production instructions in raw speech text. End the final spoken scene with “Dứt!” or “Dứt lẹ!”.
- Narration playback speed is user-confirmed at 1.2x. The current V3 connector exposes no speed parameter: apply it once to audio in CapCut with pitch preservation, listen, and time cuts/captions from the final track; do not pad speech.

## Sample 3-scene script: black clothing rack

**Product facts visible in the reference:** black freestanding rack, two hanging rails at different heights, side hooks and lower support/base. The listing describes clothing hanging/drying and multiple variations. The exact selected variation is not verified. No dimensions, price, load capacity, material claim, bundle contents or personal-use claim in this sample. The room image contains a different rack; replacing it with this product is generated staging.

**Editorial starting point:** about 21 seconds total, 9:16, divided into three scenes. This is an editorial starting point, not a platform optimum or a fixed seven-second requirement. Let the actual generated speech and reviewed footage set each scene's duration; trim to natural pauses and don't stretch a short line with filler. Prepare one coherent clothing arrangement in the storyboard and preserve it across scenes. Garments must not appear/disappear between cuts unless the script and visible action explicitly show that change. All frames show the same product geometry and room. No still frame is a replacement for a failed video scene.

| Scene | Time guide | Visual/action | `voiceTextRaw` for ElevenLabs V3 | `cleanSubtitleText` (no tags) | Headline |
|---|---:|---|---|---|---|
| 1 — Hook | 0–7 s | Use the approved wide 3/4 master composition, with the complete product and both rails visible from frame one. Make only a small handheld push-in; no close crop or reveal that would require the model to reconstruct unseen geometry. | `[playful] Mấy dợ... giá treo này có hai thanh luôn nè!` | `Mấy dợ... giá treo này có hai thanh luôn nè!` | `Hai thanh treo?` |
| 2 — Payoff | 7–14 s | Use one precomposed medium/detail view where both rails and side hooks remain visibly correct. One simple camera move reveals the rails; keep the same clothes and their positions as in scenes 1 and 3. Do not animate garments appearing. | `[excited] Thanh trên, thanh dưới... chia áo ra, nhìn phát là thấy liền.` | `Thanh trên, thanh dưới... chia áo ra, nhìn phát là thấy liền.` | `Thanh trên / thanh dưới` |
| 3 — CTA | 14–21 s | Return to the same full wide 3/4 view and unchanged pre-staged clothes arrangement. Hold the product clearly while the camera makes a subtle settling move; end on moving video, not a still end card. | `[playful] Bên hông còn có móc nữa. Mấy ní nhớ chọn đúng phân loại trong giỏ nha. Dứt!` | `Bên hông còn có móc nữa. Mấy ní nhớ chọn đúng phân loại trong giỏ nha. Dứt!` | `Chọn đúng phân loại trong giỏ` |

Dialogue uses only visible/verified details: two rails, side hooks and multiple listing variations. It makes no claim about discount, load, price, exact size, durability or personal experience. The three time ranges are visual planning guides only; let the actual V3 audio determine scene duration and cut points, then align clean captions to the final audio in CapCut.

**Voice/edit handoff:** ElevenLabs V3 is the user's explicit provider/model selection for audio; CapCut is the selected editor. Adam remains a requested voice/style and must be verified in the account before claiming selection. Keep audio tags in V3 raw text only; captions must be tag-free. Apply user-selected 1.2x once to the narration track and review the final-speed audio.

