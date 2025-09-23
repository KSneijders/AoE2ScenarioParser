import pytest

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.managers import UnitManager
from AoE2ScenarioParser.sections import Unit
from tests.objects.managers.functions import create_unit


def test_units_setter(um: UnitManager):
    with pytest.raises(ValueError, match = r'List of units must be nested list'):
        um.units = [create_unit(Player.GAIA)]

    um.units = [
        [create_unit(Player.GAIA)],
        [create_unit(Player.ONE), create_unit(Player.ONE), create_unit(Player.ONE)],
        [create_unit(Player.TWO), create_unit(Player.TWO)]
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


def test_units_setter_updates_reference_id(um: UnitManager):
    assert um._next_unit_reference_id == 0

    um.units = [
        [Unit(Player.GAIA, 4, (1, 2), reference_id=9)],
        [Unit(Player.ONE, 4, (1, 2), reference_id=11), Unit(Player.ONE, 4, (1, 2), reference_id=3)]
    ]
    assert um._next_unit_reference_id == 12

    # Not impacted by lower numbers
    um.units = [[Unit(Player.GAIA, 4, (1, 2), reference_id=3)]]
    assert um._next_unit_reference_id == 12

    um.units = [
        [],
        [Unit(Player.ONE, 4, (1, 2), reference_id=3)],
        [],
        [],
        [Unit(Player.FOUR, 4, (1, 2), reference_id=14)],
        [Unit(Player.FIVE, 4, (1, 2), reference_id=3)]
    ]
    assert um._next_unit_reference_id == 15


def test_units_setter_throws_exception_when_invalid_player_attribute_encountered(um: UnitManager):
    with pytest.raises(ValueError, match = r'Invalid unit.player attribute encountered \[3\] in slot \[2\]'):
        um.units = [
            [create_unit(Player.GAIA)],
            [create_unit(Player.ONE), create_unit(Player.ONE), create_unit(Player.ONE)],
            [create_unit(Player.TWO), create_unit(Player.TWO), create_unit(Player.THREE)]
        ]

    with pytest.raises(ValueError, match = r'Invalid unit.player attribute encountered \[1\] in slot \[4\]'):
        um.units = [
            [],
            [],
            [],
            [],
            [create_unit(Player.ONE)],
            [],
            [],
        ]
