from typing import Union


def add_str_trail(string) -> str:
    if len(string) > 0:
        string = string + ("\x00" if string[-1] != "\x00" else "")
    return string


def has_str_trail(string) -> bool:
    if len(string) > 0 and string[-1] == 0:
        return True
    return False


def del_str_trail(string) -> Union[str, bytes]:
    if has_str_trail(string):
        string = string[:-1]
    return string


def add_prefix_chars(string, char, length):
    if len(string) > length:
        return string
    else:
        return char * (length - len(string)) + string


def add_suffix_chars(string, char, total_length):
    if len(string) > total_length:
        return string
    else:
        return string + char * (total_length - len(string))


def q_str(value: any) -> str:
    if type(value) is str:
        return f"'{value}'"
    return str(value)


def add_tabs(string: str, tabs: int):
    return ("\n\r"+("\t" * tabs)).join(string.split("\r\n"))


def create_inline_line(entries):
    return "\t" + ", ".join(map(str, entries)) + "\r\n"


def create_textual_hex(string, space_distance=2, enter_distance=48):
    """Please note that the 'enter_distance' parameter is including the - to be added - spaces. If you calculated it
    without the spaces, please multiply the number by: `block size incl space / block size excl space`"""
    return insert_char(insert_char(string, " ", space_distance), "\n", enter_distance)


# Credits: gurney alex @ https://stackoverflow.com/a/2657733/7230293
def insert_char(string, char, step=64):
    return char.join(string[i:i + step] for i in range(0, len(string), step))