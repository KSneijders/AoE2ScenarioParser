import json


files = ["tech"]
f_plural = {"tech": "techs"}
f_dict = {}
for x in files:
    f = open(f'./{f_plural[x]}.py', 'w')
    f_dict[x] = f

f_list = f_dict.values()

for name, file in f_dict.items():
    file.write(f"from enum import Enum\n\n\nclass {name.capitalize()}Info(Enum):")

    for index, id_type in enumerate(['ID', 'ICON_ID']):
        file.write(f"\n    @property\n")
        file.write(f"    def {id_type}(self):\n")
        file.write(f"        return self.value[{index}]\n")

    file.write("\n")

with open('./../techs.json', 'r') as file_content:
    json_content = json.load(file_content)

    for name, unit in json_content.items():
        x = f_dict['tech']
        x.write(f"    {name.upper()} = {unit['id']}, {unit['icon_id']}\n")

for x in f_list:
    x.close()
