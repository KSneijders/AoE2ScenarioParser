from contextlib import nullcontext as does_not_raise

import pytest

from AoE2ScenarioParser.managers import MapManager
from AoE2ScenarioParser.objects.support import Tile
from AoE2ScenarioParser.sections import TerrainTile
from objects.managers.map_manager import MockMapManager


@pytest.fixture
def mm():
    return MapManager(MockMapManager())


def test_terrain_setter_set_1d_sequence(mm: MapManager):
    mm.terrain = [TerrainTile() for _ in range(4)]
    assert mm.map_size == 2

    mm.terrain = [TerrainTile() for _ in range(9)]
    assert mm.map_size == 3

    with pytest.raises(ValueError, match = 'Invalid length given for terrain sequence'):
        mm.terrain = [TerrainTile() for _ in range(5)]
        mm.terrain = [TerrainTile() for _ in range(12)]

    # Try types other than list
    mm.terrain = tuple(TerrainTile() for _ in range(4))
    assert mm.map_size == 2


def test_terrain_setter_set_tuple(mm: MapManager):
    mm.terrain = [[TerrainTile() for _ in range(2)] for _ in range(2)]
    assert mm.map_size == 2

    mm.terrain = [[TerrainTile() for _ in range(3)] for _ in range(3)]
    assert mm.map_size == 3

    with pytest.raises(ValueError, match = 'Encountered unexpected length for nested sequence'):
        mm.terrain = [[TerrainTile() for _ in range(3)] for _ in range(2)]
        mm.terrain = [[TerrainTile() for _ in range(3)] for _ in range(4)]

    # Try types other than list
    mm.terrain = tuple(tuple(TerrainTile() for _ in range(4)) for _ in range(4))
    assert mm.map_size == 4


def test_terrain_setter_verify_assigned_tile(mm: MapManager):
    assert mm.terrain[3][4].tile == Tile(4, 3)
    assert mm.terrain[0][3].tile == Tile(3, 0)

    mm.terrain = [[TerrainTile() for _ in range(2)] for _ in range(2)]
    tiles = [terrain.tile for row in mm.terrain for terrain in row]

    assert tiles == [Tile(x, y) for y in range(2) for x in range(2)]

    mm.terrain = [TerrainTile() for _ in range(3 ** 2)]
    tiles = [terrain.tile for row in mm.terrain for terrain in row]

    assert tiles == [Tile(x, y) for y in range(3) for x in range(3)]
