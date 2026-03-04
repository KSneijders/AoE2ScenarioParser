# Plan: Generate Per-Effect Python Classes from JSON

## Context
`effect-definitions-complete.json` contains full documentation for all ~108 effect types. The v1
`Effect` base class (`sections/trigger_data/effect.py`) will have all properties renamed to match
the JSON definition names and made private (prefixed with `_`). This eliminates the need for an
explicit `ref` mapping for almost every attribute — the generator simply tries `Effect._<json_name>`
directly. Each per-effect subclass then provides the public API with typed `RetrieverRef` properties.

---

## Files to Create / Modify

| File | Action | Done |
|---|---|---|
| `AoE2ScenarioParser/sections/trigger_data/effect.py` | Rename properties to match JSON names, make private | [ ] |
| `resources/scenario/triggers/effects/effect-definitions-complete.json` | Set `ref: "@inherited"` for `location` / `area` only | [ ] |
| `resources/scenario/triggers/effects/generate_effect_classes.py` | New — generator script | [ ] |
| `AoE2ScenarioParser/sections/trigger_data/effects/<name>.py` | Generated — ~108 files | [ ] |
| `AoE2ScenarioParser/sections/trigger_data/effects/__init__.py` | Regenerated — re-exports all classes | [ ] |

---

## Step 0 — Rename `Effect` class properties

Rename all properties to `_<json_name>` convention. Properties whose current name already matches
the JSON name just get the `_` prefix. Others get both renamed and prefixed.

**Renames required (old → new):**

| Current name | New private name | JSON attribute name |
|---|---|---|
| `diplomacy` | `_diplomacy_state` | `diplomacy_state` |
| `unit_type1` | `_object_unit_id` | `object_unit_id` |
| `technology` | `_technology_id` | `technology_id` |
| `string_id` | `_str_id` | `str_id` |
| `instruction_display_time` | `_display_time` | `display_time` |
| `trigger_idx` | `_trigger` | `trigger` |
| `location_object_reference` | `_location_object_ref` | `location_object_ref` |
| `food` | `_legacy_food` | `legacy_food` |
| `wood` | `_legacy_wood` | `legacy_wood` |
| `stone` | `_legacy_stone` | `legacy_stone` |
| `gold` | `_legacy_gold` | `legacy_gold` |
| `force_research_technology` | `_force_technology` | `force_technology` |
| `unit_type2` | `_object_unit_id2` | `object_unit_id2` |
| `timer` | `_timer_id` | `timer_id` |
| `color` | `_player_color` | `player_color` |
| `string_id_option1` | `_decision_option1_str_id` | `decision_option1_str_id` |
| `string_id_option2` | `_decision_option2_str_id` | `decision_option2_str_id` |
| `selected_unit_ids` | `_selected_objects` | `selected_objects` |
| All others | `_<same_name>` | _(prefix only)_ |

The `location` and `area` `@property` methods keep their current names (they are not Retrievers
and cannot be wrapped in RetrieverRef in subclasses).

---

## Step 1 — Minimal `ref` updates in `effect-definitions-complete.json`

With the Effect rename done, the generator auto-resolves every attribute by trying `Effect._<name>`.
Only two entries need explicit `ref` values:

| JSON `name` | `ref` value | Reason |
|---|---|---|
| `location` | `"@inherited"` | `@property`, not a Retriever |
| `area` | `"@inherited"` | `@property`, not a Retriever |

**Attributes with no Effect property** (leave `ref: null` → `# TODO` in output):
`armour_attack_quantity`, `armour_attack_class`, `quantity_float`, `object_group2`,
`object_type2`, `global_sound`, `issue_group_command`, `queue_action`,
`max_units_affected`, `disable_garrison_unload_sound`, `hotkey`, `train_time`,
`local_technology_id`, `disable_sound`, `facet2`

---

## Step 2 — Generator Script: `generate_effect_classes.py`

### RetrieverRef syntax — two patterns

| Property type | Examples | Generated call |
|---|---|---|
| Direct `Retriever` (not in `_properties`) | `_message`, `_sound_name`, `_selected_objects`, `_message_option1`, `_message_option2` | `RetrieverRef(Effect._<name>)` |
| `_properties`-based `RetrieverRef` | `_diplomacy_state`, `_quantity`, `_source_player`, … | `RetrieverRef(ret(Effect._<name>))` |
| No named property (integer `ref`) | attributes not exposed on Effect | `RetrieverRef(ret(Effect._properties), <N>)` |

