# Flux Image Generation Prompts — Flatline Sessions II & III

Locked 2026-07-02. Art direction: heavily rotoscoped painted-over-live-action, graphic novel realism, mid-century sci-fi with modern cyberpunk noir.

## Core Environment Style (Rooms & Establishing Shots)

**Core rotoscope + retro 35mm prompt:**

```text
heavily rotoscoped painted-over-live-action, graphic novel realism, flattened color planes, visible ink contour lines, slightly unstable rotoscope edges, hand-painted surfaces, realistic perspective and lighting underneath, sun-faded retro 35mm film palette, symmetrical deadpan framing, mid-century sci-fi production design, warm film grain, theatrical stillness, modern cyberpunk noir, [GAME ACCENT COLOR] neon accent lighting, no people, unoccupied environment,
```

**Suffix for room/environment plates:**

```text
Premium modern adventure-game background plate, clear navigable environment, wide establishing shot, no people, no readable text, no signage, no posters with words, no gore. Screens and neon may be abstract glow only.
```

## Cyberspace Style

**Rotoscoped cyberspace prompt:**

```text
modern cyberspace interpreted in heavily rotoscoped graphic-novel style: infinite black void gridded with glowing neon wireframe lines, luminous data architecture, cinematic perspective with hand-painted inked surfaces, flattened glow planes, warm film grain, [GAME CYBER COLORS], no text/logos, 16:9 game plate,
```

**Suffix for cyberspace plates:**

```text
Premium modern cyberspace game plate, clear readable composition, no people, no text, no logos, no readable symbols.
```

## Album Cover Style

For soundtrack artwork:

```text
square soundtrack album cover art, text-free front cover, heavy rotoscope animation look with bold traced contours, painted-over live-action frames, flattened color regions, hand-inked edge lines, subtle analog-film grain, halation, pastel sci-fi production design, tactile miniatures-and-practical-set feeling, no CGI smoothness, no uncanny faces, no anime, no pixel art, no visible text, no logos
```

## Negative Prompts

**Standard (rooms & environments):**

```text
text, watermark, logo, signage, gibberish writing, subtitles, readable words, letters, posters with text, storefront signs, neon signs with letters, menus, UI text, signatures, artist mark, people, characters, human figures, faces, extra limbs, deformed hands, mutated anatomy, gore, viscera, blood, human heart, exposed organs, corpse, blurry, low quality, photoreal CGI, glossy 3D render, CGI smoothness, plastic render, anime, cel shading, pixel art, out of frame, cropped, worst quality
```

**Cyberspace negative:**

```text
text, watermark, logo, gibberish writing, readable words, letters, people, faces, blurry, low quality, photoreal CGI, glossy 3D render, flat colors, muddy
```

## Color Accents by Game

- **Flatline Sessions II:** teal/cyan accents
- **Flatline Sessions III:** violet/magenta accents

Substitute `[GAME ACCENT COLOR]` and `[GAME CYBER COLORS]` with these values.

## Production Settings (Approved Batch 2026-07-02)

```text
Engine:    FLUX.2-Klein
Size:      1344x768 (16:9 game plate)
Steps:     4
CFG Scale: 1.0
LoRA:      None
Hires:     Off
```

## Usage Notes

- **Combine with per-scene factual descriptions.** Use existing per-room prompts as navigable scene descriptions; wrap them with the core style prompt above, not inside.
- **Avoid name-dropping living directors.** Describe the visual grammar and technique instead (e.g., "rotoscoped," "hand-painted," "theatrical framing").
- **The target is intentionally illustrated, not photoreal CGI or pixel art.** Reject renders that look like 3D models or untraceable AI generation.
- **Screens and neon should be abstract glow only.** Regenerate if you see obvious text, signage, storefront letters, poster text, or artist signatures.
- **Stable rotoscope edges, not wobbly or broken.** Approved renders show confident hand-traced contours, not wavering uncertainty or artifact edges.

## References

- OMI note: *Flatline Sessions sequel art style LOCKED — heavy rotoscope plus retro 35mm sci-fi grammar (2026-07-02)*
- Related: `docs/art-style-prompt.md` (abbreviated version)
- Approved verbally by CJ during batch render: *"Jesus Christ, Dix. These are amazing."*
