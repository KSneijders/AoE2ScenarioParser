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

    docstr.append('"' * 3)
    return "\n    ".join(docstr)


def gen_attr_class(attrs: AttrDescs) -> str:
    lines = [
        'from __future__ import annotations',
        '',
        'from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums',
        '',
        '',
        r'class ObjectAttribute(_DataSetIntEnums):',
        '''    """''',
        '    This enum class provides the integer values used to reference all the different object attributes in the game. Used',
        '    in the \'Modify Attribute\' effect to control which attribute of an object is modified.',
        '',
        '    **Examples**',
        '',
        '    >>> ObjectAttribute.LINE_OF_SIGHT',
        '    <ObjectAttribute.LINE_OF_SIGHT: 1>',
        '''    """''',
    ]

    for id_, desc in attrs.items():
        lines.extend([
            tab(train_case(desc["name"]) + f" = {id_}"),
            gen_docstr(desc)
        ])

    return "\n".join(lines)


def main():
    url = r"https://raw.githubusercontent.com/Divy1211/AoE2DE_UGC_Guide/main/docs/general/attributes/attributes.json"
    res = requests.get(url)
    attrs = res.json()

    with open("../../trigger_lists/object_attribute.py", "w") as file:
        file.write(gen_attr_class(attrs))


if __name__ == "__main__":
    main()
