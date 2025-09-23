from AoE2ScenarioParser.managers import UnitManager
from AoE2ScenarioParser.sections import Unit
from datasets.player_data import Player
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
