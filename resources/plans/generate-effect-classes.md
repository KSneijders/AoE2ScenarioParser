# Plan: Generate Per-Effect Python Classes from JSON

## Context
`effect-definitions-complete.json` documents all ~108 effect types. The v1 `Effect` base class
previously exposed every data slot as a named `RetrieverRef` property — those have been renamed
with a leading underscore (e.g. `_diplomacy_state`, `_quantity`), making `Effect` a plain binary
struct with private `_`-prefixed slots. Each per-effect subclass creates its own typed public
`RetrieverRef` properties via `RetrieverRef(Effect._<attr_name>)`, where `<attr_name>` comes
directly from the attribute `name` in `effect-definitions-complete.json` — no index/field mapping
is required.

---

## Files to Create / Modify

| File | Action | Done |
|---|---|---|
| `AoE2ScenarioParser/sections/trigger_data/effect.py` | Rename named `RetrieverRef` properties to `_`-prefixed | [x] |
| `resources/scenario/triggers/effects/effect-attributes.json` | No structural changes needed — used as-is for descriptions | — |
| `resources/scenario/triggers/effects/effect-definitions-complete.json` | `ref` field is optional override when attribute name ≠ Effect field name | [x] |
| `resources/scenario/triggers/effects/generate_effect_classes.py` | New — generator script | [ ] |
| `AoE2ScenarioParser/sections/trigger_data/effects/<name>.py` | Generated — ~108 files | [ ] |
| `AoE2ScenarioParser/sections/trigger_data/effects/__init__.py` | Regenerated — re-exports all classes | [ ] |

---

## Step 0 — ~~Strip named properties from `Effect`~~ ✓ Done

Named `RetrieverRef` properties have been renamed to `_`-prefixed (e.g. `diplomacy_state` → `_diplomacy_state`). What remains in `effect.py`:

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

    _location: ...   = RetrieverRef(...)   # _-prefixed, like all other attributes
    _area: ...       = RetrieverRef(...)   # _-prefixed, like all other attributes
```

---

## Step 1 — ~~`effect-definitions-complete.json` `ref` field~~ ✓ Done

`effect-attributes.json` is used as-is (no structural changes). It remains the source of
attribute descriptions for the generator.

The `ref` field on individual attributes in `effect-definitions-complete.json` is an **optional
override** for when the attribute's JSON name differs from the corresponding `_`-prefixed field
on `Effect`. When `null` (the common case), the generator emits:

```
RetrieverRef(Effect._<attr_name>)
```

where `<attr_name>` is the attribute's `name` field. The `ref` field only needs to be set for
the handful of attributes where the JSON name and the Effect field name diverge.

---

## Step 2 — Generator Script: `generate_effect_classes.py`

### Reference resolution (per attribute)

```
ref = attr["ref"]   # from effect-definitions-complete.json (optional override)

if ref is not None  → RetrieverRef(Effect.<ref>)          # use override verbatim
else                → RetrieverRef(Effect._<attr_name>)   # default: prepend _
```

All generated RetrieverRef lines carry `  # type: ignore`.

### Logic flow

```
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
        resolve ref (override → default _<attr_name>)
        emit RetrieverRef line

    write file
```

---

## Step 3 — Generated File Structure

```python
from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.sections.trigger_data.effect import Effect

# ====== CUSTOM IMPORTS START ======
# ====== CUSTOM IMPORTS END ======


class ChangeDiplomacy(Effect):
    """
    This effect can be used to change the diplomacy stance of the source players
    with the target player. It does NOT change the stance both ways.
    """

    diplomacy_state: int = RetrieverRef(Effect._diplomacy_state)  # type: ignore
    """The diplomacy stance to set."""

    source_player: int = RetrieverRef(Effect._source_player)  # type: ignore
    """The player whose stance will be changed."""

    target_player: int = RetrieverRef(Effect._target_player)  # type: ignore
    """The target player whose diplomacy stance will be changed for the source player."""

    message: str = RetrieverRef(Effect._message)  # type: ignore
    """The message to send to the player."""

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

## Step 4 — Regenerate `__init__.py`

```python
# Auto-generated — do not edit manually
from .change_diplomacy import ChangeDiplomacy
from .research_technology import ResearchTechnology
# ...
```

Fully regenerated on every run.

---

## Verification

1. Verify `effect.py` imports cleanly
2. Run `python resources/scenario/triggers/effects/generate_effect_classes.py`
3. Confirm ~108 `.py` files appear in `AoE2ScenarioParser/sections/trigger_data/effects/`
4. Run `python -c "from AoE2ScenarioParser.sections.trigger_data.effects import *"` — no errors
5. Inspect a generated file (e.g. `change_diplomacy.py`) — confirm `RetrieverRef(Effect._<attr_name>)` pattern
6. Add dummy content to CUSTOM IMPORTS / CUSTOM LOGIC, re-run, verify both survive
