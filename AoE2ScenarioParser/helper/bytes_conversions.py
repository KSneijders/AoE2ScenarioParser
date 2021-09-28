import struct
from typing import Union, TYPE_CHECKING

from AoE2ScenarioParser import settings
from AoE2ScenarioParser.helper.printers import warn
from AoE2ScenarioParser.helper.string_manipulations import has_str_trail, del_str_trail, q_str, \
    trunc_bytes, add_str_trail


if TYPE_CHECKING:
    from AoE2ScenarioParser.sections.retrievers.retriever import Retriever


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


def bytes_to_str(byte_elements, charset=settings.MAIN_CHARSET, fallback_charset=settings.FALLBACK_CHARSET) \
        -> Union[str, bytes]:
    """
    Converts bytes to string based on given charset.

    Args:
        byte_elements (bytes): Bytes to be decoded to string.
        charset (str): Main charset used to decode the bytes. Defaults settings.MAIN_CHARSET.
        fallback_charset (str): Fallback charset used to decode the bytes when the main fails. Defaults settings.FALLBACK_CHARSET.

    Returns:
        The decoded string or the byte elements when the string cannot be decoded
    """
    trailless_elements = del_str_trail(byte_elements) if has_str_trail(byte_elements) else byte_elements

    for c in [charset, fallback_charset]:
        try:
            return trailless_elements.decode(c)
        except ValueError:
            continue

    # Return the string as bytes when it cannot be decoded.
    # This will leave the string as-is.
    warn(f"Unable to decode bytes using '{charset}' and '{fallback_charset}', bytes: \n\t{trunc_bytes(byte_elements, 25)}")
    return byte_elements


def str_to_bytes(
        string: str,
        charset=settings.MAIN_CHARSET,
        fallback_charset=settings.FALLBACK_CHARSET
):
    """
    Converts string to bytes based on given charsets

    Args:
        string: The string to convert
        charset: The main charset used while encoding
        fallback_charset: The fallback charset when the main fails

    Returns:
        The converted string

    Raises:
        ValueError: When the string cannot be decoded with either of the charsets
    """
    for c in [charset, fallback_charset]:
        try:
            return string.encode(c)
        except ValueError:
            continue
    raise ValueError(f"Unable to encode string using '{charset}' and '{fallback_charset}'. String:\n\t{q_str(string)}")


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


def parse_val_to_bytes(retriever: 'Retriever', val):
    var_type, var_len = retriever.datatype.type_and_length

    if var_type == "u" or var_type == "s":  # int
        return int_to_bytes(val, var_len, signed=(var_type == "s"))
    elif var_type == "str":  # str
        try:
            byte_string = str_to_bytes(val)
        except AttributeError as e:
            if type(val) is bytes:
                byte_string = val
            else:
                raise e from None

        if retriever.name not in _no_string_trail:
            byte_string = add_str_trail(byte_string)

        return _combine_int_str(byte_string, var_len, endian="little", signed=True, retriever=retriever)
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


def _combine_int_str(byte_string, length, endian, signed, retriever: 'Retriever' = None) -> bytes:
    try:
        return int_to_bytes(len(byte_string), length, endian=endian, signed=signed) + byte_string
    except OverflowError as e:
        if str(e) == "int too big to convert":
            name: str = retriever.name if retriever else ""
            raise OverflowError(
                f"{name.capitalize()} is too long. Length must be below {pow(2, length*8-1)}, but is: {len(byte_string)}"
            ) from None
