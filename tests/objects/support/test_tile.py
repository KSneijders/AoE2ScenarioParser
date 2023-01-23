from unittest import TestCase

from AoE2ScenarioParser.objects.support import Tile


class TestUuidList(TestCase):
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

    def test_bound(self):
        self.assertEqual(self.tile, self.tile.bound(5))
        self.assertEqual(Tile(2, 2), self.tile.bound(2))

        self.tile = Tile(10, 4)
        self.assertEqual(Tile(6, 4), self.tile.bound(6))

    def test_resolve_negative_coords(self):
        self.assertEqual(self.tile, self.tile.resolve_negative_coords())

        self.tile = Tile(-1, -1)
        self.assertEqual(Tile(9, 9), self.tile.resolve_negative_coords(10))
        self.tile = Tile(-1, 5)
        self.assertEqual(Tile(9, 5), self.tile.resolve_negative_coords(10))

        self.assertRaises(ValueError, lambda: self.tile.resolve_negative_coords())

    def test_mid_tile(self):
        self.assertEqual(self.tile, self.tile.mid_tile(self.tile))
        # work in progress...
