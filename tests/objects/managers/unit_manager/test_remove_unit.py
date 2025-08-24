from AoE2ScenarioParser.managers import UnitManager
from AoE2ScenarioParser.sections import Unit


def test_remove_unit(um: UnitManager):
    unit = Unit(x=1, y=1)

    um.units = [
        [Unit() for _ in range(3)],
        [Unit() for _ in range(4)],
        [Unit() for _ in range(6)],
        [Unit() for _ in range(5)] + [unit] + [Unit() for _ in range(2)],
        [Unit() for _ in range(2)],
        [Unit() for _ in range(3)],
    ]

    assert [len(player_units) for player_units in um.units] == [3, 4, 6, 8, 2, 3, 0, 0, 0]

    um.remove_unit(unit)

    assert [len(player_units) for player_units in um.units] == [3, 4, 6, 7, 2, 3, 0, 0, 0]

    for unit in um.get_all_units():
        assert unit.x == .5


def test_remove_units(um: UnitManager):
    units = [Unit(x=1, y=1), Unit(x=2, y=2), Unit(x=3, y=3)]

    um.units = [
        [Unit() for _ in range(3)],
        [Unit() for _ in range(4)],
        [Unit() for _ in range(6)],
        [Unit() for _ in range(5)] + units + [Unit() for _ in range(2)],
        [Unit() for _ in range(2)],
        [Unit() for _ in range(3)],
    ]

    assert [len(player_units) for player_units in um.units] == [3, 4, 6, 10, 2, 3, 0, 0, 0]

    um.remove_units(units)

    assert [len(player_units) for player_units in um.units] == [3, 4, 6, 7, 2, 3, 0, 0, 0]

    for unit in um.get_all_units():
        assert unit.x == .5
