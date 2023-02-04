from __future__ import annotations

from typing import Union, Tuple, TypeVar
from AoE2ScenarioParser.objects.support.area import Area

TileT = Tuple[int, int]
AreaT = Union[Area, Tuple[TileT, TileT], Tuple[TileT]]

Scenario: TypeVar = TypeVar('Scenario', bound='AoE2Scenario')
"""A type variable (generic) that represents an instance of the AoE2Scenario class or any of its subclasses"""
