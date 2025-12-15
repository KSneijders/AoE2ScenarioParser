import json
from pathlib import Path

from helper.pretty_format import pretty_format_dict

effects_json = Path(__file__).parent.parent.parent / 'AoE2ScenarioParser' / 'versions' / 'DE' / 'v1.56' / 'effects.json'

with effects_json.open() as f:
    effects = json.load(f)
    print(pretty_format_dict(effects))
    