from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.managers import UnitManager
from AoE2ScenarioParser.objects.support import Area
from AoE2ScenarioParser.sections import Unit


def test_get_units_in_area_general_selection(um: UnitManager):
    um.add_units(Player.ONE, [
        Unit(type = 4, location = (0.5, 0.5)),
        Unit(type = 4, location = (1.5, 1.5)),
        Unit(type = 4, location = (1.5, 2.5)),
        Unit(type = 4, location = (2.5, 2.5)),
        Unit(type = 4, location = (3.5, 3.5)),
        Unit(type = 4, location = (4.5, 4.5)),
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
    um.add_unit(Player.ONE, Unit(type = 4, location = (1, 0)))

    units = um.get_units_in_area(Area((0, 0), (0, 0)))
    assert len(list(units)) == 0

    um.add_unit(Player.ONE, Unit(type = 4, location = (0.99, 0)))

    units = um.get_units_in_area(Area((0, 0), (0, 0)))
    assert len(list(units)) == 1


def test_get_units_in_area_multiple_players(um: UnitManager):
    um.add_unit(Player.ONE, Unit(type = 4, location = (0, 0)))
    um.add_unit(Player.TWO, Unit(type = 4, location = (1, 1)))

    units = um.get_units_in_area(Area((0, 0), (1, 1)))
    assert len(list(units)) == 2

    units = um.get_units_in_area(Area((1, 1), (1, 1)))
    assert len(list(units)) == 1


def test_get_units_in_area_player_filter(um: UnitManager):
    um.add_unit(Player.ONE, Unit(type = 4, location = (0, 0)))
    um.add_unit(Player.TWO, Unit(type = 4, location = (1, 1)))
    um.add_unit(Player.TWO, Unit(type = 4, location = (1, 1)))

    units = um.get_units_in_area(Area((0, 0), (1, 1)))  # No filter check
    assert len(list(units)) == 3

    units = um.get_units_in_area(Area((0, 0), (1, 1)), players = [Player.ONE])
    assert len(list(units)) == 1

    units = um.get_units_in_area(Area((0, 0), (1, 1)), players = [Player.TWO])
    assert len(list(units)) == 2


def test_get_units_in_area_given_units(um: UnitManager):
    um.add_unit(Player.ONE, Unit(type = 4, location = (0, 0)))
    um.add_unit(Player.TWO, Unit(type = 4, location = (1, 0)))
    um.add_unit(Player.THREE, Unit(type = 4, location = (0, 1)))
    um.add_unit(Player.FOUR, Unit(type = 4, location = (1, 1)))
    um.add_unit(Player.FIVE, Unit(type = 4, location = (2, 0)))
    um.add_unit(Player.SIX, Unit(type = 4, location = (0, 2)))
    um.add_unit(Player.SEVEN, Unit(type = 4, location = (2, 2)))
    um.add_unit(Player.EIGHT, Unit(type = 4, location = (1, 2)))
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
        Unit(type = 4, location = (0, 0)),
        Unit(type = 4, location = (1, 0)),
        Unit(type = 4, location = (0, 1)),
        Unit(type = 4, location = (1, 1)),
    ]

    units = um.get_units_in_area(Area((0, 1), (1, 1)), units = all_units)
    assert len(list(units)) == 2

    # Units without players should not be returned when filtering for players
    units = um.get_units_in_area(Area((0, 1), (1, 1)), units = all_units, players = [Player.ONE])
    assert len(list(units)) == 0
