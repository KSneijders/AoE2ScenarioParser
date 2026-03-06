# Plan: Generate Per-Effect Python Classes from JSON

## Context
`effect-definitions-complete.json` documents all ~108 effect types. The v1 `Effect` base class
currently exposes every data slot as a named `RetrieverRef` property (e.g. `diplomacy`, `quantity`,
…). The goal is to strip those named properties from `Effect` entirely, making it a plain binary
struct. Each per-effect subclass then creates its own typed `RetrieverRef` properties pointing
directly into `Effect._properties[N]` or the handful of direct `Retriever` fields. `effect-attributes.json`
is restructured to serve as the authoritative lookup table for which index / field each attribute
maps to, so the generator never needs a hard-coded mapping in Python.

---

## Files to Create / Modify

| File | Action | Done |
|---|---|---|
| `AoE2ScenarioParser/sections/trigger_data/effect.py` | Remove all named `RetrieverRef` properties | [ ] |
| `resources/scenario/triggers/effects/effect-attributes.json` | Convert to `{name: {description_template, effect_reference}}` | [ ] |
| `resources/scenario/triggers/effects/effect-definitions-complete.json` | `ref` field becomes optional per-effect override (same format as `effect_reference`) | [ ] |
| `resources/scenario/triggers/effects/generate_effect_classes.py` | New — generator script | [ ] |
| `AoE2ScenarioParser/sections/trigger_data/effects/<name>.py` | Generated — ~108 files | [ ] |
| `AoE2ScenarioParser/sections/trigger_data/effects/__init__.py` | Regenerated — re-exports all classes | [ ] |

---

## Step 0 — Strip named properties from `Effect`

Remove every `RetrieverRef(ret(_properties), N)` line from `effect.py`. What remains:

```python
class Effect(BaseStruct):
    __default_ver__ = TRIGGER_LATEST

    type: int                    = Retriever(i32,          default = -1)
    _properties: list[int]       = Retriever(Array32[i32], default_factory = ..., on_read = ...)
    message: str                 = Retriever(nt_str32,     default = "")
    sound_name: str              = Retriever(nt_str32,     default = "")
    selected_unit_ids: list[int] = Retriever(i32,          default = -1, repeat = 0)
    message_option1: str         = Retriever(nt_str32,     default = "", min_ver = ...)
    message_option2: str         = Retriever(nt_str32,     default = "", min_ver = ...)

    @property
    def location(self) -> Tile: ...    # unchanged — directly reads _properties[14:16]

    @property
    def area(self) -> Area: ...        # unchanged — directly reads _properties[16:20]
```

---

## Step 1 — Restructure `effect-attributes.json`

Convert the flat `{name: description}` map to `{name: {description_template, effect_reference}}`.

**`effect_reference` format:**

| Value | Generated RetrieverRef call |
|---|---|
| `"properties:N"` | `RetrieverRef(ret(Effect._properties), N)` |
| `"direct:field_name"` | `RetrieverRef(Effect.field_name)` |
| `"@inherited"` | skip (already an `@property` on `Effect`) |
| `null` | `# TODO` comment in generated file |

**Full mapping (all entries in current `effect-attributes.json`):**

| Attribute key | `effect_reference` |
|---|---|
| `ai_script_goal` | `"properties:0"` |
| `quantity` | `"properties:1"` |
| `resource` | `"properties:2"` |
| `diplomacy_state` | `"properties:3"` |
| `object_unit_id` | `"properties:6"` |
| `source_player` | `"properties:7"` |
| `target_player` | `"properties:8"` |
| `technology_id` | `"properties:9"` |
| `str_id` | `"properties:10"` |
| `display_time` | `"properties:12"` |
| `trigger_id` | `"properties:13"` |
| `location` | `"@inherited"` |
| `location_object_ref` | `"properties:44"` |
| `area` | `"@inherited"` |
| `object_group` | `"properties:20"` |
| `object_type` | `"properties:21"` |
| `instruction_panel_position` | `"properties:22"` |
| `attack_stance` | `"properties:23"` |
| `time_unit` | `"properties:24"` |
| `enabled` | `"properties:25"` |
| `legacy_food` | `"properties:26"` |
| `legacy_wood` | `"properties:27"` |
| `legacy_stone` | `"properties:28"` |
| `legacy_gold` | `"properties:29"` |
| `item_id` | `"properties:30"` |
| `flash_object` | `"properties:31"` |
| `force_technology` | `"properties:32"` |
| `visibility_state` | `"properties:33"` |
| `scroll` | `"properties:34"` |
| `operation` | `"properties:35"` |
| `object_unit_id2` | `"properties:36"` |
| `button_location` | `"properties:37"` |
| `ai_signal_value` | `"properties:38"` |
| `object_attributes` | `"properties:40"` |
| `variable` | `"properties:41"` |
| `timer_id` | `"properties:42"` |
| `facet` | `"properties:43"` |
| `play_sound` | `"properties:45"` |
| `player_color` | `"properties:46"` |
| `color_mood` | `"properties:48"` |
| `reset_timer` | `"properties:49"` |
| `object_state` | `"properties:50"` |
| `action_type` | `"properties:51"` |
| `resource1` | `"properties:52"` |
| `resource1_quantity` | `"properties:53"` |
| `resource2` | `"properties:54"` |
| `resource2_quantity` | `"properties:55"` |
| `resource3` | `"properties:56"` |
| `resource3_quantity` | `"properties:57"` |
| `decision_id` | `"properties:58"` |
| `decision_option1_str_id` | `"properties:59"` |
| `decision_option2_str_id` | `"properties:60"` |
| `variable2` | `"properties:61"` |
| `message` | `"direct:message"` |
| `sound_name` | `"direct:sound_name"` |
| `selected_object_ids` | `"direct:selected_unit_ids"` |
| `message_option1` | `"direct:message_option1"` |
| `message_option2` | `"direct:message_option2"` |
| `armour_attack_quantity` | `null` — not in EffectStruct retrievers |
| `armour_attack_class` | `null` — not in EffectStruct retrievers |
| `quantity_float` | `"properties:70"` — stored as raw float bits in the i32 array |
| `object_group2` | `"properties:68"` |
| `object_type2` | `"properties:69"` |
| `facet2` | `"properties:71"` |
| `global_sound` | `"properties:72"` |
| `issue_group_command` | `"properties:73"` |
| `queue_action` | `"properties:74"` |
| `max_units_affected` | `"properties:62"` |
| `disable_garrison_unload_sound` | `"properties:63"` |
| `hotkey` | `"properties:64"` |
| `train_time` | `"properties:65"` |
| `local_technology_id` | `"properties:66"` — struct field name is `local_technology` |
| `disable_sound` | `"properties:67"` |

