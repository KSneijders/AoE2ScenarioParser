import math

import pytest

from AoE2ScenarioParser.objects.support import Point


@pytest.fixture
def point():
    return Point(3.25, 4.75)


def test_bound(point):
    assert point == point.bound(5)
    assert Point(2.0, 2.0) == point.bound(2)

    p = Point(10.0, 4.0)
    assert Point(6.0, 4.0) == p.bound(6)


def test_resolve_negative_coords(point):
    p = Point(-1.0, -1.0)
    assert Point(9.0, 9.0) == p.resolve_negative_coords(10)
    p = Point(-1.0, 5.0)
    assert Point(9.0, 5.0) == p.resolve_negative_coords(10)


def test_mid_point(point):
    assert point.mid_point(Point(0.5, 0.5)) == Point(1.875, 2.625)
    assert point.mid_point(Point(3.25, 6.75)) == Point(3.25, 5.75)
    assert point.mid_point(Point(6.75, 3.25)) == Point(5.0, 4.0)


def test_mid_tile(point):
    from AoE2ScenarioParser.objects.support import Tile

    assert Tile(3, 6) == point.mid_tile(Point(3.25, 7.25), de_behaviour=False)
    assert Tile(4, 6) == point.mid_tile(Point(3.25, 7.25), de_behaviour=True)


def test_dist(point):
    assert point.dist(Point(3.25, 4.75)) == 0.0
    assert point.dist(Point(4.25, 4.75)) == 1.0
    assert point.dist(Point(3.25, 3.75)) == 1.0
    assert point.dist(Point(2.25, 3.75)) == math.sqrt(2)


def test_dist_taxicab(point):
    assert point.dist_taxicab(Point(3.25, 4.75)) == 0.0
    assert point.dist_taxicab(Point(4.25, 4.75)) == 1.0
    assert point.dist_taxicab(Point(3.25, 3.75)) == 1.0
    assert point.dist_taxicab(Point(2.25, 3.75)) == 2.0


def test_from_value():
    p = Point(34.0, 4.0)

    assert p is Point.from_value(p)
    assert Point(1.0, 2.0) == Point.from_value((1.0, 2.0))
    assert Point(1.0, 2.0) == Point.from_value([1.0, 2.0])
    assert Point(1.0, 2.0) == Point.from_value({'x': 1.0, 'y': 2.0})


def test_is_within_bounds():
    # Without: resolve_negative_coords
    p = Point(34.0, 4.0)
    assert p.is_within_bounds(50) is True
    assert p.is_within_bounds(35) is True
    assert p.is_within_bounds(34) is False

    # With: resolve_negative_coords
    p = Point(-1.0, -20.0)
    assert p.is_within_bounds(50, resolve_negative_coords=True) is True
    assert p.is_within_bounds(35, resolve_negative_coords=True) is True
    assert p.is_within_bounds(19, resolve_negative_coords=True) is False
