import json
from pathlib import Path

from AoE2ScenarioParser.helper.pretty_format import pretty_format_dict
from resources.scenario.triggers.effects.definitions import EffectDefinition

template_file = Path(__file__).parent / 'effect-definitions-template.json'
complete_file = Path(__file__).parent / 'effect-definitions-complete.json'


with complete_file.open('r') as f:
    complete_effects: dict[int, EffectDefinition] = {effect['id']: effect for effect in json.load(f)}

print(pretty_format_dict(complete_effects))

with template_file.open('r') as f:
    templates: list[EffectDefinition] = json.load(f)

    for effect in templates:
        for attribute in effect['attributes']:
            existing_attributes = complete_effects[effect['id']]['attributes']

            print(existing_attributes)