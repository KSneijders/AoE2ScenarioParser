import json

files = ["unit", "building", "hero", "other"]
f_plural = {"unit": "units", "building": "buildings", "hero": "heroes", "other": "other"}
f_dict = {}
for x in files:
    f = open(f'./{f_plural[x]}.py', 'w')
    f_dict[x] = f

f_list = f_dict.values()

gaia_only = """
    @staticmethod
    def gaia_only():
        result = []
        for x in __CLASSNAME__:
            if x.IS_GAIA:
                result.append(x)
        return result\n"""
non_gaia = """
    @staticmethod
    def non_gaia():
        result = []
        for x in __CLASSNAME__:
            if not x.IS_GAIA:
                result.append(x)
        return result\n\n"""

for name, file in f_dict.items():
    file.write(f"from enum import Enum\n\n\nclass {name.capitalize()}Info(Enum):")

    for index, id_type in enumerate(['ID', 'ICON_ID', 'DEAD_ID', 'IS_GAIA_ONLY']):
        file.write(f"\n    @property\n")
        file.write(f"    def {id_type}(self):\n")
        file.write(f"        return self.value[{index}]\n")

    file.write(gaia_only.replace('__CLASSNAME__', f'{name.capitalize()}Info'))
    file.write(non_gaia.replace('__CLASSNAME__', f'{name.capitalize()}Info'))

with open('./../dataset.json', 'r') as file_content:
    json_content = json.load(file_content)

    for name, unit in json_content.items():
        x = f_dict[unit.get('type')]
        x.write(f"    {name.upper()} = {unit['id']}, {unit['icon_id']}, {unit['dead_id']}, {unit['gaia_only']}\n")

for x in f_list:
    x.close()
