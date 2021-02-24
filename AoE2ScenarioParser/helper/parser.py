import time
from typing import List, TYPE_CHECKING

from AoE2ScenarioParser import settings
from AoE2ScenarioParser.helper.bytes_to_x import *
from AoE2ScenarioParser.helper.exceptions import EndOfFileError
from AoE2ScenarioParser.helper.helper import listify
from AoE2ScenarioParser.helper.incremental_generator import IncrementalGenerator
from AoE2ScenarioParser.sections.dependencies.dependency_action import DependencyAction

attributes = ['on_refresh', 'on_construct', 'on_commit']


def vorl(retriever, value):
    """
    Variable or List

    Args:
        retriever (Retriever): The retriever
        value (Any): A value to be put in the retriever

    Returns:
        Given value itself or list form depending on retriever configuration
    """
    if retriever.potential_list:
        if retriever.datatype.repeat != 1:
            return listify(value)
        for attribute in attributes:
            if hasattr(retriever, attribute):
                for x in listify(getattr(retriever, attribute)):
                    if x.dependency_action == DependencyAction.SET_REPEAT:
                        return listify(value)

    # Fallback to length check
    if type(value) is list:
        if len(value) == 1:
            return value[0]
    return value


def retrieve_bytes(igenerator: IncrementalGenerator, retriever) -> List[bytes]:
    """
    Retrieves the bytes belonging to this retriever.

    Args:
        igenerator (IncrementalGenerator): The generator to return the bytes from
        retriever (Retriever): The retriever holding the bytes

    Returns:
        The corresponding bytes in a list. When 4 int8s need to retrieved, the list will have a length of 4 where each
            entry is 1 byte each.
    """
    var_type, var_len = retriever.datatype.type_and_length
    retrieved_bytes = []

    try:
        for i in range(retriever.datatype.repeat):
            if var_type != "str":  # (Signed) ints, floats, chars, plain bytes etc.
                retrieved_bytes.append(igenerator.get_bytes(var_len))
            else:  # String, Stored as: (signed int (n), string (string_length = n))
                int_bytes = igenerator.get_bytes(var_len)
                string_length = bytes_to_int(int_bytes, signed=True)
                string_bytes = b'' if string_length == 0 else igenerator.get_bytes(string_length)
                retrieved_bytes.append(int_bytes + string_bytes)
    except EndOfFileError:
        if is_end_of_file_mark(retriever):
            retriever.datatype.repeat = 0
            return []

    # If more bytes present in the file after END_OF_FILE_MARK
    handle_end_of_file_mark(igenerator, retriever)
    # If invalid version (Currently only 1.40 supported)
    handle_unsupported_version(retriever, retrieved_bytes)

    return retrieved_bytes


def handle_unsupported_version(retriever, retrieved_bytes: List[bytes]) -> None:
    if retriever.name == "version" and retriever.datatype.var == "c4":
        v = bytes_to_fixed_chars(retrieved_bytes[0])
        # Todo: Decide to keep, maybe check using float version. Only show when < ??? - (Probably just remove)
        if v not in ["1.40", "1.41"]:
            print("\n\n")
            print('\n'.join([
                "#### SORRY FOR THE INCONVENIENCE ####",
                "Scenarios that are not converted to the latest version of the game (Update 42848) are not "
                "supported at this time.",
                f"Your current version is: '{v}'. The currently only supported version is: '1.40'.",
                "The reason for this is a huge rework for version support.",
                "This rework will take some time to complete, so until then, please upgrade your scenario to the "
                "newest version. You can do this by saving it again in the in-game editor.",
                "If you do not want to upgrade the scenarios, please downgrade this library to version 0.0.11. You "
                "can do so by executing the following command in cmd:",
                "",
                ">>> pip install --force-reinstall AoE2ScenarioParser==0.0.11",
                "",
                "Thank you in advance."
            ]))
            time.sleep(1)
            print("- KSneijders")
            time.sleep(1)
            raise ValueError("Currently unsupported version. Please read the message above. Thank you.")


def is_end_of_file_mark(retriever) -> bool:
    """Returns true if the retriever is the __END_OF_FILE_MARK__ retriever else false"""
    return retriever.name == "__END_OF_FILE_MARK__"


def handle_end_of_file_mark(igenerator, retriever) -> None:
    """
    Print message when the END_OF_FILE_MARK is reached and more bytes are present.\n
    You can disable this check (and thereby this message) using:\n
    ``>> from AoE2ScenarioParser import settings``\n
    ``>> settings.NOTIFY_UNKNOWN_BYTES = False``

    Args:
        igenerator (IncrementalGenerator): The generator to check if more bytes are present
        retriever (Retriever): The retriever to check if it's the end of file mark

    Returns:
        None
    """
    if is_end_of_file_mark(retriever) and settings.NOTIFY_UNKNOWN_BYTES:
        retrieved_bytes = igenerator.get_remaining_bytes()
        print("\n\n" + "\n".join([
            "The file being read has more bytes than anticipated.",
            "Please notify me (MrKirby/KSneijders) about this message!",
            "This will help with understanding more parts of scenario files! Thanks in advance!",
            "You can contact me using:",
            "- Discord: MrKirby#5063",
            "- Github: https://github.com/KSneijders/AoE2ScenarioParser/issues",
            "",
            "You can disable this check (and thereby this message) using:",
            ">>> from AoE2ScenarioParser import settings",
            ">>> settings.NOTIFY_UNKNOWN_BYTES = False",
            "",
            "Please be so kind and include the map in question. Thanks again!\n\n",
            "",
            "Extra data found in the file:",
            f"\t'{retrieved_bytes}'"
        ]))
        retriever.datatype.repeat = 1
