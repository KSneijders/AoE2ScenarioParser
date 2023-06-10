from unittest import TestCase

from AoE2ScenarioParser.objects.support import Area, Tile


class TestArea(TestCase):
    area: Area

    def setUp(self) -> None:
        self.area = Area((2, 2), (5, 6))

    def test_init(self):
        self.assertEqual(2, self.area.corner1.x)
        self.assertEqual(2, self.area.corner1.y)
        self.assertEqual(5, self.area.corner2.x)
        self.assertEqual(6, self.area.corner2.y)

        self.assertEqual(self.area, Area((2, 2), (5, 6)))
        self.assertEqual(Area((2, 3), (2, 3)), Area((2, 3)))

        self.assertEqual(Area((2, 2), (4, 4)), Area((4, 4), (2, 2)))

    def test_center(self):
        """Short test as the specific logic is tested within the Tile class"""
        self.assertEqual(Tile(4, 4), self.area.center_tile)

    def test_center_point(self):
        """Short test as the specific logic is tested within the Tile class"""
        self.assertEqual((3.5, 4.0), self.area.center_point)

    def test_width(self):
        self.assertEqual(4.0, self.area.width)

    def test_height(self):
        self.assertEqual(5.0, self.area.height)

    def test_dimensions(self):
        self.assertEqual((4.0, 5.0), self.area.dimensions)

    def test_resolve_negative_coords(self):
        self.area = Area((-4, -4), (-2, -2))
        self.assertEqual(Area((6, 6), (8, 8)), self.area.resolve_negative_coords(10))
        # self.area = Tile(-1, 5)
        # self.assertEqual(Tile(9, 5), self.area.resolve_negative_coords(10))

    def test_bound(self):
        self.assertEqual(Area((2, 2), (4, 4)), self.area.bound(4))
        self.assertEqual(Area((2, 2), (3, 4)), Area((2, 2), (3, 6)).bound(4))
        self.assertEqual(Area((0, 0)), Area((-1, -1)).bound(4))

    def test_contains(self):
        self.assertTrue(self.area.contains(Tile(2, 2)))
        self.assertTrue(self.area.contains(Tile(2, 6)))
        self.assertTrue(self.area.contains(Tile(5, 2)))
        self.assertTrue(self.area.contains(Tile(5, 6)))

        self.assertTrue(self.area.contains(Tile(4, 2)))
        self.assertTrue(self.area.contains(Tile(3, 3)))

        self.assertFalse(self.area.contains(Tile(2, 1)))
        self.assertFalse(self.area.contains(Tile(3, 7)))
        self.assertFalse(self.area.contains(Tile(6, 2)))

    def test__iter__(self):
        tiles = (self.area.corner1, self.area.corner2)
        for i, t in enumerate(self.area):
            self.assertIs(tiles[i], t)

    def test__getitem__(self):
        tiles = (self.area.corner1, self.area.corner2)
        for i in range(2):
            self.assertTrue(tiles[i], self.area[i])

    def test__eq__(self):
        self.assertEqual(self.area, Area((2, 2), (5, 6)))
        self.assertNotEqual(self.area, Area((2, 3), (5, 6)))

        self.assertEqual(Area((3, 3)), Area((3, 3), (3, 3)))
        self.assertEqual(((3, 4), (5, 6)), Area((3, 4), (5, 6)))

    def test_from_value(self):
        area = Area((0, 1), (0, 1))

        self.assertEqual(area, Area.from_value(Tile(0, 1)))
        self.assertEqual(area, Area.from_value((0, 1)))
        self.assertEqual(area, Area.from_value([0, 1]))
        self.assertEqual(area, Area.from_value({'a': 0, 'b': 1}))
        self.assertEqual(area, Area.from_value({'corner1': Tile(0, 1)}))

        area = Area((0, 1), (2, 3))
        self.assertEqual(area, Area.from_value(area))
        self.assertEqual(area, Area.from_value((Tile(0, 1), Tile(2, 3))))
        self.assertEqual(area, Area.from_value((0, 1, 2 , 3)))
        self.assertEqual(area, Area.from_value([0, 1, 2 , 3]))
        self.assertEqual(area, Area.from_value([Tile(0, 1), Tile(2, 3)]))
        self.assertEqual(area, Area.from_value([Tile(0, 1), Tile(2, 3)]))
        self.assertEqual(area, Area.from_value({'a': Tile(0, 1), 'b': Tile(2, 3)}))
        self.assertEqual(area, Area.from_value({'a': 0, 'b': 1, 'c': 2, 'd': 3}))
        self.assertEqual(area, Area.from_value({'corner1': Tile(0, 1), 'corner2': Tile(2, 3)}))
