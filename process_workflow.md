# Video-to-Landing-Page Process Workflow

The complete end-to-end pipeline for building a premium landing page from video inspiration. This document captures every step of the process, including the ones that require human judgment.

---

## Overview

```
VIDEO INPUT ──→ FRAME EXTRACTION ──→ GRID ANALYSIS ──→ ELEMENT MAPPING
     │                                                        │
     │                                                        ▼
     │                                            SECTIONED DEEP ANALYSIS
     │                                                        │
     │                                                        ▼
     │                                            ANIMATION CLASSIFICATION
     │                                            (movement vs style-based)
     │                                                        │
     │               ┌────────────────────────────────────────┤
     │               ▼                                        ▼
     │     PROPORTION ANALYSIS                    ENGLISH ANIMATION SPECS
     │               │                                        │
     │               ▼                                        ▼
     │     SECTION MAPPING                        TECHNICAL IMPLEMENTATION
     │     (template or contextual)                           │
     │               │                                        │
     │               └──────────────┬─────────────────────────┘
     │                              ▼
     │                        BUILD PAGE
     │                              │
     │                              ▼
     └──────────────────→  MANUAL REFINEMENT
                          (scroll timing, stacked animations)
```

---

## Phase 1: Frame Extraction

**Input:** Video file (screen recording of a website, or standalone motion design)
**Output:** Raw frames at multiple FPS rates

### Step 1.1 — Extract at 2 FPS (broad overview)
```bash
ffmpeg -i input.mp4 -vf "fps=2" frames/broad/frame-%04d.jpg
```
This gives you one frame every 500ms — enough to see every section and major element.

### Step 1.2 — Extract at 10+ FPS (deep analysis, done later per section)
Run on specific time ranges after the broad scan identifies interesting sections.
```bash
python3 deep_analyze.py "input.mp4" <start> <end> --fps 10 --name <section>
```

---

## Phase 2: Grid Analysis & Element Mapping

**Input:** Broad frames from Phase 1
**Output:** Complete element inventory with coordinates

### Step 2.1 — Overlay Cartesian Grid

Overlay a fine coordinate grid on the frames. Use the highest practical resolution — the finer the grid, the better you can detect subtle movements.

**Do NOT limit to a 5×5 grid.** The grid should be fine enough that small element movements are visible across cells. Think of it as placing the frame on a Cartesian plane where every element can be precisely located.

```bash
python3 overlay_grid.py frames/broad/
```

### Step 2.2 — Broad Element Mapping (Single Pass)

Review ALL grid-overlaid frames and create a complete inventory of every visible element:

```
ELEMENT INVENTORY
─────────────────
Element: [name/description]
  First seen: frame [N] at grid position [X,Y]
  Last seen:  frame [M] at grid position [X,Y]
  Type:       [text | image | card | 3D object | chart | icon | nav | button]
  Behavior:   [static | moves | appears/disappears | style change | unknown]
```

This single pass maps the ENTIRE page. Every heading, card, image, animation, nav element — everything.

### Step 2.3 — Divide Elements into Sections

Group the elements into logical sections based on when they appear in the scroll. Each section becomes a unit for deep analysis.

**Prioritize sections for deep analysis:**
1. Start with the largest and most complex section
2. Then work through remaining sections by complexity (descending)
3. Track which sections have been analyzed and which are pending

```
SECTION BREAKDOWN
─────────────────
Section: [name]
  Frame range: [N] to [M] (~[X]s of scroll)
  Elements:    [list of elements from inventory]
  Complexity:  [high | medium | low]
  Status:      [pending | in-progress | analyzed]
```

---

## Phase 3: Sectioned Deep Analysis

**Input:** Section breakdown from Phase 2
**Output:** Per-element animation properties

For each section (starting with the most complex):

### Step 3.1 — Run Tier 2 Deep Analysis
```bash
python3 deep_analyze.py "input.mp4" <start_sec> <end_sec> --fps 10 --name <section_name>
```

### Step 3.2 — Track Element Movement (max 3 elements per pass)

Analyzing too many elements simultaneously causes failures. For each deep analysis pass:

1. Select up to 3 elements to track
2. Review composite frames to trace their movement
3. Document using the animation property format:

