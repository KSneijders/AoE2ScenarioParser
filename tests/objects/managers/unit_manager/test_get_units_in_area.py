import pytest

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.managers import UnitManager
from AoE2ScenarioParser.objects.support import Area
from AoE2ScenarioParser.sections import Unit
from tests.objects import MockScenarioSections


@pytest.fixture
def um():
    return UnitManager(MockScenarioSections())


def test_get_units_in_area_general_selection(um: UnitManager):
    um.add_units(Player.ONE, [
        Unit(x=0.5, y=0.5),
        Unit(x=1.5, y=1.5),
        Unit(x=1.5, y=2.5),
        Unit(x=2.5, y=2.5),
        Unit(x=3.5, y=3.5),
        Unit(x=4.5, y=4.5),
    ])
    # Y ↓ / X →
    # .         #
    #   .       #
    #   . .     #
    #       .   #
    #         . #

    units = um.get_units_in_area(Area((1, 1), (1, 1)))
    assert len(list(units)) == 1

    units = um.get_units_in_area(Area((1, 1), (2, 2)))
    assert len(list(units)) == 3

    units = um.get_units_in_area(Area((2, 0), (2, 4)))
    assert len(list(units)) == 1

    units = um.get_units_in_area(Area((0, 2), (4, 4)))
    assert len(list(units)) == 4


def test_get_units_in_area_edge_selection(um: UnitManager):
    um.add_unit(Player.ONE, Unit(x=1, y=0))

    units = um.get_units_in_area(Area((0, 0), (0, 0)))
    assert len(list(units)) == 0

    um.add_unit(Player.ONE, Unit(x=0.99, y=0))

    units = um.get_units_in_area(Area((0, 0), (0, 0)))
    assert len(list(units)) == 1


def test_get_units_in_area_multiple_players(um: UnitManager):
    um.add_unit(Player.ONE, Unit(x=0, y=0))
    um.add_unit(Player.TWO, Unit(x=1, y=1))

    units = um.get_units_in_area(Area((0, 0), (1, 1)))
    assert len(list(units)) == 2

    units = um.get_units_in_area(Area((1, 1), (1, 1)))
    assert len(list(units)) == 1


def test_get_units_in_area_player_filter(um: UnitManager):
    um.add_unit(Player.ONE, Unit(x=0, y=0))
    um.add_unit(Player.TWO, Unit(x=1, y=1))
    um.add_unit(Player.TWO, Unit(x=1, y=1))

    units = um.get_units_in_area(Area((0, 0), (1, 1)))  # No filter check
    assert len(list(units)) == 3

    units = um.get_units_in_area(Area((0, 0), (1, 1)), players = [Player.ONE])
    assert len(list(units)) == 1

    units = um.get_units_in_area(Area((0, 0), (1, 1)), players = [Player.TWO])
    assert len(list(units)) == 2


def test_get_units_in_area_given_units(um: UnitManager):
    um.add_unit(Player.ONE, Unit(x=0, y=0))
    um.add_unit(Player.TWO, Unit(x=1, y=0))
    um.add_unit(Player.THREE, Unit(x=0, y=1))
    um.add_unit(Player.FOUR, Unit(x=1, y=1))
    um.add_unit(Player.FIVE, Unit(x=2, y=0))
    um.add_unit(Player.SIX, Unit(x=0, y=2))
    um.add_unit(Player.SEVEN, Unit(x=2, y=2))
    um.add_unit(Player.EIGHT, Unit(x=1, y=2))
    # Y ↓ / X →
    # . . . #
    # . .   # → all_units
    # . . . # → all_units

    all_units = list(um.get_units_in_area(Area((0, 1), (2, 2))))  # Get part of units
    assert len(all_units) == 5

    units = um.get_units_in_area(Area((0, 0), (1, 1)), units = all_units)
    assert len(list(units)) == 2

    units = um.get_units_in_area(Area((1, 1), (2, 2)), units = all_units)
    assert len(list(units)) == 3


def test_get_units_in_area_given_units_no_player(um: UnitManager):
    all_units = [
        Unit(x=0, y=0),
        Unit(x=1, y=0),
        Unit(x=0, y=1),
        Unit(x=1, y=1),
    ]

    units = um.get_units_in_area(Area((0, 1), (1, 1)), units = all_units)
    assert len(list(units)) == 2

    # Units without players should not be returned when filtering for players
    units = um.get_units_in_area(Area((0, 1), (1, 1)), units = all_units, players = [Player.ONE])
    assert len(list(units)) == 0
