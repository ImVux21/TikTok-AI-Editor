# Storyboard images to Flow scenes

Use this workflow when the user asks to compose one to three product-in-room storyboard images, approve those images, then animate an approved image in Google Flow. The storyboard step and video step are separate gates: do not submit a Flow video until the exact image for that scene has passed visual review.

## 1. Make and approve the storyboard images

Create one to three **separate** storyboard images, normally one intended composition per Flow scene. Each image may combine the supplied product and background during the storyboard/image-composition stage. Review the rendered composition before video generation. Confirm product identity and visible geometry, product scale and position, background identity, perspective, lighting, crop, aspect ratio, and absence of unsupported props, text, logos, or product claims. Record requested fixes and create a new image version when needed. Only an explicitly approved version may be handed to Flow.

Do not ask Flow to combine the user's raw product photo and raw background photo. Flow receives only the approved, already-composited storyboard image(s). Keep raw source images in the provenance record and use them in the upstream storyboard composition/review; do not send them to Flow as alternate product or background references.

If a later scene needs a genuinely different camera angle, room arrangement, or product placement, create and review a separate storyboard image for that scene first. Do not ask video generation to invent unseen geometry or infer the back/side of a product from a single approved still.

## 2. Lock script, audio, and one source template

Before writing scene prompts, lock the whole-video script and scene mapping. Every Flow scene in the published video uses the same one source template selected in `video-profile.json`, with the same source file and SHA-256. Scene prefixes may vary; the source template bytes may not. Do not choose another template for a later scene.

Follow `workflow/VOICE-POLICY.md` and the user's explicit provider choice. When the user chooses ElevenLabs V3 plus CapCut, keep the exact narration and all V3 delivery tags in a separate V3 input; never paste those tags or narration into a Flow visual prompt. Prefer one whole-video V3 narration for a coherent voice. Review the actual complete audio before editing, then time cuts and captions from the recording rather than assuming the script timing is exact. Do not infer V3 authorization when the user has not chosen it for the current work.

## 3. Animate one approved image per scene

Use the exact approved image version for the corresponding scene. In Flow Frames, the default is the approved storyboard as the start frame only. An end frame is optional and must be a separately reviewed image of the intended final state. Reuse the same image as both start and end only when a deliberately stationary scene is desired. Do not add raw product or background photos to Flow; use only approved composite storyboard assets. Record the actual UI mode and ordered reference roles. Never claim a mode or setting was selected based only on an old screenshot or prompt.

With an approved storyboard, allow at most one simple, planned action that is specified in the locked script and scene plan. The action need not already be occurring in the still, but the approved storyboard must establish the relevant product geometry, object/hand contact points, and plausible movement path. If a materially different end state or interaction geometry is needed, create and review another storyboard image for that state before Flow. Preserve the approved product and room geometry. Do not orbit, tilt to reveal outside the image, zoom into a crop that hides required product details, widen the field of view, expose unseen surfaces, or fabricate depth, camera angles, room geometry, objects, or unplanned actions. When no action is planned, use only subtle crop-safe in-plane motion.

### Flow scene prefix example

Replace bracketed fields with exact reviewed filenames, version, approved scene purpose, and permitted action. This is an example prefix for one approved composite image; it is not a request to merge raw sources.

```text
Newly written scene prefix — [scene ID]

Approved storyboard start frame: [exact path and version of the approved product-plus-background image]. Its SHA-256 is [hash]. Use this one composite as the scene's visual source of truth. Flow end frame: [none / exact path and version + SHA-256 of a separately reviewed intended final-state image]. Reuse the start image as the end frame only for a deliberately stationary scene. Do not send raw product/background photos to Flow.

Scene purpose: [one sentence from the locked script]. Product and room details, perspective, relative scale, placement, lighting, and crop must match the approved storyboard. Show only approved objects and product geometry. Do not add props, logos, text, features, unseen surfaces, or claims.

Planned action: [none / one simple action from the locked script]. It need not already be happening in the start still; the approved storyboard must establish its relevant geometry, contact points, path, and intended state. Use a separately approved end frame when the final state materially differs. Motion: [one crop-safe movement]. Preserve the product and room; do not invent a new angle, orbit, tilt, room geometry, product parts, or unplanned action. Use the approved storyboard as the Flow start frame; the end frame is optional and follows the separately reviewed plan above.

Flow audio: visual clip only, with no spoken narration, dialogue, lyrics, vocalization, generated speaker, or visible speaking person. Optional nonverbal ambience only, if supported and useful; otherwise silent audio. Do not speak production directions.
```

Keep narration out of the Flow prefix. For a user-approved V3 workflow, store a separate V3 input containing the exact locked narration plus its V3 tags, for example:

```text
[V3 delivery tags, if any] [exact locked whole-video Vietnamese narration]
```

V3 tags are instructions to the V3 narration tool only. They are never dialogue or instructions for Flow. Prefer one whole-video narration; if separate takes are required by the edit, keep the same approved voice/settings and record each exact input and output. Listen to the entire generated narration and use its actual phrasing and timing for CapCut cuts and captions.

