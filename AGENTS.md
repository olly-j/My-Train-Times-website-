# TubeBoard Assets Workspace Agent Instructions

This public repository contains TubeBoard brand assets, screenshots, launch
materials, and a pinned submodule of the website/Live Activity service. Product
work is coordinated from `olly-j/My-Train-Times` and the private TubeBoard
Delivery Project.

## Authority And Tracking

- Every change requires an owner-approved `TB-NNN` Issue in
  `olly-j/My-Train-Times`. Link PRs with
  `Relates to olly-j/My-Train-Times#NN`; do not create another backlog here.
- `docs/README.md` defines which asset and prose locations are active.
- `brand/` and `website/` contain active working guidance.
- `Brand-Package-Liquid-Glass/` is a dated June 2026 package snapshot. Preserve
  it as evidence; do not update it to simulate current product truth.
- `03-Website` pins an approved service source commit from
  `olly-j/tubeboard.co.uk/main`. The pin is not proof of production deployment;
  deployed revision truth is recorded by the app workspace and production
  `/healthz`.

## Required Work Loop

1. Read this file, `docs/README.md`, the central Issue, and the relevant active
   source before editing.
2. Start from current `origin/main` on a short-lived branch containing the
   `TB-NNN` ID.
3. Preserve unrelated assets and avoid bulk regeneration or format churn.
4. Confirm public copy, pricing, privacy, screenshots, and product claims
   against their app-repository authorities before publishing.
5. Run `scripts/check-assets.sh`. Visually inspect every changed image at its
   intended size; automated checks do not prove visual quality.
6. Reconcile the central Issue/Project and any affected app, service, website,
   metadata, or release record in the same task.

## Safety

- Never commit credentials, APNs/Fly/TfL keys, runtime token data, personal
  editor state, or disposable AI run output.
- Do not use TfL/London Underground trademarks, roundels, fonts, or maps
  without documented rights. TubeBoard must remain clearly independent.
- Do not change the `03-Website` pin until its commit is available on the
  service remote and the central Issue records whether it is source-ready or
  deployed.
- Never deploy the service or alter App Store Connect from this repository.
- Follow `.github/SECURITY.md` for vulnerabilities or credential exposure. Use
  private reporting, rotate credentials before source cleanup, and link a
  central `TB-NNN` without copying sensitive evidence into it.
- Dependency alerts, secret scanning, push protection, and private
  vulnerability reporting are enabled. Do not enable automated update PRs or
  add security workflows without a central owner-approved impact assessment.
- Use PRs, squash one coherent work item, pass the lightweight Assets Quality
  check, and delete merged branches.
