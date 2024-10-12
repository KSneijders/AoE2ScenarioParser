from contextlib import nullcontext as does_not_raise

import pytest

from AoE2ScenarioParser.managers import MapManager
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
