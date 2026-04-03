# Atlas10X — 3D Animated Landing Page Build Guide

You are building a premium, scroll-driven 3D animated landing page for **Atlas10X** — a creative intelligence platform for performance marketers. This page must feel like an Apple product page: cinematic, scroll-controlled animations with content that reveals as the user scrolls.

This document defines **how** to build. The companion file `design_context.md` is your **accumulated design intelligence** — all brand analysis, inspiration findings, user preferences, likes/dislikes, copy decisions, and asset status live there. Read both before building. Write to `design_context.md` every time you analyze something or receive feedback.

---

## Part 1 — What You're Building For

### Atlas10X in One Line
A creative intelligence platform that helps performance marketers and brands never start from scratch — turning millions of real ads, competitor strategies, and proven creative formulas into a machine for producing high-converting ads at speed.

### The Three Core Capabilities to Showcase

**1. Creative Discovery — "The World's Smartest Ad Library"**
- Semantic search across millions of real ads by concept, emotion, visual style — not keywords
- AI "DNA breakdown" of every ad: what hook it uses, what emotion it triggers, what proof it offers, how it closes
- Personal swipe files organized by strategy

**2. Creative Intelligence — "Your Automated Competitive War Room"**
- Paste a URL → Atlas auto-extracts brand DNA, discovers 25 competitors, pulls all live Facebook ads
- Analyzes every ad across 5 dimensions: Visual, Vibe, Pitch, Proof, Closer
- Generates strategic reports: positioning maps, threat assessments, vulnerabilities, remix recipes

**3. Creative Studio — "Intelligence-Driven Ad Generation"**
- Generates ads from competitive intelligence + reference images — not from nothing
- AI creative director proposes 2–3 distinct directions
- Production-ready output, no "AI slop" — grounded in real reference images
- Conversational refinement ("Make the logo bigger," "Add more urgency")

### Core Messaging Angles (use in headlines/copy)
- "Never start from scratch"
- "Steal like an artist. Build like an engineer."
- "Creative is the new targeting"
- "Your competitors already solved your problem"
- "Millions in R&D, for free"
- "Ads are systems, not one-offs"

