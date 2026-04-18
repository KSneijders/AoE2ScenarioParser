import json
from pathlib import Path

from helper.pretty_format import pretty_format_list
from helper.printers import print_columns
from resources.scenario.triggers.conditions.definitions import AttributeDefinition, ConditionDefinition

# -----------------------------------------------------------------------
# Generate a new condition into the condition-definitions-complete.json file
# -----------------------------------------------------------------------
# When adding a new condition, execute this module to produce a single
# new condition. After this, fill all empty attributes inside the
# generated JSON file.

if __name__ == '__main__':
    condition_attribute_descriptions_file = (Path(__file__).parent / 'condition-attributes.json')
    with condition_attribute_descriptions_file.open('r') as f:
        condition_attribute_descriptions: dict[str, str] = json.load(f)

    print('\n\n')
    print_columns(list(condition_attribute_descriptions.keys()), 4)
    print('\n\n')

    condition_id = input("Enter condition ID: ")
    if condition_id == '':
        exit()
    condition_name = input("Enter condition name (snake_case): ")
    if condition_name == '':
        exit()

    condition_attributes = []

    while True:
        condition_attribute = input("Enter condition attribute to add: ")

        if condition_attribute == '':
            print('Condition added:\n')
            print(f'[{condition_id}] {condition_name} => ' + pretty_format_list(condition_attributes))
            break

        if condition_attribute not in condition_attribute_descriptions:
            print('Invalid condition attribute')

        condition_attributes.append(condition_attribute)

    complete_file = Path(__file__).parent / 'condition-definitions-complete.json'
    with complete_file.open('r') as f:
        complete_conditions: list[ConditionDefinition] = json.load(f)

    complete_conditions.append(
        ConditionDefinition(
            id = int(condition_id),
            name = condition_name,
            description = '----- DESCRIPTION TO BE FILLED -----',
            attributes = [
                AttributeDefinition(
                    name = attr,
                    ref = None,
                    type = '------ UNKNOWN TYPE ------',
                    description = condition_attribute_descriptions.get(attr),
                    default = None,
                ) for attr in condition_attributes
            ]
        )
    )

    with complete_file.open('w') as f:
        f.write(json.dumps(complete_conditions, indent = 2))
