import pytest

from AoE2ScenarioParser.managers import MapManager
from AoE2ScenarioParser.objects.support import Area, Tile
from tests.objects.managers.map_manager import MockMapManager


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


def test_terrain_from_function_area_args(mm: MapManager):
    area_1_1_2_2 = mm.get_square_1d(((1, 1), (2, 2)))

    tiles = mm.terrain_from(Area((1, 1), (2, 2)))
    assert len(tiles) == 4
    assert list(tiles.keys()) == [Tile(1, 1), Tile(2, 1), Tile(1, 2), Tile(2, 2)]
    terrain_tiles = list(tiles.values())
    for i in range(len(area_1_1_2_2)):
        assert terrain_tiles[i] == area_1_1_2_2[i]


def test_terrain_from_function_area_pattern_args(mm: MapManager):
    area1 = Area((1, 1), (3, 1))
    area3 = Area((1, 3), (3, 3))

    row_y1 = mm.get_square_1d(area1)
    row_y3 = mm.get_square_1d(area3)
    expected_terrain_tiles = row_y1 + row_y3

    expected_tiles = area1.to_tiles() | area3.to_tiles()

    area_pattern = mm \
        .get_area_pattern() \
        .select((1, 1), (3, 3)) \
        .use_pattern_lines(axis = 'x', gap_size = 1, line_width = 1)

    tiles = mm.terrain_from(area_pattern)
    assert len(tiles) == 6
    assert set(tiles.keys()) == expected_tiles
    terrain_tiles = list(tiles.values())
    for i in range(len(expected_terrain_tiles)):
        assert terrain_tiles[i] == expected_terrain_tiles[i]
