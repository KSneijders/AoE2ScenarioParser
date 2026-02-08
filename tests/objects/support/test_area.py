from unittest import TestCase
from uuid import UUID

from AoE2ScenarioParser.objects.data_objects.terrain_tile import TerrainTile
from AoE2ScenarioParser.objects.support.area import Area, AreaState, AreaAttr
from AoE2ScenarioParser.objects.support.tile import Tile
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
        self.assertEqual(0, self.area._x1)
        self.assertEqual(0, self.area._y1)
        self.assertEqual(self.area.maximum_coordinate, self.area._x2)
        self.assertEqual(self.area.maximum_coordinate, self.area._y2)

    def test_area_select(self):
        self.area.select(10, 11, 20, 22)
        self.assertEqual(10, self.area.x1)
        self.assertEqual(11, self.area.y1)
        self.assertEqual(20, self.area.x2)
        self.assertEqual(22, self.area.y2)

        self.area.select(10, 22)
        self.assertEqual(10, self.area.x1)
        self.assertEqual(22, self.area.y1)
        self.assertEqual(10, self.area.x2)
        self.assertEqual(22, self.area.y2)

        self.area.select(1, 2, -1, -2)
        self.assertEqual(1, self.area.x1)
        self.assertEqual(2, self.area.y1)
        self.assertEqual(143, self.area.x2)
        self.assertEqual(142, self.area.y2)

        self.area.select(1, 2, -2)
        self.assertEqual(1, self.area.x1)
        self.assertEqual(2, self.area.y1)
        self.assertEqual(142, self.area.x2)
        self.assertEqual(2, self.area.y2)

        self.area.select(1, 2, y2=-2)
        self.assertEqual(1, self.area.x1)
        self.assertEqual(2, self.area.y1)
        self.assertEqual(1, self.area.x2)
        self.assertEqual(142, self.area.y2)

    def test_area_select_from_center(self):
        self.area.select_centered(5, 5, 3, 3)
        self.assertEqual(4, self.area.x1)
        self.assertEqual(4, self.area.y1)
        self.assertEqual(6, self.area.x2)
        self.assertEqual(6, self.area.y2)

        self.area.select_centered(5, 5, 4, 4)

        self.assertEqual(4, self.area.get_width())
        self.assertEqual(4, self.area.get_height())

        self.assertEqual(3, self.area.x1)
        self.assertEqual(3, self.area.y1)
        self.assertEqual(6, self.area.x2)
        self.assertEqual(6, self.area.y2)

        self.area.select_centered(5, 5, 2, 5)

        self.assertEqual(4, self.area.x1)
        self.assertEqual(3, self.area.y1)
        self.assertEqual(5, self.area.x2)
        self.assertEqual(7, self.area.y2)

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
        self.assertEqual(((12, 13), (18, 20)), self.area.get_selection())
        self.area.shrink(1000)  # ====== All ======
        self.assertEqual(((18, 20), (18, 20)), self.area.get_selection())

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
        self.assertEqual(self.area.map_size - 1, self.area.y2)

        map_size = self.area.map_size
        self.area.select(10, 10, 20, 20).expand(2)  # ====== All ======
        self.assertEqual(((8, 8), (22, 22)), self.area.get_selection())
        self.area.expand(500)
        self.assertEqual(((0, 0), (map_size - 1, map_size - 1)), self.area.get_selection())

    def test_area_to_terrain_tiles(self):
        self.area.associate_scenario(SCN)
        self.area.select(1, 1, 2, 2)
        self.assertSetEqual(
            set(MM.terrain[6:8] + MM.terrain[11:13]),
            self.area.to_coords(as_terrain=True)
        )

    def test_area_selection(self):
        self.assertEqual(((3, 3), (5, 5)), self.area.select(3, 3, 5, 5).get_selection())

    def test_area_center(self):
        self.assertEqual(((8, 8), (8, 8)), self.area.center(8, 8).get_selection())

        self.area.select(3, 3, 5, 5)
        self.assertEqual((4, 4), self.area.get_center())
        self.area.select(3, 3, 6, 6)
        self.assertEqual((4.5, 4.5), self.area.get_center())
        self.assertEqual((5, 5), self.area.get_center_int())

        self.area.select(3, 3, 5, 5).center(8, 8)
        self.assertEqual((8.0, 8.0), self.area.get_center())
        self.assertEqual(((7, 7), (9, 9)), self.area.get_selection())

        self.area.select(5, 10, 20, 20).center(5, 0)
        self.assertEqual((6.0, 2.5), self.area.get_center())
        self.assertEqual(((0, 0), (12, 5)), self.area.get_selection())

        self.area.select(10, 10, 20, 20)
        original_dimensions = self.area.get_dimensions()
        self.area.center(0, 0).center(20, 20)
        self.assertEqual(original_dimensions, self.area.get_dimensions())

        self.area.select_centered(5, 5, 4, 4)
        self.assertEqual((5, 5), self.area.get_center_int())

    def test_area_center_bound(self):
        self.area.select(3, 3, 5, 5).center_bounded(8, 8)
        self.assertEqual((8.0, 8.0), self.area.get_center())
        self.assertEqual(((7, 7), (9, 9)), self.area.get_selection())

        self.area.select(5, 10, 20, 20).center_bounded(5, 0)
        self.assertEqual((7.5, 5.0), self.area.get_center())
        self.assertEqual(((0, 0), (15, 10)), self.area.get_selection())

        max_ = self.area.maximum_coordinate
        self.area.select(100, 80, 130, 128)
        self.assertEqual((115, 104), self.area.get_center())
        self.area.center_bounded(140, 140)
        self.assertEqual((128, 119), self.area.get_center())
        self.assertEqual(((113, 95), (max_, max_)), self.area.get_selection())

    def test_area_size(self):
        self.area.center(8, 8).size(9)
        self.assertEqual(((4, 4), (12, 12)), self.area.get_selection())

        self.area.size(10)
        self.assertEqual(((3, 3), (12, 12)), self.area.get_selection())

        max_ = self.area.maximum_coordinate
        self.area.center(5, 5).size(300)
        self.assertEqual(((0, 0), (max_, max_)), self.area.get_selection())

        # Set size should also work when called first
        self.area = Area(self.area._map_size)
        self.area.size(9).center(8, 8)
        self.assertEqual(((4, 4), (12, 12)), self.area.get_selection())

        # Set size should function like aoe2 'center on even size' logic
        self.area.center(8, 8).size(4)
        self.assertEqual(((6, 6), (9, 9)), self.area.get_selection())

    def test_area_height(self):
        self.area.center(8, 8)
        self.area.height(3)
        self.assertEqual(((8, 7), (8, 9)), self.area.get_selection())
        self.area.height(10)
        self.assertEqual(((8, 3), (8, 12)), self.area.get_selection())
        self.area.height(4)
        self.assertEqual(((8, 6), (8, 9)), self.area.get_selection())
        self.area.height(1)
        self.assertEqual(((8, 8), (8, 8)), self.area.get_selection())

    def test_area_width(self):
        self.area.center(8, 8)
        self.area.width(6)
        self.assertEqual(((5, 8), (10, 8)), self.area.get_selection())
        self.area.width(11)  # increase 5
        self.assertEqual(((2, 8), (12, 8)), self.area.get_selection())
        self.area.width(8)  # decrease 3
        self.assertEqual(((4, 8), (11, 8)), self.area.get_selection())
        self.area.width(2)  # decrease 6
        self.assertEqual(((7, 8), (8, 8)), self.area.get_selection())
        self.area.width(6)  # increase 4
        self.assertEqual(((5, 8), (10, 8)), self.area.get_selection())

    def test_area_use_full(self):
        self.area.use_full()
        self.assertEqual(AreaState.FULL, self.area.state)
        self.area.use_only_edge().use_full()
        self.assertEqual(AreaState.FULL, self.area.state)

        self.area.select(3, 3, 5, 5)
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3),
                (3, 4), (4, 4), (5, 4),
                (3, 5), (4, 5), (5, 5),
            },
            self.area.to_coords()
        )
        self.area.shrink_x1(1)
        self.assertSetEqual(
            {
                (4, 3), (5, 3),
                (4, 4), (5, 4),
                (4, 5), (5, 5),
            },
            self.area.to_coords()
        )

        self.area.invert()
        self.assertSetEqual(set(), self.area.to_coords())

    def test_area_to_chunks(self):
        self.area.select(3, 3, 5, 5)
        self.assertListEqual(
            [{
                (3, 3), (4, 3), (5, 3),
                (3, 4), (4, 4), (5, 4),
                (3, 5), (4, 5), (5, 5),
            }],
            self.area.to_chunks()
        )

        self.area.select(3, 3, 6, 7).use_pattern_lines(axis="x")
        self.assertListEqual(
            [
                {(3, 3), (4, 3), (5, 3), (6, 3)},
                {(3, 5), (4, 5), (5, 5), (6, 5)},
                {(3, 7), (4, 7), (5, 7), (6, 7)},
            ],
            self.area.to_chunks()
        )

        self.area.select(3, 3, 7, 7).use_pattern_grid(block_size=2)
        self.assertListEqual(
            [
                {(3, 3), (4, 3), (3, 4), (4, 4)},
                {(6, 3), (7, 3), (6, 4), (7, 4)},
                {(3, 6), (4, 6), (3, 7), (4, 7)},
                {(6, 6), (7, 6), (6, 7), (7, 7)},
            ],
            self.area.to_chunks()
        )

        self.area.invert()
        self.assertListEqual(
            [{
                (5, 3),
                (5, 4),
                (3, 5), (4, 5), (5, 5), (6, 5), (7, 5),
                (5, 6),
                (5, 7),
            }],
            self.area.to_chunks()
        )

    def test_area_to_chunks_order(self):
        self.area.select(3, 3, 8, 8).use_pattern_grid(block_size=3, gap_size=1)
        tiles = [
            (3, 3), (4, 3), (5, 3),  # First (left top) block (3x3)
            (3, 4), (4, 4), (5, 4),
            (3, 5), (4, 5), (5, 5),
            (7, 3), (8, 3),  # Second (right top) block (2x3)
            (7, 4), (8, 4),
            (7, 5), (8, 5),
            (3, 7), (4, 7), (5, 7),  # Third (left bottom) block (3x2)
            (3, 8), (4, 8), (5, 8),
            (7, 7), (8, 7),  # Fourth (right bottom) block (2x2)
            (7, 8), (8, 8),
        ]

        index = 0
        for ords in self.area.to_chunks():
            for tile in ords:
                self.assertEqual(tiles[index], tile)
                index += 1

    def test_area_get_chunk_id(self):
        self.area.use_pattern_grid().select(1, 1, 5, 5)
        self.assertEqual(0, self.area._get_chunk_id(Tile(1, 1)))
        self.assertEqual(4, self.area._get_chunk_id(Tile(3, 3)))
        self.assertEqual(-1, self.area._get_chunk_id(Tile(3, 4)))
        self.area.attrs(gap_size=0)
        self.assertEqual(0, self.area._get_chunk_id(Tile(1, 1)))
        self.assertEqual(12, self.area._get_chunk_id(Tile(3, 3)))
        self.assertEqual(17, self.area._get_chunk_id(Tile(3, 4)))

        self.area.use_pattern_lines(axis="y", gap_size=1)
        self.assertEqual(0, self.area._get_chunk_id(Tile(1, 1)))
        self.assertEqual(-1, self.area._get_chunk_id(Tile(2, 4)))
        self.assertEqual(2, self.area._get_chunk_id(Tile(5, 3)))
        self.area.attrs(gap_size=0)
        self.assertEqual(0, self.area._get_chunk_id(Tile(1, 1)))
        self.assertEqual(1, self.area._get_chunk_id(Tile(2, 4)))
        self.assertEqual(4, self.area._get_chunk_id(Tile(5, 3)))

        self.area.use_only_corners()
        self.assertEqual(0, self.area._get_chunk_id(Tile(1, 1)))
        self.assertEqual(1, self.area._get_chunk_id(Tile(5, 1)))
        self.assertEqual(2, self.area._get_chunk_id(Tile(5, 5)))
        self.assertEqual(3, self.area._get_chunk_id(Tile(1, 5)))
        self.assertEqual(-1, self.area._get_chunk_id(Tile(5, 4)))

    def test_area_use_only_edge(self):
        self.area.use_only_edge()
        self.assertEqual(AreaState.EDGE, self.area.state)

        self.area.select(3, 3, 6, 7)
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3),
                (3, 4), (6, 4),
                (3, 5), (6, 5),
                (3, 6), (6, 6),
                (3, 7), (4, 7), (5, 7), (6, 7),
            },
            self.area.to_coords()
        )

        self.area.select(3, 3, 8, 8).use_only_edge().attr(AreaAttr.LINE_WIDTH, 2)
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3),
                (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4),
                (3, 5), (4, 5), (7, 5), (8, 5),
                (3, 6), (4, 6), (7, 6), (8, 6),
                (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7),
                (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8),
            },
            self.area.to_coords()
        )

        self.area.invert()
        self.assertSetEqual(
            {
                (5, 5), (6, 5),
                (5, 6), (6, 6),
            },
            self.area.to_coords()
        )

    def test_area_use_lines(self):
        self.area.use_pattern_lines(axis="y")
        self.assertEqual(AreaState.LINES, self.area.state)

        self.area.select(3, 3, 6, 7)
        self.assertSetEqual(
            {
                (3, 3), (5, 3),
                (3, 4), (5, 4),
                (3, 5), (5, 5),
                (3, 6), (5, 6),
                (3, 7), (5, 7),
            },
            self.area.to_coords()
        )

        self.area.use_pattern_lines(axis="x")
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3),
                (3, 5), (4, 5), (5, 5), (6, 5),
                (3, 7), (4, 7), (5, 7), (6, 7),
            },
            self.area.to_coords()
        )

        self.area.use_pattern_lines(axis="x", gap_size=2)
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3),
                (3, 6), (4, 6), (5, 6), (6, 6),
            },
            self.area.to_coords()
        )

        self.area.use_pattern_lines(axis="x", gap_size=1, line_width=2)
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3),
                (3, 4), (4, 4), (5, 4), (6, 4),
                (3, 6), (4, 6), (5, 6), (6, 6),
                (3, 7), (4, 7), (5, 7), (6, 7),
            },
            self.area.to_coords()
        )

    def test_area_use_grid(self):
        self.area.use_pattern_grid()
        self.assertEqual(AreaState.GRID, self.area.state)

        self.area.select(3, 3, 6, 7)
        self.assertSetEqual(
            {
                (3, 3), (5, 3),
                (3, 5), (5, 5),
                (3, 7), (5, 7),
            },
            self.area.to_coords()
        )

        self.area.select(3, 3, 6, 7).invert()
        self.assertSetEqual(
            {
                (4, 3), (6, 3),
                (3, 4), (4, 4), (5, 4), (6, 4),
                (4, 5), (6, 5),
                (3, 6), (4, 6), (5, 6), (6, 6),
                (4, 7), (6, 7),
            },
            self.area.to_coords()
        )

    def test_area_use_only_corners(self):
        self.area.use_only_corners()
        self.assertEqual(AreaState.CORNERS, self.area.state)

        self.area.select(3, 3, 6, 7)
        self.assertSetEqual(
            {
                (3, 3), (6, 3),
                (3, 7), (6, 7),
            },
            self.area.to_coords()
        )

        self.area.attrs(corner_size=2)
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3),
                (3, 4), (4, 4), (5, 4), (6, 4),
                (3, 6), (4, 6), (5, 6), (6, 6),
                (3, 7), (4, 7), (5, 7), (6, 7),
            },
            self.area.to_coords()
        )

        self.area.attrs(corner_size_x=1, corner_size_y=2)
        self.assertSetEqual(
            {
                (3, 3), (6, 3),
                (3, 4), (6, 4),
                (3, 6), (6, 6),
                (3, 7), (6, 7),
            },
            self.area.to_coords()
        )

    def test_area_attr_config(self):
        self.area.attr('gap_size', 3)
        self.assertEqual(3, self.area.gap_size_x)
        self.assertEqual(3, self.area.gap_size_y)
        self.area.attr(AreaAttr.GAP_SIZE_X, 4)
        self.assertEqual(4, self.area.gap_size_x)
        self.assertEqual(3, self.area.gap_size_y)
        self.area.attr(AreaAttr.LINE_WIDTH, 10)
        self.assertEqual(10, self.area.line_width_x)
        self.assertEqual(10, self.area.line_width_y)
        self.area.attr('line_width_x', 12)
        self.assertEqual(12, self.area.line_width_x)
        self.assertEqual(10, self.area.line_width_y)

    def test_area_attrs_kwarg_configs(self):
        self.area.attrs(gap_size=3, line_width=4)
        self.assertEqual(3, self.area.gap_size_x)
        self.assertEqual(3, self.area.gap_size_y)
        self.assertEqual(4, self.area.line_width_x)
        self.assertEqual(4, self.area.line_width_y)

        self.area.attrs(gap_size_x=1, gap_size_y=3, line_width_x=5, line_width_y=7)
        self.assertEqual(1, self.area.gap_size_x)
        self.assertEqual(3, self.area.gap_size_y)
        self.assertEqual(5, self.area.line_width_x)
        self.assertEqual(7, self.area.line_width_y)

        self.area.attrs(gap_size=10, line_width_x=1, line_width_y=2)
        self.assertEqual(10, self.area.gap_size_x)
        self.assertEqual(10, self.area.gap_size_y)
        self.assertEqual(1, self.area.line_width_x)
        self.assertEqual(2, self.area.line_width_y)

        self.area.attrs(gap_size_x=8, gap_size_y=11, line_width=10)
        self.assertEqual(8, self.area.gap_size_x)
        self.assertEqual(11, self.area.gap_size_y)
        self.assertEqual(10, self.area.line_width_x)
        self.assertEqual(10, self.area.line_width_y)

        self.area.attrs(gap_size=11, gap_size_x=8, line_width=10, line_width_y=2)
        self.assertEqual(8, self.area.gap_size_x)
        self.assertEqual(11, self.area.gap_size_y)
        self.assertEqual(10, self.area.line_width_x)
        self.assertEqual(2, self.area.line_width_y)

    # -------------- test_area_use_grid_with_configs --------------

    def test_area_use_grid_with_configs(self):
        self.area.select(3, 3, 6, 7).use_pattern_grid(gap_size=2)
        self.assertSetEqual(
            {
                (3, 3), (6, 3),
                (3, 6), (6, 6),
            },
            self.area.to_coords()
        )

    def test_area_use_grid_with_configs_2(self):
        self.area.select(3, 3, 6, 7).use_pattern_grid(block_size=2)
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (6, 3),
                (3, 4), (4, 4), (6, 4),
                (3, 6), (4, 6), (6, 6),
                (3, 7), (4, 7), (6, 7),
            },
            self.area.to_coords()
        )

    def test_area_use_grid_with_configs_3(self):
        self.area.select(3, 3, 6, 7).use_pattern_grid(block_size=2, gap_size=2)
        self.assertSetEqual(
            {
                (3, 3), (4, 3),
                (3, 4), (4, 4),
                (3, 7), (4, 7),
            },
            self.area.to_coords()
        )

    # -------------- test_area_use_grid_with_configs_abuse_as_lines --------------

    def test_area_use_grid_with_configs_abuse_as_lines(self):
        self.area.select(3, 3, 6, 7).use_pattern_grid(gap_size_y=0)
        self.assertSetEqual(
            {
                (3, 3), (5, 3),
                (3, 4), (5, 4),
                (3, 5), (5, 5),
                (3, 6), (5, 6),
                (3, 7), (5, 7),
            },
            self.area.to_coords()
        )

    def test_area_use_grid_with_configs_abuse_as_lines2(self):
        self.area.select(3, 3, 6, 7).use_pattern_grid(gap_size_x=0)
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3),

                (3, 5), (4, 5), (5, 5), (6, 5),

                (3, 7), (4, 7), (5, 7), (6, 7),
            },
            self.area.to_coords()
        )

    def test_area_use_grid_with_configs_abuse_as_lines3(self):
        self.area.select(3, 3, 6, 7).use_pattern_grid(gap_size_x=0, block_size_y=2)
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3),
                (3, 4), (4, 4), (5, 4), (6, 4),

                (3, 6), (4, 6), (5, 6), (6, 6),
                (3, 7), (4, 7), (5, 7), (6, 7),
            },
            self.area.to_coords()
        )

    def test_area_get_x_range(self):
        self.area.select(3, 4, 5, 6)
        self.assertEqual(range(3, 5 + 1), self.area.get_range_x())

    def test_area_get_y_range(self):
        self.area.select(3, 4, 5, 6)
        self.assertEqual(range(4, 6 + 1), self.area.get_range_y())

    def test_area_get_width(self):
        self.area.select(3, 5, 8, 11)
        self.assertEqual(6, self.area.get_width())

        self.area = Area(10)
        self.area.select(3, 4, 9, 9)
        self.assertEqual(7, self.area.get_width())

    def test_area_get_height(self):
        self.area.select(3, 5, 8, 11)
        self.assertEqual(7, self.area.get_height())

    def test_area_is_within_selection(self):
        self.area.select(3, 5, 8, 11)
        self.assertEqual(True, self.area.is_within_selection(3, 5))
        self.assertEqual(True, self.area.is_within_selection(8, 11))
        self.assertEqual(True, self.area.is_within_selection(7, 7))
        self.assertEqual(False, self.area.is_within_selection(2, 7))
        self.assertEqual(False, self.area.is_within_selection(11, 7))
        self.assertEqual(False, self.area.is_within_selection(5, 4))
        self.assertEqual(False, self.area.is_within_selection(5, 13))

    def test_area_is_within_bounds(self):
        self.area.select(0, 0, 10, 10)
        self.assertTrue(self.area.is_within_bounds())
        self.area.move(offset_x=-1)
        self.assertFalse(self.area.is_within_bounds())
        # Select exactly the right-most corner
        self.area.select_centered(140, 140, 7, 7)
        self.assertTrue(self.area.is_within_bounds())
        self.area.move(offset_x=1)
        self.assertFalse(self.area.is_within_bounds())
        self.area.move(offset_x=-1, offset_y=1)
        self.assertFalse(self.area.is_within_bounds())
        self.area.move(offset_y=-1)
        self.assertTrue(self.area.is_within_bounds())

    def test_area_is_edge_tile(self):
        self.area.select(3, 5, 8, 11).use_only_edge()
        self.assertEqual(True, self.area.is_within_selection(3, 5))
        self.assertEqual(True, self.area.is_within_selection(8, 11))
        self.assertEqual(True, self.area.is_within_selection(3, 7))
        self.assertEqual(True, self.area.is_within_selection(6, 5))
        self.assertEqual(False, self.area.is_within_selection(5, 7))
        self.assertEqual(False, self.area.is_within_selection(2, 10))
        self.assertEqual(False, self.area.is_within_selection(4, 12))

    def test_area_axis(self):
        self.area.along_axis("y")
        self.assertEqual("y", self.area.axis)
        self.area.use_pattern_lines(axis="x")
        self.assertEqual("x", self.area.axis)

    def test_area_copy(self):
        area2 = self.area.copy()
        self.area.select(1, 2, 3, 4)
        self.area.attrs(line_width_x=5, line_width_y=6, gap_size_x=7, gap_size_y=8)
        self.area.use_pattern_grid().invert()
        self.area.map_size = 20
        self.area.uuid = TEST_UUID  # Must match an actual UUID if you've set one
        self.area.axis = "y"

        self.assertNotEqual(area2.x1, self.area.x1)
        self.assertNotEqual(area2.y1, self.area.y1)
        self.assertNotEqual(area2.x2, self.area.x2)
        self.assertNotEqual(area2.y2, self.area.y2)
        self.assertNotEqual(area2.line_width_x, self.area.line_width_x)
        self.assertNotEqual(area2.line_width_y, self.area.line_width_y)
        self.assertNotEqual(area2.gap_size_x, self.area.gap_size_x)
        self.assertNotEqual(area2.gap_size_y, self.area.gap_size_y)
        self.assertNotEqual(area2._map_size_value, self.area._map_size_value)
        self.assertNotEqual(area2.uuid, self.area.uuid)
        self.assertNotEqual(area2.state, self.area.state)
        self.assertNotEqual(area2.inverted, self.area.inverted)
        self.assertNotEqual(area2.axis, self.area.axis)

    def test_area_move(self):
        self.area = Area(x1=0, y1=1, x2=2, y2=3)

        self.area.move(offset_x=10)
        self.assertEqual(10, self.area.x1)
        self.assertEqual(1, self.area.y1)
        self.assertEqual(12, self.area.x2)
        self.assertEqual(3, self.area.y2)

        self.area.move(offset_y=10)
        self.assertEqual(10, self.area.x1)
        self.assertEqual(11, self.area.y1)
        self.assertEqual(12, self.area.x2)
        self.assertEqual(13, self.area.y2)

        self.area.move(offset_x=-5, offset_y=-5)
        self.assertEqual(5, self.area.x1)
        self.assertEqual(6, self.area.y1)
        self.assertEqual(7, self.area.x2)
        self.assertEqual(8, self.area.y2)

    def test_area_move_to(self):
        self.area = Area(x1=0, y1=0, x2=3, y2=4)

        original_dimensions = self.area.get_dimensions()

        self.area.move_to(x=20, y=20, corner="north")
        self.assertTupleEqual(((17, 20), (20, 24)), self.area.get_selection())
        self.assertTupleEqual(original_dimensions, self.area.get_dimensions())

        self.area.move_to(x=20, y=20, corner="east")
        self.assertTupleEqual(((17, 16), (20, 20)), self.area.get_selection())
        self.assertTupleEqual(original_dimensions, self.area.get_dimensions())

        self.area.move_to(x=20, y=20, corner="south")
        self.assertTupleEqual(((20, 16), (23, 20)), self.area.get_selection())
        self.assertTupleEqual(original_dimensions, self.area.get_dimensions())

        self.area.move_to(x=20, y=20, corner="west")
        self.assertTupleEqual(((20, 20), (23, 24)), self.area.get_selection())
        self.assertTupleEqual(original_dimensions, self.area.get_dimensions())

    def test_area_instantiate_without_map_size(self):
        self.area = Area(x1=0, y1=1, x2=2, y2=3)
        self.assertEqual(0, self.area.x1)
        self.assertEqual(1, self.area.y1)
        self.assertEqual(2, self.area.x2)
        self.assertEqual(3, self.area.y2)

        self.area = Area(x1=0, y1=3)
        self.assertEqual(0, self.area.x1)
        self.assertEqual(3, self.area.y1)
        self.assertEqual(0, self.area.x2)
        self.assertEqual(3, self.area.y2)

    def test_map_size_functions_without_map_size(self):
        self.area = Area(x1=10, y1=10, x2=12, y2=12)

        self.assertRaises(ValueError, lambda: self.area.center_bounded(5, 5))
        self.assertRaises(ValueError, lambda: self.area.select_entire_map())

        self.area.width(5)
        self.assertEqual(9, self.area.x1)
        self.assertEqual(10, self.area.y1)
        self.assertEqual(13, self.area.x2)
        self.assertEqual(12, self.area.y2)

    def test_area_corners(self):
        self.area = Area(x1=1, y1=2, corner1=Tile(3, 4))
        self.assertEqual(3, self.area.x1)
        self.assertEqual(4, self.area.y1)
        self.assertEqual(3, self.area.x2)
        self.assertEqual(4, self.area.y2)

        self.area = Area(corner1=Tile(2, 4), corner2=Tile(6, 8))
        self.assertEqual(2, self.area.x1)
        self.assertEqual(4, self.area.y1)
        self.assertEqual(6, self.area.x2)
        self.assertEqual(8, self.area.y2)
        self.assertEqual(Tile(2, 4), self.area.corner1)
        self.assertEqual(Tile(6, 8), self.area.corner2)

        self.area = Area(corner1=Tile(3, 5))
        self.assertEqual(3, self.area.x1)
        self.assertEqual(5, self.area.y1)
        self.assertEqual(3, self.area.x2)
        self.assertEqual(5, self.area.y2)
        self.assertEqual(Tile(3, 5), self.area.corner1)
        self.assertEqual(Tile(3, 5), self.area.corner2)

        self.area.corner1 = Tile(10, 15)
        self.assertEqual(Tile(10, 15), self.area.corner1)
        self.assertEqual(10, self.area.x1)
        self.assertEqual(15, self.area.y1)
        self.assertEqual(Tile(3, 5), self.area.corner2)  # Should be unchanged
        self.assertEqual(3, self.area.x2)  # Should be unchanged
        self.assertEqual(5, self.area.y2)  # Should be unchanged

        self.area.corner2 = Tile(20, 25)
        self.assertEqual(Tile(10, 15), self.area.corner1)  # Should be unchanged
        self.assertEqual(10, self.area.x1)  # Should be unchanged
        self.assertEqual(15, self.area.y1)  # Should be unchanged
        self.assertEqual(Tile(20, 25), self.area.corner2)
        self.assertEqual(20, self.area.x2)
        self.assertEqual(25, self.area.y2)


# Mock Objects & Variables
TEST_UUID = "TEST_UUID"


class MM:
    """Mock object for map_manager"""
    map_size = 5
    terrain = [TerrainTile(_index=index, uuid=TEST_UUID) for index in range(pow(map_size, 2))]


class SCN:
    """Mock object for scenario"""
    map_manager = MM
    uuid: UUID = TEST_UUID
    name = "mock"
