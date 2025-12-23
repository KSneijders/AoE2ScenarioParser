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

        attributes = effect_definition['attributes']
        if 'effect_type' in attributes:
            attributes.remove('effect_type')

        replacements = {
            'location_x': '_location_x',
            'location_y': '_location_y',
            'area_x1':    '_area_x1',
            'area_y1':    '_area_y1',
            'area_x2':    '_area_x2',
            'area_y2':    '_area_y2',
        }

        # TODO: Maybe replace with something like "HIDDEN PROPS" per attribute (for location: location_x)

        for before, after in replacements.items():
            if before in attributes:
                if before == "location_x":
                    attributes.append("location")
                if before == "area_x1":
                    attributes.append("area")

                attributes.remove(before)
                attributes.append(after)

        attributes = [
            AttributeDefinition(
                name = attribute,
                ref = None,
                type = types.get(attribute, '------ UNKNOWN TYPE ------'),
                description = effect_attribute_descriptions.get(attribute, None),
                default = None,
            ) for attribute in attributes
        ]

        result.append(
            EffectDefinition(
                id = int(effect_id),
                name = effect_definition['name'],
                description = '----- DESCRIPTION TO BE FILLED -----',
                attributes = attributes
            )
        )


complete_file = Path(__file__).parent / 'effect-definitions-complete.json'
with complete_file.open('w') as f:
    f.write(json.dumps(result, indent=2))
