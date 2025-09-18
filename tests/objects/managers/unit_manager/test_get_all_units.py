from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.managers import UnitManager
from AoE2ScenarioParser.sections import Unit
from tests.objects.managers.functions import create_unit


def test_get_all_units_amount(um: UnitManager):
    assert len(list(um.get_all_units())) == 0

    um.add_unit(Player.ONE, create_unit())
    assert len(list(um.get_all_units())) == 1

    um.add_unit(Player.TWO, create_unit())
    assert len(list(um.get_all_units())) == 2

    um.add_units(Player.THREE, (create_unit(), create_unit(), create_unit()))
    assert len(list(um.get_all_units())) == 5


def test_get_all_units_ordered_by_player(um: UnitManager):
    um.add_unit(Player.ONE, Unit(4, (0, 0)))
    um.add_unit(Player.TWO, Unit(4, (3, 0)))
    um.add_unit(Player.ONE, Unit(4, (1, 0)))
    um.add_unit(Player.FOUR, Unit(4, (5, 0)))
    um.add_unit(Player.THREE, Unit(4, (4, 0)))
    um.add_unit(Player.ONE, Unit(4, (2, 0)))

    for index, unit in enumerate(um.get_all_units()):
        assert unit.x == index
