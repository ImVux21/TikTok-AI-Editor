---
name: affiliate-homegoods
description: Choose and lock one unchanged source prompt from the user's home-goods section for a whole TikTok affiliate video; use for household product videos.
---

# Đồ gia dụng

Read [the prompt registry](../../../workflow/PROMPT-MODES.md) and the original [home-goods section](../../../workflow/assets/homegoods-source.txt). For one video, choose exactly one of [DAILY VLOG](../../../workflow/assets/daily-vlog-mode.txt) or [HANDHELD](../../../workflow/assets/handheld-product-review.txt). Use the chosen text unchanged for every Flow-generated clip in that video. HANDHELD is for showing the physical product in a hand; DAILY VLOG is for a verified household-use action and visible result. If the references do not establish an accurate use action, do not invent it. Record the choice and template hash in the video's profile. Write the whole-video script first, then scene-specific prefixes; use the parent `$tiktok-affiliate-video` workflow for generation, review, voice, and editing.

## Audio default
Follow [voice policy](../../../workflow/VOICE-POLICY.md): the user selected ElevenLabs V3 Adam narration and CapCut assembly, with 1.2x narration playback. Current connector has no speed parameter: apply 1.2x once to the audio track in CapCut, preserve pitch, then align captions and listen to the final track. Flow produces storyboard-based visuals/optional ambience, no speech. Keep audio tags in V3 raw text only, never captions or Flow dialogue. Preserve immutable source templates and record explicit audio/storyboard overrides. Do not relabel historical audio.
