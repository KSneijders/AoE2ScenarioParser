import pytest

from AoE2ScenarioParser.managers import MapManager
from tests.objects.managers.map_manager import MockScenarioSections


@pytest.fixture
def mm():
    return MapManager(MockScenarioSections())


def test_terrain_set_elevation_simple(mm: MapManager):
    print('')
    mm.set_elevation(area = ((2, 2), (3, 3)), elevation = 1)

    elevations = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]

    assert [[tile.elevation for tile in row] for row in mm.terrain] == elevations
    mm.set_elevation(area = (0, 0), elevation = 2)

    elevations = [
        [2, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]

    assert [[tile.elevation for tile in row] for row in mm.terrain] == elevations


def test_terrain_set_elevation_corner(mm: MapManager):
    mm.set_elevation(area = ((0, 0), (0, 2)), elevation = 1)
    mm.set_elevation(area = ((0, 0), (2, 0)), elevation = 1)

    elevations = [
        [1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    assert [[tile.elevation for tile in row] for row in mm.terrain] == elevations


def test_terrain_set_elevation_side(mm: MapManager):
    mm.set_elevation(area = ((3, 0), (4, 4)), elevation = 3)

    elevations = [
        [0, 1, 2, 3, 3],
        [0, 1, 2, 3, 3],
        [0, 1, 2, 3, 3],
        [0, 1, 2, 3, 3],
        [0, 1, 2, 3, 3],
    ]

    assert [[tile.elevation for tile in row] for row in mm.terrain] == elevations
    mm.set_elevation(area = ((0, 3), (4, 4)), elevation = 3)

    elevations = [
        [0, 1, 2, 3, 3],
        [1, 1, 2, 3, 3],
        [2, 2, 2, 3, 3],
        [3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3],
    ]

    assert [[tile.elevation for tile in row] for row in mm.terrain] == elevations
    mm.set_elevation(area = ((3, 3), (4, 4)), elevation = 1)

    elevations = [
        [0, 1, 2, 3, 3],
        [1, 1, 2, 3, 3],
        [2, 2, 2, 2, 2],
        [3, 3, 2, 1, 1],
        [3, 3, 2, 1, 1],
    ]

    assert [[tile.elevation for tile in row] for row in mm.terrain] == elevations
