from AoE2ScenarioParser.managers import UnitManager
from AoE2ScenarioParser.sections import Unit
from datasets.buildings import BuildingInfo
from datasets.player_data import Player
from datasets.units import UnitInfo
from tests.objects.managers.functions import create_unit


def test_remove_unit(um: UnitManager):
    unit = Unit(Player.THREE, type = 4, location = (1, 1))

    um.add_units([
        *[create_unit(Player.GAIA) for _ in range(3)],
        *[create_unit(Player.ONE) for _ in range(4)],
        *[create_unit(Player.TWO) for _ in range(6)],
        *[create_unit(Player.THREE) for _ in range(5)] + [unit] + [create_unit(Player.THREE) for _ in range(2)],
        *[create_unit(Player.FOUR) for _ in range(2)],
        *[create_unit(Player.FIVE) for _ in range(3)],
    ])

    assert [len(player_units) for player_units in um.units] == [3, 4, 6, 8, 2, 3, 0, 0, 0]

    um.remove_unit(unit)

    assert [len(player_units) for player_units in um.units] == [3, 4, 6, 7, 2, 3, 0, 0, 0]

    for unit in um.get_all_units():
        assert unit.x == .5


def test_remove_units(um: UnitManager):
    units = [
        Unit(Player.THREE, 4, (1, 1)),
        Unit(Player.THREE, 4, (2, 2)),
        Unit(Player.THREE, 4, (3, 3)),
    ]

    um.add_units([
        *[create_unit(Player.GAIA) for _ in range(3)],
        *[create_unit(Player.ONE) for _ in range(4)],
        *[create_unit(Player.TWO) for _ in range(6)],
        *[create_unit(Player.THREE) for _ in range(5)] + units + [create_unit(Player.THREE) for _ in range(2)],
        *[create_unit(Player.FOUR) for _ in range(2)],
        *[create_unit(Player.FIVE) for _ in range(3)],
    ])

    assert [len(player_units) for player_units in um.units] == [3, 4, 6, 10, 2, 3, 0, 0, 0]

    um.remove_units(units)

    assert [len(player_units) for player_units in um.units] == [3, 4, 6, 7, 2, 3, 0, 0, 0]

    for unit in um.get_all_units():
        assert unit.x == .5


def test_remove_unit_with_garrisoned_units_should_not_remove_garrisoned_units(um: UnitManager):
    parent = Unit(
        player = Player.ONE,
        type = BuildingInfo.CASTLE.ID,
        location = (1, 1),
        garrisoned_units = [Unit.garrisoned(Player.ONE, type = 4) for _ in range(10)]
    )

    um.add_unit(parent)

    assert len(um.units[Player.ONE]) == 11
    assert len(parent.garrisoned_units) == 10
    assert parent._struct is not None
    assert parent.reference_id != -1

    for unit in parent.garrisoned_units:
        assert unit._struct is not None
        assert unit.reference_id != -1

    um.remove_unit(parent)

    assert len(um.units[Player.ONE]) == 10
    assert parent._struct is None
    assert parent.reference_id == -1

    for unit in parent.garrisoned_units:
        assert unit._struct is not None
        assert unit.reference_id != -1


def test_remove_unit_should_unlink_unit(um: UnitManager):
    unit = um.add_unit(create_unit(Player.ONE))

    assert um._unit_is_linked(unit)
    assert unit.reference_id != -1

    um.remove_unit(unit)

    assert unit._struct is None
    assert unit.reference_id == -1


def test_remove_unit_should_remove_from_garrisoned_units(um: UnitManager):
    unit1 = Unit.garrisoned(Player.ONE, type = 4)
    unit2 = Unit.garrisoned(Player.ONE, type = 4)
    parent = Unit(
        player = Player.ONE,
        type = UnitInfo.BATTERING_RAM.ID,
        location = (1, 1),
        garrisoned_units = [unit1, unit2]
    )

    um.add_unit(parent)
    um.remove_unit(unit1)

    assert len(parent.garrisoned_units) == 1

    assert parent.garrisoned_units[0] is unit2
