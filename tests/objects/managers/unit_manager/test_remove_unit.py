from AoE2ScenarioParser.managers import UnitManager
from AoE2ScenarioParser.sections import Unit
from tests.objects.managers.functions import create_unit


def test_remove_unit(um: UnitManager):
    unit = Unit(type = 4, location = (1, 1))

    um.units = [
        [create_unit() for _ in range(3)],
        [create_unit() for _ in range(4)],
        [create_unit() for _ in range(6)],
        [create_unit() for _ in range(5)] + [unit] + [create_unit() for _ in range(2)],
        [create_unit() for _ in range(2)],
        [create_unit() for _ in range(3)],
    ]

    assert [len(player_units) for player_units in um.units] == [3, 4, 6, 8, 2, 3, 0, 0, 0]

    um.remove_unit(unit)

    assert [len(player_units) for player_units in um.units] == [3, 4, 6, 7, 2, 3, 0, 0, 0]

    for unit in um.get_all_units():
        assert unit.x == .5


def test_remove_units(um: UnitManager):
    units = [Unit(type = 4, location = (1, 1)), Unit(type = 4, location = (2, 2)), Unit(type = 4, location = (3, 3))]

    um.units = [
        [create_unit() for _ in range(3)],
        [create_unit() for _ in range(4)],
        [create_unit() for _ in range(6)],
        [create_unit() for _ in range(5)] + units + [create_unit() for _ in range(2)],
        [create_unit() for _ in range(2)],
        [create_unit() for _ in range(3)],
    ]

    assert [len(player_units) for player_units in um.units] == [3, 4, 6, 10, 2, 3, 0, 0, 0]

    um.remove_units(units)

    assert [len(player_units) for player_units in um.units] == [3, 4, 6, 7, 2, 3, 0, 0, 0]

    for unit in um.get_all_units():
        assert unit.x == .5
