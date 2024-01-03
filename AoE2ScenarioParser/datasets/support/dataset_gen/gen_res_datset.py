from typing import TypedDict

import requests
import regex

from common import tab, train_case

DefaultValue = str
UseDesc = str


class ResDesc(TypedDict):
    name: str
    desc: str
    defaults: dict[DefaultValue, UseDesc]
    note: str


ResId = int
ResDescs = dict[ResId, ResDesc]


def gen_docstr(desc: ResDesc) -> str:
    docstr = [
        tab('"' * 3),
        f"- Purpose: {desc['desc']}",
    ]

    if len(desc['defaults']) > 0:
        docstr.extend([
            "",
            "- Defaults:",
            "",
        ])

        for val, use in desc['defaults'].items():
            docstr.append(
                tab(f"- {val}: {use.strip()}")
            )  # use has a space prefix

    if len((desc['note'])) > 0:
        note = desc['note']

        if "See also:" in desc['note']:
            note = note.replace(")\n\n", ")\n")

            repl = r"    - https://ugc.aoe2.rocks/general/resources/resources/\1"
            note = regex.sub(r"\[.+\]\(\.\/(.+)\)", repl, note)

        docstr.extend([
            "",
            f"- Note: {note}",
        ])

    docstr.append('"' * 3)
    return "\n    ".join(docstr)


def gen_res_class(resources: ResDescs) -> str:
    klass = [r"class Attribute(_DataSetIntEnums):"]

    for id_, desc in resources.items():
        klass.extend([
            tab(train_case(desc["name"]) + f" = {id_}"),
            gen_docstr(desc)
        ])

    return "\n".join(klass)


def main():
    res = requests.get(
        r"https://raw.githubusercontent.com/Divy1211/AoE2DE_UGC_Guide/main/docs/general/resources/res_desc.json")
    resources = res.json()

    with open("resources.py", "w") as file:
        file.write(gen_res_class(resources))


if __name__ == "__main__":
    main()
