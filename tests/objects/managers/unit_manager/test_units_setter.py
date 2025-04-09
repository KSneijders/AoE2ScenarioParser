import pytest

from AoE2ScenarioParser.managers import UnitManager
from AoE2ScenarioParser.sections import Unit
from datasets.player_data import Player
from tests.objects import MockScenarioSections


@pytest.fixture
def um():
    return UnitManager(MockScenarioSections())


def test_units_setter(um: UnitManager):
    with pytest.raises(ValueError, match = r'List of units must be nested list'):
        um.units = [Unit()]

    um.units = [
        [Unit()],
        [Unit(), Unit(), Unit()],
        [Unit(), Unit()]
    ]
    assert len(um.units) == 9
    assert len(list(um.get_all_units())) == 6

    assert [len(player_units) for player_units in um.units] == [1, 3, 2] + [0] * 6

    assert um.units[Player.GAIA][0].player == Player.GAIA
    assert um.units[Player.ONE][0].player == Player.ONE
    assert um.units[Player.ONE][1].player == Player.ONE
    assert um.units[Player.ONE][2].player == Player.ONE
    assert um.units[Player.TWO][0].player == Player.TWO
    assert um.units[Player.TWO][1].player == Player.TWO

    um.units = []
    assert len(um.units) == 9
    assert len(list(um.get_all_units())) == 0
    assert [len(player_units) for player_units in um.units] == [0] * 9


def test_units_setter_reference_id(um: UnitManager):
    assert um._next_unit_reference_id == 0

    um.units = [
        [Unit(reference_id=9)],
        [Unit(reference_id=11), Unit(reference_id=3)]
    ]
    assert um._next_unit_reference_id == 12

    # Not impacted by lower numbers
    um.units = [[Unit(reference_id=3)]]
    assert um._next_unit_reference_id == 12

    um.units = [[], [Unit(reference_id=3)], [], [], [Unit(reference_id=14)], [Unit(reference_id=3)]]
    assert um._next_unit_reference_id == 15
