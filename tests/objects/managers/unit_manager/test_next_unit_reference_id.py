from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.managers import UnitManager
from AoE2ScenarioParser.sections import Unit


def test_next_unit_reference_id(um: UnitManager):
    assert um._next_unit_reference_id == 0

    assert um.next_unit_reference_id == 0
    assert um.next_unit_reference_id == 1
    assert um.next_unit_reference_id == 2
    assert um.next_unit_reference_id == 3
    assert um._next_unit_reference_id == 4

    um.add_unit(Player.ONE, Unit())

    assert um.next_unit_reference_id == 5
    