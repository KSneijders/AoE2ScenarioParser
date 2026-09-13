import pytest

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.exceptions.asp_exceptions import ObjectAlreadyLinkedError
from AoE2ScenarioParser.managers import UnitManager
from AoE2ScenarioParser.sections import Unit
from tests.objects.managers.functions import create_unit


def test_add_unit_returns_unit(um: UnitManager):
    result = um.add_unit(Unit(Player.THREE, 4, (1, 2)))

    assert isinstance(result, Unit)
    assert result.object_id == 4
    assert result.x == 1
    assert result.y == 2


def test_add_unit_adds_unit(um: UnitManager):
    assert len(list(um.get_all_units())) == 0

    um.add_unit(create_unit(Player.ONE))
    assert len(list(um.get_all_units())) == 1
    assert len(um.units[Player.ONE]) == 1

    um.add_unit(create_unit(Player.TWO))
    assert len(list(um.get_all_units())) == 2
    assert len(um.units[Player.TWO]) == 1


def test_add_unit_places_unit_in_right_player_units(um: UnitManager):
    unit = create_unit(Player.TWO)
    assert unit.player is Player.TWO
    um.add_unit(unit)
    assert unit.player == Player.TWO
    assert unit in um.units[Player.TWO]


def test_add_unit_already_linked_units(um: UnitManager, um2: UnitManager):
    unit = create_unit(Player.ONE)
    um.add_unit(unit)

    with pytest.raises(ObjectAlreadyLinkedError):
        um2.add_unit(unit)


def test_add_parent_unit_adds_child_units_automatically(um: UnitManager):
    child1 = Unit.garrisoned(Player.ONE, 3)
    child2 = Unit.garrisoned(Player.ONE, 3)

    parent = Unit(Player.ONE, 4, (1, 2), garrisoned_units = [child1, child2])
    um.add_unit(parent)

    assert parent.reference_id != -1
    assert child1.reference_id != -1
    assert child2.reference_id != -1


def test_add_child_unit_adds_parent_and_other_children_automatically(um: UnitManager):
    child1 = Unit.garrisoned(Player.ONE, 3)
    child2 = Unit.garrisoned(Player.ONE, 3)

    parent = Unit(Player.ONE, 4, (1, 2), garrisoned_units = [child1, child2])
    um.add_unit(child1)

    assert parent.reference_id != -1
    assert child1.reference_id != -1
    assert child2.reference_id != -1
