import pytest

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.exceptions.asp_exceptions import ObjectAlreadyLinkedError
from AoE2ScenarioParser.managers import UnitManager
from AoE2ScenarioParser.sections import ScenarioSections, Unit
from tests.objects.managers.functions import create_unit


def test_add_unit_with_units_garrisoned(um: UnitManager):
    unit1 = Unit.garrisoned(Player.ONE, type = 4)
    unit2 = Unit.garrisoned(Player.ONE, type = 4)

    parent = Unit(
        player = Player.ONE,
        type = UnitInfo.BATTERING_RAM.ID,
        location = (1, 2),
        garrisoned_units = [unit1, unit2]
    )

    um.add_unit(parent)

    assert len(um.units[1]) == 3
    assert parent.reference_id != -1
    assert unit1.reference_id != -1
    assert unit2.reference_id != -1

    assert parent.reference_id != unit1.reference_id
    assert parent.reference_id != unit2.reference_id


def test_add_garrisoned_unit_to_linked_unit_from_parent(um: UnitManager):
    unit1 = Unit.garrisoned(Player.ONE, type = 4)
    unit2 = Unit.garrisoned(Player.ONE, type = 4)
    parent = Unit(
        player = Player.ONE,
        type = 4,
        location = (1, 2),
    )

    um.add_unit(parent)
    parent.add_garrisoned_units(unit1, unit2)

    assert len(um.units[Player.ONE]) == 3
    assert parent.reference_id != -1
    assert unit1.reference_id != -1
    assert unit2.reference_id != -1

    assert um._is_linked_to_same(unit1)
    assert um._is_linked_to_same(unit2)
    assert um._is_linked_to_same(parent)


def test_add_already_linked_unit_through_parent_raises_exception():
    unit = Unit.garrisoned(Player.ONE, type = 4)
    parent = Unit(
        player = Player.ONE,
        type = 4,
        location = (1, 2),
    )

    um = UnitManager(ScenarioSections())
    um._initialize_properties()
    um2 = UnitManager(ScenarioSections())
    um2._initialize_properties()

    um.add_unit(unit)
    um2.add_unit(parent)

    with pytest.raises(ObjectAlreadyLinkedError):
        parent.add_garrisoned_units(unit)


def test_add_garrisoned_unit_to_linked_unit_from_child(um: UnitManager):
    unit = Unit.garrisoned(Player.ONE, type = 4)
    parent = Unit(
        player = Player.ONE,
        type = 4,
        location = (1, 2),
    )

    um.add_unit(unit)
    unit.garrisoned_in = parent

    assert len(um.units[Player.ONE]) == 2
    assert parent.reference_id != -1
    assert unit.reference_id != -1

    assert um._is_linked_to_same(unit)
    assert um._is_linked_to_same(parent)


def test_add_already_linked_unit_through_child_raises_exception():
    unit = Unit.garrisoned(Player.ONE, type = 4)
    parent = Unit(
        player = Player.ONE,
        type = 4,
        location = (1, 2),
    )

    um = UnitManager(ScenarioSections())
    um._initialize_properties()
    um2 = UnitManager(ScenarioSections())
    um2._initialize_properties()

    um.add_unit(unit)
    um2.add_unit(parent)

    with pytest.raises(ObjectAlreadyLinkedError):
        unit.garrisoned_in = parent


def test_adding_already_linked_unit_raises_exception():
    um = UnitManager(ScenarioSections())
    um._initialize_properties()
    um2 = UnitManager(ScenarioSections())
    um2._initialize_properties()

    unit = create_unit(Player.ONE)
    um.add_unit(unit)

    with pytest.raises(ObjectAlreadyLinkedError):
        um2.add_unit(unit)
