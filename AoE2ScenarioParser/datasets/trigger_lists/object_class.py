from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class ObjectClass(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the object class in the game. Used in a lot of effects
    and conditions, like 'Kill Object', 'Objects in Area' under the name 'Object Group'.

    **Examples**

    >>> ObjectClass.CIVILIAN
    <ObjectClass.CIVILIAN: 4>
    """
    ARCHER = 0
    ARTIFACT = 1
    TRADE_BOAT = 2
    BUILDING = 3
    CIVILIAN = 4
    OCEAN_FISH = 5
    INFANTRY = 6
    BERRY_BUSH = 7
    STONE_MINE = 8
    PREY_ANIMAL = 9
    PREDATOR_ANIMAL = 10
    MISCELLANEOUS = 11
    CAVALRY = 12
    SIEGE_WEAPON = 13
    TERRAIN = 14
    TREE = 15
    TREE_STUMP = 16
    HEALER = 17
    MONK = 18
    TRADE_CART = 19
    TRANSPORT_BOAT = 20
    FISHING_BOAT = 21
    WARSHIP = 22
    CONQUISTADOR = 23
    WAR_ELEPHANT = 24
    HERO = 25
    ELEPHANT_ARCHER = 26
    WALL = 27
    PHALANX = 28
    DOMESTIC_ANIMAL = 29
    FLAG = 30
    DEEP_SEA_FISH = 31
    GOLD_MINE = 32
    SHORE_FISH = 33
    CLIFF = 34
    PETARD = 35
    CAVALRY_ARCHER = 36
    DOPPELGANGER = 37
    BIRD = 38
    GATE = 39
    SALVAGE_PILE = 40
    RESOURCE_PILE = 41
    RELIC = 42
    MONKWITH_RELIC = 43
    HAND_CANNONEER = 44
    TWO_HANDED_SWORDSMAN = 45
    PIKEMAN = 46
    SCOUT = 47
    ORE_MINE = 48
    FARM = 49
    SPEARMAN = 50
    PACKED_UNIT = 51
    TOWER = 52
    BOARDING_BOAT = 53
    UNPACKED_SIEGE_UNIT = 54
    BALLISTA = 55
    RAIDER = 56
    CAVALRY_RAIDER = 57
    LIVESTOCK = 58
    KING = 59
    MISC_BUILDING = 60
    CONTROLLED_ANIMAL = 61
    OYSTERS = 63
