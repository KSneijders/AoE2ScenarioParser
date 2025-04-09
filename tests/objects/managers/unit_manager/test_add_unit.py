import pytest

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.managers import UnitManager
from AoE2ScenarioParser.sections import Unit
from tests.objects import MockScenarioSections


@pytest.fixture
def um():
    return UnitManager(MockScenarioSections())


def test_add_unit_adds_units(um: UnitManager):
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
