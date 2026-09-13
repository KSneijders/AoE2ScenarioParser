from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.managers import UnitManager
from tests.objects.managers.functions import create_unit


def test_change_ownership(um: UnitManager):
    unit = create_unit(Player.ONE)
    um.add_unit(unit)

    assert unit.player == Player.ONE
    assert len(um.units[Player.ONE]) == 1
    assert len(um.units[Player.TWO]) == 0

    um.change_ownership(Player.TWO, unit)

    assert unit.player == Player.TWO
    assert len(um.units[Player.ONE]) == 0
    assert len(um.units[Player.TWO]) == 1


def test_change_ownership_to_self(um: UnitManager):
    unit = create_unit(Player.ONE)
    um.add_unit(unit)

    assert unit.player == Player.ONE
    assert len(um.units[Player.ONE]) == 1
    assert len(um.units[Player.TWO]) == 0

    um.change_ownership(Player.ONE, unit)

    assert unit.player == Player.ONE
    assert len(um.units[Player.ONE]) == 1
    assert len(um.units[Player.TWO]) == 0


def test_change_ownership_on_external_unit(um: UnitManager):
    unit = create_unit(Player.ONE)

    assert unit.player is Player.ONE
    assert len(um.units[Player.ONE]) == 0
    assert len(um.units[Player.TWO]) == 0

    um.change_ownership(Player.TWO, unit)

    assert unit.player == Player.TWO
    assert len(um.units[Player.ONE]) == 0
    assert len(um.units[Player.TWO]) == 1
