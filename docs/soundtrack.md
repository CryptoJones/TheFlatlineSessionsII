# Original Soundtrack

First soundtrack pass generated 2026-07-02 from CJ's local licensed sample
library on pluto (`/mnt/hdd1/Samples/packs`). Tracks are loopable Ogg Vorbis
assets for in-game playback.

Distribution note: before shipping a public build, verify the upstream sample
pack licenses permit redistribution as rendered game music.

## Album

**The Flatline Sessions II: Count Binary - Original Soundtrack**

## Game Cues

| Cue | File | Duration |
|---|---|---:|
| Title | `assets/audio/music/title.ogg` | 1:14 |
| Streets fallback | `assets/audio/music/streets.ogg` | 1:14 |
| Shops | `assets/audio/music/shops.ogg` | 1:14 |
| Cyberspace | `assets/audio/music/cyberspace.ogg` | 1:14 |
| ICE combat | `assets/audio/music/ice_combat.ogg` | 1:14 |

## Chapter Tracks

| Chapter | Track | File | Duration |
|---|---|---|---:|
| 01 | Smooth-Running Gun | `ch01_smooth_running_gun.ogg` | 1:32 |
| 02 | Bobby Pulls a Wilson | `ch02_bobby_pulls_a_wilson.ogg` | 1:32 |
| 03 | Virek's Garden | `ch03_vireks_garden.ogg` | 1:32 |
| 04 | On Site | `ch04_on_site.ogg` | 1:32 |
| 05 | The Projects | `ch05_the_projects.ogg` | 1:32 |
| 06 | Names of the Dead | `ch06_names_of_the_dead.ogg` | 1:32 |
| 07 | The Squirrel Wood | `ch07_the_squirrel_wood.ogg` | 1:32 |
| 08 | Count Binary Interrupt | `ch08_count_binary_interrupt.ogg` | 1:32 |
| 09 | The Boxmaker | `ch09_the_boxmaker.ogg` | 1:32 |

`AudioManager` maps normal exploration to the active chapter track. Explicit
room music still wins, shops use `shops`, and matrix/ICE views use their
specialized cues.
