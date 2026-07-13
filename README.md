<p align="center">
  <img src="assets/ui/cover.png" alt="The Flatline Sessions II — Count Binary" width="880">
</p>

# The Flatline Sessions II — Count Binary

A fan-made, modern-look cyberpunk adventure after a famous cyberpunk trilogy — the second game in
the Flatline Sessions trilogy, built on the engine from
[The Flatline Sessions](../neuromancer-godot). Where the first game was deliberately retro, this one renders clean at a
**native 1920×1080 canvas in full 32-bit color**: flat panels, one neon accent, full-res art.

## The shape of the game

*Count Binary* runs through three viewpoint characters. Nine chapters
play in campaign order, each locking you to one PoV:

| # | Chapter | You play |
|---|---------|----------|
| 01 | Smooth-Running Gun | Turner |
| 02 | Bobby Pulls a Wilson | Bobby Newmark |
| 03 | Virek's Garden | Marly Krushkhova |
| 04 | On Site | Turner |
| 05 | The Projects | Bobby Newmark |
| 06 | Names of the Dead | Marly Krushkhova |
| 07 | The Squirrel Wood | Turner |
| 08 | Count Binary Interrupt | Bobby Newmark |
| 09 | The Boxmaker | Marly Krushkhova |

Each chapter has its own room graph, main quest, NPCs, and starting kit. Finishing a
chapter unlocks the next. Bobby's chapters include cyberspace runs (ICE combat); Turner's
and Marly's stay in the meat.

## Status

**Playable end to end with a complete production art pass.**
The whole story is playable from beginning to end.
All dialog, quests, items, shops, and matrix targets are in place, written as original in-world
prose throughout.

The final art pass is in `assets/backgrounds_hd/` and `assets/cyberspace/`, with
production artwork cropped consistently to the game's 1344×768 plate format.

The first soundtrack pass is in `assets/audio/music/`, with chapter cues plus title,
shops, cyberspace, and ICE-combat loops. See [`docs/soundtrack.md`](docs/soundtrack.md).
Album-cover art is stored in [`assets/album_art/`](assets/album_art/) and mirrored in
[`docs/album_art/`](docs/album_art/) for review/export workflows.

Read **[The Art of The Flatline Sessions II](docs/The_Art_of_The_Flatline_Sessions_II.pdf)**
for the complete indexed art book. It includes every production plate and the
room, story, interaction, or dialogue context explaining where it appears.

## Run it

```sh
./run.sh            # imports assets, launches (software GL by default on Linux)
GPU=1 ./run.sh      # force GPU rendering
```

Requires Godot 4.3+. Keyboard: WASD/arrows move, I inventory, Q quest log, F5/F9 quick
save/load, Esc backs out of menus.

## Validate the scaffold

```sh
godot --headless --path . --script res://tests/validate_data.gd
```

Checks every chapter, room graph, exit, NPC dialog graph, quest flag, item, and shop
reference. Run it after any data edit.

## Layout

```
data/chapters.json        chapter spine (PoV, rooms file, quest, intro/outro, start kit)
data/quests.json          one flag-driven quest per chapter
data/rooms/chNN_*.json    per-chapter room graphs
data/npcs/*.json          branching dialog (set_flag / grant / credits / require_flag)
data/items.json           item catalog     data/shops.json  shops
data/cyberspace/*.json    matrix targets (per-chapter, ICE-rated)
data/pax/*.json           NET news + boards
src/                      engine (see src/core/Game.gd)
```

## Credits

Fan project after a famous cyberpunk trilogy. Game code and all in-game
prose are original to this project. Copyright **CryptoJones** <cryptojones@owasp.org>;
engine shared with The Flatline Sessions.
