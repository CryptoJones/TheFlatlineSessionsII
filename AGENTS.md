# The Flatline Sessions II — Working State

## Current user direction

- This is a visual-novel adaptation of *Count Zero* using the EPUB at the repository root as a story reference.
- Preserve the existing nine-chapter campaign, point-of-view rotation, approved media library, and original critical path.
- Expanded story material must use original prose and remain optional unless explicitly noted.
- Optional quest objectives display `[Optional]`, do not block progression or chapter completion, and should be non-linear whenever their location is accessible.
- Chapter 1 exception: the Heathrow scene where Turner vomits into a blue airport waste can is mandatory and appears in the chapter introduction.
- Chapter 1 ends when the player completes the final required objective, `Board Hosaka's charter and depart for Arizona`; that interaction directly launches the chapter outro.

## Implemented changes

- Added data-driven room `interactions` for inspect/search/call-style narrative scenes.
- The room action bar shows one `Investigate` button; available interactions open in a menu and render through the illustrated story pager.
- Interaction completion supports story flags, elapsed minutes, autosave, hints, one-time visibility, item/flag gates, and direct chapter conclusion.
- Optional quest steps are first-class data via `"optional": true`. Quest completion and NPC ordering ignore unfinished optional steps, while the quest log tracks and labels them.
- Chapter 1 has nine expanded interactions and a mandatory boarding conclusion.
- Chapters 2–9 each have two optional source-derived investigations. Original quest objectives remain required.
- Existing chapter, room, NPC, item, and flag IDs were preserved for save compatibility.

## Production artbook

- `docs/The_Art_of_The_Flatline_Sessions_II.pdf` is the indexed production artbook.
- Every asset has a stable `IMG-###` ID, an index entry, and its mapped story, interaction, and dialogue context.
- Regenerate the PDF and Markdown catalog with `tools/generate_artbook.py` using Python with ReportLab and Pillow installed.
- The generator creates compressed PDF-only previews under `/tmp`; it does not alter source images.

## Validation

Run after story or engine changes:

```sh
godot --headless --path . --script res://tests/optional_quests.gd
godot --headless --path . --script res://tests/validate_data.gd
godot --headless --path . --script res://tests/playthrough.gd
godot --headless --path . --script res://tests/content_budget.gd
godot --headless --path . --editor --quit
```

The optional-quest regression, data validator, automated playthrough, and Godot parse check were passing at the time this state was written.

## Workspace status and cautions

- Work is currently uncommitted. Inspect `git status` and preserve all existing user changes.
- The game was most recently launched with `./run.sh`; a prior session may still be running.
- Do not replace or regenerate artwork without explicit direction. Use the stable IDs in the artbook when discussing replacements.
- The larger original target of a 6–9 hour campaign has not been reached: Chapter 1 is the densest expansion, while Chapters 2–9 currently have only two new optional interactions each.
