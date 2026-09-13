from typing import Iterable

import pytest

from AoE2ScenarioParser.datasets.terrains import TerrainId
from AoE2ScenarioParser.managers import MapManager
from AoE2ScenarioParser.objects.support.enums.direction import Direction
from AoE2ScenarioParser.sections import TerrainTile


@pytest.fixture(autouse = True)
def set_terrain(mm):
    for row in mm.terrain:
        for tile in row:
            tile.type = 1
            tile.mask_type = 0
            tile.elevation = 1


@pytest.fixture(params = [4, 3])
def shrink_size(request):
    return request.param


@pytest.fixture(params = [6, 7])
def expand_size(request):
    return request.param


@pytest.fixture(
    params = [
        (Direction.NORTH, 0, 1),
        (Direction.EAST, 0, 0),
        (Direction.SOUTH, 1, 0),
        (Direction.WEST, 1, 1)
    ]
)
def direction_params(request):
    return request.param


def assert_square_size(terrain: tuple[tuple[TerrainTile, ...], ...], size: int):
    assert size == len(terrain)
    for row in terrain:
        assert size == len(row)


def assert_elevation(terrain: Iterable[TerrainTile], elevation: int):
    for tile in terrain:
        assert tile.elevation == elevation


def test_terrain_shrink_map_by(mm: MapManager):
    # Shrink (5 → 4)
    result = mm.shrink_map_by(1)

    assert_square_size(mm.terrain, 4)
    assert_elevation(mm._terrain, 1)

    assert len(result) == 0

    # Shrink again (4 → 2)
    result = mm.shrink_map_by(2)

    assert_square_size(mm.terrain, 2)
    assert_elevation(mm._terrain, 1)

    assert len(result) == 0


def test_terrain_change_map_size_using_center(mm: MapManager):
    result = mm.change_map_size(7, Direction.CENTER)
    assert len(result) == 24

    assert_square_size(mm.terrain, 7)

    result = mm.shrink_map_by(1, Direction.CENTER)
    assert len(result) == 0

    assert_square_size(mm.terrain, 6)

    result = mm.expand_map_by(1, Direction.CENTER)
    assert len(result) == 13

    assert_square_size(mm.terrain, 7)

    result = mm.expand_map_by(3, Direction.CENTER)
    assert len(result) == 51

    assert_square_size(mm.terrain, 10)


def test_terrain_expand_map_by(mm: MapManager):
    # Expand (5 → 7)
    previous_size = mm.map_size
    expand_by = 2

    result = mm.expand_map_by(expand_by)

    assert_square_size(mm.terrain, previous_size + expand_by)
    assert_elevation(mm.terrain_from(result).values(), 0)

    assert len(result) == (previous_size * expand_by) * 2 + pow(expand_by, 2)

    # Expand again (7 → 8)
    previous_size = mm.map_size
    expand_by = 1

    result = mm.expand_map_by(expand_by)

    assert_square_size(mm.terrain, previous_size + expand_by)
    assert_elevation(mm.terrain_from(result).values(), 0)

    assert len(result) == (previous_size * expand_by) * 2 + pow(expand_by, 2)


def test_terrain_change_map_size__shrink_to_x(
    mm: MapManager,
    direction_params: tuple[Direction, int, int],
    shrink_size: int
):
    direction, xo, yo = direction_params

    x_offset = (mm.map_size - shrink_size) * xo
    y_offset = (mm.map_size - shrink_size) * yo
    new_terrain_2d = tuple(
        tuple(mm.terrain[y + y_offset][x + x_offset] for x in range(shrink_size))
            for y in range(shrink_size)
    )

    result = mm.change_map_size(shrink_size, direction)
    assert_square_size(mm.terrain, shrink_size)

    assert mm.terrain == new_terrain_2d
    assert len(result) == 0


def test_terrain_change_map_size__expand_to_x(
    mm: MapManager,
    direction_params: tuple[Direction, int, int],
    expand_size: int
):
    direction, xo, yo = direction_params

    previous_terrain = mm.terrain
    previous_size = len(previous_terrain)

    result = mm.change_map_size(expand_size, direction)
    assert_square_size(mm.terrain, expand_size)

    x_offset = (expand_size - previous_size) * xo
    y_offset = (expand_size - previous_size) * yo
    previous_terrain_after_change = tuple(
        tuple(mm.terrain[y + y_offset][x + x_offset] for x in range(previous_size))
            for y in range(previous_size)
    )

    assert previous_terrain == previous_terrain_after_change
    assert_square_size(mm.terrain, expand_size)
    assert_elevation(mm.terrain_from(result).values(), 0)


def test_terrain_change_map_size_with_terrain_template(mm: MapManager):
    template = TerrainTile(type = TerrainId.DIRT_1, elevation = 4, zone = 3, mask_type = 2, layer_type = 1)

    new_tiles = mm.expand_map_by(5, terrain_template = template)
    expected_elevations = {5: 2, 6: 3, 7: 4, 8: 4, 9: 4}

    for tile, terrain_tile in mm.terrain_from(new_tiles).items():
        coord = max(*tile)
        expected_elevation = expected_elevations[coord] if coord in expected_elevations else 1

        assert terrain_tile.elevation == expected_elevation
        assert terrain_tile.zone == 3
        assert terrain_tile.mask_type == 2
        assert terrain_tile.layer_type == 1
