from AoE2ScenarioParser.managers import UnitManager
from AoE2ScenarioParser.sections import Unit
from datasets.player_data import Player
from tests.objects.managers.functions import create_unit


def test_get_all_units_amount(um: UnitManager):
    assert len(list(um.get_all_units())) == 0

    um.add_unit(create_unit(Player.ONE))
    assert len(list(um.get_all_units())) == 1

    um.add_unit(create_unit(Player.TWO))
    assert len(list(um.get_all_units())) == 2

    um.add_units((create_unit(Player.THREE), create_unit(Player.THREE), create_unit(Player.THREE)))
    assert len(list(um.get_all_units())) == 5


def test_get_all_units_ordered_by_player(um: UnitManager):
    um.add_unit(Unit(Player.ONE, 4, (0, 0)))
    um.add_unit(Unit(Player.TWO, 4, (3, 0)))
    um.add_unit(Unit(Player.ONE, 4, (1, 0)))
    um.add_unit(Unit(Player.FOUR, 4, (5, 0)))
    um.add_unit(Unit(Player.THREE, 4, (4, 0)))
    um.add_unit(Unit(Player.ONE, 4, (2, 0)))

    for index, unit in enumerate(um.get_all_units()):
        assert unit.x == index
