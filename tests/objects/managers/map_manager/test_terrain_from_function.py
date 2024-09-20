from unittest import TestCase

from AoE2ScenarioParser.managers import MapManager
from AoE2ScenarioParser.objects.support import Tile
from objects.managers.map_manager import MockScxSecTestMM


class Test(TestCase):
    mm: MapManager

    def setUp(self) -> None:
        self.mm = MapManager(MockScxSecTestMM())

    def test_terrain_from_function_tile_args(self):
        terrain_3_3 = self.mm.get_tile(Tile(3, 3))
        terrain_1_1 = self.mm.get_tile(Tile(1, 1))
        terrain_4_3 = self.mm.get_tile(Tile(4, 3))

        tiles = self.mm.terrain_from(Tile(3, 3))
        self.assertEqual(len(tiles), 1)
        self.assertEqual(list(tiles.keys()), [Tile(3, 3)])
        self.assertIs(tiles[Tile(3, 3)], terrain_3_3)

        tiles = self.mm.terrain_from((Tile(1, 1), Tile(4, 3)))
        self.assertEqual(len(tiles), 2)
        self.assertEqual(list(tiles.keys()), [Tile(1, 1), Tile(4, 3)])
        self.assertIs(tiles[Tile(1, 1)], terrain_1_1)
        self.assertIs(tiles[Tile(4, 3)], terrain_4_3)
