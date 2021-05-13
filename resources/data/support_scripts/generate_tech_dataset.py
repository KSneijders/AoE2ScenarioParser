import json

from resources.data.support_scripts.strings_tech_dataset import unique_techs

files = ["tech"]
f_plural = {"tech": "techs"}
f_dict = {}
for x in files:
    f = open(f'./{f_plural[x]}.py', 'w')
    f_dict[x] = f

f_list = f_dict.values()

from_id = """
    @classmethod
    def from___NAME__(cls, value):
        if value == -1:
            raise ValueError("-1 is not a valid __NAME__ value")
        for x in cls._member_map_.values():
            if x.value[__VALUE__] == value:
                return x
        raise ValueError(f"{value} is not a valid __NAME__ value")\n"""

for name, file in f_dict.items():
    file.write(f"from enum import Enum\n\n\nclass {name.capitalize()}Info(Enum):")

    for index, id_type in enumerate(['ID', 'ICON_ID']):  # 'HOTKEY_ID'
        file.write(f"\n    @property\n")
        file.write(f"    def {id_type}(self):\n")
        file.write(f"        return self.value[{index}]\n")

        file.write(
            from_id.replace('__VALUE__', str(index)).replace('__NAME__', f'{id_type.lower()}')
        )

    file.write(unique_techs)

    file.write("\n")

with open('./../techs.json', 'r') as file_content:
    json_content = json.load(file_content)

    for name, unit in json_content.items():
        x = f_dict['tech']
        x.write(f"    {name.upper()} = {unit['id']}, {unit['icon_id']}\n")  # , {unit['hotkey_id']}

for x in f_list:
    x.close()