```
ANIMATION: [element name]
  Property:   [position | opacity | fill | rotation | scale | color | clip-path]
  Mechanism:  [progressive fill | uniform fade | scroll-mapped | staggered | etc.]
  Appears:    frame [N] at [position] — [initial state description]
  Settles:    frame [M] at [position] — [final state description]
  Travel:     [distance/direction or "none — style change only"]
  Duration:   [frame count] ÷ [fps] = [seconds]
  Drive:      [scroll-driven | time-driven | hybrid]
  Easing:     [ease-out | ease-in | linear | ease-in-out] — from diff intensity curve
  Synced with: [other elements that animate together]
```

### Step 3.3 — Repeat Passes Until All Elements Are Tracked

Run as many passes as needed (the grid overlay only needs to be generated once — it's the analysis that repeats with different element focus).

---

## Phase 4: Animation Classification

**Input:** Element tracking data from Phase 3
**Output:** Classified animation list with both behavior type and surface type

Animation classification has **two axes** — both must be identified for correct implementation:
1. **Behavior** — HOW the animation works (detected via grid analysis / diff heatmaps)
2. **Surface** — WHAT the animation is applied to (determines which technique to use)

---

### Axis 1: Behavior (How to Detect)

**Movement-Based**
Elements that change POSITION across frames. Grid analysis shows displacement.
- Slide-in, scroll parallax, carousel, staggered card entry
- These translate directly to CSS transforms / scroll-mapped position

**Style-Based**
Elements that stay in place but change APPEARANCE. Grid analysis shows NO movement — only diff heatmaps reveal coral hotspots on the element itself.
- Opacity fades, color fills, typewriter reveals, mosaic dissolutions
- **These MUST receive written English specs** (see `animation_spec_template.md`)
- Grid analysis alone will NOT capture these — you need diff heatmaps or manual identification

**Hybrid**
Elements that move AND change style simultaneously.
- Slide-in with simultaneous fade, rotate with color shift
- Document both the movement component and the style component separately

### Detection Method
1. Check diff heatmaps: yellow displacement = movement-based
2. Check diff heatmaps: coral hotspots without displacement = style-based
3. Both present = hybrid
4. If an element appears in the inventory but shows NO diff activity, it may be static or may have extremely subtle changes — flag for manual review

---

### Axis 2: Surface (What It's Applied To)

The surface type determines which implementation technique is appropriate. **Mismatching surface and technique is a common failure mode** — e.g., trying to apply a mosaic effect to text, or a typewriter effect to an image.

| Surface | Element Type | Technique | When to Use |
|---------|-------------|-----------|-------------|
| **Text** | Headlines, statements, labels | JS character splitting + scroll-mapped progress per span | High-impact copy that needs to feel "alive" — hero statements, transition sections, pull quotes. The text carries narrative weight and deserves individual character control. |
| **Image** | Product screenshots, photos, card backgrounds | DOM grid overlay (mosaic), CSS clip-path, or opacity mask | Revealing a visual asset with drama. The image itself is the payoff — the animation builds anticipation for the reveal. |
| **SVG Scene** | Process flows, diagrams, abstract illustrations | Hand-drawn SVG elements with CSS @keyframes (pulse, rotate, draw-in, flow) | Explaining abstract concepts — workflows, systems, step-by-step processes. SVGs allow individual element animation (nodes pulse, lines draw, data flows) without frame sequences. |
| **Canvas Frames** | 3D objects, cinematic product shots | Preloaded WebP sequence, scroll-driven frame index | Cinematic hero moments where a 3D object rotates or transforms. Requires pre-rendered frame sequences (from Runway/similar). Most expensive but highest fidelity. |
| **Data Viz** | Charts, gauges, counters, dashboards | SVG/DOM animated elements — see subtypes below | Metrics sections, social proof, performance dashboards. The animation IS the data — bars growing, numbers counting, gauges filling. |
| **CSS Reveal** | Cards, sections, any general content | IntersectionObserver + opacity/transform CSS transition | Default for everything that just needs to "enter" the viewport. Fade-in, slide-up, stagger. Low complexity, high reliability. |

#### Data Viz Subtypes

Data visualization sections often contain dense bento grids of animated dashboard components. Each subtype has its own technique:

| Subtype | Visual | Technique |
|---------|--------|-----------|
| **Donut/Pie chart** | Circular segments filling in | SVG `stroke-dasharray` on `<circle>`. Each segment gets `data-target` (arc length) and `data-offset` (start position). Stagger segments by 200ms. |
| **Gauge/Dial** | Clock-like hands pointing to values | CSS `transform: rotate()` with `data-rotate` attributes. Transition triggered on scroll intersection. |
| **Bar chart** | Vertical bars growing to target height | DOM elements `height: 0` → `data-height`. Stagger each bar by 60ms. |
| **Line chart** | SVG polylines showing trends | SVG `<polyline>` with `stroke-dasharray` draw-in animation or opacity fade. |
| **Counter/Number** | Large numbers counting up from zero | JS interpolation 0 → target via eased `requestAnimationFrame`. Support suffixes (+, %, M, K), decimals, and `toLocaleString()` formatting. |
| **Progress bar** | Horizontal fill bar | CSS `width: 0` → `width: N%` or `clip-path` animation. |
| **Evolution bars** | Grouped vertical bars with category labels | Same as bar chart but staggered at 150ms with label text beneath each bar. |
| **News ticker** | Scrolling horizontal text | CSS `@keyframes` with `translateX(0)` → `translateX(-50%)`, duplicated content for seamless infinite loop. |

All data viz animations are **scroll-triggered** (IntersectionObserver at ~30% threshold) and **play once**. They do NOT loop (except tickers/marquees). Each widget in a data viz bento grid animates independently when it enters the viewport, with staggered delays creating a "dashboard coming alive" effect.

When identifying a metrics/dashboard section in the reference video:
1. Identify each individual chart/widget component
2. Classify its data viz subtype from the table above
3. Note the stagger order (which widget animates first)
4. Note the target values visible in the reference (numbers, percentages, bar heights)
5. Implement each widget's animation independently with its own IntersectionObserver

### Surface Selection Rules

When analyzing a reference video and deciding which surface type to assign:

1. **Is it text that changes character-by-character?** → Text surface (typewriter, fill, scramble)
2. **Is it an image being revealed through a mask or grid?** → Image surface (mosaic, clip-path, blur-to-sharp)
3. **Is it an abstract diagram with individually animated parts?** → SVG scene (node graphs, flow diagrams, step illustrations)
4. **Is it a 3D object or cinematic product rotating/transforming?** → Canvas frames (requires asset generation pipeline)
5. **Is it numbers, bars, charts, gauges, or dashboards animating to final values?** → Data viz (identify the specific subtype)
6. **Is it content simply appearing on scroll?** → CSS reveal (the default — use this unless the animation demands more)

**Default to CSS reveal.** Only escalate to a more complex surface type when the reference video clearly shows behavior that CSS reveal can't replicate. Over-engineering animations wastes time and creates fragile code.

### Combined Classification Output

For each animation, document both axes:

```
ANIMATION: [element name]
  Behavior:  [movement | style | hybrid]
  Surface:   [text | image | svg-scene | canvas-frames | data-viz | css-reveal]
  Technique: [specific approach, e.g., "character splitting + scroll-mapped fill"]
  Spec needed: [yes — for style-based/hybrid/complex | no — for standard css-reveal]
```

---

## Phase 5: Proportion Analysis

**Input:** Grid-overlaid frames
**Output:** Element size measurements as viewport percentages

For every significant element, measure its proportions relative to the viewport:

### What to Measure
- **Width:** What percentage of the viewport width does the element span?
- **Height:** What percentage of the viewport height does the element occupy?
- **Position:** Where is it placed (top/center/bottom, left/center/right)?
- **Spacing:** How much whitespace exists between this element and adjacent ones?
- **Text scale:** How large is the text relative to the viewport width?

### How to Measure
Look at the grid-overlaid frames. The grid cells give you proportional reference:
- An element spanning 3 out of 5 columns = ~60% viewport width
- An element occupying 2 out of 5 rows = ~40% viewport height
- With a finer grid, measurements become more precise

### Output Format
```
PROPORTIONS: [section name]
───────────────────────────
Element: [name]
  Width:    ~[X]% viewport width
  Height:   ~[X]% viewport height
  Position: [top-left | center | bottom-right | etc.]
  Spacing:  ~[X]% gap above, ~[X]% gap below

Text Scale: [element name]
  Size relative to viewport: ~[X]vw equivalent
  Weight: [light | regular | medium | bold | black]
  Proportion to adjacent elements: [e.g., "3x larger than body text"]
```

### Why This Matters
The proportions define the visual hierarchy. A headline that takes up 60% viewport width communicates differently than one at 40%. These measurements become the `clamp()` values, grid fractions, and spacing tokens in the final CSS.

---

## Phase 6: English Animation Specs

**Input:** Classified animations from Phase 4
**Output:** Written specifications per animation

### When a Spec is Required
- ALL style-based animations (grid analysis can't capture them)
- ALL stacked/compound animations (multiple effects on one element)
- All animations with complex trigger logic
- Any novel animation not reducible to a standard fade/slide

### Spec Format
Use the template in `animations/animation_spec_template.md`:
1. **Objective** — what it does and why
2. **Visual Breakdown** — numbered steps from initial to final state
3. **Technical Implementation Plan** — structure, trigger, logic, CSS
4. **Edge Cases** — resize, mobile, performance, accessibility

### File Naming
Save as `animations/{animation_name}_spec.md`

### Style-Based Animations — Special Attention
These are the ones most likely to cause implementation failures because:
- There is no positional movement to reference
- The "animation" is a visual property change (opacity, color, fill, clip-path)
- Trying to pull implementation from grid analysis alone fails — the grid shows nothing moved
- The spec must describe the VISUAL EFFECT in enough detail that implementation is unambiguous

---

## Phase 7: Section Mapping

**Input:** Element inventory + animation specs + proportion analysis
**Output:** Page architecture with section-to-content mapping

### Two Approaches — Ask the User

**Option A: General Template**
If the user doesn't have specific content context, generate a templated section map based on common landing page patterns observed in the reference video:
- Map each observed section type to a generic purpose (hero, features, social proof, CTA, etc.)
- Use the proportions and animation styles from the analysis
- Let the user fill in their own content later

**Option B: Contextual Mapping**
If the user has product/brand documentation:
- Read their context documents
- Map the reference video's sections to the user's specific features/content
- Suggest which content fits which section type based on the reference's information hierarchy
- Propose the mapping, then refine based on user feedback

### Output Format
```
PAGE ARCHITECTURE
─────────────────
Section 1: [name]
  Reference: frames [N]-[M] of source video
  Purpose:   [what this section communicates]
  Layout:    [description from proportion analysis]
  Animation: [list of animations, referencing specs]
  Content:   [what goes here — from user context or template]

Section 2: [name]
  ...
```

---

## Phase 8: Build

**Input:** All outputs from Phases 1-7 + brand assets
**Output:** Coded landing page

Follow the build guide in `agent.md`:
1. Brand analysis (Part 2)
2. Page architecture from section mapping (Part 4)
3. Canvas scroll engine for animation sections (Part 6)
4. Visual polish (Part 7)
5. All code decisions must trace back to the analysis

---

## Phase 9: Manual Refinement

**These steps require human judgment and cannot be fully automated.**

### Scroll Timing
The relationship between scroll position and animation progress requires visual tuning:
- How fast should the animation play relative to scroll speed?
- At what scroll position should content overlays appear/disappear?
- Does the animation feel "right" at the current scroll-to-frame mapping?

**Process:** Build with initial estimates → user scrolls through → adjust scroll ranges → repeat.

### Stacked Animations
When two or more effects layer on the same element (e.g., typewriter fill = scroll-driven sequencing + opacity reveal + color interpolation):
- The English spec must describe the stacking explicitly
- Implementation often requires multiple passes to get the layering right
- The system may struggle to understand how effects compose — describe each layer independently, then explain how they combine

### Animation Assets
If the reference uses 3D animations that need to be generated:
- Follow the asset pipeline in `agent.md` Part 5
- Image generation (Nano Banana 2) → Video generation (Runway Gen-3) → Frame extraction (FFmpeg)
- See `animations/prompting_nano_banana.md` and `animations/prompting_runway.md`

---

## Checklist

```
[ ] Phase 1: Frames extracted at 2 FPS (broad) ✓
[ ] Phase 2: Cartesian grid overlaid ✓
[ ] Phase 2: Complete element inventory ✓
[ ] Phase 2: Sections identified and prioritized ✓
[ ] Phase 3: Deep analysis complete for all sections ✓
[ ] Phase 3: All elements tracked (3 per pass max) ✓
[ ] Phase 4: Animations classified (movement / style / hybrid) ✓
[ ] Phase 5: Proportions measured for all major elements ✓
[ ] Phase 6: English specs written for all style-based/complex animations ✓
[ ] Phase 7: Section mapping completed (template or contextual) ✓
[ ] Phase 8: Page built ✓
[ ] Phase 9: Scroll timing manually refined ✓
[ ] Phase 9: Stacked animations verified ✓
```
