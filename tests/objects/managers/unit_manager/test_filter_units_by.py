import pytest

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.managers import UnitManager
from AoE2ScenarioParser.sections import Unit


@pytest.fixture
def make_units_for_players(um: UnitManager):
    units = []

    u1 = Unit(reference_id=101, type=4)
    u2 = Unit(reference_id=102, type=5)
    units.extend(um.add_units(Player.ONE, [u1, u2]))

    u3 = Unit(reference_id=201, type=5)
    u4 = Unit(reference_id=202, type=6)
    units.extend(um.add_units(Player.TWO, [u3, u4]))

    u5 = Unit(reference_id=301, type=4)
    u6 = Unit(reference_id=302, type=7, state=3)
    units.extend(um.add_units(Player.THREE, [u5, u6]))

    return units


def test_filter_units_by_allowlist_attr_values(um: UnitManager, make_units_for_players: list[Unit]):
    units = make_units_for_players

    result = list(um.filter_units_by_type([4, 5]))
    assert list(u.type for u in result) == [4, 5, 5, 4]

    result2 = list(um.filter_units_by("state", [2]))
    assert len(result2) == (len(units) - 1)

    result3 = list(um.filter_units_by_id([101, 202]))
    assert list(u.reference_id for u in result3) == [101, 202]


def test_filter_units_by_blocklist(um: UnitManager, make_units_for_players: list[Unit]):
    result = list(um.filter_units_by_type([5, 7], is_allowlist=False))
    assert list(u.type for u in result) == [4, 6, 4]


def test_filter_units_by_with_players_subset(um: UnitManager, make_units_for_players: list[Unit]):
    result = list(um.filter_units_by_type([4], players=[Player.ONE, Player.THREE]))
    assert list(u.reference_id for u in result) == [101, 301]


def test_filter_units_by_uses_custom_units_iterable(um: UnitManager, make_units_for_players: list[Unit]):
    player_two_units = [u for u in um.get_all_units() if u.player == Player.TWO]

    result = list(um.filter_units_by_type([5], is_allowlist=False, units=player_two_units))
    assert len(result) == 1
    assert result[0].reference_id == 202


def test_filter_units_by_invalid_attribute_raises(um: UnitManager, make_units_for_players: list[Unit]):
    with pytest.raises(AttributeError):
        list(um.filter_units_by("nonexistent", [1]))
