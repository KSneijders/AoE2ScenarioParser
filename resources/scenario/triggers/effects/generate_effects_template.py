import json
from pathlib import Path

from definitions import EffectDefinition, LegacyEffectDefinition
from resources.scenario.triggers.effects.definitions import AttributeDefinition

effects_json = (Path(__file__).parent.parent.parent.parent.parent
                / 'AoE2ScenarioParser' / 'versions' / 'DE' / 'v1.56' / 'effects.json')

effect_attribute_descriptions_file = (Path(__file__).parent / 'effect-attributes.json')
with effect_attribute_descriptions_file.open('r') as f:
    effect_attribute_descriptions: dict[str, str] = json.load(f)

result: list[EffectDefinition] = []
with effects_json.open('r') as f:
    legacy_effect_definition: dict[str, LegacyEffectDefinition] = json.load(f)

    for effect_id, effect_definition in legacy_effect_definition.items():
        if effect_id == '-1':  # Skip representation
            continue

        # noinspection PyTypedDict
        types: dict[str, str] = legacy_effect_definition['-1']['attribute_presentation']
        types['area'] = 'Area'
        types['location'] = 'Tile'

        for key, value in types.items():
            if value.endswith('[]'):
                value = f"list[{value[:-2]}]"
                types[key] = value

        attributes_list = effect_definition['attributes']
        if 'effect_type' in attributes_list:
            attributes_list.remove('effect_type')

        attributes: dict[str, str | None] = {attr: attr for attr in attributes_list}

        replacements = {
            'location_x': 'location',
            'location_y': None,
            'area_x1': 'area',
            'area_y1': None,
            'area_x2': None,
            'area_y2': None,
            'selected_object_ids': 'selected_objects'
        }

        for before, after in replacements.items():
            if before in attributes:
                attributes[before] = after

        attr_definitions = [
            AttributeDefinition(
                name = after,
                ref = None,
                type = types.get(before) or types.get(after) or '------ UNKNOWN TYPE ------',
                description = effect_attribute_descriptions.get(after, None),
                default = None,
            ) for before, after in attributes.items() if after is not None
        ]

        result.append(
            EffectDefinition(
                id = int(effect_id),
                name = effect_definition['name'],
                description = '----- DESCRIPTION TO BE FILLED -----',
                attributes = attr_definitions
            )
        )

complete_file = Path(__file__).parent / 'effect-definitions-complete.json'
with complete_file.open('w') as f:
    f.write(json.dumps(result, indent = 2))
