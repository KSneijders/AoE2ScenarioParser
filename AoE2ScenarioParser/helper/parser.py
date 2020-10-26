from typing import Any, List

import AoE2ScenarioParser.pieces.structs.aoe2_struct
from AoE2ScenarioParser.helper.bytes_to_x import *
from AoE2ScenarioParser.helper.generator import repeat_generator as r_gen
from AoE2ScenarioParser.helper.retriever import Retriever, get_retriever_by_name
from AoE2ScenarioParser.helper.retriever_dependency import DependencyAction

types = [
    "s",  # Signed int
    "u",  # Unsigned int
    "f",  # FloatingPoint
    "c",  # Character string
    "str",  # Variable length string
    "data",  # Data (Can be changed by used using bytes_to_x functions)
]


def vorl(var: Any, retriever: Retriever = None):
    """vorl stands for "Variable or List". This function returns the value if the list is a size of 1"""
    if Retriever is not None:
        if retriever.set_repeat is not None or retriever.datatype.repeat is not 1:
            return listify(var)
    if type(var) is list:
        if len(var) is 1:
            return var[0]
    return var


def listify(var):
    """Always return item as list"""
    if type(var) is list:
        return var
    else:
        return [var]


class Parser:
    def __init__(self):
        self._saves = dict()

    def retrieve_value(self, generator, retriever, retrievers=None, pieces=None, as_length=False):
        if (pieces is None or retrievers is None) and not as_length:
            raise ValueError("Normal retrieval of length requires pieces parameter.")
        if (pieces is not None and retrievers is None) or (pieces is None and retrievers is not None):
            raise ValueError("The retrievers and pieces parameters always need to be used simultaneously")
        length = 0
        result = list()
        var_type, var_len = datatype_to_type_length(retriever.datatype.var)

        if retriever.set_repeat is not None:
            retriever.datatype.repeat = parse_repeat_string(self._saves, retriever.set_repeat)

        if retriever.on_construct is not None:
            handle_retriever_dependency(retriever, retrievers, "construct", pieces)

        for i in range(0, retriever.datatype.repeat):
            length += var_len

            if var_type == "struct":
                val = retriever.datatype.var(self)
                val.set_data_from_generator(generator, pieces)
                result.append(val)
                i = val.get_length()

                length += i
                continue
            if var_type == "u" or var_type == "s":
                val = bytes_to_int(r_gen(generator, var_len), signed=(var_type == "s"))
            elif var_type == "f":
                if var_len == 4:
                    val = bytes_to_float(r_gen(generator, var_len))
                else:  # Always 4 except for trigger version
                    val = bytes_to_double(r_gen(generator, var_len))
            elif var_type == "c":
                val = bytes_to_fixed_chars(r_gen(generator, var_len))
            elif var_type == "data":
                val = r_gen(generator, var_len)
            elif var_type == "str":
                string_length = bytes_to_int(r_gen(generator, var_len), endian="little", signed=True)
                try:
                    data = r_gen(generator, string_length)
                    val = bytes_to_str(data)
                    length += string_length
                except StopIteration as e:
                    print(f"\n[StopIteration] Parser.retrieve_value: \n"
                          f"\tRetriever: {retriever}\n"
                          f"\tString length: {string_length}\n")
                    raise StopIteration(e)
            else:
                break
            result.append(val)

        if retriever.save_as is not None:
            self.add_to_saves(retriever.save_as, vorl(result, retriever))

        return vorl(result, retriever) if not as_length else length

    def add_to_saves(self, name, value):
        self._saves[name] = value


def handle_retriever_dependency(retriever: Retriever, retrievers: List[Retriever], state, pieces):
    print(retriever.name)
    if state == "construct":
        retriever_on_x = retriever.on_construct
    elif state == "commit":
        retriever_on_x = retriever.on_commit
    elif state == "refresh":
        retriever_on_x = retriever.on_refresh
    else:
        raise ValueError("State must be any of: construct, commit or refresh")

    dep_action = retriever_on_x.dependency_type
    dep_target = retriever_on_x.dependency_target
    if dep_action == DependencyAction.REFRESH_SELF:
        # print("REFRESH SELF!")
        handle_retriever_dependency(retriever, retrievers, "refresh", pieces)
    elif dep_action == DependencyAction.REFRESH:
        listified_target = listify(dep_target.target_piece)
        listified_target_attr = listify(dep_target.piece_attr_name)
        for i in range(len(listified_target)):
            retriever_list = handle_dependency_target(listified_target[i], retrievers, pieces)
            retriever_to_be_refreshed = get_retriever_by_name(retriever_list, listified_target_attr[i])
            # print("REFRESH OTHER!")
            handle_retriever_dependency(retriever_to_be_refreshed, retriever_list, "refresh", pieces)
    elif dep_action in [DependencyAction.SET_VALUE, DependencyAction.SET_REPEAT]:
        retriever_list = handle_dependency_target(dep_target.target_piece, retrievers, pieces)
        retriever_data = get_retriever_by_name(retriever_list, dep_target.piece_attr_name).data
        value = handle_dependency_eval(retriever_on_x, retriever_data)
        if dep_action == DependencyAction.SET_VALUE:
            retriever.data = value
        elif dep_action == DependencyAction.SET_REPEAT:
            retriever.datatype.repeat = value

    # print("END", state, retriever)


