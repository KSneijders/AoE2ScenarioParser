from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class DamageClass(_DataSetIntEnums):
    """
    This enum class provides the integer values that represent the damage classes in the game. Used in the 'Chnage
    Object Attack/Armour' and 'Modify Attribute' with the 'Attack/Armour' attibutes

    **Examples**

    >>> DamageClass.INFANTRY
    <DamageClass.INFANTRY: 1>
    """
    WONDER = 0
    """Since HD. Only wonders has this armour class. However there is no unit that has this attack class."""
    INFANTRY = 1
    TURTLE_SHIPS = 2
    BASE_PIERCE = 3
    BASE_MELEE = 4
    WAR_ELEPHANTS = 5
    UNUSED_ID6 = 6
    UNUSED_ID7 = 7
    CAVALRY = 8
    UNUSED_ID9 = 9
    UNUSED_ID10 = 10
    ALL_BUILDINGS_EXCEPT_PORT = 11
    """Port is the building with id 446"""
    UNUSED_ID12 = 12
    STONE_DEFENSE = 13
    PREDATOR_ANIMALS_FE = 14
    """Wolf, Bear, Jaguar, Tiger, etc. have this armour class"""
    ARCHERS = 15
    BATTLE_SHIPS_AND_SABOTEUR = 16
    """Camels also had this armour class before AK"""
    RAMS_TREBUCHETS_SIEGE_TOWERS = 17
    TREES = 18
    UNIQUE_UNITS = 19
    SIEGE_WEAPONS = 20
    STANDARD_BUILDINGS = 21
    WALLS_AND_GATES = 22
    GUNPOWDER_UNITS = 23
    BOARS = 24
    MONKS = 25
    CASTLES = 26
    """Castles, Kreposts, Fortresses, Poenari Castles"""
    SPEARMEN = 27
    CAVALRY_ARCHERS = 28
    EAGLE_WARRIORS = 29
    CAMELS = 30
    """Camels use this armour class since and after AK"""
    UNUSED_ID31 = 31
    CONDOTTIERI = 32
    PROJECTILE_GUNPOWDER_SECONDARY = 33
    FISHING_SHIPS = 34
    MAMELUKES = 35
    HEROES_AND_KINGS = 36
    HUSSITE_WAGONS = 37
    UNUSED_ID38 = 38
    UNUSED_ID39 = 39
    UNUSED_ID40 = 40
    UNUSED_ID41 = 41
    UNUSED_ID42 = 42
    UNUSED_ID43 = 43
    UNUSED_ID44 = 44
    UNUSED_ID45 = 45
    UNUSED_ID46 = 46
    UNUSED_ID47 = 47
    UNUSED_ID48 = 48
    UNUSED_ID49 = 49
