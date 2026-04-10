# Runway — Frame-Referenced Video Generation Guide for Atlas10X

Guide for generating smooth transition videos from keyframe pairs using Runway, which will be extracted into WebP frame sequences for scroll-driven canvas animations.

---

## Which Model to Use

**Runway Gen-3 Alpha Turbo** — supports **First Frame + Last Frame** keyframe input. This is exactly what we need.

- Upload Frame 1 as "First Frame"
- Upload Frame 2 as "Last Frame"
- Runway generates a smooth video transitioning between them
- This is NOT simple interpolation — it uses generative AI that understands 3D structure, lighting, and motion

**Important: Gen-4 does NOT support Last Frame input.** Gen-4 only takes a first frame. For our start-to-end frame workflow, use **Gen-3 Alpha Turbo**.

**Access:** runwayml.com — requires Standard plan or above.

---

## Prompt Strategy

When using First Frame + Last Frame, the images carry most of the visual information. The text prompt should focus almost entirely on **describing the motion**, not the object.

### Prompt Formula

```
[Motion description], [speed], [background stability], [camera behavior], [quality keywords]
```

### The Less-Is-More Rule

If your keyframes are clear and consistent, a minimal prompt often works best:

```
Smooth slow rotation, dark background, studio lighting,
product photography, seamless motion, fixed camera
```

Over-prompting can conflict with the visual information in your keyframes and cause artifacts.

---

## Prompt Templates for Atlas10X Animations

### Hero — Orb Rotation
```
The glowing orb rotates slowly and smoothly clockwise, amber veins
catching the light at different angles. Fixed camera, pure dark
background, consistent studio lighting throughout. Slow deliberate
constant-speed motion. Product visualization, cinematic quality.
```

### Creative Discovery — Floating Screens
```
Three floating glass screens rotate slowly as a group, drifting
gently. Smooth continuous motion, fixed camera, pure black background
unchanged. Consistent lighting throughout. Slow, premium product
photography feel. No camera movement.
```

### Creative Intelligence — Data Cube
```
The cube rotates smoothly clockwise, revealing its transparent
face with glowing internal data visualization. Rigid object
maintaining exact shape. Fixed tripod shot, dark background,
consistent studio lighting. Slow constant-speed rotation,
seamless motion.
```

### Creative Studio — Cylindrical Device
```
The device rotates smoothly to reveal its top surface, LED ring
catching the light. Slow deliberate rotation, rigid object
maintaining precise geometry. Fixed camera, pure black background,
no background changes. Studio product photography, ultra-smooth
motion.
```

---

## Recommended Settings

| Setting | Value | Why |
|---------|-------|-----|
| **Model** | Gen-3 Alpha Turbo | Only model supporting First + Last Frame |
| **Duration** | 5s or 10s | 5s for subtle rotations (30-45°). 10s for larger rotations (60°+) to avoid abrupt morphing |
| **Resolution** | 1280×768 (16:9) | Matches our keyframe aspect ratio and canvas display |
| **Motion Amount** | Low to Medium | Product rotation needs controlled motion. High = warping |
| **Variations** | Generate 3-4 | Pick the smoothest one |
| **Seed** | Fixed | For iteration — same seed + different prompt = comparable results |

### Duration Math for Frame Extraction

| Runway Duration | FPS | Total Frames | After Trimming (remove first/last 3) | WebP at quality 80 |
|-----------------|-----|-------------|--------------------------------------|---------------------|
| 5s | 24 | 120 frames | ~114 frames | ~15-20MB total |
| 10s | 24 | 240 frames | ~234 frames | ~30-40MB total |

For scroll animation, **120 frames is the sweet spot** — smooth enough, not too heavy. A 5-second Runway generation is ideal.

---

## Motion Description Best Practices

### Do Say
| Phrase | What it does |
|--------|-------------|
| "Smooth continuous rotation" | Even, constant angular velocity |
| "Slowly rotating clockwise/counterclockwise" | Clear direction and speed |
| "The object pivots on its vertical axis" | Defines rotation axis |
| "Fixed camera, no camera movement" | Locks camera, forces motion onto object |
| "Rigid object maintaining exact shape" | Prevents morphing/deformation |
| "Consistent lighting throughout" | Prevents flickering |
| "Pure black background, no changes" | Stabilizes background |
| "Constant-speed motion" | Prevents uneven acceleration |

