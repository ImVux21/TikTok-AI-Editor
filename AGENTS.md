# Affiliate video coordination

For full affiliate-video production and revisions, the user requests parallel subagent work. Delegate independent work to the existing project agents without asking again. Use at most three active subagents, subject to the session's actual limit. Small questions and edits can stay with the coordinator. Read `.agents/skills/tiktok-affiliate-video/SKILL.md` and `workflow/WORKFLOW.md` for the production requirements.

Use a pipeline rather than a barrier between every agent:
- `affiliate_script` owns research and the script; `affiliate_flow_prompt` owns scene prompts after the script and template are locked.
- The coordinator owns Google Flow interaction, generation submission, downloads, and `project.json`. Only one agent controls a shared Flow tab. Record exact model, references, generation IDs and downloaded files.
- `affiliate_visual_qa` owns `qa/`. Hand off each downloaded clip immediately for full review while the coordinator prepares or generates the next independent scene. First validate one representative scene before committing to a batch of the same technique. Downstream edits may use only clips explicitly passed by QA.
- `affiliate_post` owns narration timing, captions and baseline assembly. Prepare timing and captions from approved narration while Flow and QA run; assemble passed clips incrementally without filling rejected scenes with still images.
- `pro_video_editor` takes exclusive ownership of the CapCut draft after the baseline handoff. The assembler and editor must not mutate the same draft concurrently. Final QA runs after the exact export is saved.
- `affiliate_publishing` prepares the final post package only after that export passes. It can collect category sources earlier.

Every assignment identifies inputs, expected output paths, dependencies and ownership. Agents share a workspace: preserve other agents' changes and avoid editing another owner's files. Give focused context and reuse existing agents for follow-up work. Handoffs identify exact files and versions, not "the latest clip". Never claim a sample scan is a full QA pass.

When the same material generation defect repeats twice, reconsider references, action and camera design before another paid retry; continue independent preparation. For stalled downloads, use bounded supported waits, inspect the failure and change the download route instead of repeating the same stalled action indefinitely. Existing spending authorization and final QA requirements still apply.

Record phase start/end times, generation attempts, download delays and unresolved blockers in each run's QA notes. Report elapsed time for the actual production turn rather than the age of the chat.

The user explicitly chose ElevenLabs V3 narration and CapCut assembly on 2026-10-16, superseding the earlier Flow-speech default. Follow `workflow/VOICE-POLICY.md` and `workflow/ADAM_V3_PROMPT_SPEC.md`: use the requested Adam voice ID only after verifying availability, preserve V3 audio tags in raw TTS input and remove them from captions, and listen to the full track before approving it. Flow generates storyboard-based visuals and optional ambience without narration or a speaker. Prefer one narration track for a short video; prepare cuts/captions from actual reviewed audio timing while independent visual work continues. User-confirmed narration playback speed is 1.2x. The current ElevenLabs connector exposes no speed control: apply 1.2x once to the narration track in CapCut with pitch preservation, then align captions to that final audio. Record actual application and listening QA separately from the requested setting. Preserve historical audio provenance and existing spending boundaries; do not silently replace approved past exports.
