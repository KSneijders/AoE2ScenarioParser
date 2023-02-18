from __future__ import annotations

import math
from enum import Enum
from typing import Any

from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.support.info_dataset_base import InfoDatasetBase
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.exceptions.asp_exceptions import type_error_message

""" =============================================================
============================= OTHER =============================
=============================================================="""


def value_is_valid(value: Any) -> bool:
    """
    Check if value is valid by making sure it's neither -1 nor None

    Args:
        value:

    Returns:
        `True` if value is not None or -1. `False` if it is either of those.
    """
    return value not in [None, -1]


def values_are_valid(*args: Any) -> bool:
    """
    Check if value is valid by making sure it's not -1 nor None

    Returns:
        `True` if all values are not None or -1. `False` if any of them are either of those.
    """
    return any(map(lambda v: v not in [None, -1], args))


def get_enum_from_unit_const(const: int) -> InfoDatasetBase | None:
    """
    Get the enum value for the given unit constant

    Args:
        const: The unit ID

    Returns:
        The enum value for the given unit constant
    """
    enums = [UnitInfo, BuildingInfo, HeroInfo, OtherInfo]
    for enum in enums:
        try:
            return enum.from_id(const)
        except (ValueError, KeyError):
            continue
    return None


def get_int_len(num: int) -> int:
    """
    Get the length (in digits) of the given number

    Args:
        num: The number to find the length

    Returns:
        The length of the given number
    """
    if num > 0:
        return math.floor(math.log10(num))
    return 0


def mutually_exclusive(*args) -> bool:
    """
    `True` only if one of the entries is true, `False` otherwise.

    Args:
        *args: values that can be converted to booleans

    Returns:
        True/False
    """
    return sum(map(bool, args)) == 1


def raise_if_not_int_subclass(values: dict):
    for k, v in values.items():
        if not issubclass(v.__class__, int):
            raise TypeError(type_error_message(v, k, issubclass(v.__class__, Enum)))


def typename(x: Any):
    """Get the name of the class of the given object"""
    return type(x).__name__


def bound(value: int | float, bounds: tuple[int | float, int | float]) -> int | float:
    """
    If a given value is within a specified range (i.e., between the given bounds), return that value.
    If the given value is outside the specified range (i.e., it overflows one of the bounds), return the value of the
    bound that it overflowed.

    Args:
        value: The value to check
        bounds: The bounds to check the value against

    Returns:
        The given value if within the bounds, otherwise the corresponding bound value
    """
    low, high = bounds
    return max(low, min(high, value))
