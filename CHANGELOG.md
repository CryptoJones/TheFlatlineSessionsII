# Changelog

All notable changes to **The Flatline Sessions II — Count Binary** are documented
here. This project adheres to [Semantic Versioning](https://semver.org).

## [1.1.3] — 2026-07-12

### Fixed
- **Title screen mouse click.** "Press any key" now also responds to a mouse
  click — clicks were previously swallowed before reaching the input handler.

### Changed
- **Allison stays talkable.** Her Talk button on the beach no longer disappears
  after the first conversation — you can keep talking to her (and hear her
  random Spanish one-liners) until you slot the language chip.

## [1.1.2] — 2026-07-12

### Changed
- **New studio logo.** The Ronin 48 Games Studio pre-splash ident is now the
  pixel-art version (samurai on a hill of skulls under a red sun).

## [1.1.1] — 2026-07-11

### Changed
- **Quest-ordered conversations.** A **Talk to X** button now appears only when X is
  the *current* quest objective — an NPC a later step needs stays hidden until it's
  their turn, so you talk to people in quest order (all chapters).
- **Chapter 1 flow.** The quest now runs **Talk to Allison → Insert the Spanish
  microsoft → Talk to Allison**: you meet her, realize you can't understand her,
  slot the language chip, then have the real conversation. Her Talk button appears,
  disappears while you slot the chip, and reappears.

## [1.1.0] — 2026-07-11

### Added
- **Music volume slider.** Settings gains a **Music Volume** control (applied live to
  the playing cue and remembered between sessions).
- **"Spanish Language microsoft" — Chapter 1.** A language chip now auto-starts in
  your inventory; slot it into your skull socket to understand **Allison** on the
  beach. Until it's slotted she speaks only Spanish, one random line per talk. This
  introduces a general **slottable chip** mechanic (`slot` items) plus flag-gated and
  random-line dialogue in the engine.
- **Ronin 48 Games Studio logo.** A studio ident now plays on boot, before the
  dedication card and title.
- **New title cover.** The title screen is now a circuit-board brain (Unsplash+,
  photograph by Sumaid pal Singh Bakshi), credited in `data/image_credits.json`,
  `docs/IMAGE_CREDITS.md`, and a new **Title Art** page in the art book.
- **New game button.** Chapter select gains a **New game** button beside **Load game**
  (left of it when no save exists yet, right of it once a save exists).

### Changed
- **README** now leads with the title cover as a hero image.

## [1.0.7] — 2026-07-11

### Added
- **Approved Unsplash art book.** A 109-page edition of *The Art of The
  Flatline Sessions II* presents all 100 production plates with their in-game
  room or story descriptions, contributor display names, clickable Unsplash
  usernames, profile links, and original-photo links.
- **Complete image attribution.** Human-readable and machine-readable credit
  manifests record the contributor, profile, source photograph, destination,
  and license for every plate.

### Changed
- **Final photographic art pass.** Replaced the 100 generated room,
  cyberspace, and story placeholders with the officially approved Unsplash and
  Unsplash+ selections, cropped consistently to 1344×768.

## [1.0.6] — 2026-07-10

### Fixed
- **Reused canonical outro art.** Chapter-outro pages that depicted existing
  room scenes now reuse those room plates instead of carrying duplicate renders.

## [1.0.5] — 2026-07-03

### Changed
- **Endgame quote.** The finale now closes on William Gibson's line —
  *"The future is already here. It's just not evenly distributed."*

## [1.0.4] — 2026-07-03

### Added
- **Give Hint.** A "? Give Hint" button (and the `H` key) in every room maps the
  compass route to your current objective and names the action to take — e.g.
  *"E, N, E → Talk to Conroy"*. Still-locked doors are routed around.
- **Endgame.** Finishing the final chapter now plays a proper finale card
  (THE END + a closing coda) before returning to the title, instead of dropping
  to chapter select.

### Fixed
- **Chapter 8 soft-lock.** Bobby's borrowed rig — Jammer's club deck, a software
  item — now enables the Jack In button, so the siege chapter's matrix runs are
  reachable. A software item flagged as a deck now counts as a deck.
- **Action-bar clutter.** A conversation you've finished drops its Talk button
  (kept only when the current objective still needs that NPC), so crowded rooms
  no longer overflow the button bar.

## [1.0.3] — 2026-07-03

### Added
- **Dedication loading card.** Every boot now opens on a quiet fade-in dedication
  — "Dedicated to William Gibson and all other Science Fiction authors; past,
  present, and future." — that holds, fades out, and hands off to the title.
  Any key or click skips it straight to the title.
- **Console-cowboy title cover.** The title screen now full-bleeds the baked
  cover art (`assets/ui/cover.png`), with the game title — *THE FLATLINE
  SESSIONS II* / *COUNT BINARY* — overlaid and outlined so it reads cleanly
  over the plate (the cover carries no lettering of its own).
- **Autosave (on by default).** The game now keeps a rolling `Autosave` slot,
  refreshed at every room entry and on chapter completion, so progress survives
  without ever opening the Save menu. Toggle it in Settings; it's remembered
  between runs and appears in the Load menu like any save.
- **Chapter-select atmosphere.** The chapter-select screen now carries the title
  cover as a faint background wash behind the list.

### Changed
- **Fixed compass.** The W/N/S/E direction controls are now shown in every room;
  directions that aren't real exits sit visibly dimmed and unclickable rather
  than disappearing, so the navigation layout no longer shifts room to room.

## [1.0.2] — 2026-07-03

### Added
- Settings panel with a music on/off toggle (remembered between runs).

### Fixed
- The Load menu always offers a way back, even with a long or empty save list.

## [1.0.1] — 2026-07-03

### Changed
- Baked the approved background art, committed render presets, and regenerated
  the art book.

## [1.0.0] — 2026-07-02

### Added
- First release: approved Splice-licensed soundtrack, cover art, and full art
  pass across all nine chapters.
