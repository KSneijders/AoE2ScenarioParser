import json

"""
Prints the dataset to console. Not written to a file due to it not having it's own file anyway.
"""

explanation = """
    Enum for all possible static keys
    
    Many hotkeys will be missing from this file (Like arrow up). The reason for this is explained in the UGC guide:
    https://divy1211.github.io/AoE2DE_UGC_Guide/general/hotkeys/hotkeys/
    We'll try to update this list every update (when new strings are added to the game).
    """

with open('../hotkeys.json', 'r') as file:
    json_content = json.load(file)

    print("\nfrom enum import IntEnum\n")
    print("class Hotkey(IntEnum):")
    print(f"\t\"\"\"{explanation}\"\"\"\n")

    for char, struct in json_content.items():
        string_id, text_char = list(struct.values())

        if text_char:
            print(f"\t{text_char.upper()} = {string_id}")