### Scene precedence override example

Put this in a separate override file and append it after the unchanged template using `--override`. It makes conflicts explicit while preserving the original source template byte-for-byte:

```text
SCENE-SPECIFIC PRECEDENCE — apply these approved constraints when any earlier source-template instruction conflicts:
1. The approved storyboard image(s) control product identity, visible geometry, room/background, perspective, composition, scale, lighting, crop, allowed props, and the states/path for the one planned action. Preserve these; do not invent or alter details.
2. The locked script controls factual claims and exact approved narration. Generate narration separately with the explicitly approved V3 tool; keep V3 tags in that V3 input only. Flow must produce no spoken words, lyrics, vocalization, or visible speaker. Optional Flow audio is nonverbal ambience only. These audio rules override conflicting source-template instructions without editing the template.
3. This scene's approved motion limits control camera movement and action. Animate only the one planned, storyboard-supported action; no other action or unseen geometry.
4. Apply the locked source template unchanged for compatible pacing, tone, and editing feel only. Do not follow any template instruction that violates items 1–3. The template itself remains unchanged for provenance and all other scenes.
```

Use the same template path and hash from the current profile. The composer accepts both current nested profile fields (`prompt_template.path` and `prompt_template.sha256`) and legacy flat fields (`template_path` and `template_sha256`). Example:

```powershell
python scripts/compose_flow_prompt.py `
  --scene projects/<date>/<product>/video-01/prompts/scene-01-prefix.txt `
  --profile projects/<date>/<product>/video-01/video-profile.json `
  --override projects/<date>/<product>/video-01/prompts/scene-01-override.txt `
  --output projects/<date>/<product>/video-01/prompts/scene-01-flow-prompt.txt
```

Composition order is prefix, locked source template unchanged, then optional scene precedence override. Without `--override`, the existing prefix-plus-template output is unchanged. The override is not a second template and must not be used to rewrite or omit source-template content.

## 4. Exact storyboard and Flow handoff record

Record one row or structured object per storyboard version and scene. Use exact paths and hashes, never “latest image” or “latest clip”.

| Stage | Required handoff fields |
|---|---|
| Source assets | Product source path + SHA-256; background source path + SHA-256; listing/script facts that are verified and claims that remain unverified |
| Storyboard | Storyboard ID; scene ID; exact file path; version; SHA-256; width × height; aspect ratio; composition tool/model and settings if generated; source asset paths/hashes; reviewer; review timestamp/time zone; pass/fail; notes on product identity, room match, geometry, perspective, crop, lighting, unwanted content; explicit approver and approval timestamp |
| Locked video plan | Script path/version/hash; exact narration; one template path/name/SHA-256; explicit audio provider choice; separate V3 input path/hash including tags; requested/selected voice and settings; whole-video audio approval status |
| Scene prompt | Prefix path/hash; override path/hash (if used); composed prompt path/hash; composer version; explicit precedence text; exact storyboard asset and Flow reference role/order; explicit no-speech/ambience-only instruction |
| Flow submission | Submission timestamp/time zone; current UI mode and settings as observed; model, aspect ratio, resolution, duration, count; ordered approved-composite reference files/roles; start frame file/version; optional end frame file/version and approval; planned action; audio mode (no speech; ambience only if used); Flow project/editor ID; generation/task ID; displayed cost; download path/hash and download timestamps/delay |
| Clip QA | Exact clip path/hash; reviewer; QA start/end timestamps/time zone; full-frame coverage and playback/audio coverage; findings with time ranges; pass/reject; approved usable in/out ranges; confirm no generated narration/speech and record any nonverbal ambience |
| Narration QA | Exact V3 input path/hash and tags; exact generated audio path/hash; reviewer; full listening coverage; heard wording/pronunciation/voice consistency and audio quality; selected voice/model/settings; pass/fix decision |
| Assembly handoff | Exact passed clip path/hash and approved range; source storyboard/prompt IDs; approved V3 audio path/hash; actual audio in/out timing for cuts and captions; EDL/caption owner; unresolved blockers |

Each image is reviewed before its Flow scene is submitted. Each downloaded clip goes immediately to full visual QA; only clips and ranges explicitly marked PASS can proceed to CapCut. Final export still requires full video QA. Preserve all source storyboard images and rejected versions for traceability.

## Compatibility notes

The DAILY VLOG source template requests several short shots and frequent angle, distance, height, and camera-position changes. A storyboard image cannot substantiate unseen views or unplanned action. Use the explicit scene precedence override to retain the source wording while following the approved storyboard(s) and script for geometry, one planned action, and camera limits. For the user's explicit ElevenLabs V3 + CapCut choice, Flow visuals contain no spoken narration or generated speaker; V3 narration and tags stay in a separate V3 input, and cuts/captions follow the approved audio. Keep only compatible daily-vlog qualities such as natural pacing, subtle handheld feel, and clean motivated cuts. Do not edit the locked template asset to resolve a conflict.
