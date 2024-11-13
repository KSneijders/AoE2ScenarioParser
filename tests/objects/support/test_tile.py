import math

import pytest

from AoE2ScenarioParser.objects.support import Tile


@pytest.fixture
def tile():
    return Tile(3, 4)


def test_from_i(tile):
    tile = Tile.from_i(2, 10)
    assert tile.x == 2
    assert tile.y == 0

    tile = Tile.from_i(10, 10)
    assert tile.x == 0
    assert tile.y == 1

    tile = Tile.from_i(10, 8)
    assert tile.x == 2
    assert tile.y == 1

    with pytest.raises(ValueError):
        Tile.from_i(102, 10)


def test_to_i(tile):
    tile = Tile.from_i(2, 10)
    assert tile.to_i(10) == 2

    tile = Tile.from_i(10, 10)
    assert tile.to_i(10) == 10

    tile = Tile.from_i(10, 8)
    assert tile.to_i(8) == 10


def test_bound(tile):
    assert tile == tile.bound(5)
    assert Tile(2, 2) == tile.bound(2)

    tile = Tile(10, 4)
    assert Tile(6, 4) == tile.bound(6)


def test_resolve_negative_coords(tile):
    tile = Tile(-1, -1)
    assert Tile(9, 9) == tile.resolve_negative_coords(10)
    tile = Tile(-1, 5)
    assert Tile(9, 5) == tile.resolve_negative_coords(10)


def test_mid_tile(tile):
    assert tile == tile.mid_tile(tile)

    assert Tile(3, 5) == tile.mid_tile(Tile(3, 6))
    assert Tile(5, 7) == tile.mid_tile(Tile(7, 9))
    assert Tile(4, 3) == tile.mid_tile(Tile(5, 2))
    assert Tile(2, 2) == tile.mid_tile(Tile(0, 0))

    assert Tile(3, 5) == tile.mid_tile(Tile(3, 7), de_behaviour = False)
    assert Tile(3, 6) == tile.mid_tile(Tile(3, 7), de_behaviour = True)


def test_mid_point(tile):
    assert tile.mid_point(Tile(0, 0)) == (1.5, 2.0)
    assert tile.mid_point(Tile(3, 6)) == (3.0, 5.0)
    assert tile.mid_point(Tile(6, 3)) == (4.5, 3.5)


def test_dist(tile):
    assert tile.dist(Tile(3, 4)) == 0.0
    assert tile.dist(Tile(4, 4)) == 1.0
    assert tile.dist(Tile(3, 3)) == 1.0
    assert tile.dist(Tile(2, 3)) == math.sqrt(2)


def test_dist_taxicab(tile):
    assert tile.dist_taxicab(Tile(3, 4)) == 0.0
    assert tile.dist_taxicab(Tile(4, 4)) == 1.0
    assert tile.dist_taxicab(Tile(3, 3)) == 1.0
    assert tile.dist_taxicab(Tile(2, 3)) == 2.0


def test_from_value():
    tile = Tile(34, 4)

    assert tile is Tile.from_value(tile)
    assert Tile(1, 2) == Tile.from_value((1, 2))
    assert Tile(1, 2) == Tile.from_value([1, 2])
    assert Tile(1, 2) == Tile.from_value({'x': 1, 'y': 2})


def test_is_within_bounds():
    # Without: resolve_negative_coords
    tile = Tile(34, 4)
    assert tile.is_within_bounds(50) is True
    assert tile.is_within_bounds(35) is True
    assert tile.is_within_bounds(34) is False

    # With: resolve_negative_coords
    tile = Tile(-1, -20)
    assert tile.is_within_bounds(50, resolve_negative_coords = True) is True
    assert tile.is_within_bounds(35, resolve_negative_coords = True) is True
    assert tile.is_within_bounds(19, resolve_negative_coords = True) is False
