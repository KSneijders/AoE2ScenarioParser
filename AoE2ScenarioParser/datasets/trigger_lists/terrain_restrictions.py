from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class TerrainRestrictions(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the terrain restriction IDs in the game. Used in the
    'Modify Attribute' effects

    **Examples**

    >>> TerrainRestrictions.LAND_AND_SHALLOWS
    <TerrainRestrictions.LAND_AND_SHALLOWS: 1>
    """
    ALL = 0
    """Used by terrain eyecandy and sundries"""
    LAND_AND_SHALLOWS = 1
    """Used by part of animals"""
    BEACH = 2
    WATER_SMALL_TRAIL = 3
    """Used by most ships and sea gate"""
    LAND = 4
    """Used by most land buildings"""
    NOTHING = 5
    WATER_NO_TRAIL = 6
    """Used by docks"""
    ALL_EXCEPT_WATER = 7
    """Used by land troops"""
    LAND_EXCEPT_FARM = 8
    """Used by land resources"""
    NOTHING_2 = 9
    LAND_AND_BEACH = 10
    """Used by land walls and gates"""
    LAND_EXCEPT_FARM_2 = 11
    """Used by trees and mountains"""
    ALL_EXCEPT_WATER_BRIDGE_CANNON = 12
    WATER_MEDIUM_TRAIL = 13
    """Used by big fish and fishing ship"""
    ALL_EXCEPT_WATER_BRIDGE_ARROW = 14
    WATER_LARGE_TRAIL = 15
    """Only used by transport ship"""
    GRASS_AND_BEACH = 16
    WATER_AND_BRIDGE_EXCEPT_BEACH = 17
    ALL_EXCEPT_WATER_BRIDGE_SPEAR = 18
    ONLY_WATER_AND_ICE = 19
    """Used by fish"""
    ALL_EXCEPT_WATER_WHEEL = 20
    """Used by units with wheels, such as Rams and Scorpions"""
    SHALLOW_WATER = 21
    ALL_DART = 22
    ALL_ARROW_FIRE = 23
    """Only used by Arrows with fire (After chemistry)"""
    ALL_CANNON_FIRE = 24
    """Only used by Cannon balls (After chemistry)"""
    ALL_SPEAR_FIRE = 25
    """Only used by Spears with fire (After chemistry)"""
    ALL_DART_FIRE = 26
    """Only used by Darts with fire (After chemistry)"""
    ALL_LASER = 27
    """Only used by Projectile Laser with id 1595"""
    ALL_EXCEPT_WATER_CAVALRY = 28
    """Such as Cavalry Archer, Cavalry, Conquistador, Missionary and Flaming Camel"""
    ALL_EXCEPT_WATER_PACKET_TREBUCHET = 29
    """All types of Trebuchet(Packed)"""
    WATER_SMALLEST_TRAIL = 30
    """Used by medium ships, such as Trade Cog, Fire Galley and Longboat"""
