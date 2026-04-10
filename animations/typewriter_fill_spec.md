# Typewriter Fill (Sequential Character Reveal) Specification

## Objective
The goal is to create a cinematic, scroll-driven text reveal where a sentence "types" itself out as the user scrolls. Unlike a standard typewriter effect which is time-based, this effect is **scroll-position based**, allowing the user to control the speed and direction of the reveal.

The effect is used for high-impact transition statements (e.g., "We analyze every ad..."), making the copy feel like it is being actively thought out or processed by the AI in real-time.

---

## The Visual Breakdown

1.  **The Ghost State (Initial):** The entire sentence is visible but highly translucent (e.g., `12%` opacity), acting as a "stencil" for the incoming text.
2.  **Sequential Reveal:** As the user scrolls, letters "fill" to 100% opacity from left to right. Only one character is ever in a partial-fill state at a time.
3.  **Accent Color Shift:** Specific "accent" words do not just fade to white; they transition from the ghost gray to a vibrant brand color (e.g., Atlas Coral #E8573A).
4.  **Sticky Focus:** The text remains centered in the viewport throughout the duration of the animation via a sticky container, ensuring the user's attention remains on the narrative.

---

## Technical Implementation Plan

To implement this effect reliably, follow this architecture:

### 1. The Structure (HTML/CSS)
*   **Runway Container (`.trans-s`)**: A tall section (e.g., `150vh` to `300vh`) that provides the "scroll runway."
*   **Sticky Wrapper (`.trans-sticky`)**: A `sticky` element set to `top: 0` and `height: 100vh` to lock the text in place.
*   **Text Container (`.trans-t`)**: The actual paragraph. Each word should be wrapped in a `.trans-word` span to allow for easy splitting.

```css
.trans-char {
  color: rgba(255, 255, 255, 0.12); /* Initial ghost state */
  display: inline-block;
  will-change: color, opacity;
}
```

### 2. The DOM Splitting (JavaScript)
Writing every letter as a individual `<span>` in HTML is too verbose. A JS function should:
*   Select all `.trans-word` elements.
*   Iterate through each word, splitting its text into individual characters.
*   Replace the word's content with a sequence of `<span>` elements for each letter.
*   Preserve "accent" word status by passing a `data-accent` attribute to the child spans.

### 3. The Scroll Mapping Logic
The core of the effect is mapping `window.scrollY` to a character index:
1.  Calculate the `progress` (0 to 1) of the scroll through the parent section.
2.  Determine the `charPosition` by multiplying `progress` by `totalCharacters`.
3.  **State Management**:
    *   `if (index < charPosition - 1)`: Character is **Fully Filled** (100% opacity).
    *   `else if (index < charPosition)`: Character is **Currently Filling** (Partial opacity based on the decimal remainder).
    *   `else`: Character is **Ghost** (12% opacity).

### 4. Color Interpolation (Math)
For accent words, calculate the RGB values based on the fill percentage (0 to 1):
```js
// Example transition from White (255,255,255) to Coral (232,87,58)
const r = 255 + (brandR - 255) * fill;
const g = 255 + (brandG - 255) * fill;
const b = 255 + (brandB - 255) * fill;
```

---

## Edge Cases & Performance Considerations

*   **Window Resizing**: Re-calculating the total character count and section bounds on resize is critical if the text wraps differently.
*   **Scroll Smoothness**: Since the color/opacity changes are handled in JS, use `requestAnimationFrame` or a passive scroll listener to prevent main-thread jank.
*   **Mobile Support**: On small screens, the scroll runway might need to be shorter or the font size more aggressively clamped to prevent excessive scrolling.
*   **Accessibility**: Ensure the text is still readable by screen readers by keeping the original text content in the DOM and only using spans for visual styling.
