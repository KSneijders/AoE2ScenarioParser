from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.managers import UnitManager
from AoE2ScenarioParser.sections import Unit
from sections import ScenarioSections


def test_import_units_allows_unlinked_units(um: UnitManager):
    unit1 = Unit(Player.ONE, 6, (1, 2), reference_id = 45)
    unit2 = Unit(Player.ONE, 7, (1, 2), reference_id = 46)

    next_reference_id = um._next_unit_reference_id

    um.import_units((unit1, unit2))

    assert unit1.reference_id == next_reference_id
    assert unit2.reference_id == next_reference_id + 1


def test_import_units_allows_linked_units():
    unit1 = Unit(Player.ONE, 6, (1, 2))
    unit2 = Unit(Player.ONE, 7, (1, 2))

    um1 = UnitManager(ScenarioSections())
    um1.add_units((unit1, unit2))

    assert um1._is_linked_to_same(unit1)

    um2 = UnitManager(ScenarioSections())
    um2.import_units((unit1, unit2))

    assert um2._is_linked_to_same(unit1)
