# Approved Image Inventory

Completed image inventory for **The Flatline Sessions II — Count Binary**.

**Status: complete and officially approved as of v1.0.7.** All 100 production
plates have been replaced with the selected Unsplash and Unsplash+ artwork at
1344×768. See [`docs/The_Art_of_The_Flatline_Sessions_II.pdf`](docs/The_Art_of_The_Flatline_Sessions_II.pdf)
for the art book and [`docs/IMAGE_CREDITS.md`](docs/IMAGE_CREDITS.md) for complete
contributor attribution.

The game references **100 unique image files**:

- 60 room/location plates
- 3 cyberspace plates
- 27 unique chapter-intro story plates
- 10 unique chapter-outro story plates

The intended replacement source for grounded scenes is the free/open Unsplash
library. Keep the final game images at 16:9 / 1344×768 or crop them to that
shape. Avoid readable text, logos, watermarks, and identifiable people where
possible.

## Room/location plates

These are the 60 room backgrounds referenced by `data/rooms/ch*.json` and
resolved through `data/art_prompts.json`.

### Chapter 1 — Smooth-Running Gun

| Needed file | Location |
|---|---|
| `assets/backgrounds_hd/C1_bedroom.png` | Beach House — Bedroom |
| `assets/backgrounds_hd/C1_veranda.png` | Beach House — Veranda |
| `assets/backgrounds_hd/C1_beach.png` | The Beach |
| `assets/backgrounds_hd/C1_tidepools.png` | Tide Pools |
| `assets/backgrounds_hd/C1_road.png` | Coast Road |
| `assets/backgrounds_hd/C1_cantina.png` | Cantina |
| `assets/backgrounds_hd/C1_airstrip.png` | Airstrip |

### Chapter 2 — Bobby Pulls a Wilson

| Needed file | Location |
|---|---|
| `assets/backgrounds_hd/C2_bedroom.png` | Your Room |
| `assets/backgrounds_hd/C2_living.png` | Condo — Living Room |
| `assets/backgrounds_hd/C2_hall.png` | Covina Concourse Courts — Hallway |
| `assets/backgrounds_hd/C2_street.png` | Barrytown Street |
| `assets/backgrounds_hd/C2_leons.png` | Leon's |
| `assets/backgrounds_hd/C2_alley.png` | Service Alley |
| `assets/backgrounds_hd/C2_playground.png` | Big Playground |

### Chapter 3 — Virek's Garden

| Needed file | Location |
|---|---|
| `assets/backgrounds_hd/C3_gallery.png` | Galerie Duperey — Interview |
| `assets/backgrounds_hd/C3_construct.png` | Virek's Garden — Parque Güell |
| `assets/backgrounds_hd/C3_street.png` | Brussels — Rue au Beurre, Rain |
| `assets/backgrounds_hd/C3_train.png` | TGV — Brussels to Paris |
| `assets/backgrounds_hd/C3_ternes.png` | Quartier des Ternes |
| `assets/backgrounds_hd/C3_andrea.png` | Andrea's Flat |
| `assets/backgrounds_hd/C3_cafe.png` | Café Blanc |

### Chapter 4 — On Site

| Needed file | Location |
|---|---|
| `assets/backgrounds_hd/C4_bunker.png` | Command Bunker |
| `assets/backgrounds_hd/C4_mall.png` | Dead Mall Concourse |
| `assets/backgrounds_hd/C4_perimeter.png` | Perimeter — The Wire |
| `assets/backgrounds_hd/C4_ridge.png` | Ridge Lookout |
| `assets/backgrounds_hd/C4_medpod.png` | Surgical Pod |
| `assets/backgrounds_hd/C4_pad.png` | Landing Pad |
| `assets/backgrounds_hd/C4_crash.png` | Crash Site |
| `assets/backgrounds_hd/C4_jet.png` | The Jet |

### Chapter 5 — The Projects

| Needed file | Location |
|---|---|
| `assets/backgrounds_hd/C5_recovery.png` | Recovery Room |
| `assets/backgrounds_hd/C5_altar.png` | Hounfor — Altar Room |
| `assets/backgrounds_hd/C5_kitchen.png` | Rhea's Kitchen |
| `assets/backgrounds_hd/C5_gallery.png` | Projects Gallery — View of Barrytown |
| `assets/backgrounds_hd/C5_twoaday.png` | Two-a-Day's Apartment |
| `assets/backgrounds_hd/C5_elevator.png` | Down Elevator |