**Example entry:**
```json
"diplomacy_state": {
    "description_template": "The diplomacy stance to set",
    "effect_reference": "properties:3"
}
```

---

## Step 2 — `effect-definitions-complete.json` `ref` field

The `ref` field on individual attributes in this file is now an **optional per-effect override**
for `effect_reference`. It uses the same format (`"properties:N"`, `"direct:field"`,
`"@inherited"`). When `null`, the generator falls back to `effect-attributes.json`.

Only `location` and `area` attributes across all effects need `"ref": "@inherited"` since they
are `@property` on Effect — and this is already covered by `effect-attributes.json`, so the
definitions file `ref` fields can all remain `null` unless a specific effect needs a deviation.

---

## Step 3 — Generator Script: `generate_effect_classes.py`

### Reference resolution (per attribute)

```
effect_ref = attr["ref"]                        # from effect-definitions-complete.json (override)
          ?? effect_attributes[name]["effect_reference"]  # from effect-attributes.json (default)

if effect_ref == "@inherited"          → skip
elif effect_ref starts with "properties:" → RetrieverRef(ret(Effect._properties), N)
elif effect_ref starts with "direct:"     → RetrieverRef(Effect.<field_name>)
elif effect_ref is None                   → # TODO: <name> (add effect_reference to effect-attributes.json)
```

All generated RetrieverRef lines carry `  # type: ignore`.

### Logic flow

```
load effect_attrs = effect-attributes.json

for each effect in effect-definitions-complete.json:
    filename  = sanitize(effect.name) + ".py"
    classname = PascalCase(effect.name)          # "none" → "NoneEffect"

    if file exists:
        preserved_custom_imports = extract between CUSTOM IMPORTS markers
        preserved_custom_logic   = extract between CUSTOM LOGIC markers
    else:
        preserved_custom_imports = ""
        preserved_custom_logic   = ""

    for each attribute in effect.attributes:
        resolve effect_ref (override → default → None)
        emit line using effect_ref format

    write file
```

---

## Step 4 — Generated File Structure

```python
from __future__ import annotations

from bfp_rs import RetrieverRef, ret

from AoE2ScenarioParser.sections.trigger_data.effect import Effect

# ====== CUSTOM IMPORTS START ======
# ====== CUSTOM IMPORTS END ======


class ChangeDiplomacy(Effect):
    """
    This effect can be used to change the diplomacy stance of the source players
    with the target player. It does NOT change the stance both ways.
    """

    diplomacy_state: int = RetrieverRef(ret(Effect._properties), 3)  # type: ignore
    """The diplomacy stance to set."""

    source_player: int = RetrieverRef(ret(Effect._properties), 7)  # type: ignore
    """The player whose stance will be changed."""

    target_player: int = RetrieverRef(ret(Effect._properties), 8)  # type: ignore
    """The target player whose diplomacy stance will be changed for the source player."""

    message: str = RetrieverRef(Effect.message)  # type: ignore
    """The message to send to the player."""

    # TODO: armour_attack_class — add effect_reference to effect-attributes.json

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
```

**Notes:**
- Standard imports (`from __future__`, `bfp_rs`, `Effect`) are always regenerated.
- Only content between `CUSTOM IMPORTS` markers is preserved. Users add semantic type imports there.
- Type annotation uses the JSON `type` field as-is (e.g. `DiplomacyState`, `PlayerId`).
- Each attribute gets a docstring on the following line with its JSON description.
- Multi-line JSON descriptions (arrays) are joined with a space.
- The `CUSTOM IMPORTS` and `CUSTOM LOGIC` marker lines are never modified.

---

## Step 5 — Regenerate `__init__.py`

```python
# Auto-generated — do not edit manually
from .change_diplomacy import ChangeDiplomacy
from .research_technology import ResearchTechnology
# ...
```

Fully regenerated on every run.

---

## Verification

1. Verify `effect.py` imports cleanly after removing named properties
2. Run `python resources/scenario/triggers/effects/generate_effect_classes.py`
3. Confirm ~108 `.py` files appear in `AoE2ScenarioParser/sections/trigger_data/effects/`
4. Run `python -c "from AoE2ScenarioParser.sections.trigger_data.effects import *"` — no errors
5. Inspect a generated file (e.g. `change_diplomacy.py`) — confirm `RetrieverRef(ret(Effect._properties), N)` pattern
6. Add dummy content to CUSTOM IMPORTS / CUSTOM LOGIC, re-run, verify both survive
