import math
from unittest import TestCase

from AoE2ScenarioParser.objects.support import Tile


class TestTile(TestCase):
    tile: Tile

    def setUp(self) -> None:
        self.tile = Tile(3, 4)

    def test_from_i(self):
        self.tile = Tile.from_i(2, 10)
        self.assertEqual(2, self.tile.x)
        self.assertEqual(0, self.tile.y)

        self.tile = Tile.from_i(10, 10)
        self.assertEqual(0, self.tile.x)
        self.assertEqual(1, self.tile.y)

        self.tile = Tile.from_i(10, 8)
        self.assertEqual(2, self.tile.x)
        self.assertEqual(1, self.tile.y)

        self.assertRaises(ValueError, lambda: Tile.from_i(102, 10))

    def test_to_i(self):
        self.tile = Tile.from_i(2, 10)
        self.assertEqual(2, self.tile.to_i(10))

        self.tile = Tile.from_i(10, 10)
        self.assertEqual(10, self.tile.to_i(10))

        self.tile = Tile.from_i(10, 8)
        self.assertEqual(10, self.tile.to_i(8))

    def test_bound(self):
        self.assertEqual(self.tile, self.tile.bound(5))
        self.assertEqual(Tile(2, 2), self.tile.bound(2))

        self.tile = Tile(10, 4)
        self.assertEqual(Tile(6, 4), self.tile.bound(6))

    def test_resolve_negative_coords(self):
        self.tile = Tile(-1, -1)
        self.assertEqual(Tile(9, 9), self.tile.resolve_negative_coords(10))
        self.tile = Tile(-1, 5)
        self.assertEqual(Tile(9, 5), self.tile.resolve_negative_coords(10))

    def test_mid_tile(self):
        self.assertEqual(self.tile, self.tile.mid_tile(self.tile))

        self.assertEqual(Tile(3, 5), self.tile.mid_tile(Tile(3, 6)))
        self.assertEqual(Tile(5, 7), self.tile.mid_tile(Tile(7, 9)))
        self.assertEqual(Tile(4, 3), self.tile.mid_tile(Tile(5, 2)))
        self.assertEqual(Tile(2, 2), self.tile.mid_tile(Tile(0, 0)))

        self.assertEqual(Tile(3, 5), self.tile.mid_tile(Tile(3, 7), de_behaviour=False))
        self.assertEqual(Tile(3, 6), self.tile.mid_tile(Tile(3, 7), de_behaviour=True))

    def test_mid_point(self):
        self.assertEqual((1.5, 2.0), self.tile.mid_point(Tile(0, 0)))
        self.assertEqual((3.0, 5.0), self.tile.mid_point(Tile(3, 6)))
        self.assertEqual((4.5, 3.5), self.tile.mid_point(Tile(6, 3)))

    def test_dist(self):
        self.assertEqual(0.0, self.tile.dist(Tile(3, 4)))
        self.assertEqual(1.0, self.tile.dist(Tile(4, 4)))
        self.assertEqual(1.0, self.tile.dist(Tile(3, 3)))
        self.assertEqual(math.sqrt(2), self.tile.dist(Tile(2, 3)))

    def test_dist_taxicab(self):
        self.assertEqual(0.0, self.tile.dist_taxicab(Tile(3, 4)))
        self.assertEqual(1.0, self.tile.dist_taxicab(Tile(4, 4)))
        self.assertEqual(1.0, self.tile.dist_taxicab(Tile(3, 3)))
        self.assertEqual(2.0, self.tile.dist_taxicab(Tile(2, 3)))

    def test_from_value(self):
        tile = Tile(34, 4)

        self.assertIs(tile, Tile.from_value(tile))
        self.assertEqual(Tile(1, 2), Tile.from_value((1, 2)))
        self.assertEqual(Tile(1, 2), Tile.from_value([1, 2]))
        self.assertEqual(Tile(1, 2), Tile.from_value({'x': 1, 'y': 2}))
