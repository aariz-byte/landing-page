# Nano Banana 2 — Prompting Guide for Atlas10X Assets

Guide for generating consistent start/end keyframe pairs using Google's Nano Banana 2 (Gemini's image generation model) for scroll-driven 3D animations.

---

## What is Nano Banana 2

Nano Banana 2 is Google's image generation model, built on the Gemini 3 family. It combines Nano Banana Pro's capabilities with Gemini Flash's speed. It applies deep reasoning to fully understand prompts before generating images.

**Access via:**
- Gemini app (gemini.google.com) — Gemini Advanced subscribers
- Google AI Studio (aistudio.google.com) — select Gemini model with image gen enabled
- Vertex AI API — programmatic access

**Key strengths for our use case:**
- Photorealistic product renders
- Precise text rendering (useful for UI mockup renders)
- Multi-object consistency (up to 14 objects in one image)
- Conversational context — Frame 2 generated in the same chat as Frame 1 maintains better consistency

---

## Prompt Formula

```
[Subject description] + [Material/finish] + [Orientation/angle] + [Lighting setup] + [Background] + [Render style] + [Aspect ratio]
```

---

## Lighting Rig (Use for ALL Atlas10X Renders)

Lock this into every prompt to maintain visual consistency across all assets:

```
Three-point studio lighting setup:
- Key light: warm amber (3200K) from upper-right at 45 degrees, soft diffusion
- Fill light: cool subtle blue from the left at 20% intensity
- Rim light: sharp white backlight creating a thin bright edge outline
- Background: seamless pure black (#0A0A0A) with no gradient, no reflections
```

This matches both the Atlas10X product UI (warm amber orb glow on dark bg) and the Platform reference (dark bg, warm accents).

---

## Generating Consistent Frame Pairs

The critical challenge: Frame 1 and Frame 2 must look like the SAME object from different angles.

### Method 1: Same Conversation (Recommended)

Generate both frames in a single Gemini conversation:

```
Message 1:
"Generate a photorealistic product render of [detailed object description].
[Full lighting rig from above]. The object faces the camera at a front
3/4 angle, tilted slightly downward. Commercial product photography,
physically-based rendering, 8K, 16:9 aspect ratio."

Message 2 (after receiving Frame 1):
"Now generate the exact same object with identical materials, lighting,
scale, and background. The only change: rotate the object 45 degrees
clockwise, now showing a rear 3/4 view from slightly above. Keep
everything else pixel-identical."
```

### Method 2: Anchor Object Spec

Write a hyper-detailed "object spec" and include it verbatim in both prompts:

```
Object spec: "A floating abstract crystalline device, 20cm tall,
made of dark obsidian glass with internal amber LED veins running
along each edge. The form is a truncated octahedron with beveled
edges. Surface has a matte-to-gloss gradient from base to top.
A thin ring of coral-orange (#E8573A) light glows at its equator."

Frame 1: [Object spec] + [Lighting rig] + "Front-left 3/4 view,
30-degree elevation. 16:9, photorealistic, octane render."

Frame 2: [Object spec] + [Lighting rig] + "Rear-right 3/4 view,
15-degree elevation. 16:9, photorealistic, octane render."
```

### Method 3: Edit of Frame 1

Upload Frame 1 back into the conversation and request an edit:

```
"Using this image as a reference, rotate the object 45 degrees
clockwise. Change nothing else — same materials, same lighting,
same background, same scale. Only the viewing angle changes."
```

---

## Prompt Templates for Atlas10X Sections

### Hero — Abstract Tech Orb
```
Frame 1:
"Photorealistic 3D render of an abstract floating orb made of dark
polished obsidian with glowing amber-gold (#D4A44A) energy veins
running across its surface in a circuit-like pattern. Subtle particles
of warm light drift away from the orb like embers. The orb hovers in
a pure black void. Three-point studio lighting: warm amber key light
from upper-right, cool blue fill from left at 20%, sharp white rim
light from behind. Front 3/4 view, slightly below eye level looking up
at the orb. Commercial product photography, ray-traced, 8K, 16:9."

Frame 2:
"[Same description]. Rear 3/4 view from slightly above, the orb has
rotated 60 degrees clockwise. The amber veins now visible on the far
side catch different light angles. All lighting, particles, and
background remain identical."
```