### Chapter 6 — Names of the Dead

| Needed file | Location |
|---|---|
| `assets/backgrounds_hd/C6_andrea.png` | Andrea's Flat |
| `assets/backgrounds_hd/C6_ternes.png` | Quartier des Ternes |
| `assets/backgrounds_hd/C6_brasserie.png` | Brasserie — Napoleon Court |
| `assets/backgrounds_hd/C6_louvre.png` | Louvre Embankment |
| `assets/backgrounds_hd/C6_alain.png` | Alain's Flat |
| `assets/backgrounds_hd/C6_orly.png` | Orly — JAL Concourse |
| `assets/backgrounds_hd/C6_shuttle.png` | JAL Shuttle — Seat 3A |

### Chapter 7 — The Squirrel Wood

| Needed file | Location |
|---|---|
| `assets/backgrounds_hd/C7_road.png` | County Road |
| `assets/backgrounds_hd/C7_yard.png` | Farmhouse Yard |
| `assets/backgrounds_hd/C7_kitchen.png` | Farm Kitchen |
| `assets/backgrounds_hd/C7_lab.png` | Rudy's Workshop |
| `assets/backgrounds_hd/C7_backroom.png` | Back Room — Angie |
| `assets/backgrounds_hd/C7_treeline.png` | The Squirrel Wood |
| `assets/backgrounds_hd/C7_hover.png` | The Hover, Predawn |

### Chapter 8 — Count Binary Interrupt

| Needed file | Location |
|---|---|
| `assets/backgrounds_hd/C8_hypermart.png` | Hypermart Maze |
| `assets/backgrounds_hd/C8_escalator.png` | Dead Escalators |
| `assets/backgrounds_hd/C8_club.png` | Jammer's — Main Room |
| `assets/backgrounds_hd/C8_office.png` | Jammer's Office |
| `assets/backgrounds_hd/C8_window.png` | Barricaded Windows |
| `assets/backgrounds_hd/C8_floor.png` | Dance Floor |

### Chapter 9 — The Boxmaker

| Needed file | Location |
|---|---|
| `assets/backgrounds_hd/C9_sweetjane.png` | Sweet Jane — Cabin |
| `assets/backgrounds_hd/C9_dock.png` | Docking Collar |
| `assets/backgrounds_hd/C9_tunnel.png` | Cold Corridor |
| `assets/backgrounds_hd/C9_chapel.png` | The Wig's Chapel |
| `assets/backgrounds_hd/C9_dome.png` | Boxmaker's Dome |

## Cyberspace plates

These are referenced by `data/cyberspace/databases.json`.

| Needed file | Matrix scene |
|---|---|
| `assets/cyberspace/CYBER_target.png` | Unmarked Industrial Node |
| `assets/cyberspace/CYBER_hired.png` | Hired Ice — Perimeter |
| `assets/cyberspace/CYBER_slide.png` | Slide Construct — Los Angeles |

These scenes are abstract/non-photographic. Free stock photography is unlikely
to be a good direct replacement; abstract light, architecture, ocean, or night
photography could be used only as a deliberate new visual direction.

## Chapter intro story plates

