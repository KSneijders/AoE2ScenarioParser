from __future__ import annotations

from typing import Any, List


def add_str_trail(string: str | bytes) -> str | bytes:
    """
    Appends the null character b"\x00" to the end of the bytes if it is not already present

    Args:
        string: The string/bytes to append the null character to

    Returns:
        Bytes ending with a null character
    """
    if not has_str_trail(string):
        string += b"\x00"
    return string


def has_str_trail(string: str | bytes) -> bool:
    """
    Checks if the given bytes ends with the null character

    Args:
        string: The string/bytes to check the last character of

    Returns:
        `True` if the given bytes end with a null character else 0
    """
    return string.endswith(b"\x00")


def del_str_trail(string: str | bytes) -> str | bytes:
    """
    Removes the the null character from the end of a string/bytes

    Args:
        string: The string/bytes to remove the null character from

    Returns:
        string/bytes with the null character removed from the end
    """
    if has_str_trail(string):
        string = string[:-1]
    return string


def add_prefix_chars(string: str, char: str, length: int) -> str:
    """
    Adds the specified character at the front of a string so that the string is of a given length

    Args:
        string: The string to prepend the characters to
        char: The character to prepend
        length: The desired length of the final string

    Returns:
        A string with the required number of characters prepended to make it of the given length
    """
    if len(string) > length:
        return string
    else:
        return char * (length - len(string)) + string


def add_suffix_chars(string: str, char: str, total_length: int) -> str:
    """
    Adds the specified character at the end of a string so that the string is of a given length

    Args:
        string: The string to append the characters to
        char: The character to append
        total_length: The desired length of the final string

    Returns:
        A string with the required number of characters appended to make it of the given length
    """
    if len(string) > total_length:
        return string
    else:
        return string + char * (total_length - len(string))


def remove_prefix(string: str, prefix: str) -> str:
    """
    Cheap knockoff function of: https://docs.python.org/3/library/stdtypes.html?highlight=removesuffix#str.removeprefix

    Args:
        string: The string to check it's prefix
        prefix: The prefix to remove from the string

    Returns:
        The given string or the string without the prefix if it was present
    """
    return string[len(prefix):] if string.index(prefix) == 0 else string


def q_str(value: Any) -> str:
    """
    Converts the given value into a string. If the value is in string or byte form, quotes are added
    around the value. Bytes are also represented in hex.

    Args:
        value: The value to return the string representation of

    Returns:
        The string representation of the given value. Slightly modified if it's a string or bytes value.
    """
    if type(value) is str:
        return f"'{value}'"
    if type(value) is bytes:
        return f"b'{value.hex()}'"
    return str(value)


def trunc_string(string: str | bytes, length=30, add_ellipsis=True) -> str | bytes:
    """
    Truncates string to a certain length and possibly adds ellipsis to said string.

    Args:
        string: The string to truncate if its length is longer than the specified max (see length)
        length: The max given length the string can be
        add_ellipsis: If ellipsis should be added if the string is truncated

    Returns:
        The truncated string (with ellipsis) if it was longer than the given length
    """
    ellipsis_ = '...' if isinstance(string, str) else b'...'
    alt = '' if isinstance(string, str) else b''
    return (string[:length] + (ellipsis_ if add_ellipsis else alt)) if len(string) > length else string


def add_tabs(string: str, tabs: int) -> str:
    """
    Adds tabs to a string. Tabs are added in front of each line of the string

    Args:
        string: The string to add tabs to
        tabs: The amount of tabs to add before each line

    Returns:
        The tabbed string
    """
    split_string = string.splitlines(keepends=True)
    return ("\t" * tabs) + ("\t" * tabs).join(split_string) 


def create_inline_line(entries: List[Any]):
    """
    Creates inline string of elements from the given list, converts the elements to strings and appends them.
    The created string always starts with a tab and ends with a newline.

    Args:
        entries: The entries to convert to an inline, comma separated, string

    Returns:
        The created inline string
    """
    return "\t" + ", ".join(map(str, entries)) + "\r\n"


def create_textual_hex(string: str, space_distance: int = 2, enter_distance: int = 48):
    """
    Converts string to a textual hex format. Splitting the string with spaces and enters spaced appropriately.

    **Please note**: that the 'enter_distance' parameter is including the - to be added - spaces. If you calculated it
    without the spaces, please multiply the number by: `block size incl space / block size excl space`

    Args:
        string: The string to split up
        space_distance: The distance between spaces. Defaults to 2.
        enter_distance: The distance between enters (includes added spaces). Defaults to 48 (Every 32 string chars).

    Returns:
        The converted string with spaces and enters
    """
    return insert_char(insert_char(string, " ", space_distance), "\n", enter_distance)


def insert_char(string: str, char: str, step: int=64):
    """
    Inserts a character every x amount of letters into a string.

    Args:
        string: The string to add the letters into
        char: The character to add to the string
        step: The amount of characters in between each character insertion

    Returns:
        The created string with the new characters within it

    :Author:
        gurney alex @ https://stackoverflow.com/a/2657733/7230293
    """
    return char.join(string[i:i + step] for i in range(0, len(string), step))