### Creative Discovery — Floating Ad Frames
```
Frame 1:
"Photorealistic render of three rectangular glass screens floating at
staggered angles in a pure black void. Each screen displays a faint,
abstract impression of a social media ad (blurred imagery, warm tones).
The screens are made of frosted dark glass with thin coral-orange
(#E8573A) borders glowing softly. Arrangement: one center-facing, one
tilted 20 degrees left, one tilted 15 degrees right and slightly behind.
Three-point studio lighting: warm amber key from upper-right, subtle
blue fill from left, white rim from behind. Eye-level view.
Photorealistic, 8K, 16:9."

Frame 2:
"[Same description]. The three screens have rotated as a group 30 degrees
clockwise, revealing more of the side and back edges. The center screen
now shows its right edge prominently. All lighting and spacing identical."
```

### Creative Intelligence — Competitive Analysis Orb
```
Frame 1:
"Photorealistic render of a dark matte titanium cube, 15cm, floating in
a black void. One face of the cube is transparent glass, revealing an
interior grid of glowing coral-orange (#E8573A) data lines — like a
neural network visualization trapped inside. Warm amber key light from
upper-right creates a highlight on the top edge. Cool blue fill from
left. Sharp rim light from behind. Front-facing view, eye level.
Photorealistic, octane render, 8K, 16:9."

Frame 2:
"[Same description]. The cube has rotated 45 degrees to the right and
15 degrees upward, now showing two faces — the transparent data face
is now at an angle, and a solid matte titanium face is visible. All
lighting, interior glow, and background remain identical."
```

### Creative Studio — Ad Generation Device
```
Frame 1:
"Photorealistic render of a sleek cylindrical device, matte black with
a single thin glowing coral-orange (#E8573A) LED ring around its center.
The top surface has a subtle holographic sheen. Floating in a pure black
void. Three-point studio lighting: warm amber key from upper-right,
cool fill from left, white rim from behind. Straight-on view, eye level.
Photorealistic, 8K, 16:9."

Frame 2:
"[Same description]. The device is now viewed from 40 degrees to the
right and 20 degrees above, showing the top surface and the LED ring
as an ellipse. All lighting and materials identical."
```

---

## Settings

| Setting | Value |
|---------|-------|
| Aspect ratio | 16:9 (matches Runway input and canvas display) |
| Style | Photorealistic (avoid artistic/stylized) |
| Candidates | Generate 4 per prompt, pick best match |
| Output format | PNG (lossless, for feeding to Runway) |
| Temperature | Low (0.2-0.4) for consistency |

---

## Post-Processing Before Runway

After selecting your best Frame 1 and Frame 2:
1. **Color-grade both** to ensure identical color temperature and contrast (use Lightroom/Photoshop)
2. **Verify dimensions** match exactly (same width × height)
3. **Check background** is truly uniform black in both — no subtle gradients introduced by the model
4. **Save as PNG** (lossless) for Runway input

---

## Common Pitfalls

| Issue | Fix |
|-------|-----|
| Object looks different between frames | Use Method 1 (same conversation) or Method 3 (edit of Frame 1) |
| Lighting inconsistent | Include the full lighting rig verbatim in both prompts |
| Background not pure black | Add "pure black background, no gradient, no reflection, no floor" |
| Object proportions shift | Include exact dimensions in the object spec ("20cm tall, 15cm wide") |
| Too artistic/painterly | Add "photorealistic, product photography, octane render" — avoid "artistic" |
| Model adds unwanted elements | Add "no text, no watermark, no other objects, isolated subject" |

Sources:
- [Ultimate prompting guide for Nano Banana — Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana)
- [Nano Banana 2 — Google AI Blog](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/)
- [6 Best Nano Banana 2 Prompts — eWeek](https://www.eweek.com/news/best-nano-banana-2-prompts-gemini-3-1-flash-image/)
- [Nano Banana 2 Prompt Guide — ImagineArt](https://www.imagine.art/blogs/nano-banana-2-prompt-guide)
- [GitHub: awesome-nanobanana-pro](https://github.com/ZeroLu/awesome-nanobanana-pro)
