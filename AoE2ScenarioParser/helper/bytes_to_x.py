import struct

from AoE2ScenarioParser.helper import helper


def bytes_to_fixed_chars(byte_elements, codec="utf-8"):
    return byte_elements.decode(codec)


def fixed_chars_to_bytes(string, codec="utf-8"):
    return string.encode(codec)


_non_trail_names = [
    "filename",
    "ascii_instructions",
    "ascii_hints",
    "ascii_victory",
    "ascii_loss",
    "ascii_history",
    "ascii_scouts",
    "ascii_pregame",
    "ascii_victory",
    "ascii_loss",
    "ascii_filename",
    "strings",
    "ai_names",
    "ai_per_file_text",
    "map_color_mood",
    "unknown_string",
    "script_name",
    "creator_name",
    "constant_name",
    "name_or_func"
]


def bytes_to_str(byte_elements, retriever, codec="utf-8"):
    if retriever.name in _non_trail_names:
        return byte_elements.decode(codec)
    return helper.del_str_trail(byte_elements).decode(codec)


def str_to_bytes(string, retriever, codec="utf-8"):
    if retriever.name in _non_trail_names:
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
