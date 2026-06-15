# TubeBoard App Icon System

## App Icon Audit

Current state: the repository includes a complete flat black/amber icon system in SVG and PNG sizes. The core metaphor is correct: a live departure board, not a train, map, or official transport mark.

Keep:
- Black stage.
- Amber/yellow live-board signal.
- Abstract board rows.
- No official TfL roundel.
- No tiny text.

Improve:
- Add purposeful Liquid Glass depth.
- Create a more ownable silhouette than stacked rounded bars.
- Use LED/dot-matrix texture subtly.
- Add line-colour accents as functional traces, not logo imitation.
- Regenerate App Store icon without alpha.

Replace for launch:
- Current PNG export set, after final v2 master is approved.
- Current mark PNG, after brand mark v2 is approved.

## Final Recommended Direction

Direction: **Glass Board Signal**.

Core metaphor: a deep black glass departure-board slab with amber live rows, a vertical signal spine, small LED train-light dots, and a restrained line-colour trace at the top edge.

Why this wins:
- Instantly reads as live arrivals at small sizes.
- Avoids official TfL roundel confusion.
- Feels native to premium iOS through depth and material rather than novelty.
- Keeps the app’s actual interface promise at the center.
- Can be built as deterministic vector source and exported cleanly.

## Refined Icon Concepts

### 1. Glass Board Signal

Description: deep black glass square, raised board panel, amber row stack, left signal spine, tiny LED points on selected rows.

Layer breakdown: base black, cool glass rim, raised board, amber rows, LED dots, line-colour top trace, highlights/shadows.

Memorable because: the icon becomes a tiny platform board rather than a generic transit badge.

Not generic because: no random gradients; every glow maps to board information.

Risk: if row shapes are too similar to current icon, it can still feel flat.

Production prompt: “Premium iOS app icon, black glass departure board, amber LED rows, subtle Liquid Glass rim, tiny station-node dots, restrained London line-colour trace, no text, no official transit logo.”

Negative prompt: “roundel, TfL logo, red-blue circle, station names, tiny text, random blobs, toy train, mascot, excessive rainbow gradient, watermark.”

Export notes: build as SVG/Figma layers; export no-alpha PNG for App Store.

### 2. Station Node Countdown

Description: abstract station node grid with three amber countdown light clusters over a black board surface.

Layer breakdown: glass base, map trace, station nodes, three countdown clusters, edge highlight.

Memorable because: hints at “where is my train?” without mapping the official Tube map.

Risk: can become too abstract at 32px.

### 3. Platform Board Slab

Description: tilted slab of black glass with luminous board rows and a platform yellow header.

Layer breakdown: base, slab shadow, yellow header, amber rows, cool specular edge.

Memorable because: strongest App Store shelf impact.

Risk: perspective can reduce small-size readability.

### 4. Train-Light Perspective

Description: two amber lights moving through a dark tunnel-like board grid.

Layer breakdown: dark glass, route perspective, two light dots, row glows.

Memorable because: cinematic and emotionally commute-specific.

Risk: less directly communicates a departures app.

### 5. Abstract TB Board

Description: stacked board geometry subtly implies T/B through negative space without readable letters.

Layer breakdown: base, top platform strip, vertical signal column, amber rows, glass mask.

Memorable because: more ownable brand mark.

Risk: letter implication can become forced or decorative.

## Layer Specification

- Background layer: `#050607` with radial cool depth, no alpha in final export.
- Outer glass shell: rounded internal panel with cool rim, low-opacity white top-left highlight, deep bottom shadow.
- Board layer: raised `#0B0D0F` slab with subtle row grid.
- Light/dot layer: amber LED dots on row starts and selected row endings.
- Line-colour accent layer: four short top traces, offset and thin; never roundel-like.
- Shadow/highlight layer: amber bloom behind active rows, cool glass glint on upper edge.
- Mask layer: Apple icon mask for preview only; final source should remain square.
- Export layers: source SVG/Figma, 1024 PNG no alpha, iPhone/iPad/Spotlight/Settings/Notification PNGs, favicons, website mark.

## Export Requirements

- App Store: 1024x1024 PNG, RGB, no alpha, square corners supplied; Apple applies corner mask.
- iPhone: 180, 120.
- iPad: 167, 152.
- Spotlight: 120.
- Settings: 87, 58.
- Notification: 60, 40.
- Favicon/web: 512, 192, 32.
- Check at 1024, 180, 120, 60, 40, and 32px.
- Test on black, white, blurred wallpaper, and App Store search result backgrounds.

## Generated Concept Reference

An AI-generated concept board was created for critique and saved at:

`Brand-Package-Liquid-Glass/10-Exports/tubeboard-icon-concepts-ai-reference.png`

Use it only as exploration. Final production should use the deterministic vector direction in `Brand-Package-Liquid-Glass/03-App-Icon/tubeboard-icon-liquid-glass-v2.svg`.

