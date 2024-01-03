from typing import TypedDict

import requests

from common import tab, train_case


UseDesc = str
FlagValue = str
FlagDesc = str
class AttrDesc(TypedDict):
    name: str
    desc: str
    notes: list[UseDesc]
    flags: dict[FlagValue, FlagDesc]

AttrId = int
AttrDescs = dict[AttrId, AttrDesc]

def gen_docstr(desc: AttrDesc) -> str:
    docstr = [
        tab('"' * 3),
        desc['desc'],
    ]

    if len(desc['flags']) > 0:
        docstr.extend([
            "",
            "- Flags:",
            "",
        ])

        for val, use in desc['flags'].items():
            docstr.append(
                tab(f"- {val}: {use}")
            )

    if len(desc['notes']) > 0:
        docstr.extend([
            "",
            "- Notes:",
            "",
            *map(tab, desc["notes"]),
        ])

    docstr.append('"'*3)
    return "\n    ".join(docstr)

def gen_attr_class(attrs: AttrDescs) -> str:
    klass = [r"class ObjectAttribute(_DataSetIntEnums):"]

    for id_, desc in attrs.items():
        klass.extend([
            tab(train_case(desc["name"]) + f" = {id_}"),
            gen_docstr(desc)
        ])

    return "\n".join(klass)


def main():
    res = requests.get(r"https://raw.githubusercontent.com/Divy1211/AoE2DE_UGC_Guide/main/docs/general/attributes/attributes.json")
    attrs = res.json()

    with open("attributes.py", "w") as file:
        file.write(gen_attr_class(attrs))


if __name__ == "__main__":
    main()
