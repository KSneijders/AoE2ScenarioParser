import json
from pathlib import Path

from helper.pretty_format import pretty_format_list
from helper.printers import print_columns

# ---------------------------------------------------------------------------
# Generate a new condition or effect into the corresponding *-complete.json
# ---------------------------------------------------------------------------

VALID_TYPES = ('condition', 'effect')


def main(ce_type: str) -> None:
    base = Path(__file__).parent / f'{ce_type}s'

    attributes_file = base / f'{ce_type}-attributes.json'
    with attributes_file.open('r') as f:
        attribute_descriptions: dict[str, str] = json.load(f)

    ce_id = input(f'Enter {ce_type} ID: ')
    if ce_id == '':
        return
    ce_name = input(f'Enter {ce_type} name (snake_case): ')
    if ce_name == '':
        return

    print('\n\n')
    print_columns([k for k in attribute_descriptions.keys() if k != "type"], 4)
    print('\n\n')

    attributes = []
    while True:
        attr = input(f'Enter {ce_type} attribute to add: ')
        if attr == '':
            print(f'{ce_type.capitalize()} added:\n')
            print(f'[{ce_id}] {ce_name} => ' + pretty_format_list(attributes))
            break
        if attr not in attribute_descriptions:
            print(f'Invalid {ce_type} attribute')
            continue
        attributes.append(attr)

    complete_file = base / f'{ce_type}-definitions-complete.json'
    with complete_file.open('r') as f:
        complete_entries: list[dict] = json.load(f)

    complete_entries.append({
        'id': int(ce_id),
        'name': ce_name,
        'description': '----- DESCRIPTION TO BE FILLED -----',
        'attributes': [
            {
                'name': attr,
                'ref': None,
                'type': '------ UNKNOWN TYPE ------',
                'description': attribute_descriptions.get(attr),
                'default': None,
            }
            for attr in attributes
        ],
    })

    with complete_file.open('w') as f:
        f.write(json.dumps(complete_entries, indent=2))


if __name__ == '__main__':
    choice = input('Generate new [C/e]: ').strip().lower()
    if choice == 'c':
        main(ce_type='condition')
    elif choice == 'e':
        main(ce_type='effect')
    else:
        print('Invalid choice. Enter C/c for condition or E/e for effect.')
