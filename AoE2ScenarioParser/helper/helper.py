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


def exclusive_if(*args):
    """Returns True if exactly one entry is true. False otherwise"""
    return sum(map(bool, args)) == 1
