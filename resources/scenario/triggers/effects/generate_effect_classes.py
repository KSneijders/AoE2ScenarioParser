#!/usr/bin/env python3
"""Generate per-effect Python classes from effect-definitions-complete.json."""
from __future__ import annotations

import json
import keyword
import re
from pathlib import Path

EFFECTS_JSON = Path(__file__).parent / "effect-definitions-complete.json"
_PKG_ROOT = Path(__file__).parent.parent.parent.parent.parent / "AoE2ScenarioParser"
OUTPUT_DIR = _PKG_ROOT / "sections" / "trigger_data" / "effects"
DATASETS_ROOT = _PKG_ROOT / "datasets"

# @formatter:off
CUSTOM_IMPORTS_START = "    # ====== CUSTOM IMPORTS START ======"
CUSTOM_IMPORTS_PASS =  "    pass"
CUSTOM_IMPORTS_END =   "    # ====== CUSTOM IMPORTS END ======"
CUSTOM_LOGIC_START =   "    # ====== CUSTOM LOGIC START ======"
CUSTOM_LOGIC_END =     "    # ====== CUSTOM LOGIC END ======"
# @formatter:on

PROPERTY_INHERIT_SNIPPET = f"""
    @property
    def <ATTR>(self) -> <GET_ATTR_TYPE>:
        \"\"\"<ATTR_DESC>\"\"\"
        return self._<ATTR>

    @<ATTR>.setter
    def <ATTR>(self, value: <SET_ATTR_TYPE>) -> None:
        \"\"\"<ATTR_DESC>\"\"\"
        self._<ATTR> = value"""


def to_pascal_case(name: str) -> str:
    name = name.replace('/', '_')
    return "".join(word.capitalize() for word in name.split("_"))


def effect_class_name(effect_name: str) -> str:
    pascal = to_pascal_case(effect_name)
    if keyword.iskeyword(pascal) or pascal in dir(__builtins__):
        pascal += "Effect"
    return pascal


def get_property_snippet(name: str, desc: str, get_type: str, set_type: str) -> str:
    return (PROPERTY_INHERIT_SNIPPET
            .replace("<ATTR>", name)
            .replace("<ATTR_DESC>", desc)
            .replace("<GET_ATTR_TYPE>", get_type)
            .replace("<SET_ATTR_TYPE>", set_type))


RETS = [
    'message',
    'sound_name',
    'selected_objects',
    'message_option1',
    'message_option2',
]

PROPERTIES: dict[str, tuple[str, str]] = {
    'location': ('Tile', 'TileT'),
    'area': ('Area', 'AreaT'),
}

ALTERNATE_TYPES: dict[str, str] = {
    "Tile": "Tile, TileT",
    "Area": "Area, AreaT",
}


ROOT_DATASET_CLASSES: dict[str, str] = {
    "BuildingInfo":    "AoE2ScenarioParser.datasets.buildings",
    "ConditionId":     "AoE2ScenarioParser.datasets.conditions",
    "EffectId":        "AoE2ScenarioParser.datasets.effects",
    "HeroInfo":        "AoE2ScenarioParser.datasets.heroes",
    "OtherInfo":       "AoE2ScenarioParser.datasets.other",
    "ProjectileInfo":  "AoE2ScenarioParser.datasets.projectiles",
    "ScenarioVariant": "AoE2ScenarioParser.datasets.scenario_variant",
    "TechInfo":        "AoE2ScenarioParser.datasets.techs",
    "TerrainId":       "AoE2ScenarioParser.datasets.terrains",
    "UnitInfo":        "AoE2ScenarioParser.datasets.units",
    "Tile, TileT":     "AoE2ScenarioParser.objects.support",
    "Area, AreaT":     "AoE2ScenarioParser.objects.support",
    "Unit":            "AoE2ScenarioParser.sections",
    "Trigger":         "AoE2ScenarioParser.sections",
    "Variable":        "AoE2ScenarioParser.sections",
}


def discover_dataset_classes() -> dict[str, str]:
    """Scan trigger_data and player_data, deriving class names from filenames (snake_case → PascalCase).

    Root-level dataset classes are mapped manually via _ROOT_DATASET_CLASSES.
    Returns a mapping of {ClassName: "AoE2ScenarioParser.datasets.<pkg>.<module>"}.
    """
    class_map = dict(ROOT_DATASET_CLASSES)
    for pkg in ("trigger_data", "player_data"):
        pkg_dir = DATASETS_ROOT / pkg
        if not pkg_dir.exists():
            continue
        for filepath in sorted(pkg_dir.glob("*.py")):
            if filepath.name == "__init__.py":
                continue
            cls_name = to_pascal_case(filepath.stem)
            class_map[cls_name] = f"AoE2ScenarioParser.datasets.{pkg}.{filepath.stem}"
    return class_map


def extract_type_names(type_str: str) -> list[str]:
    """Return all capitalised identifiers from a type annotation string."""
    return re.findall(r"\b([A-Z][A-Za-z0-9_]*)\b", type_str)


