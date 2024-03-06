from __future__ import annotations

import struct
from typing import TYPE_CHECKING

from AoE2ScenarioParser import settings
from AoE2ScenarioParser.exceptions.asp_warnings import ByteDecodeWarning
from AoE2ScenarioParser.helper.printers import warn
from AoE2ScenarioParser.helper.string_manipulations import has_str_trail, del_str_trail, q_str, \
    add_str_trail, trunc_string

if TYPE_CHECKING:
    from AoE2ScenarioParser.sections.retrievers.retriever import Retriever


def bytes_to_fixed_chars(byte_elements: bytes) -> str:
    """
    Converts the given bytes to characters using the specified codec

    Args:
        byte_elements: The bytes to convert

    Returns:
        A string of decoded characters
    """
    end_of_string = byte_elements.find(b"\x00")
    if end_of_string != -1:
        byte_elements = byte_elements[:end_of_string]
    return bytes_to_str(byte_elements)


def fixed_chars_to_bytes(string: str, var_len: int) -> bytes:
    """
    Converts the given string to bytes using the specified codec

    Args:
        string: The string to convert
        var_len: The length of the string. If shorter, appended with `b'\x00'` to fill up to length.

    Returns:
        bytes of the encoded string
    """
    bytes_ = str_to_bytes(string)
    return bytes_ + b"\x00" * (var_len - len(bytes_))


# @formatter:off
# Update tests if this changes
# Tests *should* fail - but just to be sure
_no_string_trail = [
    "filename",             # Scenario filename
    "ascii_instructions",   # Messages
    "ascii_hints",          # Messages
    "ascii_victory",        # Messages
    "ascii_loss",           # Messages
    "ascii_history",        # Messages
    "ascii_scouts",         # Messages
    "ascii_pregame",        # Cinematics
    "ascii_victory",        # Cinematics
    "ascii_loss",           # Cinematics
    "ascii_filename",       # Cinematics
    "strings",              # in PlayerDataTwo
    "ai_names",             # in PlayerDataTwo
    "ai_per_file_text",     # in AIStruct
    "unknown_string",       # in Map
    "map_color_mood",       # in Map
    "script_name",          # in Map
    "water_definition",     # in Map
    "message",              # in Trigger  [ADDED SO THEY'RE IGNORED - HANDLED IN EFFECT COMMIT CALLBACK]
    "sound_name",           # in Trigger  [ADDED SO THEY'RE IGNORED - HANDLED IN EFFECT COMMIT CALLBACK]
    "script_file_path",     # in Files
    "script_file_content",  # in Files
]
# @formatter:on


def bytes_to_str(
        byte_elements: bytes,
        charset: str = settings.MAIN_CHARSET,
        fallback_charset: str = settings.FALLBACK_CHARSET
) -> str | bytes:
    """
    Converts bytes to string based on given charset.

    Args:
        byte_elements: Bytes to be decoded to string.
        charset: Main charset used to decode the bytes. Defaults to settings.MAIN_CHARSET.
        fallback_charset: Fallback charset used to decode the bytes when the main fails.
            Defaults to settings.FALLBACK_CHARSET.

    Returns:
        The decoded string or the byte elements when the string cannot be decoded
    """
    trailless_elements = del_str_trail(byte_elements) if has_str_trail(byte_elements) else byte_elements

    for c in [charset, fallback_charset]:
        try:
            return trailless_elements.decode(c)
        except ValueError:
            continue

    # Return the string as bytes when it cannot be decoded. This will leave it as-is.
    truncated = trunc_string(byte_elements, 25)
    warn(f"Unable to decode bytes using '{charset}' and '{fallback_charset}', bytes: \n\t{truncated}",
         category=ByteDecodeWarning)
    return byte_elements


def str_to_bytes(
        string: str | bytes,
        charset: str = settings.MAIN_CHARSET,
        fallback_charset: str = settings.FALLBACK_CHARSET
) -> bytes:
    """
    Converts string to bytes based on given charsets

    Args:
        string: The string to convert
        charset: The main charset used while encoding
        fallback_charset: The fallback charset when the main fails

    Returns:
        The bytes converted from the given string

    Raises:
        ValueError: When the string cannot be encoded with either of the charsets
    """
    for c in [charset, fallback_charset]:
        try:
            return string.encode(c)
        except ValueError:
            continue
        except AttributeError as e:
            if type(string) is bytes:
                return string
            raise e
    raise ValueError(f"Unable to encode string using '{charset}' and '{fallback_charset}'. String:\n\t{q_str(string)}")


