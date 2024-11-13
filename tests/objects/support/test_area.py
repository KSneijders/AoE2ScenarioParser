import pytest

from AoE2ScenarioParser.objects.support import Area, Tile
from AoE2ScenarioParser.objects.support.enums.direction import Direction


@pytest.fixture
def area() -> Area:
    return Area((2, 2), (5, 6))


def test_init(area: Area):
    assert 2 == area.corner1.x
    assert 2 == area.corner1.y
    assert 5 == area.corner2.x
    assert 6 == area.corner2.y

    assert area == Area((2, 2), (5, 6))
    assert Area((2, 3), (2, 3)) == Area((2, 3))

    assert Area((2, 2), (4, 4)) == Area((4, 4), (2, 2))


def test_center_tile(area: Area):
    """Short test as the specific logic is tested within the Tile class"""
    assert Tile(4, 4) == area.center_tile


def test_center_point(area: Area):
    """Short test as the specific logic is tested within the Tile class"""
    assert (3.5, 4.0) == area.center_point


def test_width(area: Area):
    assert 4.0 == area.width


def test_height(area: Area):
    assert 5.0 == area.height


def test_dimensions(area: Area):
    assert (4.0, 5.0) == area.dimensions


def test_resolve_negative_coords(area: Area):
    area = Area((-4, -4), (-2, -2))
    assert Area((6, 6), (8, 8)) == area.resolve_negative_coords(10)


def test_bound(area: Area):
    assert area.bound(4) == Area((2, 2), (4, 4))
    assert Area((2, 2), (3, 6)).bound(4) == Area((2, 2), (3, 4))

    # Corner 1 and Corner 2 out of east bounds
    with pytest.raises(
        ValueError, match = 'Unable to bound area when area does not cover any tiles within given bounds'
    ):
        Area((-1, -2), (-2, -1)).bound(4)
    # Corner 1 and Corner 2 out of west bounds
    with pytest.raises(
        ValueError, match = 'Unable to bound area when area does not cover any tiles within given bounds'
    ):
        Area((5, 5), (6, 6)).bound(4)

    # Corner 1 out of east bounds
    assert Area((-1, -1), (3, 3)).bound(4) == Area((0, 0), (3, 3))
    # Corner 1 out of east bounds, Corner 2 out of west bounds
    assert Area((-1, -1), (3, 6)).bound(4) == Area((0, 0), (3, 4))


def test_contains(area: Area):
    assert area.contains(Tile(2, 2))
    assert area.contains(Tile(2, 6))
    assert area.contains(Tile(5, 2))
    assert area.contains(Tile(5, 6))

    assert area.contains(Tile(4, 2))
    assert area.contains(Tile(3, 3))

    assert not area.contains(Tile(2, 1))
    assert not area.contains(Tile(3, 7))
    assert not area.contains(Tile(6, 2))


def test_area_size(area: Area):
    area = area.size(3)
    assert ((3, 3), (5, 5)) == area.corners
    assert area.dimensions == (3, 3)

    area = area.size(width = 10)
    assert ((-1, 3), (8, 5)) == area.corners
    assert area.dimensions == (10, 3)

    area = area.size(height = 6)
    assert ((-1, 1), (8, 6)) == area.corners
    assert area.dimensions == (10, 6)

    area = area.size(size = 3, height = 7)
    assert ((3, 1), (5, 7)) == area.corners
    assert area.dimensions == (3, 7)

    area = area.size(size = 5, width = 4)
    assert ((2, 2), (5, 6)) == area.corners
    assert area.dimensions == (4, 5)

    # No changes to area when necessary
    area = Area((11, 11), (20, 20)).size(10)
    assert ((11, 11), (20, 20)) == area.corners
    assert area.dimensions == (10, 10)

    # No changes to area when necessary
    area = Area((12, 12), (20, 20)).size(9)
    assert ((12, 12), (20, 20)) == area.corners
    assert area.dimensions == (9, 9)


def test_move(area: Area):
    area = area.move(x_offset = 10)
    assert area.corners == ((12, 2), (15, 6))

    area = area.move(y_offset = 10)
    assert area.corners == ((12, 12), (15, 16))

    area = area.move(x_offset = -5, y_offset = -5)
    assert area.corners == ((7, 7), (10, 11))

    area = Area((3, 3), (5, 6)).move(x_offset = -5, y_offset = -5)
    assert area.corners == ((-2, -2), (0, 1))


