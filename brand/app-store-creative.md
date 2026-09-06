# TubeBoard App Store Creative

Status: Active v1.2 production guidance; final owner review pending

Authoritative for: screenshot narrative and asset treatment, not product access or release state

Owner: Product and design owner

Last verified: 2026-09-06

Review trigger: accepted app source, screenshot story, device specifications or feature access changes

## Copy and product authority

Use `AppStore/01-Metadata/app-store-listing.md` in `olly-j/My-Train-Times`
for editable App Store fields. The versioned exporter produces the paste-ready
files. Do not maintain another independently edited listing here.

The accepted v1.2 source is `e73d4fb926670815d921fca4d88c65a504ad581a`,
build `20260905103957`. Capture orchestration may change while the app and
extension runtime remain byte-identical to that source. This reference does
not establish public availability or App Review submission.

## Screenshot story

| Order | Headline | Required real interface |
| --- | --- | --- |
| 1 | Your next train | Populated platform board with readable station, direction and destinations |
| 2 | Follow your train | Supported train route and available live progress; Premium identified |
| 3 | Every platform | Next departures within each direction, with platform labels; Premium identified |
| 4 | London Overground | Genuine six-line catalogue or a verified named-line board; basic coverage is free |
| 5 | Heading your way | By destination station layout; Premium identified |
| 6 | Keep it in view | Native Lock Screen or Home Screen widget/Live Activity surface; Premium identified |
| 7 | Service at a glance | Genuine disruption widget with its update state; Premium identified |

The dedicated Watch set shows a native widget, departures and station choices.
A separate native visionOS set requires its own source/build and visual check.
Do not substitute phone UI in a Watch frame or present the internal Map Preview.

## Capture and composition

Capture normal text size, dark appearance, clean system chrome and populated
representative data. Deterministic fixtures must use the genuine app views;
obvious test-only station names are unsuitable for public media. A genuine
line picker can demonstrate Overground breadth without inventing a train.

Use the current licensed TubeBoard fonts, amber/black board identity and
concise benefit captions. Keep the complete interface below measured text.
Review full-size legibility and thumbnail comprehension. No generated UI,
redrawn labels, invented live states or unshipped icon concepts.

Phone exports use 1320 × 2868, iPad 2064 × 2752 and Watch 416 × 496.
Use the corresponding actual device-family capture. Preserve all earlier
release files, and retain raw captures separately from upload-ready exports.

The app repository's `compose_app_store_screenshots.py --version v1.2`
requires the complete native input inventory. `export-app-store-handoff.py`
checks its source/build binding, hashes, format, canvas and recorded visual
review. Those checks establish packaging evidence, not legal or release
acceptance. Font files are never included in consumer downloads.

## Publication

Save the reviewed images and copy in the matching App Store Connect draft.
The owner reviews and submits. Keep promotional text, public launch copy and
community announcements staged until v1.2 public availability is verified.
The v1.2.x design/icon programme is separate from this accepted app release.
