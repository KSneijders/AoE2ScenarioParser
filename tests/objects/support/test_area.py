import pytest

from AoE2ScenarioParser.objects.support import Area, Tile


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


def test_center(area: Area):
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
    assert Area((2, 2), (4, 4)) == area.bound(4)
    assert Area((2, 2), (3, 4)) == Area((2, 2), (3, 6)).bound(4)
    assert Area((0, 0)) == Area((-1, -1)).bound(4)


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