def test_move_to(area: Area):
    dimensions = area.dimensions

    area = area.move_to(Tile(20, 20), Direction.NORTH)
    assert ((17, 20), (20, 24)) == area.corners
    assert dimensions == area.dimensions

    area = area.move_to(Tile(20, 20), Direction.EAST)
    assert ((17, 16), (20, 20)) == area.corners
    assert dimensions == area.dimensions

    area = area.move_to(Tile(20, 20), Direction.SOUTH)
    assert ((20, 16), (23, 20)) == area.corners
    assert dimensions == area.dimensions

    area = area.move_to(Tile(20, 20), Direction.WEST)
    assert ((20, 20), (23, 24)) == area.corners
    assert dimensions == area.dimensions

    with pytest.raises(ValueError, match = "Invalid tile: No negative coordinates allowed"):
        area.move_to(Tile(-5, -5), Direction.NORTH)


def test_shrink():
    area = Area((10, 11), (20, 22)).shrink_corner1_by(dx = 5)

    assert area.corner1.x == 15
    area = area.shrink_corner1_by(dx = 10)
    assert area.corner1.x == 20
    area = area.shrink_corner1_by(dy = 6)
    assert area.corner1.y == 17
    area = area.shrink_corner2_by(dx = 3)
    assert area.corner2.x == 20
    area = area.shrink_corner2_by(dy = 3)
    assert area.corner2.y == 19
    area = area.shrink_corner2_by(dy = 8)
    assert area.corner2.y == 17

    area = Area((10, 11), (20, 22)).shrink(2)
    assert area == ((12, 13), (18, 20))

    # Expect this to be in the center of the selection, not either corner
    area = area.shrink(1000)
    assert area == ((15, 17), (15, 17))


def test_expand():
    area = Area((10, 10), (20, 20)).expand_corner1_by(dx = 5)

    assert area.corner1.x == 5
    area = area.expand_corner1_by(dx = 10)
    assert area.corner1.x == -5
    area = area.expand_corner1_by(dy = 6)
    assert area.corner1.y == 4
    area = area.expand_corner2_by(dx = 50)
    assert area.corner2.x == 70
    area = area.expand_corner2_by(dy = 100)
    assert area.corner2.y == 120
    area = area.expand_corner2_by(dy = 50)
    assert area.corner2.y == 170

    area = Area((10, 10), (20, 20)).expand(2)
    assert area == ((8, 8), (22, 22))
    area = area.expand(500)
    assert area == ((-492, -492), (522, 522))


def test_center(area: Area):
    assert Area((0, 0)).center((8, 8)) == ((8, 8), (8, 8))

    area = Area((3, 3), (5, 5))
    assert area.center_tile == (4, 4)
    area = Area((3, 3), (6, 6))
    assert area.center_tile == (5, 5)

    area = Area((3, 3), (5, 5)).center((8, 8))
    assert area.center_tile == (8, 8)
    assert area == ((7, 7), (9, 9))

    area = Area((5, 10), (20, 20)).center((5, 0))
    assert area == ((-3, -5), (12, 5))

    # Repeating center(...) calls is not supposed to apply bounds
    area = Area((10, 10), (20, 20))
    w, h = area.dimensions
    area = area.center((0, 0)).center((20, 20))
    assert area.dimensions == (w, h)


def test__iter__(area: Area):
    tiles = (area.corner1, area.corner2)
    for i, t in enumerate(area):
        assert tiles[i] == t


def test__getitem__(area: Area):
    tiles = (area.corner1, area.corner2)
    for i in range(2):
        assert tiles[i] == area[i]


def test__eq__(area: Area):
    assert area == Area((2, 2), (5, 6))
    assert area != Area((2, 3), (5, 6))

    assert Area((3, 3)) == Area((3, 3), (3, 3))
    assert ((3, 4), (5, 6)) == Area((3, 4), (5, 6))


def test_from_value(area: Area):
    area = Area((0, 1), (0, 1))

    assert area == Area.from_value(Tile(0, 1))
    assert area == Area.from_value((0, 1))
    assert area == Area.from_value([0, 1])
    assert area == Area.from_value({'a': 0, 'b': 1})
    assert area == Area.from_value({'corner1': Tile(0, 1)})

    area = Area((0, 1), (2, 3))
    assert area == Area.from_value(area)
    assert area == Area.from_value((Tile(0, 1), Tile(2, 3)))
    assert area == Area.from_value((0, 1, 2, 3))
    assert area == Area.from_value([0, 1, 2, 3])
    assert area == Area.from_value([Tile(0, 1), Tile(2, 3)])
    assert area == Area.from_value([Tile(0, 1), Tile(2, 3)])
    assert area == Area.from_value({'a': Tile(0, 1), 'b': Tile(2, 3)})
    assert area == Area.from_value({'a': 0, 'b': 1, 'c': 2, 'd': 3})
    assert area == Area.from_value({'corner1': Tile(0, 1), 'corner2': Tile(2, 3)})
