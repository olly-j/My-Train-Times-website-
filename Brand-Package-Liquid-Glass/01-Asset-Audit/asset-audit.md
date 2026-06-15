# TubeBoard Liquid Glass Asset Audit

Date: 2026-06-12

## Capability Check

Available:
- Repository file access and unrestricted file creation.
- Existing SVG/PNG/HTML/CSS inspection.
- Browser/web research for current Apple Liquid Glass references.
- Raster image generation for concept exploration.
- Vector/SVG authoring and PNG export through local tooling.
- ZIP packaging.
- Static website editing and local/browser verification.

Not present in this repository:
- iOS app source, `Assets.xcassets`, launch storyboard, SwiftUI screens, or build scheme.
- Editable design files such as Figma, Sketch, PSD, or layered Affinity documents.
- Real device screenshots from the finished app.
- Confirmed monetization, privacy policy URL, support URL, or App Store Connect metadata.

## Existing Asset Inventory

| Path | Type | Classification | Notes |
|---|---:|---|---|
| `01-App-Icon/svg/tubeboard-icon-master.svg` | SVG icon source | Improve | Clear board metaphor, but too flat and generic; needs layered glass, stronger small-size silhouette, and no alpha export for App Store. |
| `01-App-Icon/png/*` | PNG icon exports | Improve | Full size set exists. Current exports are useful placeholders but should be regenerated from the elevated master. |
| `02-Brand/svg/tubeboard-mark.svg` | SVG mark | Improve | Same as current icon; lacks independent brand distinctiveness beyond amber bars. |
| `02-Brand/svg/tubeboard-logo-horizontal.svg` | SVG logo | Improve | Functional, but typography is plain Arial and the lockup feels like a starter asset. |
| `02-Brand/png/tubeboard-mark-512.png` | PNG mark | Improve | Useful for quick placement; should be regenerated after SVG v2 is approved. |
| `03-Website/index.html` | Static site | Improve | Good structure, needs stronger conversion sections, more premium copy, and clearer roadmap labelling. |
| `03-Website/styles.css` | Static site styles | Improve | Current page has strong contrast but reads flat, sparse, and less Liquid Glass than requested. |
| `03-Website/assets/tubeboard-hero-2400x1400.png` | Hero raster | Replace for launch | Serviceable starter, but visually generic and too sparse for premium first impression. |
| `03-Website/assets/tubeboard-og-1200x630.png` | OG raster | Improve | Clear message, but thumbnail feels like a simple site capture rather than a branded share card. |
| `04-App-Store-Screenshots/templates/*.png` | Screenshot templates | Replace content, keep dimensions | Correct 1290x2796 size. Visual system is too repetitive; needs richer hierarchy, real app screenshots, and verified feature states. |
| `05-Social-Ads/*.png` | Social launch graphics | Improve | Good starting sizes. Current layouts are generic board copy with limited campaign range. |
| `06-Press-Kit/tubeboard-press-kit.md` | Press copy | Improve | Accurate but too short for press/reviewer use. |
| `07-Docs/tubeboard-asset-inventory.md` | Inventory | Archive/replace | Superseded by this audit. |
| `07-Docs/tubeboard-copy-pack.md` | Copy pack | Improve | Core tagline is good; needs ASO, FAQ, website, and campaign extensions. |
| `07-Docs/tubeboard-icon-brief.md` | Icon brief | Improve | Correct legal instincts; needs production layers, concept comparison, prompts, and export QA. |
| `09-Legal-Trust-Notes.md` | Legal notes | Keep and expand | Correct disclaimer baseline. Needs App Store, data, privacy, trademark, and screenshot risk notes. |
| `App Images/*.png` | App/launch screen images | Needs owner decision | Likely app screenshot/launch explorations. Must not be used as final App Store screenshots until matched to implemented UI. |

## Strengths

