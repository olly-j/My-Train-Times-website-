# TubeBoard Website Brief

Status: implemented release direction, 24 July 2026.

## Objective

Explain TubeBoard as a focused live-departure utility for iPhone and iPad, show the implemented app clearly, and make the Free/Premium split easy to understand before the App Store listing is public.

## Product Truth

- Title: **TubeBoard: Live Departures**
- Positioning: **Your station. Your platform. Your next train.**
- Free: live boards, search, Nearby Station, three recents, one favourite, Simple and Detailed modes, automatic refresh and three Live Activity sessions.
- Premium: unlimited favourites and Live Activities, Dynamic Island and StandBy, Home/Lock Screen widgets, Time to Leave, and platform headers coloured by Tube line.
- UK pricing: £1.99 monthly; £9.99 yearly with a 7-day trial and Family Sharing; £24.99 lifetime with Family Sharing.
- The former four-theme offer is retired and must not appear.
- The public App Store URL is not yet verified, so the release CTA remains “coming soon”.

## Experience Principles

- Light by default; dark only where the real board or Premium comparison benefits from it.
- Real app captures are the visual evidence. Do not invent device UI or roadmap features.
- Use the system font stack. Do not ship the unverified London Underground webfont.
- Use journey-led page structure, ruled lists and comparison tables rather than generic card grids.
- No decorative gradients, glass panels, blobs, fake metrics, tickers or universal scroll animation.
- Accessibility: semantic headings, 44px targets, visible focus, reduced motion, labelled colour states and no horizontal page overflow from 320px.

## Page Structure

1. Product-led hero with real live board.
2. Live-board explanation and product principles.
3. Station search.
4. Simple/Detailed modes.
5. Favourites and Time to Leave.
6. Live Activities, Dynamic Island, StandBy and widgets.
7. Exact Premium features and pricing.
8. Privacy, trust and FAQ.
9. Support and legal attribution.

## Technical Release

- Existing Node/Fly service remains the production architecture because it also hosts the Live Activity API and worker.
- Apex `https://tubeboard.co.uk` is canonical; `www` redirects with 308.
- HTML revalidates; versioned assets are immutable.
- Security headers, branded 404, WebP imagery, canonical support/privacy routes and `/healthz` are required.
- Inactive Live Activity records are physically deleted after the 24-hour retention window; active registrations last no more than eight hours.
