"""
Generate API documentation using pdoc.

Usage:
    python generate_api_docs.py

Output is written to docs/api/. The generated HTML can be accessed directly
alongside the docsify site (e.g. docs/api/AoE2ScenarioParser.html).
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
OUTPUT_DIR = ROOT / "docs" / "api"

# Modules to include in the generated docs.
# Add or remove entries here to control what gets documented.
MODULES = [
    "AoE2ScenarioParser.scenarios.aoe2_de_scenario",
    "AoE2ScenarioParser.objects.managers.de.trigger_manager_de",
    "AoE2ScenarioParser.objects.managers.de.unit_manager_de",
    "AoE2ScenarioParser.objects.managers.de.map_manager_de",
    "AoE2ScenarioParser.objects.managers.player_manager",
    "AoE2ScenarioParser.objects.managers.option_manager",
    "AoE2ScenarioParser.objects.managers.de.xs_manager_de",
    "AoE2ScenarioParser.objects.managers.message_manager",
    "AoE2ScenarioParser.objects.data_objects.trigger",
    "AoE2ScenarioParser.objects.data_objects.effect",
    "AoE2ScenarioParser.objects.data_objects.condition",
    "AoE2ScenarioParser.objects.data_objects.unit",
    "AoE2ScenarioParser.objects.data_objects.terrain_tile",
    "AoE2ScenarioParser.objects.data_objects.player.player",
    "AoE2ScenarioParser.objects.data_objects.variable",
    "AoE2ScenarioParser.objects.support.area",
    "AoE2ScenarioParser.datasets.units",
    "AoE2ScenarioParser.datasets.buildings",
    "AoE2ScenarioParser.datasets.heroes",
    "AoE2ScenarioParser.datasets.terrains",
    "AoE2ScenarioParser.datasets.players",
    "AoE2ScenarioParser.datasets.object_support",
    "AoE2ScenarioParser.datasets.trigger_lists",
]


def ensure_pdoc():
    try:
        import pdoc  # noqa: F401
    except ImportError:
        print("pdoc not found — installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pdoc"])


def generate():
    ensure_pdoc()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Generating API docs -> {OUTPUT_DIR}")

    subprocess.check_call(
        [
            sys.executable, "-m", "pdoc",
            "--output-dir", str(OUTPUT_DIR),
            *MODULES,
        ],
        cwd=ROOT,
    )

    print(f"Done. Open docs/api/index.html to preview.")


if __name__ == "__main__":
    generate()
