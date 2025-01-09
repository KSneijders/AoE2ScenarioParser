from __future__ import annotations

from enum import IntEnum
from typing import List


class TerrainId(IntEnum):
    """
    This enum class provides information about most of the terrains in the game. Information about the
    following properties of a terrain is found in this class:

     - Terrain ID

    **Methods**

    >>> TerrainId.beach_terrains()
    >>> TerrainId.tree_terrains()
    >>> TerrainId.water_terrains()

    **Examples**

    >>> TerrainId.FARM
    >>> 7
    """

    @staticmethod
    def water_terrains() -> List[TerrainId]:
        """
        Returns:
            A list of all Water terrains
        """
        return [
            TerrainId.WATER_DEEP,
            TerrainId.WATER_AZURE,
            TerrainId.WATER_BROWN,
            TerrainId.WATER_GREEN,
            TerrainId.WATER_MEDIUM,
            TerrainId.WATER_2D_BRIDGE,
            TerrainId.WATER_2D_SHORELESS,
            TerrainId.WATER_DEEP_OCEAN,
            TerrainId.WATER_SHALLOW,
        ]

    @staticmethod
    def beach_terrains() -> List[TerrainId]:
        """
        Returns:
            A list of all Beach terrains
        """
        return [
            TerrainId.BEACH,
            TerrainId.BEACH_ICE,
            TerrainId.BEACH_VEGETATION,
            TerrainId.BEACH_WET,
            TerrainId.BEACH_WET_GRAVEL,
            TerrainId.BEACH_WET_ROCK,
            TerrainId.BEACH_WHITE,
            TerrainId.BEACH_WHITE_VEGETATION,
        ]

    @staticmethod
    def tree_terrains() -> List[TerrainId]:
        """
        Returns:
            A list of all Tree terrains
        """
        return [
            TerrainId.FOREST_ACACIA,
            TerrainId.FOREST_AUTUMN,
            TerrainId.FOREST_AUTUMN_SNOW,
            TerrainId.FOREST_BAMBOO,
            TerrainId.FOREST_BAOBAB,
            TerrainId.FOREST_BIRCH,
            TerrainId.FOREST_BUSH,
            TerrainId.FOREST_DEAD,
            TerrainId.FOREST_DRAGON_TREE,
            TerrainId.FOREST_JUNGLE,
            TerrainId.FOREST_MANGROVE,
            TerrainId.FOREST_MEDITERRANEAN,
            TerrainId.FOREST_OAK,
            TerrainId.FOREST_OAK_BUSH,
            TerrainId.FOREST_PALM_DESERT,
            TerrainId.FOREST_PINE,
            TerrainId.FOREST_PINE_SNOW,
            TerrainId.FOREST_RAINFOREST,
            TerrainId.FOREST_REEDS,
            TerrainId.FOREST_REEDS_BEACH,
            TerrainId.FOREST_REEDS_SHALLOWS,
        ]

    BEACH = 2
    BEACH_NON_NAVIGABLE = 79
    BEACH_NON_NAVIGABLE_WET_GRAVEL = 81
    BEACH_NON_NAVIGABLE_WET_ROCK = 82
    BEACH_NON_NAVIGABLE_WET_SAND = 80
    BEACH_ICE = 37
    BEACH_VEGETATION = 52
    BEACH_WET = 107
    BEACH_WET_GRAVEL = 108
    BEACH_WET_ROCK = 109
    BEACH_WHITE = 53
    BEACH_WHITE_VEGETATION = 51
    BLACK = 47
    DESERT_CRACKED = 45
    DESERT_QUICKSAND = 46
    DESERT_SAND = 14
    DIRT_1 = 6
    DIRT_2 = 11
    DIRT_3 = 3
    DIRT_4 = 42
    DIRT_MUD = 76
    DIRT_SAVANNAH = 41
    FARM = 7
    FARM_0 = 29
    FARM_33 = 30
    FARM_67 = 31
    FARM_DEAD = 8
    FOREST_ACACIA = 50
    FOREST_AUTUMN = 104
    FOREST_AUTUMN_SNOW = 105
    FOREST_BAMBOO = 18
    FOREST_BAOBAB = 49
    FOREST_BIRCH = 110
    FOREST_BUSH = 89
    FOREST_DEAD = 106
    FOREST_DRAGON_TREE = 48
    FOREST_JUNGLE = 17
    FOREST_MANGROVE = 55
    FOREST_MEDITERRANEAN = 88
    FOREST_OAK = 10
    FOREST_OAK_BUSH = 20
    FOREST_PALM_DESERT = 13
    FOREST_PINE = 19
    FOREST_PINE_SNOW = 21
    FOREST_RAINFOREST = 56
    FOREST_REEDS = 92
    FOREST_REEDS_BEACH = 91
    FOREST_REEDS_SHALLOWS = 90
    GRASS_1 = 0
    GRASS_2 = 12
    GRASS_3 = 9
    GRASS_DRY = 100
    GRASS_FOUNDATION = 27
    GRASS_JUNGLE = 60
    GRASS_JUNGLE_RAINFOREST = 83
    GRASS_OTHER = 16
    GRAVEL_DEFAULT = 70
    GRAVEL_DESERT = 102
    ICE = 35
    ICE_NAVIGABLE = 26
    MODDABLE_GRASS_1 = 84
    MODDABLE_GRASS_2 = 85
    MODDABLE_GRASS_3 = 86
    MODDABLE_GRASS_4 = 87
    MODDABLE_DEEP_WATER = 99
    MODDABLE_NORMAL_WATER_1 = 97
    MODDABLE_NORMAL_WATER_2 = 98
    MODDABLE_SHALLOWS_1 = 93
    MODDABLE_SHALLOWS_2 = 94
    OBSOLETE_LEAVES_JUNGLE = 62
    OBSOLETE_ROAD_DESERT = 43
    OBSOLETE_ROAD_FUNGUS = 39
    OBSOLETE_ROAD_GRAVEL = 103
    OBSOLETE_ROAD_JUNGLE = 61
    OBSOLETE_ROAD_SNOW = 38
    OBSOLETE_SNOW_DIRT = 33
    OBSOLETE_SNOW_GRASS = 34
    RESERVED = 68
    RICE_FARM = 63
    RICE_FARM_0 = 65
    RICE_FARM_33 = 66
    RICE_FARM_67 = 67
    RICE_FARM_DEAD = 64
    ROAD = 24
    ROAD_BROKEN = 25
    ROAD_FUNGUS = 75
    ROAD_GRAVEL = 78
    ROCK_1 = 40
    SHALLOWS = 4
    SHALLOWS_AZURE = 59
    SHALLOWS_MANGROVE = 54
    SNOW = 32
    SNOW_FOUNDATION = 36
    SNOW_LIGHT = 73
    SNOW_STRONG = 74
    SWAMP = 111
    SWAMP_BOGLAND = 101
    UNDERBUSH = 5
    UNDERBUSH_JUNGLE = 77
    UNDERBUSH_LEAVES = 71
    UNDERBUSH_SNOW = 72
    VERY_EVIL_FOG = 69
    WATER_2D_BRIDGE = 28
    WATER_2D_SHORELESS = 15
    WATER_AZURE = 58
    WATER_BROWN = 96
    WATER_DEEP = 22
    WATER_DEEP_OCEAN = 57
    WATER_GREEN = 95
    WATER_MEDIUM = 23
    WATER_SHALLOW = 1