### Don't Say
| Phrase | Why it's bad |
|--------|-------------|
| "Morphs/transforms" | Triggers literal morphing artifacts |
| "Quick" or "fast" | Causes motion blur, frame skipping |
| "Camera flies around" | Background instability |
| "Dramatic movement" | Too vague, unpredictable |
| "Cinematic camera motion" | Conflicts with "fixed camera" intent |
| "The object changes" | Implies shape change, not rotation |

---

## Keyframe Requirements (Before Uploading to Runway)

Your Frame 1 and Frame 2 must satisfy:

| Requirement | Why |
|-------------|-----|
| Same object, same materials | Prevents morphing between different objects |
| Same lighting setup | Prevents flickering |
| Same background (pure black) | Prevents background instability |
| Same image dimensions | Required by Runway |
| Angular difference: 30-60° max | Larger gaps cause morphing artifacts |
| PNG format, high resolution | Best input quality |
| Color-graded to match | Lock in identical color temperature |

**If you need more than 60° of rotation:** Chain multiple 5-second clips with intermediate keyframes (Frame 1→2, Frame 2→3, etc.) and concatenate the extracted frames.

---

## Post-Generation: Frame Extraction

Once you have the Runway MP4:

```bash
# Extract all frames at native 24fps as WebP
ffmpeg -i runway_output.mp4 -vf "fps=24" -c:v libwebp -quality 80 frames/frame-%04d.webp

# Or extract fewer frames (12fps) for lighter loading
ffmpeg -i runway_output.mp4 -vf "fps=12" -c:v libwebp -quality 80 frames/frame-%04d.webp
```

### Post-extraction cleanup:
1. **Trim first and last 2-3 frames** — Runway sometimes has artifacts at clip boundaries
2. **Check for duplicate/held frames** at the start (model sometimes "holds" before motion begins)
3. **Verify frame count** is in the 60-200 range for scroll animation
4. Place extracted frames in the correct `animations/{section}/frames/` directory

---

## Common Pitfalls

| Issue | Cause | Fix |
|-------|-------|-----|
| Object melts/morphs mid-video | Keyframes too different (>90° apart) | Reduce angular difference to 30-60° |
| Flickering lighting | Inconsistent lighting between keyframes | Color-grade both frames identically before upload |
| Background "breathes" or shifts | Dark bg causes hallucinated patterns | Ensure pure black bg. Add "solid black background, no changes" to prompt |
| Object deforms during rotation | Model doesn't understand 3D geometry | Add "rigid object, maintains exact shape". Keep rotation small. |
| Uneven motion speed | Model allocates motion unevenly | Add "constant speed, uniform rotation, linear motion" |
| Jitter between frames | Style variation frame-to-frame | Lower motion amount. Use "photorealistic, consistent detail" |

---

## Full Workflow Summary

```
1. Generate Frame 1 in Nano Banana 2 (see prompting_nano_banana.md)
2. Generate Frame 2 in same conversation (edit of Frame 1)
3. Color-grade both frames to match
4. Upload to Runway Gen-3 Alpha Turbo as First Frame + Last Frame
5. Write motion-focused prompt (see templates above)
6. Set duration to 5s, motion to Low-Medium
7. Generate 3-4 variations, pick smoothest
8. Download MP4
9. Extract frames: ffmpeg → WebP at 24fps or 12fps
10. Trim first/last 2-3 frames
11. Place in animations/{section}/frames/
12. Canvas scroll engine renders them (see agent.md Part 6)
```

Sources:
- [Creating with Keyframes on Gen-3 — Runway Help](https://help.runwayml.com/hc/en-us/articles/34170748696595-Creating-with-Keyframes-on-Gen-3)
- [Gen-3 Alpha Prompting Guide — Runway Help](https://help.runwayml.com/hc/en-us/articles/30586818553107-Gen-3-Alpha-Prompting-Guide)
- [Creating with Gen-3 Alpha and Gen-3 Alpha Turbo — Runway Help](https://help.runwayml.com/hc/en-us/articles/30266515017875-Creating-with-Gen-3-Alpha-and-Gen-3-Alpha-Turbo)
- [Creating with Gen-4 Video — Runway Help](https://help.runwayml.com/hc/en-us/articles/37327109429011-Creating-with-Gen-4-Video)
- [Runway Gen-4 Guide — FocalML](https://focalml.com/blog/runway-gen-4-guide-whats-new-and-how-to-use-the-latest-ai-video-model/)
