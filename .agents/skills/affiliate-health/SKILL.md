---
name: affiliate-health
description: Build a health-themed affiliate video using one unchanged with-dialogue or voiceover prompt from the user's Prompt sức khỏe section.
---

# Prompt sức khỏe

Read the [original health section](../../../workflow/assets/health-source.txt) and [prompt registry](../../../workflow/PROMPT-MODES.md). The section offers a version with dialogue and a version for later voiceover. Choose one for a video, copy its source wording unchanged into a fixed template asset, and lock its hash in the video's profile. Create the whole-video script and scene-specific prefixes without altering that template. Check medical or product claims against reliable evidence before using them in an advertisement; flag unsupported claims instead of repeating them. Use the parent `$tiktok-affiliate-video` workflow for generation, visual review, voice, and editing.

## Audio default
Follow [voice policy](../../../workflow/VOICE-POLICY.md): the user selected ElevenLabs V3 Adam narration and CapCut assembly, with 1.2x narration playback. Current connector has no speed parameter: apply 1.2x once to the audio track in CapCut, preserve pitch, then align captions and listen to the final track. Flow produces storyboard-based visuals/optional ambience, no speech. Keep audio tags in V3 raw text only, never captions or Flow dialogue. Preserve immutable source templates and record explicit audio/storyboard overrides. Do not relabel historical audio.
