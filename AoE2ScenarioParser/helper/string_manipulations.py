from typing import Union, Any, List


def add_str_trail(string: bytes) -> bytes:
    """
    This funtion appends the null character b"\x00" to the end of the bytes if it is not already present

    Args:
        string (bytes): The bytes to append the null character to

    Returns:
        Bytes ending with a null character
    """
    if len(string) > 0:
        string += (b"\x00" if string[-1] != 0 else "")
    else:
        return b"\x00"
    return string


def has_str_trail(string: bytes) -> bool:
    """
    This function checks if the given bytes ends with the null character

    Args:
        string (bytes): The bytes to check the last character for

    Returns:
        True if the given bytes end with a null character else 0
    """
    return len(string) > 0 and string[-1] == 0


def del_str_trail(string: Union[str, bytes]) -> Union[str, bytes]:
    """
    This function removes the the null character from the end of a string/bytes

    Args:
        string (Union[str, bytes]): The string/bytes to remove the null character from

    Returns:
        string/bytes with the null character removed from the end
    """
    if has_str_trail(string):
        string = string[:-1]
    return string


def add_prefix_chars(string: str, char: str, length: int) -> str:
    """
    This function adds the specified character at the front of a string so that the string is of a given length

    Args:
        string (str): The string to prepend the characters to
        char (str): The character to prepend
        length (int): The desired length of the final string

    Returns:
        A string with the required number of characters prepended to make it of the given length
    """
    if len(string) > length:
        return string
    else:
        return char * (length - len(string)) + string


def add_suffix_chars(string: str, char: str, total_length: int) -> str:
    """
    This function adds the specified character at the end of a string so that the string is of a given length

    Args:
        string (str): The string to append the characters to
        char (str): The character to append
        total_length (int): The desired length of the final string

    Returns:
        A string with the required number of characters appended to make it of the given length
    """
    if len(string) > total_length:
        return string
    else:
        return string + char * (total_length - len(string))


def remove_prefix(string: str, prefix: str) -> str:
    """
    Cheap knockoff function of:
        https://docs.python.org/3/library/stdtypes.html?highlight=removesuffix#str.removeprefix

    Args:
        string (str): The string to check it's prefix
        prefix (str): The prefix to remove from the string

    Returns:
        The given string or the string without the prefix if it was present
    """
    return string[len(prefix):] if string.index(prefix) == 0 else string


def q_str(value: Any) -> str:
    """
    This function converts the given value into a string. If the value is in byte form, it is represented in hex

    Args:
        value: The value to return the string for

    Returns:

    """
    if type(value) is str:
        return f"'{value}'"
    if type(value) is bytes:
        return f"b'{value.hex()}'"
    return str(value)


def trunc_string(string: str, length=30, add_ellipsis=True):
    return (string[:length] + ('...' if add_ellipsis else '')) if len(string) > length else string


def trunc_bytes(string: bytes, length=30, add_ellipsis=True):
    return (string[:length] + (b'...' if add_ellipsis else b'')) if len(string) > length else string


def add_tabs(string: str, tabs: int) -> str:
    splitted_string = string.splitlines(keepends=True)
    return ("\t" * tabs) + ("\t" * tabs).join(splitted_string)


def create_inline_line(entries: List[Any]):
    return "\t" + ", ".join(map(str, entries)) + "\r\n"


def create_textual_hex(string: str, space_distance: int = 2, enter_distance: int = 48):
    """Please note that the 'enter_distance' parameter is including the - to be added - spaces. If you calculated it
    without the spaces, please multiply the number by: `block size incl space / block size excl space`"""
    return insert_char(insert_char(string, " ", space_distance), "\n", enter_distance)


# Credits: gurney alex @ https://stackoverflow.com/a/2657733/7230293
def insert_char(string: str, char: str, step=64):
    return char.join(string[i:i + step] for i in range(0, len(string), step))
