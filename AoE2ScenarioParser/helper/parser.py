import time
from typing import Any, List

from AoE2ScenarioParser import settings
from AoE2ScenarioParser.helper.bytes_to_x import *
from AoE2ScenarioParser.helper.exceptions import EndOfFileError
from AoE2ScenarioParser.helper.incremental_generator import IncrementalGenerator
from AoE2ScenarioParser.helper.helper import listify
from AoE2ScenarioParser.helper.retriever import Retriever, get_retriever_by_name
from AoE2ScenarioParser.helper.retriever_dependency import DependencyAction

attributes = ['on_refresh', 'on_construct', 'on_commit']


def vorl(retriever: Retriever, var):
    """VorL: "Variable or List". This function returns the value based on retriever configurations"""
    if retriever.potential_list:
        if retriever.datatype.repeat != 1:
            return listify(var)
        for attribute in attributes:
            if hasattr(retriever, attribute):
                for x in listify(getattr(retriever, attribute)):
                    if x.dependency_type == DependencyAction.SET_REPEAT:
                        return listify(var)

    # Fallback to length check
    if type(var) is list:
        if len(var) == 1:
            return var[0]
    return var


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
                # Todo: Remove commented code (x3)
                # retrieved_bytes.append(repeat_generator(generator, var_len))
                retrieved_bytes.append(igenerator.get_bytes(var_len))
            else:  # String, Stored as: (signed int (n), string (string_length = n))
                # int_bytes = repeat_generator(generator, var_len)
                int_bytes = igenerator.get_bytes(var_len)
                string_length = bytes_to_int(int_bytes, signed=True)
                # retrieved_bytes.append(int_bytes)
                string_bytes = b'' if string_length == 0 else igenerator.get_bytes(string_length)
                retrieved_bytes.append(int_bytes + string_bytes)
                # retrieved_bytes.append(int_bytes + repeat_generator(generator, string_length))
    except EndOfFileError:
        if is_end_of_file_mark(retriever):
            retriever.datatype.repeat = 0
            return [b'\x00']

    # If more bytes present in the file after END_OF_FILE_MARK
    handle_end_of_file_mark(igenerator, retriever)
    # If invalid version (Currently only 1.40 supported)
    handle_unsupported_version(retriever, retrieved_bytes)

    return retrieved_bytes


def handle_retriever_dependency(retriever: Retriever, retrievers: List[Retriever], state, pieces):
    if not hasattr(retriever, f'on_{state}'):
        return
    if state == "construct":
        retriever_on_x = retriever.on_construct
    elif state == "commit":
        retriever_on_x = retriever.on_commit
    elif state == "refresh":
        retriever_on_x = retriever.on_refresh
    else:
        raise ValueError("State must be any of: construct, commit or refresh")

    retriever_on_x_list = listify(retriever_on_x)
    for retriever_on_x in retriever_on_x_list:
        dep_action = retriever_on_x.dependency_type
        dep_target = retriever_on_x.dependency_target
        if dep_action == DependencyAction.REFRESH_SELF:
            handle_retriever_dependency(retriever, retrievers, "refresh", pieces)
        elif dep_action == DependencyAction.REFRESH:
            listified_target = listify(dep_target.target_piece)
            listified_target_attr = listify(dep_target.piece_attr_name)
            for i in range(len(listified_target)):
                retriever_list = handle_dependency_target(listified_target[i], retrievers, pieces)
                retriever_to_be_refreshed = get_retriever_by_name(retriever_list, listified_target_attr[i])
                handle_retriever_dependency(retriever_to_be_refreshed, retriever_list, "refresh", pieces)
        elif dep_action in [DependencyAction.SET_VALUE, DependencyAction.SET_REPEAT]:
            # Todo: Instead of ['self', 'self'] & ['retr_name', 'retr_name'] just have: [('self', 'retr_name'), ...]
            listified_target = listify(dep_target.target_piece)
            listified_target_attr = listify(dep_target.piece_attr_name)
            retriever_data = []
            for i in range(len(listified_target)):
                retriever_list = handle_dependency_target(listified_target[i], retrievers, pieces)
                retriever_data.append(get_retriever_by_name(retriever_list, listified_target_attr[i]).data)
            value = handle_dependency_eval(retriever_on_x, retriever_data)
            if dep_action == DependencyAction.SET_VALUE:
                retriever.data = value
            elif dep_action == DependencyAction.SET_REPEAT:
                retriever.datatype.repeat = value


def handle_dependency_target(target_piece, retrievers, pieces):
    if target_piece == "self":
        retriever_list = retrievers
    else:
        retriever_list = pieces[target_piece].retrievers
    return retriever_list


def handle_dependency_eval(retriever_on_x, value):
    eval_locals = retriever_on_x.dependency_eval.eval_locals
    # values_as_variable = retriever_on_x.dependency_eval.values_as_variable
    attribute_names = listify(retriever_on_x.dependency_target.piece_attr_name)
    # If value as is used, use it as keys for the value!
    # Todo: Remove 'values_as_variable' logic
    # if values_as_variable:
    #     print(":o")
    #     eval_locals = {**eval_locals, **dict(zip(values_as_variable, value))}
    # else:
    for i in range(len(attribute_names)):
        eval_locals[attribute_names[i]] = value[i]
    return eval(retriever_on_x.dependency_eval.eval_code, {}, eval_locals)


def handle_unsupported_version(retriever: Retriever, retrieved_bytes: List[bytes]) -> None:
    if retriever.name == "version" and retriever.datatype.var == "c4":
        if bytes_to_fixed_chars(retrieved_bytes[0]) != "1.40":
            print("\n\n")
            print('\n'.join([
                "#### SORRY FOR THE INCONVENIENCE ####",
                "Scenarios that are not converted to the latest version of the game (Update 42848) are not "
                "supported at this time.",
                f"Your current version is: '{retrieved_bytes[0]}'. The currently only supported version is: '1.40'.",
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
