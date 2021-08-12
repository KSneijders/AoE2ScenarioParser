import struct

from AoE2ScenarioParser.helper.string_manipulations import has_str_trail, del_str_trail, add_str_trail


def bytes_to_fixed_chars(byte_elements, codec="utf-8"):
    return byte_elements.decode(codec)


def fixed_chars_to_bytes(string, codec="utf-8"):
    # Todo: Add space chars to fix length
    return string.encode(codec)


# Update tests if this changes
# Tests *should* fail - but just to be sure
_no_string_trail = [
    "filename",                 # Scenario filename
    "ascii_instructions",       # Messages
    "ascii_hints",              # Messages
    "ascii_victory",            # Messages
    "ascii_loss",               # Messages
    "ascii_history",            # Messages
    "ascii_scouts",             # Messages
    "ascii_pregame",            # Cinematics
    "ascii_victory",            # Cinematics
    "ascii_loss",               # Cinematics
    "ascii_filename",           # Cinematics
    "strings",                  # in PlayerDataTwo
    "ai_names",                 # in PlayerDataTwo
    "ai_per_file_text",         # in AIStruct
    "unknown_string",           # in Map
    "map_color_mood",           # in Map
    "script_name",              # in Map
    "water_definition",         # in Map
    "message",                  # in Trigger  [ADDED SO THEY'RE IGNORED - HANDLED IN EFFECT COMMIT CALLBACK]
    "sound_name",               # in Trigger  [ADDED SO THEY'RE IGNORED - HANDLED IN EFFECT COMMIT CALLBACK]
    "script_file_path",         # in Files
    "script_file_content",      # in Files
]


def bytes_to_str(byte_elements, codec="utf-8"):  # Removed param: retriever
    if has_str_trail(byte_elements):
        byte_elements = del_str_trail(byte_elements)
        # retriever.string_end_char = True
    try:
        return byte_elements.decode(codec)
    except UnicodeDecodeError:
        return byte_elements.decode('latin-1')


def str_to_bytes(string, retriever, codec="utf-8"):
    # if retriever.string_end_char:
    if retriever.name not in _no_string_trail:
        return add_str_trail(string).encode(codec)
    return string.encode(codec)


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


# var_type_to_func = {
#     'u': lambda val, vlen: int_to_bytes(val, vlen, signed=False),
#     's': lambda val, vlen: int_to_bytes(val, vlen, signed=True),
#     'c': lambda val, vlen: fixed_chars_to_bytes(val),
#     'data': lambda val, vlen: val,
#     'f': lambda val, vlen:  float_to_bytes(val) if vlen == 4 else double_to_bytes(val)
# }


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
        # Todo: Add space chars to fix length
        return val
    elif var_type == "f":  # float
        if var_len == 4:
            return float_to_bytes(val)
        else:
            return double_to_bytes(val)
    else:
        raise ValueError(f"Unable to parse value to bytes with unknown type: ({var_type})")


def parse_bytes_to_val(retriever, byte_elements):
    var_type, var_len = retriever.datatype.type_and_length

    if var_type == "u" or var_type == "s":
        return bytes_to_int(byte_elements, signed=(var_type == "s"))
    elif var_type == "str":
        return bytes_to_str(byte_elements[var_len:])  # Note: Removed param 'retriever'
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
