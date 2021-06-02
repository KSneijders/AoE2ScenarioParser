import json

from operator import itemgetter
from resources.data.support_scripts.strings_unit_dataset import vils, unique_units

namings = {'unit': 'units', 'building': 'buildings', 'hero': 'heroes', 'other': 'other'}
file_dict = {}
for filename in namings.keys():
    file_dict[filename] = open(f'./{namings[filename]}.py', 'w')

for name, file in file_dict.items():
    file.write(
        f"from AoE2ScenarioParser.datasets.support.info_dataset_base import InfoDatasetBase\n"
        f"\n\nclass {name.capitalize()}Info(InfoDatasetBase):\n")

    if name == 'unit':
        file.write(vils)
        file.write(unique_units + '\n')

with open('./../units.json', 'r') as file_content:
    json_content = json.load(file_content)

    for name, unit in json_content.items():
        file = file_dict[unit.get('type')]

        line = itemgetter('id', 'icon_id', 'dead_id', 'hotkey_id', 'gaia_only')(unit)
        file.write(f"    {name.upper()} = {', '.join([str(x) for x in line])}\n")

for file in file_dict.values():
    file.close()
