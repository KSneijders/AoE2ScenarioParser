from unittest import TestCase

import pytest

from AoE2ScenarioParser.managers import MapManager
from AoE2ScenarioParser.objects.support import Tile
from objects.managers.map_manager import MockMapManager


@pytest.fixture
def mm():
    return MapManager(MockMapManager())


def test_terrain_from_function_tile_args(mm: MapManager):
    terrain_3_3 = mm.get_tile(Tile(3, 3))
    terrain_1_1 = mm.get_tile(Tile(1, 1))
    terrain_4_3 = mm.get_tile(Tile(4, 3))

    tiles = mm.terrain_from(Tile(3, 3))
    assert len(tiles) == 1
    assert list(tiles.keys()) == [Tile(3, 3)]
    assert tiles[Tile(3, 3)] == terrain_3_3

    tiles = mm.terrain_from((Tile(1, 1), Tile(4, 3)))
    assert len(tiles) == 2
    assert list(tiles.keys()) == [Tile(1, 1), Tile(4, 3)]
    assert tiles[Tile(1, 1)] == terrain_1_1
    assert tiles[Tile(4, 3)] == terrain_4_3
