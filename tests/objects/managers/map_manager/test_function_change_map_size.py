import math
import random
from contextlib import nullcontext as does_not_raise

import pytest
from binary_file_parser import Version

from AoE2ScenarioParser.managers import MapManager
from AoE2ScenarioParser.objects.support.enums.direction import Direction
from objects.managers.map_manager import MockMapManager


@pytest.fixture
def mm():
    return MapManager(MockMapManager(Version((99, 0))))


@pytest.fixture(autouse = True)
def randomize_terrain(mm):
    # Randomize the terrain types so __eq__ checks have something to validate
    for row in mm.terrain:
        for tile in row:
            tile.type = math.floor(random.random() * 25)
            tile.mask_type = math.floor(random.random() * 25)
            tile.elevation = random.choice([1, 2])


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


def assert_square_size(terrain, size):
    assert size == len(terrain)
    for row in terrain:
        assert size == len(row)


def test_terrain_shrink_map_by(mm: MapManager):
    mm.shrink_map_by(1)
    assert_square_size(mm.terrain, 4)

    mm.shrink_map_by(2)
    assert_square_size(mm.terrain, 2)


def test_terrain_expand_map_by(mm: MapManager):
    mm.expand_map_by(2)
    assert_square_size(mm.terrain, 7)

    mm.expand_map_by(1)
    assert_square_size(mm.terrain, 8)


def test_terrain_change_map_size__shrink_to_x_north(mm: MapManager, direction_params: tuple[Direction, int, int], shrink_size: int):
    direction, xo, yo = direction_params

    x_offset = (mm.map_size - shrink_size) * xo
    y_offset = (mm.map_size - shrink_size) * yo
    new_terrain_2d = tuple(
        tuple(mm.terrain[y + y_offset][x + x_offset] for x in range(shrink_size))
            for y in range(shrink_size)
    )

    mm.change_map_size(shrink_size, direction)
    assert_square_size(mm.terrain, shrink_size)

    assert mm.terrain == new_terrain_2d


def test_terrain_change_map_size__expand_to_x_north(mm: MapManager, direction_params: tuple[Direction, int, int], expand_size: int):
    direction, xo, yo = direction_params

    previous_terrain = mm.terrain
    previous_size = len(previous_terrain)

    mm.change_map_size(expand_size, direction)
    assert_square_size(mm.terrain, expand_size)

    x_offset = (expand_size - previous_size) * xo
    y_offset = (expand_size - previous_size) * yo
    previous_terrain_after_change = tuple(
        tuple(mm.terrain[y + y_offset][x + x_offset] for x in range(previous_size))
            for y in range(previous_size)
    )

    assert previous_terrain == previous_terrain_after_change

# Todo: Add tests for terrain preset
# Todo: Add tests for elevation smoothing (doesn't have to be thorough, just testing that it works
#   More in-depth tests should be done for the set_elevation function specifically

