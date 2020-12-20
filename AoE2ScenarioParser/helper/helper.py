import math
import sys
from enum import IntEnum
from typing import List, Dict

from AoE2ScenarioParser.datasets.buildings import Building, GaiaBuilding
from AoE2ScenarioParser.datasets.heroes import Hero
from AoE2ScenarioParser.datasets.units import Unit, GaiaUnit

""" =============================================================
========================= HEX FUNCTIONS =========================
=============================================================="""


def create_textual_hex(string, space_distance=2, enter_distance=48):
    """Please note that the 'enter_distance' parameter is including the - to be added - spaces. If you calculated it
    without the spaces, please multiply the number by: `block size incl space / block size excl space`"""
    return insert_char(insert_char(string, " ", space_distance), "\n", enter_distance)


# Credits: gurney alex @ https://stackoverflow.com/a/2657733/7230293
def insert_char(string, char, step=64):
    return char.join(string[i:i + step] for i in range(0, len(string), step))


""" =============================================================
======================= STRING MODIFIERS ========================
=============================================================="""


def add_str_trail(string):
    if len(string) > 0:
        string = string + ("\x00" if string[-1] != "\x00" else "")
    return string


def del_str_trail(string):
    if len(string) > 0:
        string = string if string[-1] != "\x00" and string[-1] != 0 else string[:-1]
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


""" =============================================================
======================== PRETTY PRINTERS ========================
=============================================================="""

_default_inline_types = {
    'int': 8,
    'float': 8
}


def pretty_print_list(plist: List, inline_types: Dict[str, int] = None):
    if len(plist) == 0:
        return "[]\r\n"
    if inline_types is None:
        inline_types = _default_inline_types
    entry_type = type(plist[0]).__name__  # Get entry type

    return_string = "[\r\n"
    line_items = []
    for index, entry in enumerate(plist):
        if entry_type in inline_types.keys():
            line_items.append(entry)
            if index % inline_types[entry_type] == inline_types[entry_type] - 1:
                return_string += _create_inline_line(line_items)
                line_items = []
            continue
        else:
            return_string += f"\t{entry}\r\n"
    if len(line_items) != 0:
        return_string += _create_inline_line(line_items)
    return return_string + "]\r\n"


def _create_inline_line(entries):
    return "\t" + ", ".join(map(str, entries)) + "\r\n"


def pretty_print_dict(pdict: dict):
    return_string = "{\n"
    for key, value in pdict.items():
        newline = f"\t{key}: {value}"
        if newline[::-2] != "\n":
            newline += "\n"
        return_string += newline
    return return_string + "}\n"


def pretty_print_name(name: str) -> str:
    """
    Returns a pretty-printed version of the name string.
    Replaces all underscores with spaces and capitalizes the first letter
    of each word.
    For example, elite_chu_ko_nu -> Elite Chu Ko Nu.

    :Author:
        T-West (https://github.com/twestura/)
    """
    return ' '.join(s[0].upper() + s[1:] for s in name.split('_'))


""" =============================================================
============================ COORDS =============================
=============================================================="""


def xy_to_i(x, y, map_size):
    return x * map_size + y


def i_to_xy(i, map_size):
    return int(i / map_size), i % map_size


""" =============================================================
============================= HASH ==============================
=============================================================="""


def hash_list(lst: list):
    return hash(tuple(lst))


def list_changed(lst, lst_hash):
    return lst_hash != hash(tuple(lst))


""" =============================================================
============================= OTHER =============================
=============================================================="""


def update_order_array(order_array, supposed_length):
    for i in range(0, supposed_length):
        if i not in order_array:
            order_array.append(i)


def get_enum_from_unit_const(const: int) -> IntEnum:
    """
    Returns an Enum corresponding with the given Const.

    Arguments:
        const: The constant representing a unit
    """
    # Todo: try catch in loop with `return x(const)` in main body. loop through enums
    if any(item == const for item in Unit):
        return Unit(const)
    if any(item.value == const for item in Building):
        return Building(const)
    if any(item.value == const for item in Hero):
        return Hero(const)
    if any(item == const for item in GaiaUnit):
        return GaiaUnit(const)
    if any(item == const for item in GaiaBuilding):
        return GaiaBuilding(const)


def get_int_len(num):
    if num > 0:
        return math.floor(math.log10(num))
    return 0


def evaluate_index_params(x_id, display_index, name):
    if x_id is None and display_index is None:
        raise ValueError(f"Please choose '{name}_id' or 'display_index' as identification for the wanted {name}")
    if x_id is not None and display_index is not None:
        raise ValueError(f"Please identify a {name} using '{name}_id' or 'display_index' but not both")


class SimpleLogger:
    def __init__(self, should_log):
        self.should_log = should_log

    def print(self, string="", end="\n", replace_line=False, last_replace_line=False):
        if self.should_log:
            if not replace_line:
                print(string, end=end)
            else:
                sys.stdout.write('\r' + string)
                if last_replace_line:
                    print()

    def __repr__(self):
        return f"SimpleLogger[should_log: {self.should_log}]"


class Tile:
    def __init__(self, x: int, y: int):
        self.x: float = x
        self.y: float = y

    def __repr__(self):
        return f"Tile[x: {self.x}, y: {self.y}]"

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, val: int):
        self._x = int(val) + .5

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, val: int):
        self._y = int(val) + .5

    @property
    def x1(self) -> int:
        return int(self.x - .5)

    @property
    def y1(self) -> int:
        return int(self.y - .5)

    @property
    def x2(self) -> int:
        return int(self.x + .5)

    @property
    def y2(self) -> int:
        return int(self.y + .5)
