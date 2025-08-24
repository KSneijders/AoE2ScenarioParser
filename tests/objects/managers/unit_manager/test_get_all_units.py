from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.managers import UnitManager
from AoE2ScenarioParser.sections import Unit


def test_get_all_units_amount(um: UnitManager):
    assert len(list(um.get_all_units())) == 0

    um.add_unit(Player.ONE, Unit())
    assert len(list(um.get_all_units())) == 1

    um.add_unit(Player.TWO, Unit())
    assert len(list(um.get_all_units())) == 2

    um.add_units(Player.THREE, (Unit(), Unit(), Unit()))
    assert len(list(um.get_all_units())) == 5


def test_get_all_units_ordered_by_player(um: UnitManager):
    um.add_unit(Player.ONE, Unit(x=0))
    um.add_unit(Player.TWO, Unit(x=3))
    um.add_unit(Player.ONE, Unit(x=1))
    um.add_unit(Player.FOUR, Unit(x=5))
    um.add_unit(Player.THREE, Unit(x=4))
    um.add_unit(Player.ONE, Unit(x=2))

    for index, unit in enumerate(um.get_all_units()):
        assert unit.x == index
