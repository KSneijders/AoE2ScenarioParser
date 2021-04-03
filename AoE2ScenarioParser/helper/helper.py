import math
from enum import IntEnum

from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.units import UnitInfo

""" =============================================================
============================ COORDS =============================
=============================================================="""


def xy_to_i(x, y, map_size):
    return x * map_size + y


def i_to_xy(i, map_size):
    return int(i / map_size), i % map_size


""" =============================================================
============================= OTHER =============================
=============================================================="""


def get_enum_from_unit_const(const: int) -> IntEnum:
    """
    Returns an Enum corresponding with the given Const.

    Arguments:
        const: The constant representing a unit
    """
    enums = [
        UnitInfo,
        BuildingInfo,
        HeroInfo,
        OtherInfo
    ]
    for enum in enums:
        try:
            return enum.from_id(const)
        except ValueError:
            continue


def get_int_len(num):
    if num > 0:
        return math.floor(math.log10(num))
    return 0


def evaluate_index_params(x_id, display_index, name):
    if x_id is None and display_index is None:
        raise ValueError(f"Please choose '{name}_id' or 'display_index' as identification for the wanted {name}")
    if x_id is not None and display_index is not None:
        raise ValueError(f"Please identify a {name} using '{name}_id' or 'display_index' but not both")