def extract_between(content: str, start: str, end: str) -> str:
    i = content.find(start)
    j = content.find(end)
    if i == -1 or j == -1:
        return ""
    return content[i + len(start):j]


def format_docstring_body(desc: str | list[str]) -> str:
    if isinstance(desc, list):
        return "\n    ".join(desc)
    return desc


def generate_file(effect: dict, dataset_map: dict[str, str]) -> str:
    has_ret_ref = False

    name = effect["name"]
    cls = effect_class_name(name)
    desc = effect.get("description", "")
    attrs = effect.get("attributes", [])

    # Collect dataset imports needed by this effect's attribute types
    dataset_imports: dict[str, str] = {}
    for attr in attrs:
        for type_name in extract_type_names(attr.get("type", "")):
            if type_name in ALTERNATE_TYPES:
                type_name = ALTERNATE_TYPES[type_name]
            if type_name in dataset_map:
                dataset_imports[type_name] = dataset_map[type_name]

    lines: list[str] = [
        "from __future__ import annotations",
        "",
        "from bfp_rs import RetrieverRef",
        "",
    ]

    for cls_name in sorted(dataset_imports):
        lines.append(f"from {dataset_imports[cls_name]} import {cls_name}")

    lines += [
        "from AoE2ScenarioParser.sections.trigger_data.effect import Effect",
        "",
        "if True:",
        CUSTOM_IMPORTS_START,
        CUSTOM_IMPORTS_PASS,
        CUSTOM_IMPORTS_END,
        "",
        "",
        f"class {cls}(Effect):",
        '    """',
        f"    {format_docstring_body(desc)}",
        '    """',
    ]

    for attr in attrs:
        attr_name = attr["name"]
        attr_ref = attr.get("ref")
        attr_type = attr.get("type", "int")
        attr_desc = attr.get("description", "")

        if attr_name in PROPERTIES:
            lines.append(get_property_snippet(attr_name, attr_desc, *PROPERTIES[attr_name]))
            continue

        if isinstance(attr_desc, list):
            attr_desc = " ".join(attr_desc)

        if attr_name in RETS:
            ret_ref = f"ret(Effect._{attr_name})"
            has_ret_ref = True
        else:
            ret_ref = f"Effect._{attr_name}"

        ref_expr = f"RetrieverRef(Effect.{attr_ref})" if attr_ref else f"RetrieverRef({ret_ref})"

        lines += [
            "",
            f"    {attr_name}: {attr_type} = {ref_expr}",
            f'    """{attr_desc}"""',
        ]

    lines += [
        "",
        CUSTOM_LOGIC_START,
        CUSTOM_LOGIC_END,
        "",
    ]

    joined_lines = "\n".join(lines)
    if has_ret_ref:
        joined_lines = joined_lines.replace("from bfp_rs import RetrieverRef", "from bfp_rs import ret, RetrieverRef")
    return joined_lines


def apply_preserved_sections(new_content: str, existing_content: str) -> str:
    custom_imports = extract_between(existing_content, CUSTOM_IMPORTS_START, CUSTOM_IMPORTS_END)
    custom_logic = extract_between(existing_content, CUSTOM_LOGIC_START, CUSTOM_LOGIC_END)

    custom_imports_pass = f"\n{CUSTOM_IMPORTS_PASS}\n"
    if not custom_imports.strip():
        custom_imports = custom_imports_pass

    new_content = new_content.replace(
        f"{CUSTOM_IMPORTS_START}{custom_imports_pass}{CUSTOM_IMPORTS_END}",
        f"{CUSTOM_IMPORTS_START}{custom_imports}{CUSTOM_IMPORTS_END}",
    )
    if custom_logic:
        new_content = new_content.replace(
            f"{CUSTOM_LOGIC_START}\n{CUSTOM_LOGIC_END}",
            f"{CUSTOM_LOGIC_START}{custom_logic}{CUSTOM_LOGIC_END}",
        )

    return new_content


def main() -> None:
    with open(EFFECTS_JSON, encoding = "utf-8") as f:
        effects = json.load(f)

    dataset_map = discover_dataset_classes()
    OUTPUT_DIR.mkdir(parents = True, exist_ok = True)

    entries: list[tuple[str, str]] = []

    for effect in effects:
        name: str = effect["name"]
        name = name.replace('/', '_')
        cls = effect_class_name(name)
        filepath = OUTPUT_DIR / f"{name}.py"
        entries.append((name, cls))

        new_content = generate_file(effect, dataset_map)

        if filepath.exists():
            new_content = apply_preserved_sections(new_content, filepath.read_text(encoding = "utf-8"))

        filepath.write_text(new_content, encoding = "utf-8")
        print(f"  {filepath.name}")

    # __init__.py
    init_lines = ["# Auto-generated — do not edit manually"]
    for name, cls in entries:
        init_lines.append(f"from .{name} import {cls}")
    init_lines.append("")
    (OUTPUT_DIR / "__init__.py").write_text("\n".join(init_lines), encoding = "utf-8")
    print(f"  __init__.py")
    print(f"\nDone — {len(effects)} effect files generated.")


if __name__ == "__main__":
    main()
