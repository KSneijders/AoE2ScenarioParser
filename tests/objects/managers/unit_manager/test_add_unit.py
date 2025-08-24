from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.managers import UnitManager
from AoE2ScenarioParser.sections import Unit


def test_add_unit_returns_unit(um: UnitManager):
    result = um.add_unit(Player.THREE, Unit(x = 1, y = 2))

    assert isinstance(result, Unit)
    assert result.x == 1
    assert result.y == 2


def test_add_unit_adds_unit(um: UnitManager):
    assert len(list(um.get_all_units())) == 0

    um.add_unit(Player.ONE, Unit())
    assert len(list(um.get_all_units())) == 1
    assert len(um.units[Player.ONE]) == 1

    um.add_unit(Player.TWO, Unit())
    assert len(list(um.get_all_units())) == 2
    assert len(um.units[Player.TWO]) == 1


def test_add_unit_sets_player(um: UnitManager):
    unit = Unit()
    assert unit.player is None
    um.add_unit(Player.TWO, unit)
    assert unit.player == Player.TWO


def test_add_units_returns_units(um: UnitManager):
    result = um.add_units(Player.ONE, [Unit(x = 1, y = 2), Unit(x = 3, y = 4), Unit(x = 5, y = 6)])

    assert isinstance(result, list)
    assert len(result) == 3

    for i in range(3):
        assert isinstance(result[i], Unit)
        assert result[i].x == 1 + (i * 2)
        assert result[i].y == 2 + (i * 2)


def test_add_units_adds_units(um: UnitManager):
    assert len(list(um.get_all_units())) == 0

    um.add_units(Player.ONE, [Unit(), Unit(), Unit()])
    assert len(list(um.get_all_units())) == 3
    assert len(um.units[Player.ONE]) == 3

    um.add_units(Player.TWO, [Unit(), Unit()])
    assert len(list(um.get_all_units())) == 5
    assert len(um.units[Player.TWO]) == 2


def test_add_units_sets_player(um: UnitManager):
    unit1, unit2 = Unit(), Unit()
    assert unit1.player is None
    assert unit2.player is None
    um.add_units(Player.FOUR, (unit1, unit2))
    assert unit1.player == Player.FOUR
    assert unit2.player == Player.FOUR
