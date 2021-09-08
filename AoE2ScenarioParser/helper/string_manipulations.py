from typing import Union, Any, List


def add_str_trail(string: bytes) -> bytes:
    if len(string) > 0:
        string += (b"\x00" if string[-1] != 0 else "")
    else:
        return b"\x00"
    return string


def has_str_trail(string: bytes) -> bool:
    return len(string) > 0 and string[-1] == 0


def del_str_trail(string: Union[str, bytes]) -> Union[str, bytes]:
    if has_str_trail(string):
        string = string[:-1]
    return string


def add_prefix_chars(string: str, char: str, length: int):
    if len(string) > length:
        return string
    else:
        return char * (length - len(string)) + string


def add_suffix_chars(string: str, char: str, total_length: int):
    if len(string) > total_length:
        return string
    else:
        return string + char * (total_length - len(string))


def q_str(value: any) -> str:
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
