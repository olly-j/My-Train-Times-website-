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

## Repository Relationship

The iOS app lives in a separate repository: `olly-j/My-Train-Times` (locally `~/Documents/GitHub/My Train Times`). This repo holds launch assets, and the production website/backend lives in the `03-Website/` submodule backed by a third repository, `olly-j/tubeboard.co.uk`. Changes that affect both the app and the site (for example privacy-policy wording, support copy, or the Live Activity API contract) must be kept in sync across repos — see `docs/website-repo-and-deploy.md` in the app repo for the end-to-end update procedure.

## Production Safety

Production website and backend changes should be made inside `03-Website/`, then tested with `npm test` from that directory before deploying with `flyctl deploy`.

Publishing requires BOTH steps — a GitHub push alone does not update the live site:

1. Commit inside `03-Website/`, push its branch to `olly-j/tubeboard.co.uk`, and update the submodule pointer in this repo.
2. Deploy from inside `03-Website/` with `flyctl deploy --remote-only` (Fly.io app `tubeboard-co-uk`). There is no push-triggered auto-deploy.

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