| Needed file | Chapter/page |
|---|---|
| `assets/backgrounds_hd/CH01_intro_01.png` | Chapter 1 intro page 1 |
| `assets/backgrounds_hd/CH01_intro_02.png` | Chapter 1 intro page 2 |
| `assets/backgrounds_hd/CH01_intro_03.png` | Chapter 1 intro page 3 |
| `assets/backgrounds_hd/CH02_intro_01.png` | Chapter 2 intro page 1 |
| `assets/backgrounds_hd/CH02_intro_02.png` | Chapter 2 intro page 2 |
| `assets/backgrounds_hd/CH02_intro_03.png` | Chapter 2 intro page 3 |
| `assets/backgrounds_hd/CH03_intro_01.png` | Chapter 3 intro page 1 |
| `assets/backgrounds_hd/CH03_intro_02.png` | Chapter 3 intro page 2 |
| `assets/backgrounds_hd/CH03_intro_03.png` | Chapter 3 intro page 3 |
| `assets/backgrounds_hd/CH04_intro_01.png` | Chapter 4 intro page 1 |
| `assets/backgrounds_hd/CH04_intro_02.png` | Chapter 4 intro page 2 |
| `assets/backgrounds_hd/CH04_intro_03.png` | Chapter 4 intro page 3 |
| `assets/backgrounds_hd/CH05_intro_01.png` | Chapter 5 intro page 1 |
| `assets/backgrounds_hd/CH05_intro_02.png` | Chapter 5 intro page 2 |
| `assets/backgrounds_hd/CH05_intro_03.png` | Chapter 5 intro page 3 |
| `assets/backgrounds_hd/CH06_intro_01.png` | Chapter 6 intro page 1 |
| `assets/backgrounds_hd/CH06_intro_02.png` | Chapter 6 intro page 2 |
| `assets/backgrounds_hd/CH06_intro_03.png` | Chapter 6 intro page 3 |
| `assets/backgrounds_hd/CH07_intro_01.png` | Chapter 7 intro page 1 |
| `assets/backgrounds_hd/CH07_intro_02.png` | Chapter 7 intro page 2 |
| `assets/backgrounds_hd/CH07_intro_03.png` | Chapter 7 intro page 3 |
| `assets/backgrounds_hd/CH08_intro_01.png` | Chapter 8 intro page 1 |
| `assets/backgrounds_hd/CH08_intro_02.png` | Chapter 8 intro page 2 |
| `assets/backgrounds_hd/CH08_intro_03.png` | Chapter 8 intro page 3 |
| `assets/backgrounds_hd/CH09_intro_01.png` | Chapter 9 intro page 1 |
| `assets/backgrounds_hd/CH09_intro_02.png` | Chapter 9 intro page 2 |
| `assets/backgrounds_hd/CH09_intro_03.png` | Chapter 9 intro page 3 |

## Unique chapter outro story plates

These outro pages still need their own image because they do not currently
reuse a room plate.

| Needed file | Chapter/page |
|---|---|
| `assets/backgrounds_hd/CH01_outro_01.png` | Chapter 1 outro page 1 |
| `assets/backgrounds_hd/CH02_outro_01.png` | Chapter 2 outro page 1 |
| `assets/backgrounds_hd/CH03_outro_02.png` | Chapter 3 outro page 2 |
| `assets/backgrounds_hd/CH04_outro_02.png` | Chapter 4 outro page 2 |
| `assets/backgrounds_hd/CH05_outro_01.png` | Chapter 5 outro page 1 |
| `assets/backgrounds_hd/CH05_outro_02.png` | Chapter 5 outro page 2 |
| `assets/backgrounds_hd/CH06_outro_02.png` | Chapter 6 outro page 2 |
| `assets/backgrounds_hd/CH08_outro_01.png` | Chapter 8 outro page 1 |
| `assets/backgrounds_hd/CH08_outro_02.png` | Chapter 8 outro page 2 |
| `assets/backgrounds_hd/CH09_outro_03.png` | Chapter 9 outro page 3 |

## Outro pages reusing room plates

Do **not** source separate images for these pages. They now reuse the canonical
room/location plate listed above:

| Chapter/page | Reused image |
|---|---|
| Chapter 1 outro page 2 | `C1_airstrip.png` |
| Chapter 2 outro pages 2–3 | `C2_hall.png`, `C2_living.png` |
| Chapter 3 outro pages 1 and 3 | `C3_gallery.png`, `C3_street.png` |
| Chapter 4 outro pages 1 and 3 | `C4_crash.png`, `C4_jet.png` |
| Chapter 5 outro page 3 | `C5_recovery.png` |
| Chapter 6 outro pages 1 and 3 | `C6_alain.png`, `C6_orly.png` |
| Chapter 7 outro pages 1–3 | `C7_lab.png`, `C7_treeline.png`, `C7_road.png` |
| Chapter 8 outro page 3 | `C8_club.png` |
| Chapter 9 outro pages 1–2 | `C9_dome.png`, `C9_tunnel.png` |

## Source references

- Room scene descriptions: `data/art_prompts.json`
- Room usage: `data/rooms/ch*.json`
- Chapter story usage: `data/chapters.json`
- Story plate descriptions: `docs/art-review-index.md`
- Shared art constraints: `docs/art-style-prompt.md`
