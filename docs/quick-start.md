# Quick Start

## Installation

Install using **pip**:

```bash
pip install AoE2ScenarioParser
```

Requires **Python 3.8** or newer. Dependencies install automatically.

To update an existing installation:

```bash
pip install --no-cache-dir --upgrade AoE2ScenarioParser
```

---

## Reading a scenario

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

scenario = AoE2DEScenario.from_file("path/to/your/scenario.aoe2scenario")
```

> [!TIP]
> Your scenario files are usually found at:
> `C:\Users\<USERNAME>\Games\Age of Empires 2 DE\<STEAMID>\resources\_common\scenario`

---

## Making changes

All edits are made through **managers**. Each manager handles a different part of the scenario:

```py
trigger_manager = scenario.trigger_manager
unit_manager    = scenario.unit_manager
map_manager     = scenario.map_manager
player_manager  = scenario.player_manager
# etc.
```

For a full overview of what each manager can do, see the [Cheatsheets](#).

---

## Writing a scenario

> [!WARNING]
> Always write to a **different file** than your input. Overwriting your source scenario can cause data loss in case of bugs or mistakes.

```py
scenario.write_to_file("path/to/your/output.aoe2scenario")
```

---

For a step-by-step walkthrough with examples, see the [Hello World](hello_world.md) guide.