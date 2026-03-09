# AoE2ScenarioParser

`AoE2ScenarioParser` is a Python library for analyzing or editing `.aoe2scenario` files from **Age of Empires 2: Definitive Edition** outside the in-game editor.

Whether you want to automate repetitive edits, build complex trigger systems, or create tools for the community, this library gives you full programmatic control over your scenarios.

---

## What can it do?

The library is organized around **managers**, each one handles a different aspect of the scenario:

| Manager           | What you can do                                                                 |
|-------------------|---------------------------------------------------------------------------------|
| `trigger_manager` | Create, edit, and remove triggers, conditions, effects, and variables           |
| `unit_manager`    | Place, edit, and remove units (including buildings, heroes, and more)           |
| `map_manager`     | Change terrain types, elevation, and map size                                   |
| `player_manager`  | Set civilizations, starting ages, diplomacy, resources, and tech disables       |
| `option_manager`  | Configure victory conditions, team settings, and secondary game modes           |
| `xs_manager`      | Store XS scripts inside a scenario for easy multiplayer transfer                |
| `message_manager` | Edit the fields shown in the in-game Messages tab                               |

---

## Scenario support

Every scenario version from **1.36** _(November 2019)_ through **1.57** _(February 2026)_ is supported.  
If a new game update is just released, it may take a short time for the library to catch up — check the [Discord server] for the latest status.

[Discord server]: https://discord.gg/DRUtmugXT3

---

## Installation

```bash
pip install AoE2ScenarioParser
```

Requires **Python 3.8** or newer.

---

## Community

- **[Discord server]** — Ask questions, share your projects, and report bugs in the community server.
- **[Hello World guide](hello_world.md)** — A step-by-step walkthrough to get you up and running.
- **[Quick start](quick-start.md)** — Installation and setup instructions.

[Discord server]: https://discord.gg/DRUtmugXT3