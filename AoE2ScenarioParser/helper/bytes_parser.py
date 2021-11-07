from typing import List

from AoE2ScenarioParser import settings
from AoE2ScenarioParser.helper.bytes_conversions import bytes_to_int
from AoE2ScenarioParser.helper.exceptions import EndOfFileError
from AoE2ScenarioParser.helper.incremental_generator import IncrementalGenerator
from AoE2ScenarioParser.sections.retrievers.retriever import Retriever

attributes = ['on_refresh', 'on_construct', 'on_commit']


def vorl(retriever: Retriever, value: list):
    """
    This function checks if a value in a retriever is meant to be a variable or list, and returns it in that form

    Args:
        retriever (Retriever): The retriever
        value (List[Any]): The value to convert to the correct form

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


def retrieve_bytes(igenerator: IncrementalGenerator, retriever: Retriever) -> List[bytes]:
    """
    Get the bytes required to set the data in the given retriever

    Args:
        igenerator (IncrementalGenerator): The generator to return the bytes from
        retriever (Retriever): The retriever for which the bytes need to be retrieved

    Returns:
        The corresponding bytes in a list.
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
        if is_end_of_file_mark(retriever):
            retriever.datatype.repeat = 0
            return []
    except TypeError:
        print(retriever)
        print(retriever.datatype.repeat)
        exit()  # Todo: Should not exit (?)

    # If more bytes present in the file after END_OF_FILE_MARK
    handle_end_of_file_mark(igenerator, retriever)

    return retrieved_bytes


def is_end_of_file_mark(retriever: Retriever) -> bool:
    """
    Returns true if the retriever is the __END_OF_FILE_MARK__ retriever else false

    Args:
        retriever (Retriever): The retriever to check

    Returns:
        A boolean value
    """
    return retriever.name == "__END_OF_FILE_MARK__"


def handle_end_of_file_mark(igenerator: IncrementalGenerator, retriever: Retriever) -> None:
    """
    This function prints a message if the file has more bytes in it than expected by the structure

    Args:
        igenerator (IncrementalGenerator): The generator to check if more bytes are present
        retriever (Retriever): The retriever to check if it's the end of file mark

    Returns:
        This function does not return anything
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
            "Extra data found in the file:",
            f"\t'{retrieved_bytes}'"
        ]))
        retriever.datatype.repeat = 1
