import json
from pathlib import Path

from helper.pretty_format import pretty_format_list
from helper.printers import print_columns
from resources.scenario.triggers.effects.definitions import AttributeDefinition, EffectDefinition

# --------------------------------------------------------------------
# Generate a new effect into the effect-definitions-complete.json file
# --------------------------------------------------------------------
# When adding a new effect, execute this module to produce a single
# new effect. After this, fill all empty attributes inside the
# generated JSON file.

if __name__ == '__main__':
    effect_attribute_descriptions_file = (Path(__file__).parent / 'effect-attributes.json')
    with effect_attribute_descriptions_file.open('r') as f:
        effect_attribute_descriptions: dict[str, str] = json.load(f)

    print('\n\n')
    print_columns(list(effect_attribute_descriptions.keys()), 4)
    print('\n\n')

    effect_id = input("Enter effect ID: ")
    if effect_id == '':
        exit()
    effect_name = input("Enter effect name (snake_case): ")
    if effect_name == '':
        exit()

    effect_attributes = []

    while True:
        effect_attribute = input("Enter effect attribute to add: ")

        if effect_attribute == '':
            print('Effect added:\n')
            print(f'[{effect_id}] {effect_name} => ' + pretty_format_list(effect_attributes))
            break

        if effect_attribute not in effect_attribute_descriptions:
            print('Invalid effect attribute')

        effect_attributes.append(effect_attribute)

    complete_file = Path(__file__).parent / 'effect-definitions-complete.json'
    with complete_file.open('r') as f:
        complete_effects: list[EffectDefinition] = json.load(f)

    complete_effects.append(
        EffectDefinition(
            id = int(effect_id),
            name = effect_name,
            description = '----- DESCRIPTION TO BE FILLED -----',
            attributes = [
                AttributeDefinition(
                    name = attr,
                    ref = None,
                    type = '------ UNKNOWN TYPE ------',
                    description = effect_attribute_descriptions.get(attr),
                    default = None,
                ) for attr in effect_attributes
            ]
        )
    )

    with complete_file.open('w') as f:
        f.write(json.dumps(complete_effects, indent = 2))
