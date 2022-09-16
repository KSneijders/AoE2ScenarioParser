from __future__ import annotations

import math
from enum import Enum
from typing import Tuple, Any

from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.support.info_dataset_base import InfoDatasetBase
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.helper import exceptions
from AoE2ScenarioParser.helper.printers import warn
from AoE2ScenarioParser.objects.support.tile import Tile

""" =============================================================
============================ COORDS =============================
=============================================================="""


def xy_to_i(x, y, map_size) -> int:
    if max(x, y) >= map_size or min(x, y) < 0:
        raise ValueError("X and Y need to be: 0 <= n < map_size")
    return x + y * map_size


def i_to_xy(i, map_size) -> Tile:
    if i < 0 or i >= pow(map_size, 2):
        raise ValueError(f"X and Y need to be: 0 <= n ({i}) < map_size ({map_size})")
    return Tile(int(i % map_size), int(i / map_size))


""" =============================================================
============================= OTHER =============================
=============================================================="""


def value_is_valid(value: Any) -> bool:
    """
    Check if value is valid by making sure it's not -1 nor None

    Returns:
        True if value is not None or -1. False if it is either of those.
    """
    return value not in [None, -1]


def values_are_valid(*args: Any) -> bool:
    """
    Check if value is valid by making sure it's not -1 nor None

    Returns:
        True if all values are not None or -1. False if any of them are either of those.
    """
    return any(map(lambda v: v not in [None, -1], args))


def get_enum_from_unit_const(const: int) -> InfoDatasetBase | None:
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


def validate_coords(x1: int, y1: int, x2: int = None, y2: int = None) -> Tuple[int, int, int, int]:
    """
    Validates given coordinates.

    - Swaps x/y1 with x/y2 if 1 is higher than it's 2 counterpart
    - Sets x/y2 to x/y1 if it's not been set.

    Args:
        x1: The X location of the left corner
        y1: The Y location of the left corner
        x2: The X location of the right corner
        y2: The Y location of the right corner

    Returns:
        The updated values through a tuple as (x1, y1, x2, y2)
    """
    if value_is_valid(x1) and not value_is_valid(x2):
        x2 = x1
    if value_is_valid(y1) and not value_is_valid(y2):
        y2 = y1
    if x1 > x2:
        x1, x2 = x2, x1
        warn("Swapping 'x1' and 'x2' values. Attribute 'x1' cannot be higher than 'x2'")
    if y1 > y2:
        y1, y2 = y2, y1
        warn("Swapping 'y1' and 'y2' values. Attribute 'y1' cannot be higher than 'y2'")
    return x1, y1, x2, y2


def typename(x: Any):
    """Get the name of the class of the given object"""
    return type(x).__name__
