# TubeBoard Launch Assets

Current TubeBoard media sources and versioned launch assets. Earlier starter exports remain historical references.

Includes app icon exports, SVG mark/logo, Open Graph/hero graphics, App Store screenshot templates, social graphics, copy pack, press kit, asset inventory, and legal trust notes.

Read `AGENTS.md` before contributing and `docs/README.md` for the active
source-of-truth map. Product work and owner decisions are tracked centrally in
`olly-j/My-Train-Times`; this repository does not maintain another backlog.

Important: TubeBoard is independent and must not imply official TfL affiliation. Do not use the TfL roundel without permission.

## Workspace Layout

- `03-Website/` pins an approved `olly-j/tubeboard.co.uk/main` source commit.
  Fly production revision is verified separately through `/healthz`; the
  gitlink alone does not prove deployment. The assets check fetches complete
  `main` ancestry before validating the pin, including in shallow CI clones.
- `brand/` contains the active brand, launch, legal, press, production, and quality-review working docs.
- `website/` contains the active website planning, copy, and visual-direction working docs.
- `Brand-Package-Liquid-Glass/` is the structured brand package/archive with matching exported assets and package notes.
- `01-App-Icon/`, `02-Brand/`, `04-App-Store-Screenshots/`, `05-Social-Ads/`, `06-Press-Kit/`, and `07-Docs/` contain launch-ready asset exports and support docs.

## Repository Relationship

The iOS app lives in a separate repository: `olly-j/My-Train-Times` (locally `~/Documents/GitHub/My Train Times`). This repo holds launch assets, and the production website/backend lives in the `03-Website/` submodule backed by a third repository, `olly-j/tubeboard.co.uk`. Changes that affect both the app and the site (for example privacy-policy wording, support copy, or the Live Activity API contract) must be kept in sync across repos — see `docs/website-repo-and-deploy.md` in the app repo for the end-to-end update procedure.

## Production Safety

Production website and backend changes belong in the separate service repository. Run `npm run check` and use its guarded `scripts/deploy-production.sh --confirm-production` procedure from clean current `main`, after the applicable owner and release gates. A raw deploy is not the normal path.

Repository checks reject tracked environment variants such as `.env.local`
and `.env.production` as well as keys, certificates, runtime data, and personal
workspace files. `.env.example` remains the only allowed environment template.

Publishing requires BOTH steps — a GitHub push alone does not update the live site:

1. Complete and merge the service PR into `olly-j/tubeboard.co.uk/main`, then
   update this repository's submodule pointer through its own PR.
2. Only after explicit owner authorization, deploy from service `main` with
   `scripts/deploy-production.sh --confirm-production`. There is no
   push-triggered auto-deploy.

The Fly service stores Live Activity runtime data on the Fly volume at `/data/live-activities.json`. Do not copy, delete, or replace that volume data during asset cleanup.

## Liquid Glass Brand Package

The June 2026 Liquid Glass package in `Brand-Package-Liquid-Glass/` is an archived snapshot. Active working guidance lives in `brand/` and `website/`.

Key production files:
- `01-App-Icon/svg/tubeboard-icon-liquid-glass-v2.svg`
- `01-App-Icon/png-v2/`
- `brand/brand-guidelines.md`
- `brand/app-store-creative.md`
- `brand/asset-production-system.md`
- `website/website-brief.md`
- `website/website-copy.md`
- `website/visual-direction.md`

Treat the original exports as starter/history assets. The app icon embedded in the accepted app build is the release authority; unselected v1.2.x concepts must not replace it. Use real accepted-source captures for the new versioned media set and retain its provenance. App Store Connect draft preparation does not establish public availability.
