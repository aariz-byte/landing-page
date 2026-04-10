# Animation Spec Template

Use this template to describe every animation in plain English **before** writing any code. Writing the spec forces you to understand the animation's full behavior, which prevents implementation failures — especially for style-based animations that don't show movement in grid analysis.

See `mosaic_animation_spec.md` and `typewriter_fill_spec.md` for completed examples.

---

## Classification

Before writing the spec, classify the animation on **two axes**:

### Axis 1: Behavior (how it animates)

| Type | How to detect | Grid analysis shows | Example |
|------|--------------|-------------------|---------|
| **Movement-based** | Element changes position across frames | Yellow displacement in diff heatmaps | Slide-in cards, scroll parallax, carousel |
| **Style-based** | Element stays in place but changes appearance | Coral hotspots on the element itself, no displacement | Opacity fade, color fill, typewriter reveal, mosaic dissolution |
| **Hybrid** | Element moves AND changes appearance | Yellow bands + coral internal hotspots | Slide-in with simultaneous fade, rotate with color shift |

**Style-based animations are invisible to grid position tracking.** They require diff heatmap analysis (Tier 2) or manual visual identification. When you spot an element that has coral hotspots but no positional movement in the diff, it's style-based and MUST get a written spec.

### Axis 2: Surface (what it's applied to)

The surface determines which implementation technique is valid. **Do not mismatch surface and technique.**

| Surface | Element Type | Technique | Use When |
|---------|-------------|-----------|----------|
| **Text** | Headlines, statements | Character splitting + per-span scroll-mapped progress | Copy carries narrative weight, needs character-level control |
| **Image** | Screenshots, photos, cards | DOM grid overlay (mosaic), clip-path, opacity mask | Revealing a visual asset with drama/anticipation |
| **SVG Scene** | Process flows, diagrams | Hand-drawn SVG + CSS @keyframes (pulse, draw, flow) | Abstract concepts — workflows, step-by-step, system diagrams |
| **Canvas Frames** | 3D objects, cinematic shots | Preloaded WebP sequence, scroll-driven frame index | Cinematic hero moments, requires pre-rendered frames |
| **Data Viz** | Charts, counters, gauges | SVG stroke-dasharray, height animation, JS interpolation | Metrics, social proof — the animation IS the data |
| **CSS Reveal** | Any general content | IntersectionObserver + opacity/transform transition | **Default.** Use unless reference clearly needs more |

Include both axes in the spec header:
```
Behavior: [movement | style | hybrid]
Surface:  [text | image | svg-scene | canvas-frames | data-viz | css-reveal]
```

---

## Spec Format

```markdown
# [Animation Name] ([Category]) Specification

## Objective
One paragraph: What the effect achieves visually, what it communicates,
and where it's used (which section/component of the page).

---

## The Visual Breakdown
1. **[State Name] (Start):** Describe the initial visual state precisely.
2. **[Transition Name]:** Describe what changes and in what order.
3. **[State Name] (End):** Describe the final visual state precisely.
(Add more steps if the animation has intermediate states)

---

## Technical Implementation Plan

### 1. The Structure (HTML/CSS)
- Container requirements (position, overflow, z-index)
- Layer ordering (what's on top of what)
- Critical CSS properties for the initial state

### 2. The Trigger Mechanism
- What initiates the animation? (scroll position, intersection, hover, page load)
- If scroll-driven: what's the scroll runway? what % range maps to this animation?
- If time-driven: what's the duration? looping or one-shot?

### 3. The Animation Logic (JavaScript, if needed)
- DOM manipulation required
- Calculation formulas (scroll-to-progress mapping, interpolation)
- State management (which elements are active/done/pending)

### 4. The Visual Transition (CSS)
- Properties that change (opacity, transform, color, clip-path, etc.)
- Easing function and reasoning
- Duration or scroll-range mapping
- Stagger pattern (if elements animate sequentially)

---

## Edge Cases & Performance Considerations
- Resize behavior
- Mobile handling (simplify or replace?)
- Performance concerns (DOM count, paint triggers, GPU layers)
- Accessibility (screen readers, reduced-motion preference)
```

---

## When to Write a Spec

Write a spec for ANY animation that meets one or more of these criteria:
- **Style-based** — grid analysis cannot detect it, so it must be described explicitly
- **Stacked/compound** — two or more effects layered on the same element (e.g., typewriter fill = opacity reveal + color interpolation + scroll-driven sequencing)
- **Complex trigger** — scroll-mapped with non-linear ranges, or dependent on other animations completing
- **Novel** — not a standard fade/slide that CSS handles trivially

Standard fade-in reveals (`.rv` class, IntersectionObserver) do NOT need specs.

---

## Naming Convention

Name the spec file: `{animation_name}_spec.md`
- Use lowercase with underscores
- Name describes the visual effect, not the technical method
- Examples: `mosaic_animation_spec.md`, `typewriter_fill_spec.md`, `dot_wave_spec.md`, `scroll_counter_spec.md`