### Positioning to Reinforce
Atlas10X is NOT:
- A spy tool (it analyzes strategy, not just shows what's running)
- A generic AI image generator (it's grounded in competitive intel)
- A template library (every output is custom to your market)
- A keyword-based ad library (semantic search by concept and emotion)

### Target Audience
Performance marketers, DTC brand founders, e-commerce teams, creative agencies managing multi-client ad production. They are drowning in creative production, tired of starting from blank canvases, and need a system — not another tool.

---

## Part 2 — Brand Analysis

Before building anything, you must extract the Atlas10X brand identity from the assets in `assets/brand/`. This is how the landing page stays visually consistent with the existing product and marketing.

### What the User Should Upload to `assets/brand/`

1. **Screenshots of the Atlas10X product UI** (at least 1–2) — the actual app interface. These are your primary source for colors, typography feel, and visual tone.
2. **Screenshots of the Atlas10X website / business page** (at least 1–2) — marketing site, social media page, or any public-facing brand presence. These show how the brand presents externally.
3. **Logo files** (if available) — SVG preferred, PNG acceptable. Drop into `assets/logo/`. If no standalone logo file is provided, extract it from the screenshots.

Optional but helpful:
- Brand guidelines PDF (if one exists)
- Social media banners or ad creatives
- Pitch deck screenshots

### How to Analyze Brand Assets

When brand assets are present in `assets/brand/`, perform this analysis **before writing any code**:

**Step 1 — Color Extraction**
Examine every screenshot and extract:
- **Primary color** — the dominant brand color used for CTAs, key UI elements, or the logo
- **Secondary color(s)** — supporting colors used for accents, highlights, or secondary actions
- **Background color(s)** — the base surface colors (likely dark if the product uses dark mode)
- **Text colors** — primary text, secondary/muted text, heading vs body contrast
- **Accent/highlight color** — used sparingly for emphasis, active states, or data visualization
- **Surface/card colors** — the color of elevated surfaces, modals, cards

Output these as CSS custom properties:
```css
:root {
  --color-primary: #____;
  --color-secondary: #____;
  --color-accent: #____;
  --color-bg: #____;
  --color-bg-elevated: #____;
  --color-text-primary: #____;
  --color-text-secondary: #____;
  --color-border: #____;
}
```

**Step 2 — Typography Feel**
You won't have the exact font files, so identify:
- Is the typography **geometric** (Inter, Helvetica), **humanist** (Open Sans, Lato), or **technical** (JetBrains Mono, Space Grotesk)?
- Weight distribution — are headings ultra-bold? Is body text light or medium?
- Letter-spacing tendencies — tight headlines, normal body?
- Select a Google Font that closely matches what you see. Document your choice and reasoning.

**Step 3 — Logo Extraction**
- If a standalone logo file exists in `assets/logo/`, use it directly
- If no logo file exists, examine the screenshots for the Atlas10X logo/wordmark
- Describe the logo precisely (wordmark? icon + wordmark? icon only? colors used?)
- If the logo appears on a solid background in a screenshot, note the exact placement style (top-left nav? centered? with tagline?)
- Tell the user if you need them to provide a clean logo file, and specify the format (SVG preferred, transparent PNG acceptable)

**Step 4 — Visual Tone Profile**
From all screenshots combined, determine:
- **Mode**: Dark mode / Light mode / Mixed
- **Surface treatment**: Flat / Subtle depth (soft shadows) / Glassmorphic / Neumorphic
- **Border style**: Hairline borders / No borders / Colored borders
- **Corner radius**: Sharp / Slightly rounded (4-8px) / Rounded (12-16px) / Pill-shaped
- **Density**: Spacious / Moderate / Dense
- **Overall feel**: Minimal-technical / Bold-marketing / Playful / Corporate

**Step 5 — Output Brand Summary**
Before proceeding to build, output a brief brand summary:
```
BRAND ANALYSIS
─────────────
Colors:     [list extracted palette]
Typography: [selected Google Font + reasoning]
Logo:       [status — file available / needs extraction / user needs to provide]
Mode:       [dark/light]
Tone:       [2-3 word description, e.g. "minimal dark-mode technical"]
Radius:     [corner radius]
Surfaces:   [treatment style]
```

This summary becomes the design system for the entire landing page. Every color, font, and stylistic decision in the build must trace back to this analysis. Do not invent colors or guess — if the screenshots are insufficient, ask the user for more.

### If No Brand Assets Are Provided
Do not guess. Ask the user to upload at least one screenshot of the Atlas10X product or business page to `assets/brand/`. Without brand assets, fall back to the default (Part 3's "When No Inspiration Is Provided" defaults), but explicitly flag that the design is not brand-aligned.

---

## Part 3 — Inspiration & Reference Handling


You will receive inspiration in the form of **links, images, videos, and files**. Here is how to process each:

### Links (URLs to live sites)
Follow the full instructions in `inspiration/links/README.md`. Summary:
1. Screenshots must be captured first — you cannot analyze a URL visually without them
2. Ask the user to run `python inspiration/links/capture_url.py <url>` to capture full-page screenshots at desktop/tablet/mobile viewports
3. If Playwright isn't available, ask the user to manually screenshot the page via Chrome DevTools (Cmd+Shift+P → "Capture full size screenshot")
4. Once screenshots exist in `inspiration/links/<site-name>/`, read them and perform the full visual analysis (layout, color, typography, spacing, animation, premium signals)
5. Output a structured **Design Brief** per the format in `inspiration/links/README.md`
6. Optionally supplement with `url_context` (Gemini) to analyze source HTML/CSS/JS — but visual analysis from screenshots always takes priority for design decisions

### Images (screenshots, mockups, design references)
1. Analyze composition, color palette, typography style, spacing, visual hierarchy
2. Identify what makes the design feel premium (contrast, whitespace, type scale, depth)
3. Apply the visual language to Atlas10X's brand — adapt, don't replicate

### Videos (animation references, scroll demos, product walkthroughs)
1. If it's a reference for scroll animation: extract keyframes, analyze the motion arc, timing, and easing
2. If it's a product demo: note the UI being shown, what features are highlighted, and the narrative flow
3. If it's for the asset pipeline: follow the frame extraction process in Part 5

### Files (PDFs, design specs, brand guidelines)
1. Extract relevant constraints: colors, fonts, logo usage, tone of voice
2. Apply as hard rules — brand guidelines override aesthetic preferences

### When No Inspiration Is Provided
Default to: dark mode, minimal, cinematic. Think Apple product pages meets Linear's marketing site. Deep blacks/charcoals, one accent color, large bold type, generous whitespace, slow deliberate animations.

---

## Part 4 — Page Architecture

The landing page follows a **scroll-driven narrative structure**. Each section occupies a tall scroll container with sticky content that animates as the user scrolls through.

### Recommended Section Flow

```
1. Hero — Full-viewport 3D animation + headline + CTA
2. Problem — The pain of starting from scratch (scroll-triggered text reveals)
3. Discovery — Showcase the ad library with scroll-driven product animation
4. Intelligence — Competitive analysis demo with scroll-driven animation
5. Studio — Ad generation showcase with scroll-driven animation
6. Social Proof — Logos, quotes, metrics (subtle parallax)
7. CTA — Final conversion section
```

Each of sections 3, 4, and 5 should have its own scroll-driven canvas animation showing the product in action. These are the hero moments of the page.

### Layout Rules
- **Max content width**: 1200px, centered
- **Scroll containers**: 300vh–500vh each (adjust per animation complexity)
- **Sticky wrappers**: `position: sticky; top: 0; height: 100vh;`
- **Content overlays**: Glassmorphic cards or clean text blocks that appear/disappear at scroll ranges
- **Typography**: Large headlines (clamp(2.5rem, 5vw, 5rem)), clean body text, high contrast
- **Spacing**: Generous — at least 120px between major sections
- **Mobile**: Stack layouts, reduce scroll container heights, consider replacing canvas animations with static hero images or CSS animations on mobile

---

## Part 5 — 3D Animation Asset Pipeline

There are two paths depending on what assets are available:

### Path A — Video Provided (MP4/MOV of 3D animation)

Extract frames and build the scroll canvas directly:

```bash
ffmpeg -i animation.mp4 -vf "fps=30" -quality 80 frames/frame-%04d.webp
```

- Target 120–200 frames per animation section
- Always use WebP (25–35% smaller than JPEG)
- Quality 75–85 is the sweet spot

### Path B — No Video, Generate from Reference

Follow this pipeline to create the animation from scratch:

**Step 1: Analyze reference** (vision model)
Upload the reference video/images and extract:
- Subject, starting pose, ending pose, motion arc, visual style, lighting setup, camera behavior

Use this prompt:
```
You are analyzing a reference video for a scroll-driven 3D product animation.
Examine the provided frames and describe:
1. The subject — what is the object, what does it look like?
2. The starting frame — exact angle, orientation, lighting, background
3. The ending frame — exact angle, orientation, lighting, background
4. The motion arc — how does the object transform between start and end?
5. The visual style — rendering style, color palette, mood
6. The lighting setup — key light, rim lights, reflections
7. Camera behavior — does the camera move, or does the object?
Be precise. Output will be used for image/video generation prompts.
```

**Step 2: Generate Frame 1** (image gen model)
Write a detailed prompt for the starting keyframe:
```
[Subject], [starting orientation], [lighting], [background], [visual style], [camera/render feel], [mood]
```

**Step 3: Generate Frame 2** (image editor — edit of Frame 1, NOT a new image)
```
Using [Frame 1] as reference, modify it so that: [orientation/angle/lighting changes].
Keep [subject identity, style, background, materials] exactly the same.
```

**Step 4: Generate transition video** (video gen model)
```
Starting with [Frame 1 description], ending with [Frame 2 description],
create a smooth [X]-second transition. [Motion arc]. [Camera behavior].
[Lighting shifts]. No cuts.
```

**Step 5: User generates assets externally, returns:**
- `frame_01.webp`, `frame_02.webp`, `animation.mp4`

**Step 6: Extract frames**
```bash
ffmpeg -i animation.mp4 -vf "fps=30" frames/frame-%04d.webp
```

---

## Part 6 — Canvas Scroll Engine (Technical Implementation)

This is the exact architecture to use for every scroll-driven animation section. Do not deviate.

### HTML Structure
```html
<section class="scroll-section" id="section-discovery">
  <div class="sticky-wrapper">
    <canvas id="canvas-discovery"></canvas>
    <div class="content-overlay" id="phase-1">
      <!-- Info card content -->
    </div>
    <div class="content-overlay" id="phase-2">
      <!-- Info card content -->
    </div>
  </div>
</section>
```

### CSS Layout
```css
.scroll-section {
  height: 400vh; /* scroll runway — adjust per section */
  position: relative;
}

.sticky-wrapper {
  position: sticky;
  top: 0;
  height: 100vh;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.scroll-section canvas {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  max-width: 100%;
  max-height: 100%;
}
```

### Frame Preloading (batch — never fire all at once)
```js
const TOTAL = 160;
const BATCH = 20;
const frames = [];

async function preloadFrames(basePath) {
  for (let i = 0; i < TOTAL; i += BATCH) {
    const batch = [];
    for (let j = i; j < Math.min(i + BATCH, TOTAL); j++) {
      batch.push(new Promise((resolve, reject) => {
        const img = new Image();
        img.onload = () => { frames[j] = img; resolve(); };
        img.onerror = reject;
        img.src = `${basePath}/frame-${String(j + 1).padStart(4, '0')}.webp`;
      }));
    }
    await Promise.all(batch);
    updateLoadingProgress(Math.min(i + BATCH, TOTAL), TOTAL);
  }
}
```

### Scroll Calculation (passive — never blocks scrolling)
```js
function getScrollProgress(section) {
  const rect = section.getBoundingClientRect();
  const progress = -rect.top / (rect.height - window.innerHeight);
  return Math.max(0, Math.min(1, progress));
}

window.addEventListener('scroll', () => {
  const progress = getScrollProgress(section);
  currentFrame = Math.min(Math.floor(progress * TOTAL), TOTAL - 1);
}, { passive: true });
```

### Rendering (separate rAF loop — never draw inside scroll handler)
```js
let currentFrame = 0;
let drawnFrame = -1;

function tick() {
  if (currentFrame !== drawnFrame && frames[currentFrame]) {
    ctx.drawImage(frames[currentFrame], 0, 0, canvas.width, canvas.height);
    drawnFrame = currentFrame;
  }
  requestAnimationFrame(tick);
}
tick();
```

### Content Overlays (tied to scroll position, never timers)
```js
const phases = [
  { el: document.getElementById('phase-1'), start: 0.08, end: 0.24 },
  { el: document.getElementById('phase-2'), start: 0.28, end: 0.46 },
  { el: document.getElementById('phase-3'), start: 0.50, end: 0.68 },
  { el: document.getElementById('phase-4'), start: 0.72, end: 0.92 },
];

// Inside scroll handler:
for (const phase of phases) {
  phase.el.classList.toggle('visible', progress >= phase.start && progress <= phase.end);
}
```

---

## Part 7 — Visual Polish

### Canvas Masking (soft-edge the animation into the background)
```css
canvas {
  mask-image: radial-gradient(ellipse 65% 60% at 52% 50%, black 40%, transparent 75%);
  -webkit-mask-image: radial-gradient(ellipse 65% 60% at 52% 50%, black 40%, transparent 75%);
}
```

### Scroll-Driven Rotation (subtle 3D feel on 2D canvas)
```js
const rotation = -4 + progress * 12;
canvas.style.transform = `translate(-50%, -50%) rotate(${rotation}deg)`;
```

### Glassmorphic Overlay Cards
```css
.content-overlay {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 16px;
  padding: 2rem;
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.5s ease, transform 0.5s ease;
}

.content-overlay.visible {
  opacity: 1;
  transform: translateY(0);
}
```

### Loading Screen
Always show a loading screen while frames preload. The user must never see a blank canvas or incomplete animation. Show a progress percentage. Only reveal the page once ALL frames for ALL sections are loaded.

### Scroll Progress Bar
```css
.progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  height: 3px;
  background: var(--accent-color);
  z-index: 9999;
  transform-origin: left;
  will-change: transform;
}
```

---

## Part 8 — Hard Rules

### DO
- Use `<canvas>` for all scroll-driven animations
- Preload ALL frames before removing loading screen
- Use `{ passive: true }` on all scroll listeners
- Separate scroll calculation from canvas rendering (rAF loop)
- Use `position: sticky` + tall scroll containers
- Use WebP for all frame images
- Tie content overlays to scroll position ranges
- Keep frame count between 120–200 per section
- Build mobile-responsive — degrade gracefully

### DO NOT
- Use `<video>` elements for scroll-driven animation
- Draw to canvas inside scroll event handlers
- Lazy-load frames on scroll (preload everything)
- Use `setTimeout` or CSS `animation-delay` for content timing
- Fire all frame requests simultaneously (batch in groups of 15–20)
- Use JPG or PNG for frame sequences
- Hardcode pixel dimensions — use relative units and clamp()
- Add scroll hijacking or smooth-scroll libraries — native scroll only
- Generate "AI slop" design — no gratuitous gradients, no generic stock imagery, no hollow buzzword copy

### SINGLE-FILE RULE
Unless explicitly told otherwise, build the entire landing page as a **single `index.html` file** with inline CSS and JS. This keeps deployment simple and avoids path issues with frame assets. The only external files should be the frame image sequences in their respective `frames/` directories.

---

## Part 9 — Workflow Per Build

When asked to build or update the landing page:

1. **Read `design_context.md`** — Check what's already been gathered. Don't re-analyze what's already there.
2. **Extract brand identity** — If Section 1 of `design_context.md` is empty, run the brand analysis from Part 2 on everything in `assets/brand/`. Write results to `design_context.md` Section 1.
3. **Receive inspiration** — Analyze all provided links/images/videos/files per Part 3. Write findings to `design_context.md` Section 2. Update merged patterns.
4. **Confirm the plan** — Before writing code, state: what sections you'll build, what animations each section needs, what assets exist vs. what needs to be generated. Write the agreed architecture to `design_context.md` Section 4.
5. **Check for frame assets** — Look for existing `frames/` directories. If frames exist, use them. If not, follow Part 5 to generate the prompts the user needs to create them externally. Update `design_context.md` Section 7.
6. **Build the page** — Write the full `index.html` following Parts 4, 6, 7, and 8. All colors, typography, layout, and animation decisions must come from `design_context.md`.
7. **Test locally** — Suggest the user open the file in a browser and scroll through to verify animation smoothness and content timing.
8. **Iterate** — Adjust scroll ranges, animation pacing, and content based on feedback. Log all feedback to `design_context.md` Section 3. Log any decision changes to Section 9.

Never skip steps 1–4. Always confirm before building.

### Writing to `design_context.md`
- **After every analysis**: Update the relevant section immediately. Don't batch.
- **After every user feedback**: Update Section 3 (Likes & Dislikes) immediately. If feedback changes a prior decision, update that decision in place and log the change in Section 9.
- **Conflicts**: If new analysis contradicts existing context, flag it to the user before overwriting. The user's explicit preferences (Section 3) always win.
- **Status field**: Update the status block at the top of `design_context.md` every time you write to it.

---

## Part 10 — Project Structure

The landing page project uses this directory layout. All paths are relative to `landing_page/`.

```
landing_page/
├── agent.md                          # This file — how to build (instructions)
├── design_context.md                 # Accumulated design intelligence (read + write)
├── index.html                        # The built landing page (you create/update this)
│
├── inspiration/                      # Reference material provided by the user
│   ├── links.md                      # URLs to reference sites with notes
│   ├── images/                       # Screenshots, mockups, design references
│   └── videos/                       # Animation references, product demos
│
├── assets/                           # Brand assets
│   ├── logo/                         # Atlas10X logos (SVG, PNG)
│   └── brand/                        # Fonts, color specs, guidelines
│
└── animations/                       # One subfolder per scroll section
    ├── discovery/                    # Creative Discovery section
    │   ├── reference/                # Source video or reference images
    │   ├── keyframes/                # Generated start/end frames (frame_01.webp, frame_02.webp)
    │   └── frames/                   # Extracted frame sequence (frame-0001.webp, ...)
    ├── intelligence/                 # Creative Intelligence section
    │   ├── reference/
    │   ├── keyframes/
    │   └── frames/
    └── studio/                       # Creative Studio section
        ├── reference/
        ├── keyframes/
        └── frames/
```

### Path Conventions
- `index.html` references frames via relative paths: `animations/discovery/frames/frame-0001.webp`
- When checking for existing assets, scan `animations/{section}/frames/` for WebP files
- When generating asset prompts (Part 5), tell the user to save outputs into the correct `keyframes/` and `reference/` folders
- Brand assets in `assets/` should be referenced with relative paths in the HTML
- New inspiration goes into `inspiration/` — always check this directory when starting a build