def bytes_to_int(byte_elements: bytes, endian: str = "little", signed: bool = True) -> int:
    """
    Converts the given bytes to an integer

    Args:
        byte_elements: The bytes to convert
        endian: If the conversion should be done with "little" or "big" endian. Defaults to "little"
        signed: If the int should be a signed int or not. Defaults to False

    Returns:
        The integer converted from the given bytes
    """
    return int.from_bytes(byte_elements, endian, signed=signed)


def int_to_bytes(integer: int, length: int, endian: str = "little", signed: bool = True) -> bytes:
    """
    Converts the given integer to bytes

    Args:
        integer: The integer to convert
        length: The number of bytes used to represent the integer
        endian: If the conversion should be done with "little" or "big" endian. Defaults to "little"
        signed: If the int is a signed int or not. Defaults to True

    Returns:
        The bytes converted from the given integer
    """
    return integer.to_bytes(length, byteorder=endian, signed=signed)


def bytes_to_float(byte_elements: bytes) -> float:
    """
    Converts the given bytes to a floating point value

    Args:
        byte_elements: The bytes to convert

    Returns:
        The floating point converted from the given bytes
    """
    return struct.unpack('f', byte_elements)[0]


def float_to_bytes(f: float) -> bytes:
    """
    Converts the given floating point value to bytes

    Args:
        f: The float to convert

    Returns:
        The bytes converted from the given float
    """
    return struct.pack('f', f)


def bytes_to_double(byte_elements: bytes) -> float:
    """
    Converts the given bytes to a double value

    Args:
        byte_elements: The bytes to convert

    Returns:
        The double value converted from the given bytes
    """
    return struct.unpack('d', byte_elements)[0]


def double_to_bytes(d: float) -> bytes:
    """
    Converts the given double value to bytes

    Args:
        d: The number to convert

    Returns:
        The bytes converted from the given double value
    """
    return struct.pack('d', d)


def parse_val_to_bytes(retriever: 'Retriever', val: int | float | str | bytes) -> bytes:
    """
    Encodes the given value to bytes according to the datatype of the retriever

    Args:
        retriever: The retriever to encode the bytes for
        val: The value to encode

    Returns:
        The encoded value as bytes

    Raises:
        ValueError: When the datatype of the retriever is not recognised or when the char string is longer than allowed.
    """
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
        if len(val) > var_len:
            raise ValueError(f"Value cannot be longer than {var_len}, retriever: {retriever}")
        return fixed_chars_to_bytes(val, var_len)
    elif var_type == "data":  # bytes
        return val
    elif var_type == "f":  # float
        if var_len == 4:
            return float_to_bytes(val)
        else:
            return double_to_bytes(val)
    else:
        raise ValueError(f"Unable to parse value to bytes with unknown type: ({var_type})")


def parse_bytes_to_val(retriever: 'Retriever', byte_elements: bytes) -> int | float | str | bytes:
    """
    Decodes the bytes given according to the datatype of the retriever

    Args:
        retriever: The retriever to decode the bytes for
        byte_elements: The bytes to decode

    Returns:
        The interpreted value of the bytes

    Raises:
        ValueError: When the datatype of the retriever is not recognised
    """
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


def _combine_int_str(
        byte_string: bytes,
        length: int,
        endian: str,
        signed: bool,
        retriever: 'Retriever' = None
) -> bytes:
    """
    Appends the length of the given bytes (this length is in byte form itself) to the front of the bytes.
    This is done because strings are stored as an integer (as bytes) that is the length of the string followed by the
    same number of bytes representing that string

    Args:
        byte_string: The byte representation of a string
        length: The length of bytes to store the length in
        endian: This is the format used to encode the length to bytes
        signed: Determines if the length is a signed or unsigned integer
        retriever: The retriever to encode the bytes for

    Returns:
        the bytes of the length + the bytes of the string

    Raises:
        OverflowError: if the number of bytes needed to store the length is higher than the allowed value for scenarios
    """
    try:
        return int_to_bytes(len(byte_string), length, endian=endian, signed=signed) + byte_string
    except OverflowError as e:
        if str(e) == "int too big to convert":
            name: str = retriever.name if retriever else ""
            raise OverflowError(
                f"'{name.capitalize()}' is too long. "
                f"Length must be below {pow(2, length * 8 - 1)}, but is: {len(byte_string)}"
            ) from None
