# TubeBoard Brand Guidelines

## Brand Essence

Product promise: the platform board, clarified for the iPhone. TubeBoard gives London commuters a fast, glanceable way to check live Tube departures without opening a route planner.

Audience: London commuters, visitors who already know their station, people managing regular journeys, and Tube users who value speed over feature bloat.

Tone: precise, calm, independent, useful, quietly premium.

Emotional feel: the relief of seeing the board before you reach the platform.

Visual feel: black glass, amber LEDs, platform yellow, cool translucent chrome, line-colour signals, and crisp live countdowns.

Memorable hook: an independent amber departure board mark inside a deep glass iOS icon, not an official roundel.

## Visual Principles

- Functional glass, not decoration.
- Depth must explain interface hierarchy: background, chrome, board, live data, controls.
- Departure information stays sharp, dark, and high contrast.
- Amber/yellow owns the board identity.
- Tube line colours are information accents, not a logo system.
- Black is the stage; glass is the interface; amber is the live signal.
- Avoid fake official TfL identity and avoid red/blue roundel compositions.
- Avoid generic AI polish: no random glossy blobs, inconsistent reflections, or unreadable micro typography.

## Liquid Glass System

Use a forward-looking iOS Liquid Glass-inspired system grounded in current Apple material guidance: translucent surfaces, environmental response, edge highlights, and layered depth. Treat “iOS 27” as an art direction label, not a claim of a public Apple design spec.

### Layers

- Level 0: Deep board black. Used for live data backgrounds and app icon base.
- Level 1: Atmospheric depth. Subtle map/circuit traces, line glows, and station-node dots.
- Level 2: Functional glass panels. Navigation, CTA panels, screenshot frames, app chrome.
- Level 3: Board content. Station names, directions, arrival rows, countdowns.
- Level 4: Live signal. Amber LED rows, seconds countdowns, warning badges, refresh states.
- Level 5: Highlights. Hairline glass rim, specular corner glints, very soft inner glow.

### Material Rules

- Glass opacity: 8-18% white over black, 20-34% for large hero panels, never over live departure text.
- Blur: use for chrome and marketing frames; never blur the actual departure board.
- Edge highlights: 1px white at 14-28% opacity, with a warmer amber edge only near live board elements.
- Inner glow: amber glow below 16% opacity, localized around live rows and dots.
- Shadow: deep black shadow plus very soft amber bloom; avoid heavy plastic bevels.
- Refraction: use slight displacement-like visual cues in hero/media assets, not in production text surfaces.
- Motion: glass should slide and settle; board rows should tick or refresh with restrained LED behavior.

### Where Glass Is Used

- Website hero panels and device mockups.
- App navigation chrome, settings, menus, and non-critical controls.
- App Store screenshot frames and captions.
- Social/ad overlays and campaign cards.
- Icon depth layers and outer shell.
- CTA cards and feature tiles.

### Where Glass Is Not Used

- Live train times.
- Countdown digits.
- Platform headings.
- Station names.
- Line status warnings.
- Any surface where translucency would reduce emergency/disruption readability.

## Colour System

| Token | Hex | Use |
|---|---:|---|
| Board Black | `#050607` | Core background, icon base, departure board. |
| Signal Black | `#0B0D0F` | Raised board panels, phone screen. |
| Glass Stroke | `#2A3036` | Subtle panel borders and icon frame. |
| Board Amber | `#FFB000` | Primary live departure signal, CTA, time values. |
| Platform Yellow | `#FFE100` | High-priority strips, platform header, App Store headline accent. |
| Warm Cream | `#F6F1DD` | Primary text on dark. |
| Muted Rail | `#98A1AA` | Secondary copy, metadata. |
| Cool Glass | `#D8F3FF` | Specular glass highlights, hover glints. |
| Disruption Red | `#E32017` | Disruption/status only, not brand. |
| Service Green | `#00B050` | Good service confirmation. |
| Shadow Blue | `#07121C` | Deep glass shadow and cool depth. |

Line colours may be used for functional line identity. Keep them as thin strips, badges, or station-state indicators; never arrange them into an official-looking lockup.

Accessibility: primary body text on board black should meet WCAG AA. Avoid yellow text on amber. Pair colour-coded status with labels.

## Typography System

- Primary UI: SF Pro or the platform system font.
- Display: SF Pro Display or a premium geometric sans with strong numerals.
- Board numerals: tabular figures, high weight, high contrast.
- Dot-matrix motif: decorative only, used in backgrounds, dividers, or oversized campaign lettering. Do not use dot-matrix for essential small copy.
- Website: system stack with tight but not negative letter spacing. Use strong hierarchy, not novelty type.
- App Store screenshots: large human benefit headline, concise support line, no paragraph blocks.
- Accessibility: support Dynamic Type in the app; avoid fixed-size text in screenshots that mimics UI controls.

## Layout System

- Spacing: 8px base grid; major sections use 48/72/96px rhythm.
- Radius: icon uses Apple mask externally; internal glass panels use 18-32px; cards should not become pill-shaped unless they are controls.
- Board rows: fixed height, tabular countdowns right-aligned.
- Hero layout: first viewport must show brand, live board, CTA, and a hint of next section.
- Icon safe area: keep critical motif inside central 72% with strong silhouette at 32px.
- Screenshot composition: headline top third, phone/screen central, proof/detail lower third where needed.
- Website rhythm: alternate dense functional demo sections with trust/privacy copy; avoid decorative nested cards.

## Motifs

- Train-light dots: small amber points moving along map traces.
- Platform-board rows: stacked luminous rows with clipped ends and subtle LED texture.
- Circuit-map traces: abstracted route lines, never a literal TfL map.
- Line badges: functional chips with labels in app UI only; colour alone is not sufficient.
- Countdown digits: tabular, amber, confident.
- Station nodes: small circular stops used as background texture or navigation indicators.
- Page dots/home indicator: iOS ecosystem references in mockups.
- London night commute: reflected lights, black platform atmosphere, but no official station signage impersonation.

## Usage Standards

- Always include the independent/TfL disclaimer in legal, footer, press, and App Store review materials.
- Use “Powered by TfL Open Data where available” only after confirming the exact attribution requirement.
- Do not use the generated concept board as final production art without cleanup.
- Launch App Store screenshots must use real app screens or clearly approved implemented states.