- The black/amber departure-board identity is immediately understandable.
- The product positioning is specific: live Tube arrivals, seconds-based countdowns, favourites, line colours, grouped directions.
- Existing PNG sizes cover key launch surfaces.
- Legal disclaimer already avoids official TfL implication.
- The icon avoids the official roundel and does not rely on tiny text.

## Weaknesses

- Existing assets are largely flat: black panel, yellow header, amber rows.
- Website and social visuals feel like first-pass templates rather than a premium iOS brand.
- Typography is not resolved: the logo uses generic Arial and the website relies on oversized display text without a distinctive system.
- Screenshot templates repeat the same phone state and lack strong benefit sequencing.
- No layered source system exists for future asset production.
- No QA rubric exists for small icon readability, accessibility, or App Store thumbnail performance.

## Generic Or AI-Looking Risks

- Overuse of black backgrounds with amber rectangles can read as generic transport UI.
- Smooth rounded bars are not enough to suggest LED/dot-matrix or live platform-board energy.
- Current assets lack meaningful glass refraction, edge highlights, depth hierarchy, and iOS-native material behavior.
- Future generated assets must avoid fake reflections, random glowing blobs, illegible microtext, and inconsistent light sources.

## Inconsistencies

- Icon, website, screenshots, and social assets do not share a formal glass layer model.
- Line colours appear only as small icon bars rather than a consistent information layer.
- Marketing copy alternates between “Live Tube board” and “Live Tube arrivals” without a messaging hierarchy.
- Roadmap features are mentioned in FAQ but are not clearly separated from launch features in visual assets.

## Missing Deliverables

- Final layered app icon source beyond SVG.
- App Store no-alpha 1024 export verified against Apple rules.
- Real App Store screenshots captured from the finished app.
- Premium website hero image or rendered mockup system.
- App preview scripts and motion direction.
- Social/ad campaign matrix.
- Complete press kit.
- Brand guidelines with colour, typography, glass, layout, and legal rules.
- Production checklist and naming/versioning system.

## Legal And Trademark Concerns

- Do not use the official TfL or London Underground roundel.
- Do not state or imply official endorsement.
- Line colours can be functional identifiers, but brand identity should not be built around a copied TfL lockup.
- TfL Open Data attribution and license requirements must be reviewed before launch copy is frozen.
- App Store screenshots must not show features that are not implemented unless clearly marked as concepts and excluded from final store submission.

## Accessibility Concerns

- Amber on black is strong, but amber on yellow or small grey-on-black copy can fail in thumbnails.
- Dot-matrix motifs must not degrade actual departure time readability.
- Screenshot headlines must remain readable at App Store thumbnail size.
- Website motion should respect `prefers-reduced-motion`.
- Live status/disruption colours need text labels, not colour alone.

## App Store Concerns

- App icon PNGs currently include alpha according to file metadata; App Store icons should be exported with no alpha.
- Current screenshot templates look too repetitive and may underperform in conversion.
- Roadmap-only items such as widgets, Live Activities, Dynamic Island, Apple Watch, and disruption alerts need implementation confirmation.
- “Tube” is descriptive in London context, but title/subtitle should maintain independent positioning.

## Website Concerns

- The hero works but feels sparse and starter-level.
- No clear final App Store CTA state beyond “Coming soon.”
- Feature sections are present but do not fully tell the commuter workflow.
- Trust/privacy/support content is too brief for launch credibility.
- Open Graph image should be refreshed after visual system approval.

## Priority Improvement List

1. Approve the elevated icon direction and regenerate no-alpha icon exports.
2. Capture real app screenshots from the current app build.
3. Replace repeated App Store templates with benefit-led screenshot art using real screen states.
4. Upgrade the static website with richer Liquid Glass depth, better conversion copy, and roadmap labelling.
5. Finalize legal copy: TfL attribution, privacy policy, support, and data freshness language.
6. Produce layered source files in Figma/Sketch/Affinity or equivalent.
7. Build social/ad variants from the new visual system, not from generic hero crops.

