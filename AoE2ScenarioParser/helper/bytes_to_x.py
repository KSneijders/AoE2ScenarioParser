import struct

from AoE2ScenarioParser.helper import helper


def bytes_to_fixed_chars(byte_elements, codec="utf-8"):
    return byte_elements.decode(codec)


def fixed_chars_to_bytes(string, codec="utf-8"):
    return string.encode(codec)


_no_string_trail = [
    "filename",  # Scenario filename
    "ascii_instructions",  # Messages
    "ascii_hints",  # Messages
    "ascii_victory",  # Messages
    "ascii_loss",  # Messages
    "ascii_history",  # Messages
    "ascii_scouts",  # Messages
    "ascii_pregame",  # Cinematics
    "ascii_victory",  # Cinematics
    "ascii_loss",  # Cinematics
    "ascii_filename",  # Cinematics
    "strings",  # in PlayerDataTwo
    "ai_names",  # in PlayerDataTwo
    "ai_per_file_text",  # in AIStruct
    "unknown_string",  # in Map
    "map_color_mood",  # in Map
    "script_name",  # in Map
]


def bytes_to_str(byte_elements, codec="utf-8"):
    trail_removed_elements = helper.del_str_trail(byte_elements)
    try:
        return trail_removed_elements.decode(codec)
    except UnicodeDecodeError:
        return trail_removed_elements.decode('latin-1')


def str_to_bytes(string, retriever, codec="utf-8"):
    if retriever.name in _no_string_trail:
        return string.encode(codec)
    return helper.add_str_trail(string).encode(codec)


def bytes_to_int(byte_elements, endian="little", signed=False):
    return int.from_bytes(byte_elements, endian, signed=signed)


def int_to_bytes(integer: int, length, endian="little", signed=True):
    return integer.to_bytes(length, byteorder=endian, signed=signed)


def bytes_to_float(byte_elements):
    return struct.unpack('f', byte_elements)[0]


def float_to_bytes(f):
    return struct.pack('f', f)


def bytes_to_double(byte_elements):
    return struct.unpack('d', byte_elements)[0]


def double_to_bytes(d):
    return struct.pack('d', d)


# Todo: Change retriever to datatype (rework string conversion)
def parse_val_to_bytes(retriever, val):
    var_type, var_len = retriever.datatype.type_and_length

    if var_type == "u" or var_type == "s":  # int
        return int_to_bytes(val, var_len, signed=(var_type == "s"))
    elif var_type == "str":  # str
        byte_string = str_to_bytes(val, retriever)
        return int_to_bytes(len(byte_string), var_len, endian="little", signed=True) + byte_string
    elif var_type == "c":  # str
        return fixed_chars_to_bytes(val)
    elif var_type == "data":  # bytes
        return val
    elif var_type == "f":  # float
        if var_len == 4:
            return float_to_bytes(val)
        else:
            return double_to_bytes(val)


def parse_bytes_to_val(datatype, byte_elements):
    var_type, var_len = datatype.type_and_length

    if var_type == "u" or var_type == "s":
        return bytes_to_int(byte_elements, signed=(var_type == "s"))
    elif var_type == "str":
        return bytes_to_str(byte_elements[var_len:])
    elif var_type == "c":
        return bytes_to_fixed_chars(byte_elements)
    elif var_type == "data":
        return byte_elements
    elif var_type == "f":
        if var_len == 4:  # Float value
            return bytes_to_float(byte_elements)
        else:  # only 'else' is the trigger version. Which is a double (8 bytes)
            return bytes_to_double(byte_elements)
    else:
        raise ValueError(f"Unable to parse bytes with unknown type: ({var_type})")
