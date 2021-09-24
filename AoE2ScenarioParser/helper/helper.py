import math
from enum import Enum
from typing import Union, Tuple

from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.support.info_dataset_base import InfoDatasetBase
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.helper import exceptions

""" =============================================================
============================ COORDS =============================
=============================================================="""


def xy_to_i(x, y, map_size) -> int:
    if max(x, y) >= map_size or min(x, y) < 0:
        raise ValueError("X and Y need to be: 0 <= n < map_size")
    return x + y * map_size


def i_to_xy(i, map_size) -> Tuple[int, int]:
    if i < 0 or i >= pow(map_size, 2):
        raise ValueError(f"X and Y need to be: 0 <= n ({i}) < map_size ({map_size})")
    return int(i % map_size), int(i / map_size)


""" =============================================================
============================= OTHER =============================
=============================================================="""


def get_enum_from_unit_const(const: int) -> Union[InfoDatasetBase, None]:
    """
    Returns an Enum corresponding with the given Const.

    Arguments:
        const: The constant representing a unit
    """
    enums = [UnitInfo, BuildingInfo, HeroInfo, OtherInfo]
    for enum in enums:
        try:
            return enum.from_id(const)
        except (ValueError, KeyError):
            continue
    return None


def get_int_len(num):
    if num > 0:
        return math.floor(math.log10(num))
    return 0


def exclusive_if(*args):
    """Returns True if exactly one entry is true. False otherwise"""
    return sum(map(bool, args)) == 1


def raise_if_not_int_subclass(values):
    for v in values:
        if not issubclass(v.__class__, int):
            raise TypeError(exceptions.type_error_message(v, issubclass(v.__class__, Enum)))
