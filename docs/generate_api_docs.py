"""
Generate API documentation using pdoc.

Usage:
    python generate_api_docs.py

Output is written to docs/api/ as a self-contained HTML site.
The docs/_sidebar.md is updated automatically with a single API Reference link.
"""

import os
import subprocess
from pathlib import Path
from typing import List, Tuple

ROOT       = Path(__file__).parent.parent
OUT_DIR    = ROOT / "docs" / "api"
SIDEBAR    = ROOT / "docs" / "_sidebar.md"
PDOC       = ROOT / ".venv1" / "Scripts" / "pdoc.exe"
PDOC_THEME = ROOT / "docs" / "_assets" / "pdoc_theme"
DOCS_URL   = "https://ksneijders.github.io/AoE2ScenarioParser/"

# Markers used to locate the API section in the sidebar.
# The content between them is replaced on every run.
def discover_package(package: str) -> List[Tuple[str, str]]:
    """
    Auto-discover all public modules in a package and return (module_path, display_name) tuples.
    Display names are derived from the filename: snake_case -> TitleCase (e.g. action_type -> ActionType).
    """
    package_dir = ROOT / Path(package.replace(".", "/"))
    modules = []
    for f in sorted(package_dir.glob("*.py")):
        if f.stem.startswith("_"):
            continue
        module_path = f"{package}.{f.stem}"
        display_name = "".join(word.capitalize() for word in f.stem.split("_"))
        modules.append((module_path, display_name))
    return modules


# Markers used to locate the API section in the sidebar.
# The content between them is replaced on every run.
SIDEBAR_START = "<!-- API_START -->"
SIDEBAR_END   = "<!-- API_END -->"

# Modules grouped for display on the pdoc index page.
# Each entry: (module_path, display_name)
GROUPS = [
    ("Scenario", [
        ("AoE2ScenarioParser.scenarios.aoe2_scenario",                              "AoE2Scenario"),
        ("AoE2ScenarioParser.scenarios.aoe2_de_scenario",                           "AoE2DEScenario"),
        ("AoE2ScenarioParser.settings",                                             "Settings"),
    ]),
    ("Managers", [
        ("AoE2ScenarioParser.objects.managers.trigger_manager",                     "Trigger Manager"),
        ("AoE2ScenarioParser.objects.managers.unit_manager",                        "Unit Manager"),
        ("AoE2ScenarioParser.objects.managers.map_manager",                         "Map Manager"),
        ("AoE2ScenarioParser.objects.managers.player_manager",                      "Player Manager"),
        ("AoE2ScenarioParser.objects.managers.option_manager",                      "Option Manager"),
        ("AoE2ScenarioParser.objects.managers.xs_manager",                          "XS Manager"),
        ("AoE2ScenarioParser.objects.managers.message_manager",                     "Message Manager"),
    ]),
    ("Data Objects", [
        ("AoE2ScenarioParser.objects.data_objects.trigger",                         "Trigger"),
        ("AoE2ScenarioParser.objects.data_objects.effect",                          "Effect"),
        ("AoE2ScenarioParser.objects.data_objects.condition",                       "Condition"),
        ("AoE2ScenarioParser.objects.data_objects.variable",                        "Variable"),
        ("AoE2ScenarioParser.objects.data_objects.unit",                            "Unit"),
        ("AoE2ScenarioParser.objects.data_objects.terrain_tile",                    "Terrain Tile"),
        ("AoE2ScenarioParser.objects.data_objects.player.player",                   "Player"),
    ]),
    ("Support", [
        ("AoE2ScenarioParser.objects.support.area",                                 "Area / AreaAttr / AreaState"),
        ("AoE2ScenarioParser.objects.support.trigger_select",                       "TriggerSelect"),
        ("AoE2ScenarioParser.objects.support.trigger_ce_lock",                      "TriggerCELock"),
        ("AoE2ScenarioParser.objects.support.new_effect",                           "NewEffect"),
        ("AoE2ScenarioParser.objects.support.new_condition",                        "NewCondition"),
        ("AoE2ScenarioParser.objects.support.xs_check",                             "XsCheck"),
    ]),
    ("Datasets", [
        ("AoE2ScenarioParser.datasets.units",                                       "UnitInfo"),
        ("AoE2ScenarioParser.datasets.buildings",                                   "BuildingInfo"),
        ("AoE2ScenarioParser.datasets.heroes",                                      "HeroInfo"),
        ("AoE2ScenarioParser.datasets.techs",                                       "TechInfo"),
        ("AoE2ScenarioParser.datasets.terrains",                                    "TerrainId"),
        ("AoE2ScenarioParser.datasets.projectiles",                                 "ProjectileInfo"),
        ("AoE2ScenarioParser.datasets.players",                                     "PlayerId / PlayerColorId / ColorId"),
        ("AoE2ScenarioParser.datasets.conditions",                                  "ConditionId"),
        ("AoE2ScenarioParser.datasets.effects",                                     "EffectId"),
        ("AoE2ScenarioParser.datasets.other",                                       "OtherInfo"),
        ("AoE2ScenarioParser.datasets.scenario_variant",                            "ScenarioVariant"),
        ("AoE2ScenarioParser.datasets.object_support",                              "Civilization / StartingAge"),
        ("AoE2ScenarioParser.datasets.support.info_dataset_base",                   "InfoDatasetBase"),
    ]),
    ("Datasets — Trigger Lists", discover_package("AoE2ScenarioParser.datasets.trigger_lists")),
]


