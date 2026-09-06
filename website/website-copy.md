# TubeBoard Website Copy

Status: Active source map for the prepared v1.2 launch

Authoritative for: locating website copy and its release boundary

Owner: Product and design owner

Last verified: 2026-09-06

Review trigger: website implementation, accepted app features, imagery or public availability changes

## Source of truth

The implemented `index.html` and `support.html` in `olly-j/tubeboard.co.uk`
are the editable website copy authority. Continue the existing TB-088 website
PR rather than maintaining a second changing copy pack in this repository.

Current product name: **TubeBoard: Live Departures**.
Prepared v1.2 headline: **Your next train. And the stops ahead.**

## Approved narrative

The free live board covers the Underground, Elizabeth line and six named
London Overground lines. Premium adds Follow a Train, direction-aware Next
departures and By destination layouts, together with the existing paid
surfaces and new Watch widgets. Existing purchases retain access.

Route context and live-train proof remain distinct. Shared links contain
public train context, not a person's precise location or saved stations.
Never promise continuous GPS tracking, browser live tracking, reliable next
workings at termini or a redesigned global station search that has not shipped.

## Media and support

Use reviewed current captures for the homepage, feature sections and sharing
preview. Update PNG/WebP files, dimensions, alternative text, preload and
Open Graph/Twitter references together. Preserve earlier assets as history.

Support must explain Follow/data gaps, train sharing, station layouts,
Overground selection, native Watch widgets, restoration and truthful widget
freshness. Use the canonical privacy notice, with no new tracker or consent
mechanism introduced by this marketing work.

## Release boundary

TubeBoard already has a public app. The new v1.2 material is prepared for
owner review; its existence in Git does not establish App Store availability.
Deploy the v1.2 launch pages only after the matching public release is verified.
Source, approved assets pin and production revision are separate records in
the central app workspace. Use the existing guarded deployment procedure.
Do not deploy through a raw `fly deploy` or overwrite the production volume.
