# Storyboard QA — video-02

## Run and references

- Review time: 2026-10-16 (Asia/Saigon); coordinator has not supplied separate start/end timestamps.
- Candidate: `storyboard/scene-01-v01-raw.png`, version v01, 941 × 1672 px, full frame reviewed without cropping.
- Candidate SHA-256: `FC4FE0CFB202DDC5F393643F80728C516CAE74CE47719A14DD2386EBBBC41A65`
- Product reference: `input/product-photo-2.jpg`; SHA-256 `11759576C070814851DB007027F92E3F103525AA1ABD0C10106E76F3AC9E837C`.
- Room reference: `input/background-photo-1.jpg`; SHA-256 `A299E90FD0D3106C93C19A4A838D9F3B9A5ACB712B048B7BDB1E9DEC0048AC9D`.
- Scope: this master reveal frame only. It depicts staged product placement; it is not evidence of real use or product performance.

## Scene 01 — master reveal

| Check | Finding |
|---|---|
| Product silhouette/count | Pass. Black tubular system retains two bars at different heights/depths, four upright posts, visible side hooks, two mid-height crossbars, and two broad foot assemblies with lower connecting rails. No extra rack or added shelf is visible. The silhouette matches the supplied product photo's staggered double-rack arrangement. |
| Hooks / joints / base | Pass for this still. Curved top corners and side hook forms remain visible; all four uprights continue down to the floor supports. Foot structures and lower connecting members are present. Fine construction details hidden in the source remain unclaimed. |
| Room / continuity | Pass. Tan upper wall, irregular boundary into the pale lower wall, white baseboard, and warm plank floor match the supplied room. Old wall rack, shelves, clothes, boxes, plant, and shoes have been removed as requested. |
| Light / shadows / perspective | Pass with minor inherent uncertainty from compositing. Rack feet meet the floor; contact shadows and wall shading are plausible. Floor perspective and plank direction read consistently with the room. No obvious cutout halo or floating support at full-frame viewing size. |
| Framing / safe area | Pass. Vertical 9:16 frame; all upper hooks/rails and all feet are in frame. The product fills the frame for a clear reveal, with some upper wall available for a short headline. Keep captions/CTA away from hooks, rails, and lower supports; lower safe space is limited. |
| People / artifacts | Pass. No person or hands in this generated frame, no visible lettering or invented branding, and no obvious duplicated or fused product part at full-frame inspection. |
| Continuity / claims | Master image only; other scenes not provided. Do not treat the staged empty rack as proof of load, dimensions, stability, or actual customer use. |

**Decision: PASS for this exact image as the master reveal frame only.** It may be used as the scene-01 Flow start frame. Approval is bound to the path, v01 and SHA-256 above; any edit, crop, regeneration or resize requires a new review. This does not approve any other proposed storyboard image, nor does it establish video-motion quality; the resulting Flow clip requires full video QA.

## Image-level disposition

| Scene / file | Version, SHA-256 | Product geometry/count/hooks/base | Room/light/shadow/perspective | Continuity / props | Framing / text-safe area | Humans / artifacts | Status | Finding / next action |
|---|---|---|---|---|---|---|---|---|
| scene-01 / `storyboard/scene-01-v01-raw.png` | v01, `FC4FE0CFB202DDC5F393643F80728C516CAE74CE47719A14DD2386EBBBC41A65` | pass | pass | pass; no props | pass; protect lower supports and hooks | pass | **pass** | Eligible for Flow start frame as scene-01 master reveal; review generated motion separately. |

## Record

- Product and room reference hashes: recorded above.
- Reviewed candidate set: one exact image, scene-01 only.
- QA decision: scene-01 approved for storyboard use; no scene-02/03 approval.

## Scene 02 — closer reveal / detail frame

- Candidate: `storyboard/scene-02-v01.png`, version v01, 941 × 1672 px, full frame reviewed without cropping.
- Candidate SHA-256: `9A417214D832E0B879EB9A99B2FE7AD1F2FAA69D2FCFE0AD33341919D900CCB7`.
- Product reference SHA-256: `11759576C070814851DB007027F92E3F103525AA1ABD0C10106E76F3AC9E837C`.
- Room reference SHA-256: `A299E90FD0D3106C93C19A4A838D9F3B9A5ACB712B048B7BDB1E9DEC0048AC9D`.

| Check | Finding |
|---|---|
| Product silhouette/count | Pass. The two offset rails, four uprights, side hooks, two mid-height crossbars, paired foot assemblies, and lower connecting rails remain consistent with the product photo and scene-01. No structural part is visibly missing or duplicated. |
| Hooks / joints / base | Pass. Hook shapes and curved rail corners stay legible; all uprights meet the floor supports, and lower braces are visible. No unsupported construction detail is asserted. |
| Room / continuity | Pass with minor framing shift. Same tan-to-pale wall boundary, pale wall, white baseboard, and warm plank floor. The irregular wall boundary sits slightly higher than in scene-01 and the rack is framed a little closer; this reads as a modest reframing, not a room/prop change. Keep later Flow camera motion restrained so the fixed boundary does not drift independently. |
| Light / shadows / perspective | Pass. The warm side-lit room, floor perspective, contact shadows and product orientation remain coherent with scene-01. No obvious cutout edge or floating foot at full size. |
| Framing / safe area | Pass. 9:16 frame with all rails, hooks and feet included. Product is slightly larger than scene-01; upper margin is modest and lower supports occupy the lower frame, so text must stay clear of both. |
| People / artifacts | Pass. No person/hands, visible writing or invented branding; no obvious fused or repeated parts. |
| Continuity / claims | Pass as a closer reveal/detail still. It is compositionally very similar to scene-01 and should not be presented as a distinct product demonstration. Staged placement does not verify real use, load, dimensions or stability. |

**Decision: PASS for this exact image as a storyboard frame.** Approval is bound to `scene-02-v01.png`, v01 and the hash above. It is eligible for Flow only if scene-02's purpose can use a slightly closer reveal; it offers little angle variation versus scene-01. Motion quality still requires full video QA.

## Updated image-level disposition

| Scene / file | Version, SHA-256 | Product geometry/count/hooks/base | Room/light/shadow/perspective | Continuity / props | Framing / text-safe area | Humans / artifacts | Status | Finding / next action |
|---|---|---|---|---|---|---|---|---|
| scene-01 / `storyboard/scene-01-v01-raw.png` | v01, `FC4FE0CFB202DDC5F393643F80728C516CAE74CE47719A14DD2386EBBBC41A65` | pass | pass | pass; no props | pass; protect lower supports and hooks | pass | **pass** | Eligible for Flow start frame as scene-01 master reveal; review generated motion separately. |
| scene-02 / `storyboard/scene-02-v01.png` | v01, `9A417214D832E0B879EB9A99B2FE7AD1F2FAA69D2FCFE0AD33341919D900CCB7` | pass | pass | pass; same room and no props | pass; tighter crop, keep text off rack | pass | **pass** | Eligible for scene-02 if a closer reveal is intended; framing is similar to scene-01, so it adds limited visual variety. |

- Updated reviewed set: scene-01 and scene-02 only; scene-03 is not present and is not approved.
