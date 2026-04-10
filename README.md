# Atlas10X Landing Page

```text
landing-page/
├── README.md
├── index.html
├── mobile.css
├── competitors.html
├── design_context.md
├── agent.md
├── animation_spec_template.md
├── replace_grid.py
├── Looping_Video_Generation_Complete.mp4
├── animations/
│   ├── animation_spec_template.md
│   ├── mosaic_animation_spec.md
│   ├── prompting_nano_banana.md
│   ├── prompting_runway.md
│   ├── typewriter_fill_spec.md
│   └── hero/
│       └── frames/
│           ├── frame-0001.webp
│           ├── ...
│           └── frame-0192.webp
└── assets/
    ├── logo/
    │   └── logo.svg
    ├── betalist_screenshots/
    │   ├── 1_dashboard.png
    │   ├── 2_analyze.png
    │   ├── 3_competitors.png
    │   ├── 4_swipe_files.png
    │   └── 5_visual_search.png
    └── brand/
        ├── brand.png
        ├── competitors.png
        ├── create.jpeg
        ├── Analyse.png
        ├── Extract.png
        ├── row_1_feature_card.png
        ├── strategic_brief.png
        ├── understand.png
        ├── visual_search.png
        ├── Row 2 card 1 (Ad DNA).png
        ├── Row 2 card 2 (Swipe Files).png
        ├── ads/
        ├── grounded generation/
        ├── iterate naturally/
        └── strategic analysis section/
```

This repository contains a static marketing landing page for Atlas10X, styled as a premium scroll-heavy product site. The implementation is intentionally simple: the page is driven directly from HTML, CSS, inline styles, inline scripts, and local image/frame assets rather than a framework build system.

## Overview

The site is centered around a single primary document, [index.html](/Users/aarizsajan/landing-page/index.html), which contains:

- page markup
- most desktop styling
- animation logic
- section transitions
- scroll-driven behaviors
- hero frame-sequence playback hooks

Responsive adjustments live in [mobile.css](/Users/aarizsajan/landing-page/mobile.css). Supporting design and production context lives in [design_context.md](/Users/aarizsajan/landing-page/design_context.md) and [agent.md](/Users/aarizsajan/landing-page/agent.md).

## Key Files

- [index.html](/Users/aarizsajan/landing-page/index.html): Main landing page implementation.
- [mobile.css](/Users/aarizsajan/landing-page/mobile.css): Mobile-specific overrides and layout fixes.
- [competitors.html](/Users/aarizsajan/landing-page/competitors.html): Secondary standalone page related to competitor-focused content.
- [design_context.md](/Users/aarizsajan/landing-page/design_context.md): Design rationale, brand notes, inspiration mapping, and section planning.
- [agent.md](/Users/aarizsajan/landing-page/agent.md): Build guidance and product/marketing context for future edits.
- [animations/](/Users/aarizsajan/landing-page/animations): Animation specs and frame assets used by the landing page.
- [assets/](/Users/aarizsajan/landing-page/assets): Product screenshots, brand imagery, and logos used throughout the site.
- [replace_grid.py](/Users/aarizsajan/landing-page/replace_grid.py): Utility script kept with the project for asset/layout support work.

## Animation Assets

The repo currently includes a frame-sequence based hero animation in [animations/hero/frames](/Users/aarizsajan/landing-page/animations/hero/frames). The page script in [index.html](/Users/aarizsajan/landing-page/index.html) references these frames for scroll or load-driven visual playback.

Animation documentation and prompts are stored alongside the assets:

- [animations/animation_spec_template.md](/Users/aarizsajan/landing-page/animations/animation_spec_template.md)
- [animations/mosaic_animation_spec.md](/Users/aarizsajan/landing-page/animations/mosaic_animation_spec.md)
- [animations/prompting_nano_banana.md](/Users/aarizsajan/landing-page/animations/prompting_nano_banana.md)
- [animations/prompting_runway.md](/Users/aarizsajan/landing-page/animations/prompting_runway.md)
- [animations/typewriter_fill_spec.md](/Users/aarizsajan/landing-page/animations/typewriter_fill_spec.md)

If you replace the frame sequence, keep naming consistent with the existing `frame-####.webp` pattern unless you also update the playback logic.

## Asset Organization

The `assets/` directory is split into two main groups:

- `assets/logo/`: brand logo files
- `assets/brand/`: product screenshots, visual references, and feature imagery used in sections across the page

There is also a `assets/betalist_screenshots/` folder containing a compact set of product screenshots that are useful for external listings, documentation, or lightweight previews.

The `assets/brand/` subtree includes multiple themed collections such as ads, grounded generation, iteration references, and strategic analysis cards. Those folders are content-heavy and should generally be treated as source media, not hand-edited code.

## Local Preview

This project does not require a build step. The simplest ways to preview it locally are:

1. Open [index.html](/Users/aarizsajan/landing-page/index.html) directly in a browser for quick inspection.
2. Serve the folder locally if browser security or asset loading becomes an issue.

Example:

```bash
cd /Users/aarizsajan/landing-page
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

## Editing Guidance

When making changes, keep these constraints in mind:

- Most of the site logic is in a single file, so even small visual changes may require editing [index.html](/Users/aarizsajan/landing-page/index.html).
- Mobile behavior is separated into [mobile.css](/Users/aarizsajan/landing-page/mobile.css), so desktop-only edits may still need mobile verification.
- Animation frame paths are hard-wired into the page script, so renaming or relocating frames will break playback unless the JS is updated too.
- The project is asset-driven. A large share of the page’s presentation depends on the images already checked into the repo.

## Recommended Workflow

1. Update copy, structure, styling, or animation references in [index.html](/Users/aarizsajan/landing-page/index.html).
2. Validate responsive behavior in [mobile.css](/Users/aarizsajan/landing-page/mobile.css).
3. Check that any new images or frame sequences are committed under `assets/` or `animations/`.
4. Review [design_context.md](/Users/aarizsajan/landing-page/design_context.md) before major visual changes so the implementation stays aligned with the intended brand direction.
5. Commit and push to `main` once local preview looks correct.

## Notes

- Empty directories are not tracked by Git, so animation folders only appear in the repo when they contain files.
- macOS metadata files like `.DS_Store` should not be committed.
- There is no package manifest, bundler config, or app framework in this repository at the moment.

## Current State

The repo is set up as a direct-edit static landing page clone/adaptation for Atlas10X. It is best suited for rapid visual iteration, asset swaps, and copy changes without introducing a build pipeline.