def handle_dependency_target(target_piece, retrievers, pieces):
    if target_piece == "self":
        retriever_list = retrievers
    else:
        retriever_list = eval("pieces[x].retrievers", {}, {
            'pieces': pieces,
            'x': target_piece
        })
        print("NOT SELF")
        print(retriever_list)
    return retriever_list


def handle_dependency_eval(retriever_on_x, value):
    eval_locals = retriever_on_x.dependency_eval.eval_locals
    eval_locals['x'] = value
    return eval(retriever_on_x.dependency_eval.eval_code, {}, eval_locals)


def parse_repeat_string(saves, repeat_string):
    while True:
        start = repeat_string.find("{")
        end = repeat_string.find("}")

        if start is -1 and end is -1:
            break

        inclusive = repeat_string[start:end + 1]
        exclusive = repeat_string[start + 1:end]

        repeat_string = repeat_string.replace(inclusive, str(saves[exclusive]))
    return eval(repeat_string)


def calculate_length(generator, retriever_list):
    parser = Parser()
    total_length = 0

    for retriever in retriever_list:
        total_length += parser.retrieve_value(generator, retriever, as_length=True)

    return total_length


def datatype_to_type_length(var):
    try:
        if issubclass(var, AoE2ScenarioParser.pieces.structs.aoe2_struct.AoE2Struct):
            return "struct", 0
        else:  # Not possible at this time
            return "", 0
    except TypeError:
        pass

    var_type = ""
    var_len = ""

    for char in var:
        if char.isnumeric():
            var_len += char
        else:
            var_type += char

    if var_type == "":
        var_type = "data"

    if var_len == "":
        var_len = 0
    else:
        var_len = int(var_len)

    assert var_type in types

    if var_type != "c" and var_type != "data":
        var_len = int(var_len / 8)

    return var_type, var_len


def retriever_to_bytes(retriever):
    var_type, var_len = datatype_to_type_length(retriever.datatype.var)

    return_bytes = b''

    is_list = type(retriever.data) == list
    if is_list:
        retriever.datatype.repeat = len(retriever.data)

    try:
        for i in range(0, retriever.datatype.repeat):
            data = retriever.data[i] if is_list else retriever.data

            if data is None:
                # No data is found in struct. Reasoning described below.
                return None

            if var_type == "struct":
                for struct_retriever in data.retrievers:
                    result = retriever_to_bytes(struct_retriever)
                    if result is None:
                        # Return default value. When non is committed.
                        # Should only happen when a value is not transferred from and to a struct.
                        # This is because structs are recreated on file generation. When the struct does not contain
                        # a certain value because it's use is unknown, the value isn't transferred between.
                        struct_retriever.data = retriever.datatype.var.defaults()[struct_retriever.name]
                        return_bytes += retriever_to_bytes(struct_retriever)
                        continue
                    return_bytes += result
            if var_type == "u" or var_type == "s":  # int
                return_bytes += int_to_bytes(data, var_len, signed=(var_type == "s"))
            elif var_type == "f":  # float
                if var_len == 4:
                    return_bytes += float_to_bytes(data)
                else:
                    return_bytes += double_to_bytes(data)
            elif var_type == "c":  # str
                return_bytes += fixed_chars_to_bytes(data)
            elif var_type == "data":  # bytes
                return_bytes += data
            elif var_type == "str":  # str
                byte_string = str_to_bytes(data)
                return_bytes += int_to_bytes(len(byte_string), var_len, endian="little", signed=True)
                return_bytes += byte_string
    except (AttributeError, TypeError) as e:
        data_text = repr(retriever.data)
        if type(retriever.data) == list and len(retriever.data) > 5:
            data_text = f"[{retriever.data[0].__class__.__name__}] * {len(retriever.data)}"

        print(f"\n{type(e).__name__} occurred in: {retriever.name} "
              f"\n\tData: {data_text}"
              f"\n\tDatatype: {str(retriever.datatype)}")
        raise e

    if retriever.log_value:
        print(retriever, "returned", return_bytes)

    return return_bytes
