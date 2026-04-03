# Atlas10X Landing Page — Design Context

This is the **single source of accumulated design intelligence** for the Atlas10X landing page. Every agent (Gemini, Claude, or human) that analyzes inspiration, brand assets, or receives feedback writes their findings here.

This document is **append-and-refine** — it grows as more context is gathered. When new analysis contradicts or updates an earlier section, update in place and note the change. Never delete context without replacing it.

---

## Status

```
Last updated: 2026-03-25
Updated by:   Claude (Claude Code)
Build status: Pre-build (context gathered, awaiting assets)
```

---

## 1. Brand Identity

_Source: `assets/brand/brand.png` — screenshot of Atlas10X product dashboard_

### Colors
| Role | Hex | Source | Notes |
|------|-----|--------|-------|
| Primary | #E8573A | Product UI — "New Analysis" button, accent highlights | Warm coral-red, very close to Platform's accent — natural fit |
| Secondary | #D4A44A | Product UI — gold/amber glow on the Atlas logo orb | Warm gold, used sparingly for premium feel |
| Accent (CTA) | #E8573A | Product UI — primary action buttons | Same as primary — single accent color system |
| Background | #0A0A0A | Product UI — main page background | Near-black, matches Platform reference |
| Background (elevated) | #1A1A1A | Product UI — card surfaces, stat boxes | Dark charcoal cards on black bg |
| Background (highlight card) | #2A1A0A | Product UI — "Analyze a brand" card | Warm dark brown with amber tint |
| Text (primary) | #FFFFFF | Product UI — headings, numbers | Pure white |
| Text (secondary) | #999999 | Product UI — labels ("BRANDS ANALYZED", "TOTAL COMPETITORS") | Medium gray |
| Text (tertiary) | #666666 | Product UI — timestamps, metadata | Darker gray for least important text |
| Border | #2A2A2A | Product UI — card borders, dividers | Very subtle, barely visible |

### Typography
| Role | Font (recommended) | Weight | Size | Tracking | Source |
|------|-------------------|--------|------|----------|--------|
| H1 (hero) | Inter or Satoshi | 800-900 | clamp(3rem, 6vw, 7rem) | -0.02em | Adapted from Platform's display titles |
| H2 (section) | Inter or Satoshi | 800-900 | clamp(2.5rem, 5vw, 5rem) | -0.02em | Platform's muted gray section titles |
| H3 (card) | Inter or Satoshi | 600 | clamp(1.25rem, 2vw, 1.5rem) | normal | Product UI card titles |
| Body | Inter or Satoshi | 400 | clamp(0.9rem, 1.1vw, 1.1rem) | normal | Clean, readable |
| Caption/label | Inter or Satoshi | 500 | 0.75rem | 0.08em (uppercase) | Product UI — "BRANDS ANALYZED" style uppercase labels |
| Nav | Inter or Satoshi | 400 | 0.9rem | normal | Minimal |
| CTA button | Inter or Satoshi | 600 | 1rem | normal | Product UI button style |
| Logo "Atlas10X" | Product's own typeface | 700 | — | tight | "Atlas" in white, "10X" bolder/larger — see logo notes |

_Note: The exact font from the Atlas10X product needs confirmation. Inter and Satoshi are both geometric sans-serifs that match the feel. Suggest using **Inter** (Google Font, free, widely supported) unless the user specifies otherwise._