def module_to_path(module: str) -> str:
    """Convert a dotted module name to its pdoc HTML path."""
    return module.replace(".", "/") + ".html"


def generate_index_template():
    """Write a custom index.html.jinja2 to the theme folder with grouped module links."""
    lines = [
        '{% extends "default/index.html.jinja2" %}',
        '{% block nav %}',
        '<h2>API Reference</h2>',
        '<ul>',
    ]

    for group_name, modules in GROUPS:
        lines.append(f'  <li><strong>{group_name}</strong>')
        lines.append('    <ul>')
        for module, display in modules:
            href = module_to_path(module)
            lines.append(f'      <li><a href="{href}">{display}</a></li>')
        lines.append('    </ul>')
        lines.append('  </li>')

    lines += [
        '</ul>',
        '<footer><a href="../">← Back to Docs</a></footer>',
        '{% endblock %}',
    ]

    template_path = PDOC_THEME / "index.html.jinja2"
    template_path.write_text("\n".join(lines), encoding="utf-8")


def generate_docs() -> bool:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    generate_index_template()

    all_modules = [module for _, entries in GROUPS for module, _ in entries]

    print("Generating API docs with pdoc...")
    result = subprocess.run(
        [str(PDOC), "-o", str(OUT_DIR), "-t", str(PDOC_THEME), *all_modules],
        capture_output=True,
        text=True,
        cwd=ROOT,
        env={**os.environ, "PYTHONPATH": str(ROOT)},
    )

    if result.stderr:
        for line in result.stderr.splitlines():
            print(f"  {line}")

    if result.returncode != 0:
        print("ERROR: pdoc failed.")
        return False

    print(f"  -> {OUT_DIR.relative_to(ROOT)}")
    return True


def update_sidebar(success: bool):
    api_link = "api/index.html" if success else "#"
    api_block = "\n".join([
        SIDEBAR_START,
        "",
        f'- <a href="{api_link}" target="_blank">API Reference</a>',
        "",
        SIDEBAR_END,
    ])

    sidebar = SIDEBAR.read_text(encoding="utf-8")

    if SIDEBAR_START in sidebar and SIDEBAR_END in sidebar:
        before = sidebar[:sidebar.index(SIDEBAR_START)]
        after  = sidebar[sidebar.index(SIDEBAR_END) + len(SIDEBAR_END):]
        sidebar = before.rstrip() + "\n\n" + api_block + after
    else:
        sidebar = sidebar.rstrip() + "\n\n" + api_block + "\n"

    SIDEBAR.write_text(sidebar, encoding="utf-8")
    print("Sidebar updated.")


if __name__ == "__main__":
    success = generate_docs()
    update_sidebar(success)
    print("Done.")