`ret()` is required when passing a `RetrieverRef` (not a raw `Retriever`). All generated lines
carry `  # type: ignore`.

### Sets used by the generator (names without `_`; generator prepends it)

**DIRECT_RETRIEVERS** (`RetrieverRef(Effect._<name>)`, no `ret()`):
```
message, sound_name, selected_objects, message_option1, message_option2
```

**PROPS_RETRIEVERS** (`RetrieverRef(ret(Effect._<name>))`):
```
ai_script_goal, quantity, resource, diplomacy_state, num_objects_selected,
legacy_location_object_ref, object_unit_id, source_player, target_player,
technology_id, str_id, sound_id, display_time, trigger,
object_group, object_type, instruction_panel_position, attack_stance,
time_unit, enabled, legacy_food, legacy_wood, legacy_stone, legacy_gold,
item_id, flash_object, force_technology, visibility_state, scroll, operation,
object_unit_id2, button_location, ai_signal_value, unknown3, object_attributes,
variable, timer_id, facet, location_object_ref, play_sound, player_color,
unknown4, color_mood, reset_timer, object_state, action_type, resource1,
resource1_quantity, resource2, resource2_quantity, resource3, resource3_quantity,
decision_id, decision_option1_str_id, decision_option2_str_id, variable2
```

### Logic flow

```
for each effect in JSON:
    filename   = sanitize(effect.name) + ".py"          # e.g. change_diplomacy.py
    classname  = PascalCase(effect.name)                # e.g. ChangeDiplomacy
                 (append "Effect" if name is a Python keyword, e.g. NoneEffect)

    if file exists:
        preserved_custom_imports = extract between CUSTOM IMPORTS markers
        preserved_custom_logic   = extract between CUSTOM LOGIC markers
    else:
        preserved_custom_imports = ""
        preserved_custom_logic   = ""

    for each attribute:
        target = ref (if ref is a string) else name     # without "_" prefix
        if ref == "@inherited"              → skip
        elif target in DIRECT_RETRIEVERS    → RetrieverRef(Effect._<target>)
        elif target in PROPS_RETRIEVERS     → RetrieverRef(ret(Effect._<target>))
        elif ref is int                     → RetrieverRef(ret(Effect._properties), <ref>)
        else                                → # TODO: <name> (no ref — add ref to JSON)

    write file
```

---

## Step 3 — Generated File Structure

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

    diplomacy_state: int = RetrieverRef(ret(Effect._diplomacy_state))  # type: ignore
    """The diplomacy stance to set."""

    source_player: int = RetrieverRef(ret(Effect._source_player))  # type: ignore
    """The player whose stance will be changed."""

    target_player: int = RetrieverRef(ret(Effect._target_player))  # type: ignore
    """The target player whose diplomacy stance will be changed for the source player."""

    message: int = RetrieverRef(Effect._message)  # type: ignore
    """The message to send to the player."""

    # TODO: armour_attack_class — no ref defined, add ref to effect-definitions-complete.json

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
```

**Notes:**
- Standard imports (`from __future__`, `bfp_rs`, `Effect`) are always regenerated.
- Only content between `CUSTOM IMPORTS` markers is preserved. Users place extra type imports there.
- Type annotation uses the JSON `type` field as-is (e.g. `DiplomacyState`, `PlayerId`).
- Each attribute gets a docstring on the next line with its JSON description.
- Multi-line JSON descriptions (arrays) are joined with a space.
- The `CUSTOM IMPORTS` and `CUSTOM LOGIC` marker lines are never modified by the generator.

---

## Step 4 — Regenerate `__init__.py`

```python
# Auto-generated — do not edit manually
from .change_diplomacy import ChangeDiplomacy
from .research_technology import ResearchTechnology
# ... one line per effect ...
```

`__init__.py` is fully regenerated (not section-preserved).

---

## Verification

1. Verify `effect.py` compiles after the renames (`python -c "from AoE2ScenarioParser.sections.trigger_data.effect import Effect"`)
2. Run `python resources/scenario/triggers/effects/generate_effect_classes.py`
3. Confirm ~108 `.py` files appear in `AoE2ScenarioParser/sections/trigger_data/effects/`
4. Run `python -c "from AoE2ScenarioParser.sections.trigger_data.effects import *"` — no import errors
5. Inspect a generated file and verify `RetrieverRef` calls match the pattern above
6. Add dummy content in the CUSTOM IMPORTS / CUSTOM LOGIC sections, re-run generator, verify survival
