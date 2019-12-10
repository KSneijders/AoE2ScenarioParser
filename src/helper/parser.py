import ast

from src.helper.bytes_to_x import *
from src.helper.generator import repeat_generator as r_gen
import operator

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "//": operator.floordiv,
}

types = [
    "s",  # Signed int
    "u",  # Unsigned int
    "f",  # FloatingPoint
    "c",  # Character string
    "str",  # Variable length string
    "data",  # Data (Can be changed by used using bytes_to_x functions)
]


def _vorl(var):
    """vorl stands for "Variable or List". This function returns the value if the list is a size of 1"""
    if len(var) is 1 and type(var) is list:
        return var[0]
    else:
        return var


class Parser:
    _saves = dict()

    def retrieve_value(self, generator, retriever):
        if retriever.set_repeat is not None:
            retriever.datatype.repeat = self.parse_repeat_string(retriever.set_repeat)

        result = list()
        var_type, var_len = datatype_to_type_length(retriever.datatype.var)

        for i in range(0, retriever.datatype.repeat):
            if var_type == "u" or var_type == "s":
                val = bytes_to_int(r_gen(generator, var_len), signed=(var_type == "s"))
            elif var_type == "f":
                val = bytes_to_float(r_gen(generator, var_len))
            elif var_type == "c":
                val = bytes_to_str(r_gen(generator, var_len))
            elif var_type == "data":
                val = r_gen(generator, var_len)
            elif var_type == "str":
                string_length = bytes_to_int(r_gen(generator, var_len), endian="little", signed=True)
                val = bytes_to_str(r_gen(generator, string_length))
            else:
                break

            if retriever.save_as is not None:
                self.add_to_saves(retriever.save_as, val)
            result.append(val)

        if retriever.on_success is not None:
            if type(result) is list:
                for x in range(0, len(result)):
                    result[x] = retriever.on_success(result[x])
            else:
                result = retriever.on_success(result)

        return _vorl(result)

    def parse_repeat_string(self, repeat_string):
        while True:
            start = repeat_string.find("{")
            end = repeat_string.find("}")

            if start is -1 and end is -1:
                break

            inclusive = repeat_string[start:end + 1]
            exclusive = repeat_string[start + 1:end]
            repeat_string = repeat_string.replace(inclusive, str(self._saves[exclusive]))

        return eval(repeat_string)

    def add_to_saves(self, name, value):
        self._saves[name] = value


def calculate_length(generator, retriever_list):
    parser = Parser()
    length = 0

    for retriever in retriever_list:
        if retriever.set_repeat is not None:
            retriever.datatype.repeat = parser.parse_repeat_string(retriever.set_repeat)

        var_type, var_len = datatype_to_type_length(retriever.datatype.var)

        for i in range(0, retriever.datatype.repeat):
            length += var_len
            if var_type == "u" or var_type == "s":
                val = bytes_to_int(r_gen(generator, var_len), signed=(var_type == "s"))
            elif var_type == "f":
                val = bytes_to_float(r_gen(generator, var_len))
            elif var_type == "c":
                val = bytes_to_str(r_gen(generator, var_len))
            elif var_type == "data":
                val = r_gen(generator, var_len)
            elif var_type == "str":
                string_length = bytes_to_int(r_gen(generator, var_len), endian="little", signed=True)
                val = bytes_to_str(r_gen(generator, string_length))
                length += string_length
            else:
                break

            if retriever.save_as is not None:
                parser.add_to_saves(retriever.save_as, val)

    return length


def datatype_to_type_length(var):
    var_type = ""
    var_len = ""

    for char in var:
        if char.isnumeric():
            var_len += char
        else:
            var_type += char

    if var_type == "":
        var_type = "data"
    var_len = int(var_len)

    assert var_type in types

    if var_type != "c" and var_type != "data":
        var_len = int(var_len / 8)

    return var_type, var_len
