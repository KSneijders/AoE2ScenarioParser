import pytest

from AoE2ScenarioParser.managers import UnitManager
from datasets.player_data import Player
from sections import Unit
from tests.objects import MockScenarioSections


@pytest.fixture
def um():
    return UnitManager(MockScenarioSections())


def test_next_unit_reference_id(um: UnitManager):
    assert um._next_unit_reference_id == 0

    assert um.next_unit_reference_id == 0
    assert um.next_unit_reference_id == 1
    assert um.next_unit_reference_id == 2
    assert um.next_unit_reference_id == 3
    assert um._next_unit_reference_id == 4

    um.add_unit(Player.ONE, Unit())

    assert um.next_unit_reference_id == 5
    