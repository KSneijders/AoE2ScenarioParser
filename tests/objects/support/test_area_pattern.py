from unittest import TestCase
from unittest.mock import Mock, patch

from AoE2ScenarioParser.objects.support import Area
from AoE2ScenarioParser.objects.support.area_pattern import AreaPattern, AreaState, AreaAttr
from AoE2ScenarioParser.objects.support.tile import Tile


class TestAreaPattern(TestCase):
    area_pattern: AreaPattern

    def setUp(self) -> None:
        self.map_size = 144
        self.maximum_coordinate = self.map_size - 1
        self.area_pattern = AreaPattern(map_size=self.map_size)

    def test_select_entire_map(self):
        self.area_pattern.select_entire_map()
        (x1, y1), (x2, y2) = self.area_pattern.area
        self.assertEqual(0, x1)
        self.assertEqual(0, y1)
        self.assertEqual(self.maximum_coordinate, x2)
        self.assertEqual(self.maximum_coordinate, y2)

    def test_select(self):
        self.area_pattern.select((10, 11), (20, 22))
        (x1, y1), (x2, y2) = self.area_pattern.area
        self.assertEqual(10, x1)
        self.assertEqual(11, y1)
        self.assertEqual(20, x2)
        self.assertEqual(22, y2)

    def test_select_single_tile(self):
        self.area_pattern.select((10, 22))
        (x1, y1), (x2, y2) = self.area_pattern.area
        self.assertEqual(10, x1)
        self.assertEqual(22, y1)
        self.assertEqual(10, x2)
        self.assertEqual(22, y2)

    def test_select_negative_tiles(self):
        self.area_pattern.select((1, 2), (-1, -2))
        (x1, y1), (x2, y2) = self.area_pattern.area
        self.assertEqual(1, x1)
        self.assertEqual(2, y1)
        self.assertEqual(143, x2)
        self.assertEqual(142, y2)

    def test_select_single_negative_tile(self):
        self.area_pattern.select((-1, -2))
        (x1, y1), (x2, y2) = self.area_pattern.area
        self.assertEqual(143, x1)
        self.assertEqual(142, y1)
        self.assertEqual(143, x2)
        self.assertEqual(142, y2)

    def test_select_centered_odd(self):
        self.area_pattern.select_centered((5, 5), dx=3, dy=5)
        (x1, y1), (x2, y2) = self.area_pattern.area

        self.assertEqual(3, self.area_pattern.area.width)
        self.assertEqual(5, self.area_pattern.area.height)
        self.assertEqual(4, x1)
        self.assertEqual(3, y1)
        self.assertEqual(6, x2)
        self.assertEqual(7, y2)

    def test_select_centered_even(self):
        self.area_pattern.select_centered((5, 5), dx=4, dy=6)
        (x1, y1), (x2, y2) = self.area_pattern.area

        self.assertEqual(4, self.area_pattern.area.width)
        self.assertEqual(6, self.area_pattern.area.height)
        self.assertEqual(3, x1)
        self.assertEqual(2, y1)
        self.assertEqual(6, x2)
        self.assertEqual(7, y2)

    def test_select_centered_mixed(self):
        self.area_pattern.select_centered((5, 5), dx=2, dy=5)
        (x1, y1), (x2, y2) = self.area_pattern.area

        self.assertEqual(2, self.area_pattern.area.width)
        self.assertEqual(5, self.area_pattern.area.height)
        self.assertEqual(4, x1)
        self.assertEqual(3, y1)
        self.assertEqual(5, x2)
        self.assertEqual(7, y2)

    def test_shrink(self):
        self.area_pattern.select((10, 11), (20, 22)).shrink_bottom_corner_by(dx=5)
        area = self.area_pattern.area
        self.assertEqual(15, area.corner1.x)
        self.area_pattern.shrink_bottom_corner_by(dx=10)
        self.assertEqual(20, area.corner1.x)
        self.area_pattern.shrink_bottom_corner_by(dy=6)
        self.assertEqual(17, area.corner1.y)
        self.area_pattern.shrink_top_corner_by(dx=3)
        self.assertEqual(20, area.corner2.x)
        self.area_pattern.shrink_top_corner_by(dy=3)
        self.assertEqual(19, area.corner2.y)
        self.area_pattern.shrink_top_corner_by(dy=8)
        self.assertEqual(17, area.corner2.y)

        self.area_pattern.select((10, 11), (20, 22)).shrink(2)
        self.assertEqual(((12, 13), (18, 20)), self.area_pattern.area)
        self.area_pattern.shrink(1000)
        self.assertEqual(((18, 20), (18, 20)), self.area_pattern.area)

    def test_expand(self):
        self.area_pattern.select((10, 10), (20, 20)).expand_bottom_corner_by(dx=5)
        area = self.area_pattern.area
        self.assertEqual(5, area.corner1.x)
        self.area_pattern.expand_bottom_corner_by(dx=10)
        self.assertEqual(0, area.corner1.x)
        self.area_pattern.expand_bottom_corner_by(dy=6)
        self.assertEqual(4, area.corner1.y)
        self.area_pattern.expand_top_corner_by(dx=50)
        self.assertEqual(70, area.corner2.x)
        self.area_pattern.expand_top_corner_by(dy=100)
        self.assertEqual(120, area.corner2.y)
        self.area_pattern.expand_top_corner_by(dy=50)
        self.assertEqual(self.maximum_coordinate, area.corner2.y)

        self.area_pattern.select((10, 10), (20, 20)).expand(2)
        self.assertEqual(((8, 8), (22, 22)), self.area_pattern.area)
        self.area_pattern.expand(500)
        self.assertEqual(((0, 0), (self.maximum_coordinate, self.maximum_coordinate)), self.area_pattern.area)

    # Todo: Fix TerrainTile after it is implemented
    # @patch('AoE2ScenarioParser.scenarios.scenario_store.getters.get_terrain')
    # @patch('AoE2ScenarioParser.scenarios.scenario_store.getters.get_map_size', return_value=5)
    # def test_to_coords_with_as_terrain(self, patched_get_map_size, patched_get_terrain):
    #     test_uuid = "TEST_UUID"
    #     mock_scx = Mock()
    #     mock_scx.uuid = test_uuid
    #     patched_get_terrain.return_value = terrain = [
    #         TerrainTile(_index=index, uuid=test_uuid) for index in range(pow(5, 2))
    #     ]
    #     self.area_pattern.link_scenario(mock_scx)
    #     self.area_pattern.select((1, 1), (2, 2))
    #     self.assertSetEqual(
    #         set(terrain[6:8] + terrain[11:13]),
    #         self.area_pattern.to_coords(as_terrain=True)
    #     )

    def test_area_selection(self):
        self.assertEqual(((3, 3), (5, 5)), self.area_pattern.select((3, 3), (5, 5)).area)

    def test_area_center(self):
        self.assertEqual(((8, 8), (8, 8)), self.area_pattern.center((8, 8)).area)

        self.area_pattern.select((3, 3), (5, 5))
        self.assertEqual((4, 4), self.area_pattern.area.center_tile)
        self.area_pattern.select((3, 3), (6, 6))
        self.assertEqual((5, 5), self.area_pattern.area.center_tile)

        self.area_pattern.select((3, 3), (5, 5)).center((8, 8))
        self.assertEqual((8, 8), self.area_pattern.area.center_tile)
        self.assertEqual(((7, 7), (9, 9)), self.area_pattern.area)

        self.area_pattern.select((5, 10), (20, 20)).center((5, 0))
        self.assertEqual(((-3, -5), (12, 5)), self.area_pattern.area)
        self.assertEqual(((0, 0), (12, 5)), self.area_pattern.area_bounded)

        self.area_pattern.select((10, 10), (20, 20))
        w, h = self.area_pattern.area.dimensions
        self.area_pattern.center((0, 0)).center((20, 20))
        self.assertEqual((w, h), self.area_pattern.area.dimensions)

        self.area_pattern.select_centered((5, 5), dx=4, dy=4)
        self.assertEqual((5, 5), self.area_pattern.area.center_tile)

    def test_set_center_then_size(self):
        self.area_pattern.center((8, 8)).size(9)
        self.assertEqual(((4, 4), (12, 12)), self.area_pattern.area)

        self.area_pattern.size(10)
        self.assertEqual(((3, 3), (12, 12)), self.area_pattern.area)

        self.area_pattern.center((5, 5)).size(300)
        self.assertEqual(((-145, -145), (154, 154)), self.area_pattern.area)
        self.assertEqual(
            ((0, 0), (self.maximum_coordinate, self.maximum_coordinate)),
            self.area_pattern.area_bounded
        )

    def test_set_size_then_center(self):
        self.area_pattern = AreaPattern(map_size=self.area_pattern.map_size)
        self.area_pattern.size(9).center((8, 8))
        self.assertEqual(((4, 4), (12, 12)), self.area_pattern.area)

        # Set size should function like aoe2 'center on even size' logic
        self.area_pattern.center((8, 8)).size(4)
        self.assertEqual(((6, 6), (9, 9)), self.area_pattern.area)

    def test_area_height(self):
        self.area_pattern.center((8, 8))
        self.area_pattern.height(3)
        self.assertEqual(((8, 7), (8, 9)), self.area_pattern.area)
        self.area_pattern.height(10)
        self.assertEqual(((8, 3), (8, 12)), self.area_pattern.area)
        self.area_pattern.height(4)
        self.assertEqual(((8, 6), (8, 9)), self.area_pattern.area)
        self.area_pattern.height(1)
        self.assertEqual(((8, 8), (8, 8)), self.area_pattern.area)

    def test_area_width(self):
        self.area_pattern.center((8, 8))
        self.area_pattern.width(6)
        self.assertEqual(((5, 8), (10, 8)), self.area_pattern.area)
        self.area_pattern.width(11)
        self.assertEqual(((3, 8), (13, 8)), self.area_pattern.area)
        self.area_pattern.width(8)
        self.assertEqual(((4, 8), (11, 8)), self.area_pattern.area)
        self.area_pattern.width(3)
        self.assertEqual(((7, 8), (9, 8)), self.area_pattern.area)

    def test_area_use_full(self):
        self.area_pattern.use_full()
        self.assertEqual(AreaState.RECT, self.area_pattern.state)
        self.area_pattern.use_only_edge().use_full()
        self.assertEqual(AreaState.RECT, self.area_pattern.state)

        self.area_pattern.select((3, 3), (5, 5))
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3),
                (3, 4), (4, 4), (5, 4),
                (3, 5), (4, 5), (5, 5),
            },
            self.area_pattern.to_coords()
        )
        self.area_pattern.shrink_bottom_corner_by(dx=1)
        self.assertSetEqual(
            {
                (4, 3), (5, 3),
                (4, 4), (5, 4),
                (4, 5), (5, 5),
            },
            self.area_pattern.to_coords()
        )

        self.area_pattern.invert()
        self.assertSetEqual(set(), self.area_pattern.to_coords())

    def test_area_to_chunks(self):
        self.area_pattern.select((3, 3), (5, 5))
        self.assertListEqual(
            [{
                (3, 3), (4, 3), (5, 3),
                (3, 4), (4, 4), (5, 4),
                (3, 5), (4, 5), (5, 5),
            }],
            self.area_pattern.to_chunks()
        )

        self.area_pattern.select((3, 3), (6, 7)).use_pattern_lines(axis="x")
        # @formatter:off
        self.assertListEqual(
            [
                {(3, 3), (4, 3), (5, 3), (6, 3)},

                {(3, 5), (4, 5), (5, 5), (6, 5)},

                {(3, 7), (4, 7), (5, 7), (6, 7)},
            ],
            self.area_pattern.to_chunks()
        )
        # @formatter:on

        self.area_pattern.select((3, 3), (7, 7)).use_pattern_grid(block_size=2)
        # @formatter:off
        self.assertListEqual(
            [
                {
                    (3, 3), (4, 3),
                    (3, 4), (4, 4)
                },
                {
                    (6, 3), (7, 3),
                    (6, 4), (7, 4)
                },
                {
                    (3, 6), (4, 6),
                    (3, 7), (4, 7)
                },
                {
                    (6, 6), (7, 6),
                    (6, 7), (7, 7)
                },
            ],
            self.area_pattern.to_chunks()
        )
        # @formatter:on

        self.area_pattern.invert()
        # @formatter:off
        self.assertListEqual(
            [{
                                (5, 3),
                                (5, 4),
                (3, 5), (4, 5), (5, 5), (6, 5), (7, 5),
                                (5, 6),
                                (5, 7),
            }],
            self.area_pattern.to_chunks()
        )
        # @formatter:on

    def test_area_to_chunks_order(self):
        self.area_pattern.select((3, 3), (8, 8)).use_pattern_grid(block_size=3, gap_size=1)
        # @formatter:off
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
        # @formatter:on

        index = 0
        for ords in self.area_pattern.to_chunks():
            for tile in ords:
                self.assertEqual(tiles[index], tile)
                index += 1

    def test_area_get_chunk_id(self):
        self.area_pattern.use_pattern_grid().select((1, 1), (5, 5))
        self.assertEqual(0, self.area_pattern._get_chunk_id(Tile(1, 1)))
        self.assertEqual(4, self.area_pattern._get_chunk_id(Tile(3, 3)))
        self.assertEqual(-1, self.area_pattern._get_chunk_id(Tile(3, 4)))
        self.area_pattern.attrs(gap_size=0)
        self.assertEqual(0, self.area_pattern._get_chunk_id(Tile(1, 1)))
        self.assertEqual(12, self.area_pattern._get_chunk_id(Tile(3, 3)))
        self.assertEqual(17, self.area_pattern._get_chunk_id(Tile(3, 4)))

        self.area_pattern.use_pattern_lines(axis="y", gap_size=1)
        self.assertEqual(0, self.area_pattern._get_chunk_id(Tile(1, 1)))
        self.assertEqual(-1, self.area_pattern._get_chunk_id(Tile(2, 4)))
        self.assertEqual(2, self.area_pattern._get_chunk_id(Tile(5, 3)))
        self.area_pattern.attrs(gap_size=0)
        self.assertEqual(0, self.area_pattern._get_chunk_id(Tile(1, 1)))
        self.assertEqual(1, self.area_pattern._get_chunk_id(Tile(2, 4)))
        self.assertEqual(4, self.area_pattern._get_chunk_id(Tile(5, 3)))

        self.area_pattern.use_only_corners()
        self.assertEqual(0, self.area_pattern._get_chunk_id(Tile(1, 1)))
        self.assertEqual(1, self.area_pattern._get_chunk_id(Tile(5, 1)))
        self.assertEqual(2, self.area_pattern._get_chunk_id(Tile(5, 5)))
        self.assertEqual(3, self.area_pattern._get_chunk_id(Tile(1, 5)))
        self.assertEqual(-1, self.area_pattern._get_chunk_id(Tile(5, 4)))

    def test_area_use_only_edge(self):
        self.area_pattern.use_only_edge()
        self.assertEqual(AreaState.EDGE, self.area_pattern.state)

        self.area_pattern.select((3, 3), (6, 7))
        # @formatter:off
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3),
                (3, 4),                 (6, 4),
                (3, 5),                 (6, 5),
                (3, 6),                 (6, 6),
                (3, 7), (4, 7), (5, 7), (6, 7),
            },
            self.area_pattern.to_coords()
        )
        # @formatter:on

        self.area_pattern.select((3, 3), (8, 8)).use_only_edge().attr(AreaAttr.LINE_WIDTH, 2)
        # @formatter:off
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3),
                (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4),
                (3, 5), (4, 5),                 (7, 5), (8, 5),
                (3, 6), (4, 6),                 (7, 6), (8, 6),
                (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7),
                (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8),
            },
            self.area_pattern.to_coords()
        )
        # @formatter:on

        self.area_pattern.invert()
        self.assertSetEqual(
            {
                (5, 5), (6, 5),
                (5, 6), (6, 6),
            },
            self.area_pattern.to_coords()
        )

    def test_area_use_lines(self):
        self.area_pattern.use_pattern_lines(axis="y")
        self.assertEqual(AreaState.LINES, self.area_pattern.state)

        self.area_pattern.select((3, 3), (6, 7))
        # @formatter:off
        self.assertSetEqual(
            {
                (3, 3),         (5, 3),
                (3, 4),         (5, 4),
                (3, 5),         (5, 5),
                (3, 6),         (5, 6),
                (3, 7),         (5, 7),
            },
            self.area_pattern.to_coords()
        )
        # @formatter:on

        self.area_pattern.use_pattern_lines(axis="x")
        # @formatter:off
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3),

                (3, 5), (4, 5), (5, 5), (6, 5),

                (3, 7), (4, 7), (5, 7), (6, 7),
            },
            self.area_pattern.to_coords()
        )
        # @formatter:on

        self.area_pattern.use_pattern_lines(axis="x", gap_size=2)
        # @formatter:off
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3),


                (3, 6), (4, 6), (5, 6), (6, 6),
            },
            self.area_pattern.to_coords()
        )
        # @formatter:on

        self.area_pattern.use_pattern_lines(axis="x", gap_size=1, line_width=2)
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3),
                (3, 4), (4, 4), (5, 4), (6, 4),
                (3, 6), (4, 6), (5, 6), (6, 6),
                (3, 7), (4, 7), (5, 7), (6, 7),
            },
            self.area_pattern.to_coords()
        )

    def test_area_use_grid(self):
        self.area_pattern.use_pattern_grid()
        self.assertEqual(AreaState.GRID, self.area_pattern.state)

        self.area_pattern.select((3, 3), (6, 7))
        # @formatter:off
        self.assertSetEqual(
            {
                (3, 3),        (5, 3),

                (3, 5),        (5, 5),

                (3, 7),        (5, 7),
            },
            self.area_pattern.to_coords()
        )
        # @formatter:on

        self.area_pattern.select((3, 3), (6, 7)).invert()
        # @formatter:off
        self.assertSetEqual(
            {
                        (4, 3),         (6, 3),
                (3, 4), (4, 4), (5, 4), (6, 4),
                        (4, 5),         (6, 5),
                (3, 6), (4, 6), (5, 6), (6, 6),
                        (4, 7),         (6, 7),
            },
            self.area_pattern.to_coords()
        )
        # @formatter:on

    def test_area_use_only_corners(self):
        self.area_pattern.use_only_corners()
        self.assertEqual(AreaState.CORNERS, self.area_pattern.state)

        self.area_pattern.select((3, 3), (6, 7))
        # @formatter:off
        self.assertSetEqual(
            {
                (3, 3),                 (6, 3),



                (3, 7),                 (6, 7),
            },
            self.area_pattern.to_coords()
        )
        # @formatter:on

        self.area_pattern.attrs(corner_size=2)
        # @formatter:off
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3),
                (3, 4), (4, 4), (5, 4), (6, 4),

                (3, 6), (4, 6), (5, 6), (6, 6),
                (3, 7), (4, 7), (5, 7), (6, 7),
            },
            self.area_pattern.to_coords()
        )
        # @formatter:on

        self.area_pattern.attrs(corner_size_x=1, corner_size_y=2)
        # @formatter:off
        self.assertSetEqual(
            {
                (3, 3),                 (6, 3),
                (3, 4),                 (6, 4),
                (3, 6),                 (6, 6),
                (3, 7),                 (6, 7),
            },
            self.area_pattern.to_coords()
        )
        # @formatter:on

    def test_area_attr_config(self):
        self.area_pattern.attr('gap_size', 3)
        self.assertEqual(3, self.area_pattern.gap_size_x)
        self.assertEqual(3, self.area_pattern.gap_size_y)
        self.area_pattern.attr(AreaAttr.GAP_SIZE_X, 4)
        self.assertEqual(4, self.area_pattern.gap_size_x)
        self.assertEqual(3, self.area_pattern.gap_size_y)
        self.area_pattern.attr(AreaAttr.LINE_WIDTH, 10)
        self.assertEqual(10, self.area_pattern.line_width_x)
        self.assertEqual(10, self.area_pattern.line_width_y)
        self.area_pattern.attr('line_width_x', 12)
        self.assertEqual(12, self.area_pattern.line_width_x)
        self.assertEqual(10, self.area_pattern.line_width_y)

    def test_area_attrs_kwarg_configs(self):
        self.area_pattern.attrs(gap_size=3, line_width=4)
        self.assertEqual(3, self.area_pattern.gap_size_x)
        self.assertEqual(3, self.area_pattern.gap_size_y)
        self.assertEqual(4, self.area_pattern.line_width_x)
        self.assertEqual(4, self.area_pattern.line_width_y)

        self.area_pattern.attrs(gap_size_x=1, gap_size_y=3, line_width_x=5, line_width_y=7)
        self.assertEqual(1, self.area_pattern.gap_size_x)
        self.assertEqual(3, self.area_pattern.gap_size_y)
        self.assertEqual(5, self.area_pattern.line_width_x)
        self.assertEqual(7, self.area_pattern.line_width_y)

        self.area_pattern.attrs(gap_size=10, line_width_x=1, line_width_y=2)
        self.assertEqual(10, self.area_pattern.gap_size_x)
        self.assertEqual(10, self.area_pattern.gap_size_y)
        self.assertEqual(1, self.area_pattern.line_width_x)
        self.assertEqual(2, self.area_pattern.line_width_y)

        self.area_pattern.attrs(gap_size_x=8, gap_size_y=11, line_width=10)
        self.assertEqual(8, self.area_pattern.gap_size_x)
        self.assertEqual(11, self.area_pattern.gap_size_y)
        self.assertEqual(10, self.area_pattern.line_width_x)
        self.assertEqual(10, self.area_pattern.line_width_y)

        self.area_pattern.attrs(gap_size=11, gap_size_x=8, line_width=10, line_width_y=2)
        self.assertEqual(8, self.area_pattern.gap_size_x)
        self.assertEqual(11, self.area_pattern.gap_size_y)
        self.assertEqual(10, self.area_pattern.line_width_x)
        self.assertEqual(2, self.area_pattern.line_width_y)

    # -------------- test_area_use_grid_with_configs --------------

    def test_area_use_grid_with_configs(self):
        self.area_pattern.select((3, 3), (6, 7)).use_pattern_grid(gap_size=2)
        # @formatter:off
        self.assertSetEqual(
            {
                (3, 3),                 (6, 3),
                (3, 6),                 (6, 6),
            },
            self.area_pattern.to_coords()
        )
        # @formatter:on

    def test_area_use_grid_with_configs_2(self):
        self.area_pattern.select((3, 3), (6, 7)).use_pattern_grid(block_size=2)
        # @formatter:off
        self.assertSetEqual(
            {
                (3, 3), (4, 3),         (6, 3),
                (3, 4), (4, 4),         (6, 4),

                (3, 6), (4, 6),         (6, 6),
                (3, 7), (4, 7),         (6, 7),
            },
            self.area_pattern.to_coords()
        )
        # @formatter:on

    def test_area_use_grid_with_configs_3(self):
        self.area_pattern.select((3, 3), (6, 7)).use_pattern_grid(block_size=2, gap_size=2)
        # @formatter:off
        self.assertSetEqual(
            {
                (3, 3), (4, 3),
                (3, 4), (4, 4),


                (3, 7), (4, 7),
            },
            self.area_pattern.to_coords()
        )
        # @formatter:on

    # -------------- test_area_use_grid_with_configs_abuse_as_lines --------------

    def test_area_use_grid_with_configs_abuse_as_lines(self):
        self.area_pattern.select((3, 3), (6, 7)).use_pattern_grid(gap_size_y=0)
        # @formatter:off
        self.assertSetEqual(
            {
                (3, 3),        (5, 3),
                (3, 4),        (5, 4),
                (3, 5),        (5, 5),
                (3, 6),        (5, 6),
                (3, 7),        (5, 7),
            },
            self.area_pattern.to_coords()
        )
        # @formatter:on

    def test_area_use_grid_with_configs_abuse_as_lines2(self):
        self.area_pattern.select((3, 3), (6, 7)).use_pattern_grid(gap_size_x=0)
        # @formatter:off
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3),

                (3, 5), (4, 5), (5, 5), (6, 5),

                (3, 7), (4, 7), (5, 7), (6, 7),
            },
            self.area_pattern.to_coords()
        )
        # @formatter:on

    def test_area_use_grid_with_configs_abuse_as_lines3(self):
        self.area_pattern.select((3, 3), (6, 7)).use_pattern_grid(gap_size_x=0, block_size_y=2)
        # @formatter:off
        self.assertSetEqual(
            {
                (3, 3), (4, 3), (5, 3), (6, 3),
                (3, 4), (4, 4), (5, 4), (6, 4),

                (3, 6), (4, 6), (5, 6), (6, 6),
                (3, 7), (4, 7), (5, 7), (6, 7),
            },
            self.area_pattern.to_coords()
        )
        # @formatter:on

    def test_area_is_within_selection(self):
        self.area_pattern.select((3, 5), (8, 11))
        self.assertEqual(True, self.area_pattern.is_within_selection((3, 5)))
        self.assertEqual(True, self.area_pattern.is_within_selection((8, 11)))
        self.assertEqual(True, self.area_pattern.is_within_selection((7, 7)))
        self.assertEqual(False, self.area_pattern.is_within_selection((2, 7)))
        self.assertEqual(False, self.area_pattern.is_within_selection((11, 7)))
        self.assertEqual(False, self.area_pattern.is_within_selection((5, 4)))
        self.assertEqual(False, self.area_pattern.is_within_selection((5, 13)))

    def test_area_is_within_bounds(self):
        self.area_pattern.select((0, 0), (10, 10))
        self.assertEqual(True, self.area_pattern.is_within_bounds())
        self.area_pattern.move(offset_x=-1)
        self.assertEqual(False, self.area_pattern.is_within_bounds())
        # Select exactly the right-most corner
        self.area_pattern.select_centered((139, 139), dx=7, dy=7)
        self.assertEqual(True, self.area_pattern.is_within_bounds())
        self.area_pattern.move(offset_x=1)
        self.assertEqual(False, self.area_pattern.is_within_bounds())
        self.area_pattern.move(offset_x=-1, offset_y=1)
        self.assertEqual(False, self.area_pattern.is_within_bounds())

    def test_area_is_edge_tile(self):
        self.area_pattern.select((3, 5), (8, 11)).use_only_edge()
        self.assertEqual(True, self.area_pattern.is_within_selection((3, 5)))
        self.assertEqual(True, self.area_pattern.is_within_selection((8, 11)))
        self.assertEqual(True, self.area_pattern.is_within_selection((3, 7)))
        self.assertEqual(True, self.area_pattern.is_within_selection((6, 5)))
        self.assertEqual(False, self.area_pattern.is_within_selection((5, 7)))
        self.assertEqual(False, self.area_pattern.is_within_selection((2, 10)))
        self.assertEqual(False, self.area_pattern.is_within_selection((4, 12)))

    def test_area_invert(self):
        self.area_pattern.invert()
        self.assertEqual(True, self.area_pattern.inverted)
        self.area_pattern.invert()
        self.assertEqual(False, self.area_pattern.inverted)

    def test_area_axis(self):
        self.area_pattern.along_axis("y")
        self.assertEqual("y", self.area_pattern.axis)
        self.area_pattern.use_pattern_lines(axis="x")
        self.assertEqual("x", self.area_pattern.axis)

    def test_area_copy(self):
        pattern = self.area_pattern.copy()
        self.area_pattern.select((1, 2), (3, 4))
        self.area_pattern.attrs(line_width_x=5, line_width_y=6, gap_size_x=7, gap_size_y=8)
        self.area_pattern.use_pattern_grid().invert()
        self.area_pattern.map_size = 20
        self.area_pattern.uuid = "TEST_UUID"  # Must match an actual UUID if you've set one
        self.area_pattern.axis = "y"

        self.assertNotEqual(pattern.area, self.area_pattern.area)
        self.assertNotEqual(pattern.line_width_x, self.area_pattern.line_width_x)
        self.assertNotEqual(pattern.line_width_y, self.area_pattern.line_width_y)
        self.assertNotEqual(pattern.gap_size_x, self.area_pattern.gap_size_x)
        self.assertNotEqual(pattern.gap_size_y, self.area_pattern.gap_size_y)
        self.assertNotEqual(pattern.uuid, self.area_pattern.uuid)
        self.assertNotEqual(pattern.state, self.area_pattern.state)
        self.assertNotEqual(pattern.inverted, self.area_pattern.inverted)
        self.assertNotEqual(pattern.axis, self.area_pattern.axis)

    def test_area_move(self):
        self.area_pattern = AreaPattern.from_tiles((0, 1), (2, 3))

        self.area_pattern.move(offset_x=10)
        self.assertTupleEqual(((10, 1), (12, 3)), self.area_pattern.area.corners)

        self.area_pattern.move(offset_y=10)
        self.assertTupleEqual(((10, 11), (12, 13)), self.area_pattern.area.corners)

        self.area_pattern.move(offset_x=-5, offset_y=-5)
        self.assertTupleEqual(((5, 6), (7, 8)), self.area_pattern.area.corners)

    def test_area_move_to(self):
        self.area_pattern = AreaPattern.from_tiles((0, 0), (3, 4))

        dimensions = self.area_pattern.area.dimensions

        self.area_pattern.move_to(x=20, y=20, corner="north")
        self.assertTupleEqual(((17, 20), (20, 24)), self.area_pattern.area.corners)
        self.assertTupleEqual(dimensions, self.area_pattern.area.dimensions)

        self.area_pattern.move_to(x=20, y=20, corner="east")
        self.assertTupleEqual(((17, 16), (20, 20)), self.area_pattern.area.corners)
        self.assertTupleEqual(dimensions, self.area_pattern.area.dimensions)

        self.area_pattern.move_to(x=20, y=20, corner="south")
        self.assertTupleEqual(((20, 16), (23, 20)), self.area_pattern.area.corners)
        self.assertTupleEqual(dimensions, self.area_pattern.area.dimensions)

        self.area_pattern.move_to(x=20, y=20, corner="west")
        self.assertTupleEqual(((20, 20), (23, 24)), self.area_pattern.area.corners)
        self.assertTupleEqual(dimensions, self.area_pattern.area.dimensions)

    def test_area_instantiate_without_map_size(self):
        self.area_pattern = AreaPattern.from_tiles((0, 1), (2, 3))
        self.assertEqual(((0, 1), (2, 3)), self.area_pattern.area)

        self.area_pattern = AreaPattern.from_tiles((0, 3))
        self.assertEqual(((0, 3),), self.area_pattern.area)

    def test_map_size_functions_without_map_size(self):
        self.area_pattern = AreaPattern.from_tiles((10, 10), (12, 12))

        self.assertRaises(ValueError, lambda: self.area_pattern.center((5, 5)).cut_overflow())
        self.assertRaises(ValueError, lambda: self.area_pattern.shift_overflow())
        self.assertRaises(ValueError, lambda: self.area_pattern.select_entire_map())

        self.area_pattern.width(5)
        self.assertEqual(((3, 4), (7, 6)), self.area_pattern.area)

    def test_area_corners(self):
        self.area_pattern = AreaPattern.from_tiles(corner1=Tile(2, 4), corner2=Tile(6, 8))
        self.assertEqual(((2, 4), (6, 8)), self.area_pattern.area)

        self.area_pattern = AreaPattern.from_tiles(corner1=Tile(3, 5))
        self.assertEqual(((3, 5),), self.area_pattern.area)

    def test_init_with_tuples(self):
        area_pattern1 = AreaPattern(corner1=(1, 1), corner2=(2, 2))
        area_pattern2 = AreaPattern.from_tiles((1, 1), (2, 2))

        self.assertEqual(area_pattern1.area, area_pattern2.area)

    def test_init_with_negative_tiles(self):
        self.assertRaises(ValueError, lambda: AreaPattern(corner1=(-5, -5), corner2=(-1, -1)))
        self.assertRaises(ValueError, lambda: AreaPattern(area=((-1, -2), (-5, -4))))

        ap = AreaPattern(corner1=(-5, -5), corner2=(-1, -1), map_size=10)
        self.assertEqual(Area((5, 5), (9, 9)), ap.area)

        ap = AreaPattern(corner1=(-5, -5), map_size=10)
        self.assertEqual(Area((5, 5), (5, 5)), ap.area)

        ap = AreaPattern(area=((-5, -5),), map_size=10)
        self.assertEqual(Area((5, 5), (5, 5)), ap.area)

        ap = AreaPattern(area=((-1, -2), (-5, -4)), map_size=10)
        self.assertEqual(Area((5, 6), (9, 8)), ap.area)