### Logo
- **File**: `assets/brand/brand.png` (screenshot only — **need standalone logo file**)
- **Type**: Wordmark — "Atlas" in lighter weight + "10X" in heavier weight, with a glowing amber/gold orb icon to the left
- **Colors used in logo**: White text + amber/gold (#D4A44A) orb with radial glow
- **Placement style**: Top-left in the product UI, with "AD INTELLIGENCE PLATFORM" as a small uppercase label above
- **Dark background version**: This IS the dark version — designed for dark backgrounds
- **Above the logo**: Small label "AD INTELLIGENCE PLATFORM" in uppercase, tracked-out, small gray text with a small amber dot

### Visual Tone
- **Mode**: Dark mode (near-black backgrounds)
- **Surface treatment**: Flat with very subtle elevation (cards slightly lighter than bg, no shadows)
- **Border style**: Hairline borders (#2A2A2A), barely visible — separation by color, not lines
- **Corner radius**: Moderately rounded (8-12px on cards, 6-8px on buttons)
- **Density**: Moderate — not cramped but not ultra-spacious in the product; landing page should be more spacious
- **Overall feel**: Premium dark-mode SaaS — clean, data-rich, technical but not cold

---

## 2. Inspiration Analysis

### Reference 1: plat-form.framer.ai

- **Source**: https://plat-form.framer.ai/ (screen recording analyzed at 2 FPS, 122 frames)
- **Analyzed by**: Claude (Claude Code) via two parallel subagents
- **Date**: 2026-03-25

**What to borrow (adapting to Atlas brand):**
- Modular section template: giant muted-gray title → "00X / brand" numbered header → content → CTA row
- Scroll-driven fade-in + slide-up with ease-out easing (~0.5-1.5s per element)
- Staggered card reveals (~0.3s each, ~0.15s stagger)
- Animated chart draw-ins and counter roll-ups on scroll
- Hero particle/generative animation (canvas-based)
- Coral circle-arrow CTA button pattern (maps directly to Atlas #E8573A)
- Brand marquee section (coral bg, continuous horizontal scroll)
- Blog/content card pixel dissolution reveal effect
- Rotating circular badge in footer
- Bento dashboard grid for showcasing analytics features
- Generous section spacing (120-160px)
- FAQ accordion with sticky side panel
- Multi-row continuous marquee as visual section break

**What to skip:**
- Platform's specific 3D industrial product renders — replace with Atlas product UI screenshots and ad creative renders
- "plat-form" numbered section pattern verbatim — adapt numbering to Atlas sections
- Team member carousel — Atlas doesn't need this for a product landing page
- Pricing tier rows — not needed unless user requests
- Contact form — unless user requests

**Layout observations (to replicate):**
- Max content width ~1200-1400px, centered
- Every section follows identical template (title → header → content → CTA)
- 3-column intro row per section (number+brand | italic description | supporting text)
- Bento grid for feature/analytics sections
- Full-width marquee as dramatic section break
- Generous vertical spacing between all sections

**Animation observations (to replicate exactly):**
- See Section 5 below for full timing details
- Key principle: ALL animations are subtle. No bounce, no spring, no overshoot. Just smooth ease-out fades and slides.
- Scroll-driven elements trigger at ~20% viewport intersection
- Looping elements run independently at all times

**Premium signals:**
1. Muted gray (#707070-#888888) for section display titles — creates depth hierarchy without screaming
2. Generous whitespace — sections breathe, nothing feels cramped
3. Consistent CTA pattern (coral circle + arrow) — unified, never generic buttons
4. Animated data visualizations — charts draw in, counters roll up
5. Particle/generative hero animation — immediately signals "this is not a template"

**Mapped to Atlas sections:**
- Platform Hero → Atlas Hero (particle animation + headline + stats)
- Platform "Our Work" → Atlas "Creative Discovery" (product showcase cards)
- Platform "Our Services" → Atlas "Creative Intelligence" (accordion/tabs with detail panel)
- Platform "Smart Analytics" → Atlas "Creative Studio" or Analytics showcase (bento dashboard)
- Platform "Our Process" → Atlas "How It Works" (step carousel)
- Platform Brand Marquee → Atlas brand marquee (coral bg)
- Platform FAQ → Atlas FAQ
- Platform "Let's Talk" → Atlas CTA closer

### Reference 2: Viktor Oddy Comparison (Google Stitch vs Claude)

- **Source**: `inspiration/videos/` — screen recording of side-by-side comparison
- **Analyzed by**: Claude (Claude Code)
- **Date**: 2026-03-25

**What to borrow:**
- Iridescent/holographic 3D renders as hero visuals — adapt for Atlas product shots
- Nature/cinematic hero imagery layered behind text
- Bento-style feature grid with mixed card sizes
- Stats bar with big numbers (200+, 98%, 3.2x)

**What to skip:**
- The specific forest/nature imagery — doesn't fit Atlas's ad intelligence positioning
- Serif headlines — Atlas should stay with geometric sans-serif to match the product

---

### Merged Patterns

_Common across both references — strong signals:_

**Consistent across references:**
- Dark mode, near-black backgrounds (#0A0A0A range)
- Coral/red-orange as the single accent color
- Large bold display typography for section headings
- Bento card grids for feature showcases
- 3D product renders as visual anchors
- Generous whitespace between sections
- Stats/metrics sections with animated counters
- Single-file CTA pattern throughout

**Conflicts between references:**
- Platform uses muted gray for section titles; Viktor Oddy reference uses full white → **Go with Platform's muted gray** (more sophisticated)
- Platform uses geometric sans-serif; Viktor Oddy uses serif for headlines → **Go with sans-serif** (matches Atlas product)

**Resolution (what we're going with):**
- Atlas colors + Platform's layout/animation system
- Geometric sans-serif (Inter) throughout
- Muted gray section titles
- Coral #E8573A as sole accent (maps perfectly to Atlas brand)
- Dark mode with Platform's spacing rhythm

---

## 3. Likes & Dislikes

### Likes
| What | Why (if stated) | Reference | Date |
|------|-----------------|-----------|------|
| Platform's overall structure and animations | Chose it as the site to replicate | plat-form.framer.ai | 2026-03-25 |
| Side-by-side comparison design language | Shared as first inspiration | Viktor Oddy video | 2026-03-25 |

### Dislikes
| What | Why (if stated) | Reference | Date |
|------|-----------------|-----------|------|
| — | — | — | — |

### Explicit Requests
| Request | Date |
|---------|------|
| Replicate plat-form.framer.ai adapted for Atlas10X | 2026-03-25 |
| Keep animations, 3D elements, and loops from Platform reference | 2026-03-25 |
| Adapt colors, fonts, and content to Atlas brand | 2026-03-25 |

---

## 4. Page Architecture

_Adapted from Platform's structure, remapped to Atlas10X's three core capabilities._

### Section Map

| # | Section | Scroll Height | Animation | Content | Status |
|---|---------|---------------|-----------|---------|--------|
| — | **Loading screen** | N/A | Progress bar | Frame preloader for all canvas animations | Planned |
| 1 | **Hero** | 400vh | Canvas particle/generative animation (looping) + fade-in on load | "Never start from scratch" headline, Atlas logo, "Book a Demo" CTA, stats counters (ads analyzed, brands served, etc.) | Needs: particle animation or 3D hero asset |
| 2 | **Transition statement** | 200vh | Scroll-driven text fade-in + floating 3D shapes | Large statement: "We turn millions of real ads into your unfair advantage" + floating 3D ad creative renders | Needs: 3D renders of ad creatives |
| 3 | **Creative Discovery** | 400vh | Scroll-driven canvas animation + staggered card reveals | "001 / Atlas10X" — Showcase the ad library: semantic search, AI DNA breakdown, swipe files. Bento grid of feature cards with product UI screenshots | Needs: Product UI screenshots, possibly canvas animation of search in action |
| 4 | **Creative Intelligence** | 400vh | Accordion tabs + scroll-driven entry | "002 / Atlas10X" — Competitive analysis: paste URL → auto-analysis. Accordion with tabs showing each dimension (Visual, Vibe, Pitch, Proof, Closer). Detail panel with competitive report preview | Needs: Product UI screenshots of competitive reports |
| 5 | **Creative Studio** | 400vh | Bento dashboard grid + chart draw-ins + counter roll-ups | "003 / Atlas10X" — Ad generation from intelligence. Bento grid showing: generation workflow, before/after ad comparisons, format exports (1:1, 4:5, 9:16) | Needs: Product UI screenshots, generated ad examples |
| 6 | **How It Works** | 300vh | Carousel with step descriptions | "004 / Atlas10X" — 3-step process: Discover → Analyze → Generate. Carousel with 3D product renders per step | Needs: 3D renders or product shots per step |
| 7 | **Metrics / Social Proof** | 300vh | Counter roll-ups + chart draw-ins | Stats dashboard: ads in library, brands analyzed, time saved, creative output multiplier | Needs: real or representative numbers |
| 8 | **Brand Marquee** | auto | Continuous horizontal scroll (looping) | Multi-row "Atlas10X" wordmark + taglines on coral background | No assets needed — pure CSS/text |
| 9 | **FAQ** | auto | Accordion | Common questions about Atlas10X | No assets needed — copy only |
| 10 | **CTA Closer** | auto | Large coral headline + contact form or waitlist | "Let's Talk" or "Start Building" | No assets needed |
| 11 | **Footer** | auto | Rotating badge (looping) + smoke particle effect | Atlas logo, nav links, newsletter signup, rotating circular text badge | Needs: clean logo file |

### Navigation
- **Style**: Fixed/sticky top bar, minimal — Atlas10X logo left, hamburger menu right (coral lines)
- **Items**: Discovery, Intelligence, Studio, Pricing, Contact
- **CTA**: "Book a Demo" button (coral bg, white text)

### Responsive Strategy
- **Desktop (1440+)**: Full experience with all canvas animations, bento grids, parallax
- **Tablet (768–1439)**: Simplified grids (2-col), smaller canvas, keep scroll animations
- **Mobile (<768)**: Stack everything single-column, replace canvas animations with static hero images or simple CSS fades, keep counter animations and marquee

---

## 5. Animation & Motion

### Global Motion Language
- **Easing**: `ease-out` for all scroll-triggered entries. `linear` for all looping elements.
- **Speed feel**: Smooth and unhurried — nothing snappy or bouncy. Premium and deliberate.
- **Scroll-driven vs CSS**: Section entries are scroll-driven (tied to scroll position). Marquees, particles, and badges are CSS/JS loops (time-driven, always running).
- **Parallax layers**: None — everything scrolls at uniform speed (matching Platform reference).
- **Trigger threshold**: Elements begin animating at ~20% viewport intersection.

### Scroll-Driven Animations (per element type)
| Element | Effect | Duration | Easing | Stagger |
|---------|--------|----------|--------|---------|
| Section display title | Fade-in + slide-up (20px) | 1–1.5s | ease-out | — |
| Section subtitle / description | Fade-in + slide-up (15px) | 0.5–1s | ease-out | simultaneous with title |
| Feature cards (bento grid) | Fade-in + slide-up (20px) | 0.3s each | ease-out | 0.15s between cards |
| Dashboard cards (analytics) | Fade-in + slight scale-up (0.95→1) | 0.3s each | ease-out | 0.1s between cards |
| Charts (donut, line, bar) | Draw-in / fill animation | ~1s | ease-out | — |
| Counter numbers | Roll-up from 0 to target | ~1s | ease-out | — |
| Blog/content images | Pixel dissolution (grid overlay fades away) | 1–1.5s | linear to ease-out | — |
| CTA rows | Fade-in | 0.5s | ease-out | — |

### Looping Animations (always running)
| Element | Effect | Speed / Duration | Technology |
|---------|--------|-----------------|------------|
| Hero particle system | Generative particle field, horizontal band, organic drift | Continuous/procedural | Canvas/WebGL |
| Stats ticker | Horizontal marquee | ~100-160px/s | CSS translateX |
| Brand marquee (coral section) | Multi-row horizontal scroll | ~100-160px/s per row | CSS translateX |
| Footer circular badge | Slow rotation of text around a circle | ~15-20s per revolution | CSS rotate |
| Footer smoke/particles | Subtle particle drift behind logo | Continuous | Canvas or CSS |

### Page Load Animation
| Element | Effect | Duration | Delay | Easing |
|---------|--------|----------|-------|--------|
| Hero headline | Fade-in (opacity 0→1) + slide-up (10px) | 1.5s | 0s | ease-out |
| Hero stats | Counter roll-up | 1s | 0.3s | ease-out |
| Hero secondary elements (CTA, nav) | Fade-in | 0.8s | 0.5s | ease-out |
| Hero particle system | Starts immediately | — | 0s | — |

### Section Display Title Treatment
Platform uses muted gray (#707070-#888888) for its massive section titles. This is a signature design choice. For Atlas:
- Use `color: #707070` for section display titles
- These are NOT meant to be high-contrast — they create a subtle depth layer
- The actual content (subtitles, cards) below is in full white/light text

---

## 6. Copy & Messaging

### Hero
- **Headline**: "— The smarter way to **discover, analyze,** and **create** winning ads."
- **Subheadline**: "Atlas10X turns millions of real ads and competitor strategies into your creative advantage."
- **CTA text**: "Book a Demo"
- **Secondary CTA**: "See Atlas in action" → "Join our guided tour and explore all features live."

### Section Headlines
| Section | Display Title (muted gray) | Subtitle (white) | Right Description (gray) |
|---------|---------------------------|-------------------|--------------------------|
| Creative Discovery | Creative Discovery | The world's smartest ad library. Search by concept, emotion, or visual style — not keywords. | Every winning ad in your market, analyzed and ready to inspire your next campaign. |
| Creative Intelligence | Creative Intelligence | Automated competitive analysis. Paste a URL, get the full picture. | Know exactly what your competitors are running, why it works, and how to beat it. |
| Creative Studio | Creative Studio | Intelligence-driven ad generation. Never create from a blank canvas again. | Production-ready creative that's grounded in what actually works in your market. |
| How It Works | How It Works | Three steps from insight to execution. | Discover. Analyze. Generate. Repeat. |
| Metrics | By the Numbers | Real results from teams using Atlas10X. | Performance that speaks for itself. |
| FAQ | Questions & Answers | Simple answers to help you get started. | Spend less time guessing, more time creating. |

### Tone of Voice
- Confident but not arrogant. Technical but accessible.
- Short, punchy statements. No filler words.
- Emphasis on speed, intelligence, and competitive advantage.
- The em-dash "—" prefix on hero headline (borrowed from Platform) adds editorial weight.

### Messaging Angles in Use
- [x] "Never start from scratch"
- [x] "Steal like an artist. Build like an engineer." (use in transition statement or feature card)
- [x] "Creative is the new targeting" (use in metrics section or marquee)
- [ ] "Your competitors already solved your problem" (could use in Intelligence section)
- [x] "Millions in R&D, for free" (use in Discovery section or marquee)
- [x] "Ads are systems, not one-offs" (use in Studio section or marquee)

### Marquee Text (coral section)
Row 1: "Atlas10X™ — Never start from scratch"
Row 2: "Atlas10X™ — Creative is the new targeting"
Row 3: "Atlas10X™ — Millions in R&D, for free"

---

## 7. Assets Inventory

### Brand Assets
| Asset | Status | Path | Notes |
|-------|--------|------|-------|
| Logo (SVG) | **NEEDED** | `assets/logo/` | Need standalone SVG of the Atlas10X wordmark + orb |
| Logo (PNG, transparent) | **NEEDED** | `assets/logo/` | Transparent PNG fallback |
| Brand screenshot | EXISTS | `assets/brand/brand.png` | Product dashboard screenshot — used for brand analysis |
| Product UI screenshots | **NEEDED** | `assets/brand/` | Need 4-6 screenshots showing: Discovery search, Intelligence competitive report, Studio ad generation, dashboard/analytics |

### Animation Assets

Pipeline: **Nano Banana 2** (Frame 1 + Frame 2) → **Runway Gen-3 Turbo** (Video) → **FFmpeg** (WebP frames) → **Canvas scroll engine**

See `animations/prompting_nano_banana.md` for image gen prompts.
See `animations/prompting_runway.md` for video gen prompts.

| Section | Frame 1 | Frame 2 | Runway Video | Extracted Frames | Status |
|---------|---------|---------|--------------|------------------|--------|
| Hero (abstract orb) | NEEDED | NEEDED | NEEDED | NEEDED | NB2 prompt ready |
| Discovery (floating screens) | NEEDED | NEEDED | NEEDED | NEEDED | NB2 prompt ready |
| Intelligence (data cube) | NEEDED | NEEDED | NEEDED | NEEDED | NB2 prompt ready |
| Studio (cylindrical device) | NEEDED | NEEDED | NEEDED | NEEDED | NB2 prompt ready |

### Static Assets (no animation pipeline — just images)
| Asset | For Section | Status |
|-------|-------------|--------|
| Brand Marquee | Marquee section | READY — pure CSS/text, no assets |
| Footer smoke texture | Footer | READY — can be coded (CSS/Canvas) |
| Footer rotating badge | Footer | READY — can be coded (SVG/CSS) |
| Product UI screenshots (4-6) | Feature cards, bento grids | **Using dummy placeholders for Phase 1** |
| 3D feature card renders (3-5) | Bento grid cards | **Using dummy placeholders for Phase 1** — generate later via NB2 |

---

## 8. Technical Decisions

| Decision | Choice | Why | Date |
|----------|--------|-----|------|
| CSS approach | Inline (single file) | agent.md default | 2026-03-25 |
| Scroll library | None (native scroll + rAF) | agent.md rule — passive scroll listeners + separate render loop | 2026-03-25 |
| Image format | WebP | agent.md rule — 25-35% smaller than JPEG | 2026-03-25 |
| Font | Inter (Google Fonts) | Closest match to Atlas product UI, free, widely supported | 2026-03-25 |
| Hero animation | Scroll-driven canvas (Nano Banana 2 → Runway → frames) | Matches Platform reference — 3D orb rotation on scroll. Canvas particle system as fallback until frames arrive | 2026-03-25 |
| All section animations | Scroll-driven canvas (NB2 → Runway → frames) per section | Each of the 4 main sections gets its own canvas animation | 2026-03-25 |
| Section scroll reveals | Intersection Observer + CSS transitions | For text, cards, and non-canvas elements | 2026-03-25 |
| Image gen tool | Nano Banana 2 (Gemini) | See animations/prompting_nano_banana.md | 2026-03-25 |
| Video gen tool | Runway Gen-3 Alpha Turbo (First + Last Frame) | See animations/prompting_runway.md | 2026-03-25 |
| Frame extraction | FFmpeg → WebP at 24fps | ~120 frames per 5s Runway clip | 2026-03-25 |
| Marquee | CSS @keyframes translateX | No JS needed for continuous scroll | 2026-03-25 |
| Counter animations | JS — count up on Intersection Observer trigger | Standard approach | 2026-03-25 |
| Chart draw-ins | SVG stroke-dashoffset animation on IO trigger | Clean, lightweight | 2026-03-25 |

---

## 9. Revision Log

| Date | Updated by | What changed |
|------|------------|-------------|
| 2026-03-25 | Claude (Claude Code) | Initial creation — blank template |
| 2026-03-25 | Claude (Claude Code) | Full population: brand analysis from product screenshot, Platform reference analysis (122 frames), Viktor Oddy reference, page architecture, animation specs, copy, asset inventory, technical decisions |

---

## How to Use This Document

### For agents (Gemini / Claude):
1. **Before building**: Read this entire document. Every design decision must trace back to something here.
2. **After analyzing a reference**: Add your findings to Section 2, update merged patterns, and check if anything in Sections 4-6 should change.
3. **After receiving user feedback**: Update Section 3 immediately. If feedback contradicts a prior decision, update that decision and note the change in Section 9.
4. **After completing brand analysis**: Populate Section 1 fully.
5. **Before generating animation prompts**: Check Section 7 for what exists.

### For humans:
1. **To give feedback**: Just say "I like X" or "I don't like Y" — the agent will log it in Section 3.
2. **To check progress**: Look at Section 4 (page architecture) and Section 7 (assets inventory).
3. **To understand decisions**: Every choice has a "Why" — check Sections 2, 3, and 8.
