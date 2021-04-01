import json

from resources.data.support_scripts.strings_unit_dataset import vils, unique_units, from_id, non_gaia, gaia_only

files = ['unit', 'building', 'hero', 'other']
f_plural = {'unit': 'units', 'building': 'buildings', 'hero': 'heroes', 'other': 'other'}
f_dict = {}
for x in files:
    f = open(f'./{f_plural[x]}.py', 'w')
    f_dict[x] = f

f_list = f_dict.values()

for name, file in f_dict.items():
    file.write(f"from enum import Enum\n\n\nclass {name.capitalize()}Info(Enum):")

    for index, id_type in enumerate(['ID', 'ICON_ID', 'DEAD_ID', 'IS_GAIA_ONLY']):
        if name == 'hero' and id_type == 'IS_GAIA_ONLY':
            continue
        file.write(f"\n    @property\n")
        file.write(f"    def {id_type}(self):\n")
        file.write(f"        return self.value[{index}]\n")

        if id_type != 'IS_GAIA_ONLY':
            file.write(from_id.replace('__VALUE__', str(index)).replace('__NAME__', f'{id_type.lower()}'))

    if name != 'hero':
        file.write(gaia_only.replace('__CLASSNAME__', name.capitalize()))
        file.write(non_gaia.replace('__CLASSNAME__', name.capitalize()))

    if name == 'unit':
        file.write(vils)
        file.write(unique_units)

    file.write("\n")

with open('./../units.json', 'r') as file_content:
    json_content = json.load(file_content)

    for name, unit in json_content.items():
        x = f_dict[unit.get('type')]
        x.write(f"    {name.upper()} = {unit['id']}, {unit['icon_id']}, {unit['dead_id']}, {unit['gaia_only']}\n")

for x in f_list:
    x.close()
