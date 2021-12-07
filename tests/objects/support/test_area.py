from unittest import TestCase

from AoE2ScenarioParser.objects.data_objects.terrain_tile import TerrainTile
from AoE2ScenarioParser.objects.support.area import Area, Tile
from AoE2ScenarioParser.scenarios.scenario_store import store


class TestArea(TestCase):
    area: Area

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        store.register_scenario(SCN)

    def setUp(self) -> None:
        self.area = Area(144)

    def test_area_tile(self):
        tile = Tile(1, 3)
        self.assertEqual(1, tile.x)
        self.assertEqual(3, tile.y)
        self.assertEqual((1, 3), tile)

    def test_area_select_entire_map(self):
        self.area.select_entire_map()
        self.assertEqual(0, self.area.x1)
        self.assertEqual(0, self.area.y1)
        self.assertEqual(self.area._map_size, self.area.x2)
        self.assertEqual(self.area._map_size, self.area.y2)

    def test_area_select(self):
        self.area.select(10, 11, 20, 22)
        self.assertEqual(10, self.area.x1)
        self.assertEqual(11, self.area.y1)
        self.assertEqual(20, self.area.x2)
        self.assertEqual(22, self.area.y2)

    def test_area_shrink(self):
        self.area.select(10, 11, 20, 22).shrink_x1(5)  # ====== X1 ======
        self.assertEqual(15, self.area.x1)
        self.area.shrink_x1(10)
        self.assertEqual(20, self.area.x1)
        self.area.shrink_y1(6)  # ====== y1 ======
        self.assertEqual(17, self.area.y1)
        self.area.shrink_x2(3)  # ====== X2 ======
        self.assertEqual(20, self.area.x2)
        self.area.shrink_y2(3)  # ====== Y2 ======
        self.assertEqual(19, self.area.y2)
        self.area.shrink_y2(8)
        self.assertEqual(17, self.area.y2)

        self.area.select(10, 11, 20, 22).shrink(2)  # ====== All ======
        self.assertEqual(((12, 13), (18, 20)), self.area.selection)
        self.area.shrink(1000)  # ====== All ======
        self.assertEqual(((18, 20), (18, 20)), self.area.selection)

    def test_area_expand(self):
        self.area.select(10, 10, 20, 20).expand_x1(5)  # ====== X1 ======
        self.assertEqual(5, self.area.x1)
        self.area.expand_x1(10)
        self.assertEqual(0, self.area.x1)
        self.area.expand_y1(6)  # ====== y1 ======
        self.assertEqual(4, self.area.y1)
        self.area.expand_x2(50)  # ====== X2 ======
        self.assertEqual(70, self.area.x2)
        self.area.expand_y2(100)  # ====== Y2 ======
        self.assertEqual(120, self.area.y2)
        self.area.expand_y2(50)
        self.assertEqual(self.area._map_size, self.area.y2)

        self.area.select(10, 10, 20, 20).expand(2)  # ====== All ======
        self.assertEqual(((8, 8), (22, 22)), self.area.selection)
        self.area.expand(500)
        self.assertEqual(((0, 0), (self.area._map_size, self.area._map_size)), self.area.selection)

    def test_area_to_coords(self):
        self.area.select(3, 3, 5, 5)
        self.assertListEqual(
            [
                (3, 3), (4, 3), (5, 3),
                (3, 4), (4, 4), (5, 4),
                (3, 5), (4, 5), (5, 5),
            ],
            self.area.to_coords()
        )
        self.area.shrink_x1(1)
        self.assertListEqual(
            [
                (4, 3), (5, 3),
                (4, 4), (5, 4),
                (4, 5), (5, 5),
            ],
            self.area.to_coords()
        )
        # With edge is tested in separate test

    def test_area_to_terrain_tiles(self):
        self.area.associate_scenario(SCN)
        self.area.select(1, 1, 2, 2)
        self.assertListEqual(
            MM.terrain[6:8] + MM.terrain[11:13],
            self.area.to_terrain_tiles()
        )

    def test_area_selection(self):
        self.assertEqual(((3, 3), (5, 5)), self.area.select(3, 3, 5, 5).selection)

    def test_area_center(self):
        self.assertEqual(((8, 8), (8, 8)), self.area.set_center(8, 8).selection)

        self.area.select(3, 3, 5, 5)
        self.assertEqual((4, 4), self.area.center)
        self.area.select(3, 3, 6, 6)
        self.assertEqual((4.5, 4.5), self.area.center)
        self.assertEqual((4, 4), self.area.center_int)

    def test_area_set_center(self):
        self.area.select(3, 3, 5, 5).set_center(8, 8)
        self.assertEqual((8.0, 8.0), self.area.center)
        self.assertEqual(((7, 7), (9, 9)), self.area.selection)

        self.area.select(5, 10, 20, 20).set_center(5, 0)
        self.assertEqual((6.0, 2.5), self.area.center)
        self.assertEqual(((0, 0), (12, 5)), self.area.selection)

    def test_area_set_center_bound(self):
        self.area.select(3, 3, 5, 5).set_center_bounded(8, 8)
        self.assertEqual((8.0, 8.0), self.area.center)
        self.assertEqual(((7, 7), (9, 9)), self.area.selection)

        self.area.select(5, 10, 20, 20).set_center_bounded(5, 0)
        self.assertEqual((7.5, 5.0), self.area.center)
        self.assertEqual(((0, 0), (15, 10)), self.area.selection)

        self.area.select(100, 80, 130, 128).set_center_bounded(140, 140)
        self.assertEqual((128.0, 119.0), self.area.center)
        self.assertEqual(((113, 95), (self.area._map_size, self.area._map_size)), self.area.selection)

    def test_area_set_size(self):
        self.area.set_center(8, 8).set_size(9)
        self.assertEqual(((4, 4), (12, 12)), self.area.selection)

        self.area.set_size(10)
        self.assertEqual(((4, 4), (13, 13)), self.area.selection)

        self.area.set_center(5, 5).set_size(300)
        self.assertEqual(((0, 0), (self.area._map_size, self.area._map_size)), self.area.selection)

        # Set size should also work when called first
        self.area = Area(self.area._map_size)
        self.area.set_size(9).set_center(8, 8)
        self.assertEqual(((4, 4), (12, 12)), self.area.selection)

    def test_area_use_filled(self):
        self.area.use_filled()
        self.assertEqual(False, self.area.edge)

    def test_area_use_edge(self):
        self.area.use_edge()
        self.assertEqual(True, self.area.edge)

        self.area.select(3, 3, 6, 7)
        self.assertListEqual(
            [
                (3, 3), (4, 3), (5, 3), (6, 3),
                (3, 4), (6, 4),
                (3, 5), (6, 5),
                (3, 6), (6, 6),
                (3, 7), (4, 7), (5, 7), (6, 7),
            ],
            self.area.to_coords()
        )

        self.area.select(3, 3, 8, 8).use_edge().edge_width(2)
        self.assertListEqual(
            [
                (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3),
                (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4),
                (3, 5), (4, 5), (7, 5), (8, 5),
                (3, 6), (4, 6), (7, 6), (8, 6),
                (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7),
                (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8),
            ],
            self.area.to_coords()
        )

    def test_area_get_x_range(self):
        self.area.select(3, 4, 5, 6)
        self.assertEqual(range(3, 5 + 1), self.area.range_x)

    def test_area_get_y_range(self):
        self.area.select(3, 4, 5, 6)
        self.assertEqual(range(4, 6 + 1), self.area.range_y)

    def test_area_get_x_edge_length(self):
        self.area.select(3, 5, 8, 11)
        self.assertEqual(6, self.area.edge_length_x)

    def test_area_get_y_edge_length(self):
        self.area.select(3, 5, 8, 11)
        self.assertEqual(7, self.area.edge_length_y)

    def test_area_is_within_selection(self):
        self.area.select(3, 5, 8, 11)
        self.assertEqual(True, self.area.is_within_selection(3, 5))
        self.assertEqual(True, self.area.is_within_selection(8, 11))
        self.assertEqual(True, self.area.is_within_selection(7, 7))
        self.assertEqual(False, self.area.is_within_selection(2, 7))
        self.assertEqual(False, self.area.is_within_selection(11, 7))
        self.assertEqual(False, self.area.is_within_selection(5, 4))
        self.assertEqual(False, self.area.is_within_selection(5, 13))

    def test_area_is_edge_tile(self):
        self.area.select(3, 5, 8, 11).use_edge()
        self.assertEqual(True, self.area.is_within_selection(3, 5))
        self.assertEqual(True, self.area.is_within_selection(8, 11))
        self.assertEqual(True, self.area.is_within_selection(3, 7))
        self.assertEqual(True, self.area.is_within_selection(6, 5))
        self.assertEqual(False, self.area.is_within_selection(5, 7))
        self.assertEqual(False, self.area.is_within_selection(2, 10))
        self.assertEqual(False, self.area.is_within_selection(4, 12))


# Mock Objects & Variables
uuid = "cool_uuid"


class MM:
    """Mock object for map_manager"""
    map_size = 5
    terrain = [TerrainTile(_index=index, host_uuid=uuid) for index in range(pow(map_size, 2))]


class SCN:
    """Mock object for scenario"""
    map_manager = MM
    uuid: UUID = uuid
