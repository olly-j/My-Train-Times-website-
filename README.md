# TubeBoard Launch Assets

Production starter assets for the TubeBoard iOS launch.

Includes app icon exports, SVG mark/logo, Open Graph/hero graphics, App Store screenshot templates, social graphics, copy pack, press kit, asset inventory, and legal trust notes.

Important: TubeBoard is independent and must not imply official TfL affiliation. Do not use the TfL roundel without permission.

## Workspace Layout

- `03-Website/` is the production website and Live Activity backend service. It is a git submodule backed by `olly-j/tubeboard.co.uk` and deployed to Fly.io from that directory.
- `brand/` contains the active brand, launch, legal, press, production, and quality-review working docs.
- `website/` contains the active website planning, copy, and visual-direction working docs.
- `Brand-Package-Liquid-Glass/` is the structured brand package/archive with matching exported assets and package notes.
- `01-App-Icon/`, `02-Brand/`, `04-App-Store-Screenshots/`, `05-Social-Ads/`, `06-Press-Kit/`, and `07-Docs/` contain launch-ready asset exports and support docs.

## Production Safety

Production website and backend changes should be made inside `03-Website/`, then tested with `npm test` from that directory before deploying with `flyctl deploy`.

The Fly service stores Live Activity runtime data on the Fly volume at `/data/live-activities.json`. Do not copy, delete, or replace that volume data during asset cleanup.

## Liquid Glass Brand Package

The upgraded iOS Liquid Glass-inspired package lives in `Brand-Package-Liquid-Glass/`, with active working docs in `brand/` and `website/`.

Key production files:
- `01-App-Icon/svg/tubeboard-icon-liquid-glass-v2.svg`
- `01-App-Icon/png-v2/`
- `brand/brand-guidelines.md`
- `brand/app-store-creative.md`
- `brand/asset-production-system.md`
- `website/website-brief.md`
- `website/website-copy.md`
- `website/visual-direction.md`

Treat the original assets as v1/starter assets. Use the v2 icon and Liquid Glass package as the current creative direction, then capture real app screenshots before final App Store exports.
