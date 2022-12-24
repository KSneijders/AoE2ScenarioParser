from unittest import TestCase
from unittest.mock import Mock, patch

from AoE2ScenarioParser.objects.data_objects.terrain_tile import TerrainTile
from AoE2ScenarioParser.objects.support.area import TilePattern, AreaState, AreaAttr, Area
from AoE2ScenarioParser.objects.support.tile import Tile


class TestTilePattern(TestCase):
    tile_pattern: TilePattern

    def setUp(self) -> None:
        self.tile_pattern = TilePattern(map_size = 144)

    def test_select_entire_map(self):
        self.tile_pattern.select_entire_map()
        (x1, y1), (x2, y2) = self.tile_pattern.area
        self.assertEqual(0, x1)
        self.assertEqual(0, y1)
        self.assertEqual(self.tile_pattern._map_size, x2)
        self.assertEqual(self.tile_pattern._map_size, y2)

    def test_select(self):
        self.tile_pattern.select((10, 11), (20, 22))
        (x1, y1), (x2, y2) = self.tile_pattern.area
        self.assertEqual(10, x1)
        self.assertEqual(11, y1)
        self.assertEqual(20, x2)
        self.assertEqual(22, y2)

    def test_select_single_tile(self):
        self.tile_pattern.select((10, 22))
        (x1, y1), (x2, y2) = self.tile_pattern.area
        self.assertEqual(10, x1)
        self.assertEqual(22, y1)
        self.assertEqual(10, x2)
        self.assertEqual(22, y2)

    def test_select_negative_tiles(self):
        self.tile_pattern.select((1, 2), (-1, -2))
        (x1, y1), (x2, y2) = self.tile_pattern.area
        self.assertEqual(1, x1)
        self.assertEqual(2, y1)
        self.assertEqual(143, x2)
        self.assertEqual(142, y2)

    def test_select_single_negative_tile(self):
        self.tile_pattern.select((-1, -2))
        (x1, y1), (x2, y2) = self.tile_pattern.area
        self.assertEqual(143, x1)
        self.assertEqual(142, y1)
        self.assertEqual(143, x2)
        self.assertEqual(142, y2)

    def test_select_centered_odd(self):
        self.tile_pattern.select_centered((5, 5), dx=3, dy=5)
        (x1, y1), (x2, y2) = self.tile_pattern.area

        self.assertEqual(3, self.tile_pattern.area.width)
        self.assertEqual(5, self.tile_pattern.area.height)
        self.assertEqual(4, x1)
        self.assertEqual(3, y1)
        self.assertEqual(6, x2)
        self.assertEqual(7, y2)

    def test_select_centered_even(self):
        self.tile_pattern.select_centered((5, 5), dx=4, dy=6)
        (x1, y1), (x2, y2) = self.tile_pattern.area

        self.assertEqual(4, self.tile_pattern.area.width)
        self.assertEqual(6, self.tile_pattern.area.height)
        self.assertEqual(3, x1)
        self.assertEqual(2, y1)
        self.assertEqual(6, x2)
        self.assertEqual(7, y2)

    def test_select_centered_mixed(self):
        self.tile_pattern.select_centered((5, 5), dx=2, dy=5)
        (x1, y1), (x2, y2) = self.tile_pattern.area

        self.assertEqual(2, self.tile_pattern.area.width)
        self.assertEqual(5, self.tile_pattern.area.height)
        self.assertEqual(4, x1)
        self.assertEqual(3, y1)
        self.assertEqual(5, x2)
        self.assertEqual(7, y2)

    def test_shrink(self):
        self.tile_pattern.select((10, 11), (20, 22)).shrink_bottom_corner_by(dx=5)
        area = self.tile_pattern.area
        self.assertEqual(15, area.corner1.x)
        self.tile_pattern.shrink_bottom_corner_by(dx=10)
        self.assertEqual(20, area.corner1.x)
        self.tile_pattern.shrink_bottom_corner_by(dy=6)
        self.assertEqual(17, area.corner1.y)
        self.tile_pattern.shrink_top_corner_by(dx=3)
        self.assertEqual(20, area.corner2.x)
        self.tile_pattern.shrink_top_corner_by(dy=3)
        self.assertEqual(19, area.corner2.y)
        self.tile_pattern.shrink_top_corner_by(dy=8)
        self.assertEqual(17, area.corner2.y)

        self.tile_pattern.select((10, 11), (20, 22)).shrink(2)
        self.assertEqual(((12, 13), (18, 20)), self.tile_pattern.area)
        self.tile_pattern.shrink(1000)
        self.assertEqual(((18, 20), (18, 20)), self.tile_pattern.area)

    def test_expand(self):
        self.tile_pattern.select((10, 10), (20, 20)).expand_bottom_corner_by(dx=5)
        area = self.tile_pattern.area
        self.assertEqual(5, area.corner1.x)
        self.tile_pattern.expand_bottom_corner_by(dx=10)
        self.assertEqual(0, area.corner1.x)
        self.tile_pattern.expand_bottom_corner_by(dy=6)
        self.assertEqual(4, area.corner1.y)
        self.tile_pattern.expand_top_corner_by(dx=50)
        self.assertEqual(70, area.corner2.x)
        self.tile_pattern.expand_top_corner_by(dy=100)
        self.assertEqual(120, area.corner2.y)
        self.tile_pattern.expand_top_corner_by(dy=50)
        self.assertEqual(self.tile_pattern._map_size, area.corner2.y)

        self.tile_pattern.select((10, 10), (20, 20)).expand(2)
        self.assertEqual(((8, 8), (22, 22)), self.tile_pattern.area)
        self.tile_pattern.expand(500)
        self.assertEqual(((0, 0), (self.tile_pattern._map_size, self.tile_pattern._map_size)), self.tile_pattern.area)

    @patch('AoE2ScenarioParser.scenarios.scenario_store.getters.get_terrain')
    @patch('AoE2ScenarioParser.scenarios.scenario_store.getters.get_map_size', return_value=5)
    def test_to_coords_with_as_terrain(self, patched_get_map_size, patched_get_terrain):
        test_uuid = "TEST_UUID"
        mock_scx = Mock()
        mock_scx.uuid = test_uuid
        patched_get_terrain.return_value = terrain = [
            TerrainTile(_index = index, uuid = test_uuid) for index in range(pow(5, 2))
        ]
        self.tile_pattern.link_scenario(mock_scx)
        self.tile_pattern.select((1, 1), (2, 2))
        self.assertSetEqual(
            set(terrain[6:8] + terrain[11:13]),
            self.tile_pattern.to_coords(as_terrain=True)
        )

    def test_area_selection(self):
        self.assertEqual(((3, 3), (5, 5)), self.tile_pattern.select((3, 3), (5, 5)).area)

    def test_area_center(self):
        self.assertEqual(((8, 8), (8, 8)), self.tile_pattern.center((8, 8)).area)

        self.tile_pattern.select((3, 3), (5, 5))
        self.assertEqual((4, 4), self.tile_pattern.area.center)
        self.tile_pattern.select((3, 3), (6, 6))
        self.assertEqual((5, 5), self.tile_pattern.area.center)

        self.tile_pattern.select((3, 3), (5, 5)).center((8, 8))
        self.assertEqual((8, 8), self.tile_pattern.area.center)
        self.assertEqual(((7, 7), (9, 9)), self.tile_pattern.area)

        self.tile_pattern.select((5, 10), (20, 20)).center((5, 0))
        self.assertEqual(((-3, -5), (12, 5)), self.tile_pattern.area)
        self.assertEqual(((0, 0), (12, 5)), self.tile_pattern.area_bounded)

        self.tile_pattern.select((10, 10), (20, 20))
        w, h = self.tile_pattern.area.dimensions
        self.tile_pattern.center((0, 0)).center((20, 20))
        self.assertEqual((w, h), self.tile_pattern.area.dimensions)

        self.tile_pattern.select_centered((5, 5), dx=4, dy=4)
        self.assertEqual((5, 5), self.tile_pattern.area.center)

    def test_set_center_then_size(self):
        self.tile_pattern.center((8, 8)).size(9)
        self.assertEqual(((4, 4), (12, 12)), self.tile_pattern.area)

        self.tile_pattern.size(10)
        self.assertEqual(((3, 3), (12, 12)), self.tile_pattern.area)

        self.tile_pattern.center((5, 5)).size(300)
        self.assertEqual(((-145, -145), (154, 154)), self.tile_pattern.area)
        self.assertEqual(
            ((0, 0), (self.tile_pattern._map_size, self.tile_pattern._map_size)),
            self.tile_pattern.area_bounded
        )

    def test_set_size_then_center(self):
        self.tile_pattern = TilePattern(map_size = self.tile_pattern._map_size)
        self.tile_pattern.size(9).center((8, 8))
        self.assertEqual(((4, 4), (12, 12)), self.tile_pattern.area)

        # Set size should function like aoe2 'center on even size' logic
        self.tile_pattern.center((8, 8)).size(4)
        self.assertEqual(((6, 6), (9, 9)), self.tile_pattern.area)

    def test_area_height(self):
        self.tile_pattern.center((8, 8))
        self.tile_pattern.height(3)
        self.assertEqual(((8, 7), (8, 9)), self.tile_pattern.area)
        self.tile_pattern.height(10)
        self.assertEqual(((8, 3), (8, 12)), self.tile_pattern.area)
        self.tile_pattern.height(4)
        self.assertEqual(((8, 6), (8, 9)), self.tile_pattern.area)
        self.tile_pattern.height(1)
        self.assertEqual(((8, 8), (8, 8)), self.tile_pattern.area)

    def test_area_width(self):
        self.tile_pattern.center((8, 8))
        self.tile_pattern.width(6)
        self.assertEqual(((5, 8), (10, 8)), self.tile_pattern.area)
        self.tile_pattern.width(11)
        self.assertEqual(((3, 8), (13, 8)), self.tile_pattern.area)
        self.tile_pattern.width(8)
        self.assertEqual(((4, 8), (11, 8)), self.tile_pattern.area)
        self.tile_pattern.width(3)
        self.assertEqual(((7, 8), (9, 8)), self.tile_pattern.area)

    def test_area_use_full(self):
        self.tile_pattern.use_full()
        self.assertEqual(AreaState.FULL, self.tile_pattern.state)
        self.tile_pattern.use_only_edge().use_full()
        self.assertEqual(AreaState.FULL, self.tile_pattern.state)

        self.tile_pattern.select((3, 3), (5, 5))
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3),
                (3, 4), (4, 4), (5, 4),
                (3, 5), (4, 5), (5, 5),
            },
            self.tile_pattern.to_coords()
        )
        self.tile_pattern.shrink_bottom_corner_by(dx=1)
        self.assertSetEqual(
            {
                (4, 3), (5, 3),
                (4, 4), (5, 4),
                (4, 5), (5, 5),
            },
            self.tile_pattern.to_coords()
        )

        self.tile_pattern.invert()
        self.assertSetEqual(set(), self.tile_pattern.to_coords())

    def test_area_to_chunks(self):
        self.tile_pattern.select((3, 3), (5, 5))
        self.assertListEqual(
            [{
                (3, 3), (4, 3), (5, 3),
                (3, 4), (4, 4), (5, 4),
                (3, 5), (4, 5), (5, 5),
            }],
            self.tile_pattern.to_chunks()
        )

        self.tile_pattern.select(3, 3, 6, 7).use_pattern_lines(axis= "x")
        self.assertListEqual(
            [
                {(3, 3), (4, 3), (5, 3), (6, 3)},
                {(3, 5), (4, 5), (5, 5), (6, 5)},
                {(3, 7), (4, 7), (5, 7), (6, 7)},
            ],
            self.tile_pattern.to_chunks()
        )

        self.tile_pattern.select(3, 3, 7, 7).use_pattern_grid(block_size=2)
        self.assertListEqual(
            [
                {(3, 3), (4, 3), (3, 4), (4, 4)},
                {(6, 3), (7, 3), (6, 4), (7, 4)},
                {(3, 6), (4, 6), (3, 7), (4, 7)},
                {(6, 6), (7, 6), (6, 7), (7, 7)},
            ],
            self.tile_pattern.to_chunks()
        )

        self.tile_pattern.invert()
        self.assertListEqual(
            [{
                (5, 3),
                (5, 4),
                (3, 5), (4, 5), (5, 5), (6, 5), (7, 5),
                (5, 6),
                (5, 7),
            }],
            self.tile_pattern.to_chunks()
        )

    def test_area_to_chunks_order(self):
        self.tile_pattern.select(3, 3, 8, 8).use_pattern_grid(block_size=3, gap_size=1)
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
        for ords in self.tile_pattern.to_chunks():
            for tile in ords:
                self.assertEqual(tiles[index], tile)
                index += 1

    def test_area_get_chunk_id(self):
        self.tile_pattern.use_pattern_grid().select(1, 1, 5, 5)
        self.assertEqual(0, self.tile_pattern._get_chunk_id(Tile(1, 1)))
        self.assertEqual(4, self.tile_pattern._get_chunk_id(Tile(3, 3)))
        self.assertEqual(-1, self.tile_pattern._get_chunk_id(Tile(3, 4)))
        self.tile_pattern.attrs(gap_size=0)
        self.assertEqual(0, self.tile_pattern._get_chunk_id(Tile(1, 1)))
        self.assertEqual(12, self.tile_pattern._get_chunk_id(Tile(3, 3)))
        self.assertEqual(17, self.tile_pattern._get_chunk_id(Tile(3, 4)))

        self.tile_pattern.use_pattern_lines(axis= "y", gap_size=1)
        self.assertEqual(0, self.tile_pattern._get_chunk_id(Tile(1, 1)))
        self.assertEqual(-1, self.tile_pattern._get_chunk_id(Tile(2, 4)))
        self.assertEqual(2, self.tile_pattern._get_chunk_id(Tile(5, 3)))
        self.tile_pattern.attrs(gap_size=0)
        self.assertEqual(0, self.tile_pattern._get_chunk_id(Tile(1, 1)))
        self.assertEqual(1, self.tile_pattern._get_chunk_id(Tile(2, 4)))
        self.assertEqual(4, self.tile_pattern._get_chunk_id(Tile(5, 3)))

        self.tile_pattern.use_only_corners()
        self.assertEqual(0, self.tile_pattern._get_chunk_id(Tile(1, 1)))
        self.assertEqual(1, self.tile_pattern._get_chunk_id(Tile(5, 1)))
        self.assertEqual(2, self.tile_pattern._get_chunk_id(Tile(5, 5)))
        self.assertEqual(3, self.tile_pattern._get_chunk_id(Tile(1, 5)))
        self.assertEqual(-1, self.tile_pattern._get_chunk_id(Tile(5, 4)))

    def test_area_use_only_edge(self):
        self.tile_pattern.use_only_edge()
        self.assertEqual(AreaState.EDGE, self.tile_pattern.state)

        self.tile_pattern.select(3, 3, 6, 7)
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3),
                (3, 4), (6, 4),
                (3, 5), (6, 5),
                (3, 6), (6, 6),
                (3, 7), (4, 7), (5, 7), (6, 7),
            },
            self.tile_pattern.to_coords()
        )

        self.tile_pattern.select(3, 3, 8, 8).use_only_edge().attr(AreaAttr.LINE_WIDTH, 2)
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3),
                (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4),
                (3, 5), (4, 5), (7, 5), (8, 5),
                (3, 6), (4, 6), (7, 6), (8, 6),
                (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7),
                (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8),
            },
            self.tile_pattern.to_coords()
        )

        self.tile_pattern.invert()
        self.assertSetEqual(
            {
                (5, 5), (6, 5),
                (5, 6), (6, 6),
            },
            self.tile_pattern.to_coords()
        )

    def test_area_use_lines(self):
        self.tile_pattern.use_pattern_lines(axis= "y")
        self.assertEqual(AreaState.LINES, self.tile_pattern.state)

        self.tile_pattern.select(3, 3, 6, 7)
        self.assertSetEqual(
            {
                (3, 3), (5, 3),
                (3, 4), (5, 4),
                (3, 5), (5, 5),
                (3, 6), (5, 6),
                (3, 7), (5, 7),
            },
            self.tile_pattern.to_coords()
        )

        self.tile_pattern.use_pattern_lines(axis= "x")
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3),
                (3, 5), (4, 5), (5, 5), (6, 5),
                (3, 7), (4, 7), (5, 7), (6, 7),
            },
            self.tile_pattern.to_coords()
        )

        self.tile_pattern.use_pattern_lines(axis= "x", gap_size=2)
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3),
                (3, 6), (4, 6), (5, 6), (6, 6),
            },
            self.tile_pattern.to_coords()
        )

        self.tile_pattern.use_pattern_lines(axis= "x", gap_size=1, line_width=2)
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3),
                (3, 4), (4, 4), (5, 4), (6, 4),
                (3, 6), (4, 6), (5, 6), (6, 6),
                (3, 7), (4, 7), (5, 7), (6, 7),
            },
            self.tile_pattern.to_coords()
        )

    def test_area_use_grid(self):
        self.tile_pattern.use_pattern_grid()
        self.assertEqual(AreaState.GRID, self.tile_pattern.state)

        self.tile_pattern.select(3, 3, 6, 7)
        self.assertSetEqual(
            {
                (3, 3), (5, 3),
                (3, 5), (5, 5),
                (3, 7), (5, 7),
            },
            self.tile_pattern.to_coords()
        )

        self.tile_pattern.select(3, 3, 6, 7).invert()
        self.assertSetEqual(
            {
                (4, 3), (6, 3),
                (3, 4), (4, 4), (5, 4), (6, 4),
                (4, 5), (6, 5),
                (3, 6), (4, 6), (5, 6), (6, 6),
                (4, 7), (6, 7),
            },
            self.tile_pattern.to_coords()
        )

    def test_area_use_only_corners(self):
        self.tile_pattern.use_only_corners()
        self.assertEqual(AreaState.CORNERS, self.tile_pattern.state)

        self.tile_pattern.select(3, 3, 6, 7)
        self.assertSetEqual(
            {
                (3, 3), (6, 3),
                (3, 7), (6, 7),
            },
            self.tile_pattern.to_coords()
        )

        self.tile_pattern.attrs(corner_size=2)
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3),
                (3, 4), (4, 4), (5, 4), (6, 4),
                (3, 6), (4, 6), (5, 6), (6, 6),
                (3, 7), (4, 7), (5, 7), (6, 7),
            },
            self.tile_pattern.to_coords()
        )

        self.tile_pattern.attrs(corner_size_x=1, corner_size_y=2)
        self.assertSetEqual(
            {
                (3, 3), (6, 3),
                (3, 4), (6, 4),
                (3, 6), (6, 6),
                (3, 7), (6, 7),
            },
            self.tile_pattern.to_coords()
        )

    def test_area_attr_config(self):
        self.tile_pattern.attr('gap_size', 3)
        self.assertEqual(3, self.tile_pattern.gap_size_x)
        self.assertEqual(3, self.tile_pattern.gap_size_y)
        self.tile_pattern.attr(AreaAttr.GAP_SIZE_X, 4)
        self.assertEqual(4, self.tile_pattern.gap_size_x)
        self.assertEqual(3, self.tile_pattern.gap_size_y)
        self.tile_pattern.attr(AreaAttr.LINE_WIDTH, 10)
        self.assertEqual(10, self.tile_pattern.line_width_x)
        self.assertEqual(10, self.tile_pattern.line_width_y)
        self.tile_pattern.attr('line_width_x', 12)
        self.assertEqual(12, self.tile_pattern.line_width_x)
        self.assertEqual(10, self.tile_pattern.line_width_y)

    def test_area_attrs_kwarg_configs(self):
        self.tile_pattern.attrs(gap_size=3, line_width=4)
        self.assertEqual(3, self.tile_pattern.gap_size_x)
        self.assertEqual(3, self.tile_pattern.gap_size_y)
        self.assertEqual(4, self.tile_pattern.line_width_x)
        self.assertEqual(4, self.tile_pattern.line_width_y)

        self.tile_pattern.attrs(gap_size_x=1, gap_size_y=3, line_width_x=5, line_width_y=7)
        self.assertEqual(1, self.tile_pattern.gap_size_x)
        self.assertEqual(3, self.tile_pattern.gap_size_y)
        self.assertEqual(5, self.tile_pattern.line_width_x)
        self.assertEqual(7, self.tile_pattern.line_width_y)

        self.tile_pattern.attrs(gap_size=10, line_width_x=1, line_width_y=2)
        self.assertEqual(10, self.tile_pattern.gap_size_x)
        self.assertEqual(10, self.tile_pattern.gap_size_y)
        self.assertEqual(1, self.tile_pattern.line_width_x)
        self.assertEqual(2, self.tile_pattern.line_width_y)

        self.tile_pattern.attrs(gap_size_x=8, gap_size_y=11, line_width=10)
        self.assertEqual(8, self.tile_pattern.gap_size_x)
        self.assertEqual(11, self.tile_pattern.gap_size_y)
        self.assertEqual(10, self.tile_pattern.line_width_x)
        self.assertEqual(10, self.tile_pattern.line_width_y)

        self.tile_pattern.attrs(gap_size=11, gap_size_x=8, line_width=10, line_width_y=2)
        self.assertEqual(8, self.tile_pattern.gap_size_x)
        self.assertEqual(11, self.tile_pattern.gap_size_y)
        self.assertEqual(10, self.tile_pattern.line_width_x)
        self.assertEqual(2, self.tile_pattern.line_width_y)

    # -------------- test_area_use_grid_with_configs --------------

    def test_area_use_grid_with_configs(self):
        self.tile_pattern.select(3, 3, 6, 7).use_pattern_grid(gap_size=2)
        self.assertSetEqual(
            {
                (3, 3), (6, 3),
                (3, 6), (6, 6),
            },
            self.tile_pattern.to_coords()
        )

    def test_area_use_grid_with_configs_2(self):
        self.tile_pattern.select(3, 3, 6, 7).use_pattern_grid(block_size=2)
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (6, 3),
                (3, 4), (4, 4), (6, 4),
                (3, 6), (4, 6), (6, 6),
                (3, 7), (4, 7), (6, 7),
            },
            self.tile_pattern.to_coords()
        )

    def test_area_use_grid_with_configs_3(self):
        self.tile_pattern.select(3, 3, 6, 7).use_pattern_grid(block_size=2, gap_size=2)
        self.assertSetEqual(
            {
                (3, 3), (4, 3),
                (3, 4), (4, 4),
                (3, 7), (4, 7),
            },
            self.tile_pattern.to_coords()
        )

    # -------------- test_area_use_grid_with_configs_abuse_as_lines --------------

    def test_area_use_grid_with_configs_abuse_as_lines(self):
        self.tile_pattern.select(3, 3, 6, 7).use_pattern_grid(gap_size_y=0)
        self.assertSetEqual(
            {
                (3, 3), (5, 3),
                (3, 4), (5, 4),
                (3, 5), (5, 5),
                (3, 6), (5, 6),
                (3, 7), (5, 7),
            },
            self.tile_pattern.to_coords()
        )

    def test_area_use_grid_with_configs_abuse_as_lines2(self):
        self.tile_pattern.select(3, 3, 6, 7).use_pattern_grid(gap_size_x=0)
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3),

                (3, 5), (4, 5), (5, 5), (6, 5),

                (3, 7), (4, 7), (5, 7), (6, 7),
            },
            self.tile_pattern.to_coords()
        )

    def test_area_use_grid_with_configs_abuse_as_lines3(self):
        self.tile_pattern.select(3, 3, 6, 7).use_pattern_grid(gap_size_x=0, block_size_y=2)
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3),
                (3, 4), (4, 4), (5, 4), (6, 4),

                (3, 6), (4, 6), (5, 6), (6, 6),
                (3, 7), (4, 7), (5, 7), (6, 7),
            },
            self.tile_pattern.to_coords()
        )

    def test_area_get_x_range(self):
        self.tile_pattern.select(3, 4, 5, 6)
        self.assertEqual(range(3, 5 + 1), self.tile_pattern.get_range_x())

    def test_area_get_y_range(self):
        self.tile_pattern.select(3, 4, 5, 6)
        self.assertEqual(range(4, 6 + 1), self.tile_pattern.get_range_y())

    def test_area_get_width(self):
        self.tile_pattern.select(3, 5, 8, 11)
        self.assertEqual(6, self.tile_pattern.get_width())

    def test_area_get_height(self):
        self.tile_pattern.select(3, 5, 8, 11)
        self.assertEqual(7, self.tile_pattern.get_height())

    def test_area_is_within_selection(self):
        self.tile_pattern.select(3, 5, 8, 11)
        self.assertEqual(True, self.tile_pattern.is_within_selection(3, 5))
        self.assertEqual(True, self.tile_pattern.is_within_selection(8, 11))
        self.assertEqual(True, self.tile_pattern.is_within_selection(7, 7))
        self.assertEqual(False, self.tile_pattern.is_within_selection(2, 7))
        self.assertEqual(False, self.tile_pattern.is_within_selection(11, 7))
        self.assertEqual(False, self.tile_pattern.is_within_selection(5, 4))
        self.assertEqual(False, self.tile_pattern.is_within_selection(5, 13))

    def test_area_is_edge_tile(self):
        self.tile_pattern.select(3, 5, 8, 11).use_only_edge()
        self.assertEqual(True, self.tile_pattern.is_within_selection(3, 5))
        self.assertEqual(True, self.tile_pattern.is_within_selection(8, 11))
        self.assertEqual(True, self.tile_pattern.is_within_selection(3, 7))
        self.assertEqual(True, self.tile_pattern.is_within_selection(6, 5))
        self.assertEqual(False, self.tile_pattern.is_within_selection(5, 7))
        self.assertEqual(False, self.tile_pattern.is_within_selection(2, 10))
        self.assertEqual(False, self.tile_pattern.is_within_selection(4, 12))

    def test_area_axis(self):
        self.tile_pattern.along_axis("y")
        self.assertEqual("y", self.tile_pattern.axis)
        self.tile_pattern.use_pattern_lines(axis= "x")
        self.assertEqual("x", self.tile_pattern.axis)

    def test_area_copy(self):
        area2 = self.tile_pattern.copy()
        self.tile_pattern.select(1, 2, 3, 4)
        self.tile_pattern.attrs(line_width_x=5, line_width_y=6, gap_size_x=7, gap_size_y=8)
        self.tile_pattern.use_pattern_grid().invert()
        self.tile_pattern.map_size = 20
        self.tile_pattern.uuid = TEST_UUID  # Must match an actual UUID if you've set one
        self.tile_pattern.axis = "y"

        self.assertNotEqual(area2.x1, self.tile_pattern.x1)
        self.assertNotEqual(area2.y1, self.tile_pattern.y1)
        self.assertNotEqual(area2.x2, self.tile_pattern.x2)
        self.assertNotEqual(area2.y2, self.tile_pattern.y2)
        self.assertNotEqual(area2.line_width_x, self.tile_pattern.line_width_x)
        self.assertNotEqual(area2.line_width_y, self.tile_pattern.line_width_y)
        self.assertNotEqual(area2.gap_size_x, self.tile_pattern.gap_size_x)
        self.assertNotEqual(area2.gap_size_y, self.tile_pattern.gap_size_y)
        self.assertNotEqual(area2._map_size_value, self.tile_pattern._map_size_value)
        self.assertNotEqual(area2.uuid, self.tile_pattern.uuid)
        self.assertNotEqual(area2.state, self.tile_pattern.state)
        self.assertNotEqual(area2.inverted, self.tile_pattern.inverted)
        self.assertNotEqual(area2.axis, self.tile_pattern.axis)

    def test_area_instantiate_without_map_size(self):
        self.tile_pattern = Area(x1=0, y1=1, x2=2, y2=3)
        self.assertEqual(0, self.tile_pattern.x1)
        self.assertEqual(1, self.tile_pattern.y1)
        self.assertEqual(2, self.tile_pattern.x2)
        self.assertEqual(3, self.tile_pattern.y2)

        self.tile_pattern = Area(x1=0, y1=3)
        self.assertEqual(0, self.tile_pattern.x1)
        self.assertEqual(3, self.tile_pattern.y1)
        self.assertEqual(0, self.tile_pattern.x2)
        self.assertEqual(3, self.tile_pattern.y2)

    def test_map_size_functions_without_map_size(self):
        self.tile_pattern = Area(x1=10, y1=10, x2=12, y2=12)

        self.assertRaises(ValueError, lambda: self.tile_pattern.center_bounded(5, 5))
        self.assertRaises(ValueError, lambda: self.tile_pattern.select_entire_map())

        self.tile_pattern.width(5)
        self.assertEqual(9, self.tile_pattern.x1)
        self.assertEqual(10, self.tile_pattern.y1)
        self.assertEqual(13, self.tile_pattern.x2)
        self.assertEqual(12, self.tile_pattern.y2)

    def test_area_corners(self):
        self.tile_pattern = Area(x1=1, y1=2, corner1=Tile(3, 4))
        self.assertEqual(3, self.tile_pattern.x1)
        self.assertEqual(4, self.tile_pattern.y1)
        self.assertEqual(3, self.tile_pattern.x2)
        self.assertEqual(4, self.tile_pattern.y2)

        self.tile_pattern = Area(corner1=Tile(2, 4), corner2=Tile(6, 8))
        self.assertEqual(2, self.tile_pattern.x1)
        self.assertEqual(4, self.tile_pattern.y1)
        self.assertEqual(6, self.tile_pattern.x2)
        self.assertEqual(8, self.tile_pattern.y2)
        self.assertEqual(Tile(2, 4), self.tile_pattern.corner1)
        self.assertEqual(Tile(6, 8), self.tile_pattern.corner2)

        self.tile_pattern = Area(corner1=Tile(3, 5))
        self.assertEqual(3, self.tile_pattern.x1)
        self.assertEqual(5, self.tile_pattern.y1)
        self.assertEqual(3, self.tile_pattern.x2)
        self.assertEqual(5, self.tile_pattern.y2)
        self.assertEqual(Tile(3, 5), self.tile_pattern.corner1)
        self.assertEqual(Tile(3, 5), self.tile_pattern.corner2)

        self.tile_pattern.corner1 = Tile(10, 15)
        self.assertEqual(Tile(10, 15), self.tile_pattern.corner1)
        self.assertEqual(10, self.tile_pattern.x1)
        self.assertEqual(15, self.tile_pattern.y1)
        self.assertEqual(Tile(3, 5), self.tile_pattern.corner2)  # Should be unchanged
        self.assertEqual(3, self.tile_pattern.x2)  # Should be unchanged
        self.assertEqual(5, self.tile_pattern.y2)  # Should be unchanged

        self.tile_pattern.corner2 = Tile(20, 25)
        self.assertEqual(Tile(10, 15), self.tile_pattern.corner1)  # Should be unchanged
        self.assertEqual(10, self.tile_pattern.x1)  # Should be unchanged
        self.assertEqual(15, self.tile_pattern.y1)  # Should be unchanged
        self.assertEqual(Tile(20, 25), self.tile_pattern.corner2)
        self.assertEqual(20, self.tile_pattern.x2)
        self.assertEqual(25, self.tile_pattern.y2)
