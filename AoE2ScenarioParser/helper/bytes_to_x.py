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
    "strings",  # in PlayerDataTwoPiece
    "ai_names",  # in PlayerDataTwoPiece
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
