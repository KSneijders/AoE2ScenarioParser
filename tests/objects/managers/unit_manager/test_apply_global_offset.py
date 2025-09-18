import pytest

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.exceptions.asp_exceptions import InvalidObjectPlacementError
from AoE2ScenarioParser.managers import UnitManager
from AoE2ScenarioParser.sections import Unit


def assert_units_inside_map(units: list[Unit], map_size: int, x_start_at: int, y_start_at: int) -> None:
    for index, unit in enumerate(units):
        assert 0 <= unit.x < map_size and 0 <= unit.y < map_size

        assert unit.x == index + x_start_at
        assert unit.y == index + y_start_at


def test_apply_global_offset(um: UnitManager):
    map_size = 5
    units = um.units[Player.ONE]

    um.add_units(Player.ONE, [Unit(4, (i, i)) for i in range(5)])

    um.apply_global_offset(x_offset = 1, y_offset = 0, map_size = map_size, unit_overflow_action = 'remove')
    assert len(units) == 4
    assert_units_inside_map(units, map_size, x_start_at = 1, y_start_at = 0)

    um.apply_global_offset(x_offset = 0, y_offset = 3, map_size = map_size, unit_overflow_action = 'remove')
    assert len(units) == 2
    assert_units_inside_map(units, map_size, x_start_at = 1, y_start_at = 3)

    um.apply_global_offset(x_offset = -2, y_offset = 0, map_size = map_size, unit_overflow_action = 'remove')
    assert len(units) == 1
    assert_units_inside_map(units, map_size, x_start_at = 0, y_start_at = 4)


def test_apply_global_offset_throw_exception(um: UnitManager):
    map_size = 5
    um.add_units(Player.ONE, [Unit(4, (i, i)) for i in range(5)])

    pytest.raises(
        InvalidObjectPlacementError,
        lambda: um.apply_global_offset(x_offset = 1, y_offset = 1, map_size = map_size, unit_overflow_action = 'error')
    )

    pytest.raises(
        InvalidObjectPlacementError,
        lambda: um.apply_global_offset(x_offset = -3, y_offset = 0, map_size = map_size, unit_overflow_action = 'error')
    )
