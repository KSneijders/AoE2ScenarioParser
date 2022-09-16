from typing import List

from AoE2ScenarioParser import settings
from AoE2ScenarioParser.helper.bytes_conversions import bytes_to_int
from AoE2ScenarioParser.helper.exceptions import EndOfFileError
from AoE2ScenarioParser.helper.incremental_generator import IncrementalGenerator

attributes = ['on_refresh', 'on_construct', 'on_commit']


def vorl(retriever, value):
    """
    Variable or List

    Args:
        retriever (Retriever): The retriever
        value (List[Any]): A value to be put in the retriever

    Returns:
        The given list or the value inside it
    """
    if retriever.datatype.repeat != 1:
        return value

    if retriever.is_list is not None:
        return value if retriever.is_list else value[0]

    # Fallback to length check
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
                string_bytes = igenerator.get_bytes(string_length)
                retrieved_bytes.append(int_bytes + string_bytes)
    except EndOfFileError:
        # END_OF_FILE_MARK retriever should always go in here
        if is_end_of_file_mark(retriever):
            retriever.datatype.repeat = 0
            return []

    # If more bytes present in the file after END_OF_FILE_MARK
    handle_end_of_file_mark(igenerator, retriever)

    return retrieved_bytes


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
            "Please be so kind and include the map in question. Thanks again!",
            "",
            f"Extra data found in the file ({len(retrieved_bytes)} bytes):",
            f"\t'{retrieved_bytes}'"
        ]))
        retriever.datatype.repeat = 1
