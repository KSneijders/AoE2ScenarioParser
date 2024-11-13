import pytest

from AoE2ScenarioParser.objects.support import Area
from AoE2ScenarioParser.objects.support.area_pattern import AreaAttr, AreaPattern, AreaState
from AoE2ScenarioParser.objects.support.tile import Tile

map_size = 144
maximum_coordinate = map_size - 1


@pytest.fixture
def area_pattern() -> AreaPattern:
    return AreaPattern(map_size = map_size)


def test_select_entire_map(area_pattern):
    area_pattern.select_entire_map()
    (x1, y1), (x2, y2) = area_pattern.area
    assert 0 == x1
    assert 0 == y1
    assert maximum_coordinate == x2
    assert maximum_coordinate == y2


def test_select(area_pattern):
    area_pattern.select((10, 11), (20, 22))
    (x1, y1), (x2, y2) = area_pattern.area
    assert 10 == x1
    assert 11 == y1
    assert 20 == x2
    assert 22 == y2


def test_select_single_tile(area_pattern):
    area_pattern.select((10, 22))
    (x1, y1), (x2, y2) = area_pattern.area
    assert 10 == x1
    assert 22 == y1
    assert 10 == x2
    assert 22 == y2


def test_select_negative_tiles(area_pattern):
    area_pattern.select((1, 2), (-1, -2))
    (x1, y1), (x2, y2) = area_pattern.area
    assert 1 == x1
    assert 2 == y1
    assert 143 == x2
    assert 142 == y2


def test_select_single_negative_tile(area_pattern):
    area_pattern.select((-1, -2))
    (x1, y1), (x2, y2) = area_pattern.area
    assert 143 == x1
    assert 142 == y1
    assert 143 == x2
    assert 142 == y2


def test_select_centered_odd(area_pattern):
    area_pattern.select_centered((5, 5), dx = 3, dy = 5)
    (x1, y1), (x2, y2) = area_pattern.area

    assert 3 == area_pattern.area.width
    assert 5 == area_pattern.area.height
    assert 4 == x1
    assert 3 == y1
    assert 6 == x2
    assert 7 == y2


def test_select_centered_even(area_pattern):
    area_pattern.select_centered((5, 5), dx = 4, dy = 6)
    (x1, y1), (x2, y2) = area_pattern.area

    assert 4 == area_pattern.area.width
    assert 6 == area_pattern.area.height
    assert 3 == x1
    assert 2 == y1
    assert 6 == x2
    assert 7 == y2


def test_select_centered_mixed(area_pattern):
    area_pattern.select_centered((5, 5), dx = 2, dy = 5)
    (x1, y1), (x2, y2) = area_pattern.area

    assert 2 == area_pattern.area.width
    assert 5 == area_pattern.area.height
    assert 4 == x1
    assert 3 == y1
    assert 5 == x2
    assert 7 == y2


def test_area_selection(area_pattern):
    assert ((3, 3), (5, 5)) == area_pattern.select((3, 3), (5, 5)).area


def test_set_center_then_size(area_pattern):
    area_pattern.center((8, 8)).size(9)
    assert area_pattern.area == ((4, 4), (12, 12))

    area_pattern.size(10)
    assert area_pattern.area == ((3, 3), (12, 12))

    area_pattern.center((5, 5)).size(300)
    assert area_pattern.area == ((-145, -145), (154, 154))


def test_set_size_then_center(area_pattern):
    area_pattern = AreaPattern(map_size = area_pattern.map_size)
    area_pattern.size(9).center((8, 8))
    assert ((4, 4), (12, 12)) == area_pattern.area

    # Set size should function like aoe2 'center on even size' logic
    area_pattern.center((8, 8)).size(4)
    assert ((6, 6), (9, 9)) == area_pattern.area


def test_area_height(area_pattern):
    area_pattern.center((8, 8))
    area_pattern.size(height=3)
    assert ((8, 7), (8, 9)) == area_pattern.area
    area_pattern.size(height=10)
    assert ((8, 3), (8, 12)) == area_pattern.area
    area_pattern.size(height=4)
    assert ((8, 6), (8, 9)) == area_pattern.area
    area_pattern.size(height=1)
    assert ((8, 8), (8, 8)) == area_pattern.area


def test_area_width(area_pattern):
    area_pattern.center((8, 8))
    area_pattern.size(width=6)
    assert ((5, 8), (10, 8)) == area_pattern.area
    area_pattern.size(width=11)
    assert ((3, 8), (13, 8)) == area_pattern.area
    area_pattern.size(width=8)
    assert ((4, 8), (11, 8)) == area_pattern.area
    area_pattern.size(width=3)
    assert ((7, 8), (9, 8)) == area_pattern.area


def test_bound(area_pattern):
    area_pattern.bound().select((3, 3), (7, 7))
    assert area_pattern.area.dimensions == (5, 5)

    area_pattern.center((3, 0)).bound()
    assert area_pattern.area.dimensions == (5, 3)

    area_pattern.center((0, 0)).bound()
    assert area_pattern.area.dimensions == (3, 2)

    # Expand should add 10 to all sides but dimensions should only increase by 10
    # Because North & West bounds block expansion
    area_pattern.expand(10).bound()
    assert area_pattern.area.dimensions == (13, 12)


def test_shift(area_pattern):
    area_pattern.select((3, 3), (7, 7)).shift()
    assert area_pattern.area.dimensions == (5, 5)

    area_pattern.center((3, 0))
    assert not area_pattern.is_within_bounds()
    area_pattern.shift()
    assert area_pattern.is_within_bounds()
    assert area_pattern.area.dimensions == (5, 5)

    area_pattern.center((0, 0))
    assert not area_pattern.is_within_bounds()
    area_pattern.shift()
    assert area_pattern.is_within_bounds()
    assert area_pattern.area.dimensions == (5, 5)

    area_pattern.expand(10)
    assert area_pattern.area.dimensions == (25, 25)
    assert not area_pattern.is_within_bounds()
    area_pattern.shift()
    assert area_pattern.is_within_bounds()
    assert area_pattern.area.dimensions == (25, 25)

    area_pattern.select_entire_map().expand(5).shift()
    assert area_pattern.area.dimensions == (map_size, map_size)


def test_area_use_full(area_pattern):
    area_pattern.use_full()
    assert AreaState.RECT == area_pattern.state
    area_pattern.use_only_edge().use_full()
    assert AreaState.RECT == area_pattern.state

    area_pattern.select((3, 3), (5, 5))
    assert {
               (3, 3), (4, 3), (5, 3),
               (3, 4), (4, 4), (5, 4),
               (3, 5), (4, 5), (5, 5),
           } == area_pattern.to_coords()

    area_pattern.shrink_corner1_by(dx = 1)
    assert {
               (4, 3), (5, 3),
               (4, 4), (5, 4),
               (4, 5), (5, 5),
           } == area_pattern.to_coords()

    area_pattern.invert()
    assert set() == area_pattern.to_coords()


def test_area_to_chunks(area_pattern):
    area_pattern.select((3, 3), (5, 5))
    assert [{
        (3, 3), (4, 3), (5, 3),
        (3, 4), (4, 4), (5, 4),
        (3, 5), (4, 5), (5, 5),
    }] == area_pattern.to_chunks()

    area_pattern.select((3, 3), (6, 7)).use_pattern_lines(axis = "x")
    assert [
               {(3, 3), (4, 3), (5, 3), (6, 3)},

               {(3, 5), (4, 5), (5, 5), (6, 5)},

               {(3, 7), (4, 7), (5, 7), (6, 7)},
           ] == area_pattern.to_chunks()

    area_pattern.select((3, 3), (7, 7)).use_pattern_grid(block_size = 2)
    assert [
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
           ] == area_pattern.to_chunks()

    area_pattern.invert()
    assert [{
        # @formatter:off
                        (5, 3),
                        (5, 4),
        (3, 5), (4, 5), (5, 5), (6, 5), (7, 5),
                        (5, 6),
                        (5, 7),
        # @formatter:on
    }] == area_pattern.to_chunks()


def test_area_to_chunks_order(area_pattern):
    area_pattern.select((3, 3), (8, 8)).use_pattern_grid(block_size = 3, gap_size = 1)
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

    given_tiles = [tile for chunk in area_pattern.to_chunks() for tile in chunk]
    assert tiles == given_tiles


def test_area_get_chunk_id(area_pattern):
    area_pattern.use_pattern_grid().select((1, 1), (5, 5))
    assert 0 == area_pattern._get_chunk_id(Tile(1, 1))
    assert 4 == area_pattern._get_chunk_id(Tile(3, 3))
    assert -1 == area_pattern._get_chunk_id(Tile(3, 4))
    area_pattern.attrs(gap_size = 0)
    assert 0 == area_pattern._get_chunk_id(Tile(1, 1))
    assert 12 == area_pattern._get_chunk_id(Tile(3, 3))
    assert 17 == area_pattern._get_chunk_id(Tile(3, 4))

    area_pattern.use_pattern_lines(axis = "y", gap_size = 1)
    assert 0 == area_pattern._get_chunk_id(Tile(1, 1))
    assert -1 == area_pattern._get_chunk_id(Tile(2, 4))
    assert 2 == area_pattern._get_chunk_id(Tile(5, 3))
    area_pattern.attrs(gap_size = 0)
    assert 0 == area_pattern._get_chunk_id(Tile(1, 1))
    assert 1 == area_pattern._get_chunk_id(Tile(2, 4))
    assert 4 == area_pattern._get_chunk_id(Tile(5, 3))

    area_pattern.use_only_corners()
    assert 0 == area_pattern._get_chunk_id(Tile(1, 1))
    assert 1 == area_pattern._get_chunk_id(Tile(5, 1))
    assert 2 == area_pattern._get_chunk_id(Tile(5, 5))
    assert 3 == area_pattern._get_chunk_id(Tile(1, 5))
    assert -1 == area_pattern._get_chunk_id(Tile(5, 4))


def test_area_use_only_edge(area_pattern):
    area_pattern.use_only_edge()
    assert AreaState.EDGE == area_pattern.state

    area_pattern.select((3, 3), (6, 7))
    # @formatter:off
    assert {
            (3, 3), (4, 3), (5, 3), (6, 3),
            (3, 4),                 (6, 4),
            (3, 5),                 (6, 5),
            (3, 6),                 (6, 6),
            (3, 7), (4, 7), (5, 7), (6, 7),
        } == area_pattern.to_coords()
    # @formatter:on

    area_pattern.select((3, 3), (8, 8)).use_only_edge().attr(AreaAttr.LINE_WIDTH, 2)
    # @formatter:off
    assert {
            (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3),
            (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4),
            (3, 5), (4, 5),                 (7, 5), (8, 5),
            (3, 6), (4, 6),                 (7, 6), (8, 6),
            (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7),
            (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8),
        } == area_pattern.to_coords()
    # @formatter:on

    area_pattern.invert()
    assert {
               (5, 5), (6, 5),
               (5, 6), (6, 6),
           } == area_pattern.to_coords()


def test_area_use_lines(area_pattern):
    area_pattern.use_pattern_lines(axis = "y")
    assert AreaState.LINES == area_pattern.state

    area_pattern.select((3, 3), (6, 7))
    # @formatter:off
    assert {
            (3, 3),         (5, 3),
            (3, 4),         (5, 4),
            (3, 5),         (5, 5),
            (3, 6),         (5, 6),
            (3, 7),         (5, 7),
        } == area_pattern.to_coords()
    # @formatter:on

    area_pattern.use_pattern_lines(axis = "x")
    # @formatter:off
    assert {
            (3, 3), (4, 3), (5, 3), (6, 3),

            (3, 5), (4, 5), (5, 5), (6, 5),

            (3, 7), (4, 7), (5, 7), (6, 7),
        } == area_pattern.to_coords()
    # @formatter:on

    area_pattern.use_pattern_lines(axis = "x", gap_size = 2)
    # @formatter:off
    assert {
            (3, 3), (4, 3), (5, 3), (6, 3),


            (3, 6), (4, 6), (5, 6), (6, 6),
        } == area_pattern.to_coords()
    # @formatter:on

    area_pattern.use_pattern_lines(axis = "x", gap_size = 1, line_width = 2)
    assert {
               (3, 3), (4, 3), (5, 3), (6, 3),
               (3, 4), (4, 4), (5, 4), (6, 4),
               (3, 6), (4, 6), (5, 6), (6, 6),
               (3, 7), (4, 7), (5, 7), (6, 7),
           } == area_pattern.to_coords()


def test_area_use_grid(area_pattern):
    area_pattern.use_pattern_grid()
    assert AreaState.GRID == area_pattern.state

    area_pattern.select((3, 3), (6, 7))
    # @formatter:off
    assert {
            (3, 3),        (5, 3),

            (3, 5),        (5, 5),

            (3, 7),        (5, 7),
        } == area_pattern.to_coords()
    # @formatter:on

    area_pattern.select((3, 3), (6, 7)).invert()
    # @formatter:off
    assert {
                    (4, 3),         (6, 3),
            (3, 4), (4, 4), (5, 4), (6, 4),
                    (4, 5),         (6, 5),
            (3, 6), (4, 6), (5, 6), (6, 6),
                    (4, 7),         (6, 7),
        } == area_pattern.to_coords()
    # @formatter:on


def test_area_use_only_corners(area_pattern):
    area_pattern.use_only_corners()
    assert AreaState.CORNERS == area_pattern.state

    area_pattern.select((3, 3), (6, 7))
    # @formatter:off
    assert {
            (3, 3),                 (6, 3),



            (3, 7),                 (6, 7),
        } == area_pattern.to_coords()
    # @formatter:on

    area_pattern.attrs(corner_size = 2)
    # @formatter:off
    assert {
            (3, 3), (4, 3), (5, 3), (6, 3),
            (3, 4), (4, 4), (5, 4), (6, 4),

            (3, 6), (4, 6), (5, 6), (6, 6),
            (3, 7), (4, 7), (5, 7), (6, 7),
        } == area_pattern.to_coords()
    # @formatter:on

    area_pattern.attrs(corner_size_x = 1, corner_size_y = 2)
    # @formatter:off
    assert {
            (3, 3),                 (6, 3),
            (3, 4),                 (6, 4),
            (3, 6),                 (6, 6),
            (3, 7),                 (6, 7),
        } == area_pattern.to_coords()
    # @formatter:on


def test_area_attr_config(area_pattern):
    area_pattern.attr('gap_size', 3)
    assert 3 == area_pattern.gap_size_x
    assert 3 == area_pattern.gap_size_y
    area_pattern.attr(AreaAttr.GAP_SIZE_X, 4)
    assert 4 == area_pattern.gap_size_x
    assert 3 == area_pattern.gap_size_y
    area_pattern.attr(AreaAttr.LINE_WIDTH, 10)
    assert 10 == area_pattern.line_width_x
    assert 10 == area_pattern.line_width_y
    area_pattern.attr('line_width_x', 12)
    assert 12 == area_pattern.line_width_x
    assert 10 == area_pattern.line_width_y


def test_area_attrs_kwarg_configs(area_pattern):
    area_pattern.attrs(gap_size = 3, line_width = 4)
    assert 3 == area_pattern.gap_size_x
    assert 3 == area_pattern.gap_size_y
    assert 4 == area_pattern.line_width_x
    assert 4 == area_pattern.line_width_y

    area_pattern.attrs(gap_size_x = 1, gap_size_y = 3, line_width_x = 5, line_width_y = 7)
    assert 1 == area_pattern.gap_size_x
    assert 3 == area_pattern.gap_size_y
    assert 5 == area_pattern.line_width_x
    assert 7 == area_pattern.line_width_y

    area_pattern.attrs(gap_size = 10, line_width_x = 1, line_width_y = 2)
    assert 10 == area_pattern.gap_size_x
    assert 10 == area_pattern.gap_size_y
    assert 1 == area_pattern.line_width_x
    assert 2 == area_pattern.line_width_y

    area_pattern.attrs(gap_size_x = 8, gap_size_y = 11, line_width = 10)
    assert 8 == area_pattern.gap_size_x
    assert 11 == area_pattern.gap_size_y
    assert 10 == area_pattern.line_width_x
    assert 10 == area_pattern.line_width_y

    area_pattern.attrs(gap_size = 11, gap_size_x = 8, line_width = 10, line_width_y = 2)
    assert 8 == area_pattern.gap_size_x
    assert 11 == area_pattern.gap_size_y
    assert 10 == area_pattern.line_width_x
    assert 2 == area_pattern.line_width_y


# -------------- test_area_use_grid_with_configs --------------

def test_area_use_grid_with_configs(area_pattern):
    area_pattern.select((3, 3), (6, 7)).use_pattern_grid(gap_size = 2)
    # @formatter:off
    assert {
            (3, 3),                 (6, 3),
            (3, 6),                 (6, 6),
        } == area_pattern.to_coords()
    # @formatter:on


def test_area_use_grid_with_configs_2(area_pattern):
    area_pattern.select((3, 3), (6, 7)).use_pattern_grid(block_size = 2)
    # @formatter:off
    assert {
            (3, 3), (4, 3),         (6, 3),
            (3, 4), (4, 4),         (6, 4),

            (3, 6), (4, 6),         (6, 6),
            (3, 7), (4, 7),         (6, 7),
        } == area_pattern.to_coords()
    # @formatter:on


def test_area_use_grid_with_configs_3(area_pattern):
    area_pattern.select((3, 3), (6, 7)).use_pattern_grid(block_size = 2, gap_size = 2)
    # @formatter:off
    assert {
            (3, 3), (4, 3),
            (3, 4), (4, 4),


            (3, 7), (4, 7),
        } == area_pattern.to_coords()
    # @formatter:on


# -------------- test_area_use_grid_with_configs_abuse_as_lines --------------

def test_area_use_grid_with_configs_abuse_as_lines(area_pattern):
    area_pattern.select((3, 3), (6, 7)).use_pattern_grid(gap_size_y = 0)
    # @formatter:off
    assert {
            (3, 3),        (5, 3),
            (3, 4),        (5, 4),
            (3, 5),        (5, 5),
            (3, 6),        (5, 6),
            (3, 7),        (5, 7),
        } == area_pattern.to_coords()
    # @formatter:on


def test_area_use_grid_with_configs_abuse_as_lines2(area_pattern):
    area_pattern.select((3, 3), (6, 7)).use_pattern_grid(gap_size_x = 0)
    # @formatter:off
    assert {
            (3, 3), (4, 3), (5, 3), (6, 3),

            (3, 5), (4, 5), (5, 5), (6, 5),

            (3, 7), (4, 7), (5, 7), (6, 7),
        } == area_pattern.to_coords()
    # @formatter:on


def test_area_use_grid_with_configs_abuse_as_lines3(area_pattern):
    area_pattern.select((3, 3), (6, 7)).use_pattern_grid(gap_size_x = 0, block_size_y = 2)
    # @formatter:off
    assert {
            (3, 3), (4, 3), (5, 3), (6, 3),
            (3, 4), (4, 4), (5, 4), (6, 4),

            (3, 6), (4, 6), (5, 6), (6, 6),
            (3, 7), (4, 7), (5, 7), (6, 7),
        } == area_pattern.to_coords()
    # @formatter:on


def test_area_is_within_bounds(area_pattern):
    area_pattern.select((0, 0), (10, 10))
    assert area_pattern.is_within_bounds()

    area_pattern.move(x_offset = -1)
    assert not area_pattern.is_within_bounds()

    # Select exactly the right-most corner
    area_pattern.select_centered((140, 140), dx = 7, dy = 7)
    assert area_pattern.is_within_bounds()

    area_pattern.move(x_offset = 1)
    assert not area_pattern.is_within_bounds()

    area_pattern.move(x_offset = -1, y_offset = 1)
    assert not area_pattern.is_within_bounds()


def test_area_is_within_selection(area_pattern):
    area_pattern.select((3, 5), (8, 11))
    assert area_pattern.is_within_selection((3, 5))
    assert area_pattern.is_within_selection((8, 11))
    assert area_pattern.is_within_selection((7, 7))
    assert not area_pattern.is_within_selection((2, 7))
    assert not area_pattern.is_within_selection((11, 7))
    assert not area_pattern.is_within_selection((5, 4))
    assert not area_pattern.is_within_selection((5, 13))


def test_area_is_edge_tile(area_pattern):
    area_pattern.select((3, 5), (8, 11)).use_only_edge()
    assert area_pattern.is_within_selection((3, 5))
    assert area_pattern.is_within_selection((8, 11))
    assert area_pattern.is_within_selection((3, 7))
    assert area_pattern.is_within_selection((6, 5))
    assert not area_pattern.is_within_selection((5, 7))
    assert not area_pattern.is_within_selection((2, 10))
    assert not area_pattern.is_within_selection((4, 12))


def test_area_invert(area_pattern):
    area_pattern.invert()
    assert area_pattern.inverted
    area_pattern.invert()
    assert not area_pattern.inverted


def test_area_axis(area_pattern):
    area_pattern.along_axis("y")
    assert "y" == area_pattern.axis
    area_pattern.use_pattern_lines(axis = "x")
    assert "x" == area_pattern.axis


def test_area_copy(area_pattern):
    pattern = area_pattern.copy()

    area_pattern.select((1, 2), (3, 4))
    area_pattern.attrs(line_width_x = 5, line_width_y = 6, gap_size_x = 7, gap_size_y = 8)
    area_pattern.use_pattern_grid().invert()
    area_pattern.map_size = 20
    area_pattern.axis = "y"

    # @formatter:off
    assert pattern.area         != area_pattern.area
    assert pattern.line_width_x != area_pattern.line_width_x
    assert pattern.line_width_y != area_pattern.line_width_y
    assert pattern.gap_size_x   != area_pattern.gap_size_x
    assert pattern.gap_size_y   != area_pattern.gap_size_y
    assert pattern.state        != area_pattern.state
    assert pattern.inverted     != area_pattern.inverted
    assert pattern.axis         != area_pattern.axis
    # @formatter:on


def test_area_instantiate_without_map_size():
    area_pattern = AreaPattern.from_tiles((0, 1), (2, 3))
    assert ((0, 1), (2, 3)) == area_pattern.area

    area_pattern = AreaPattern.from_tiles((0, 3))
    assert ((0, 3),) == area_pattern.area


def test_map_size_functions_without_map_size():
    area_pattern = AreaPattern.from_tiles((10, 10), (12, 12))

    with pytest.raises(ValueError, match = "No map size was configured for this AreaPattern"):
        area_pattern.select_entire_map()
    with pytest.raises(ValueError, match = "No map size was configured for this AreaPattern"):
        # noinspection PyStatementEffect
        area_pattern.area_bounded

    # Verify above functions did not impact selection
    area_pattern.size(width=5)
    assert ((9, 10), (13, 12)) == area_pattern.area


def test_area_corners():
    area_pattern = AreaPattern.from_tiles(corner1 = Tile(2, 4), corner2 = Tile(6, 8))
    assert ((2, 4), (6, 8)) == area_pattern.area

    area_pattern = AreaPattern.from_tiles(corner1 = Tile(3, 5))
    assert ((3, 5),) == area_pattern.area


def test_init_with_tuples():
    area_pattern1 = AreaPattern(corner1 = (1, 1), corner2 = (2, 2))
    area_pattern2 = AreaPattern.from_tiles((1, 1), (2, 2))

    assert area_pattern1.area == area_pattern2.area


def test_init_with_negative_tiles():
    with pytest.raises(ValueError, match = "Cannot use negative coordinates to make an area selection when map_size is not set"):
        AreaPattern(corner1 = (-5, -5), corner2 = (-1, -1))
        AreaPattern(area = ((-1, -2), (-5, -4)))

    area_pattern = AreaPattern(corner1 = (-5, -5), corner2 = (-1, -1), map_size = 10)
    assert Area((5, 5), (9, 9)) == area_pattern.area

    area_pattern = AreaPattern(corner1 = (-5, -5), map_size = 10)
    assert Area((5, 5), (5, 5)) == area_pattern.area

    area_pattern = AreaPattern(area = ((-5, -5),), map_size = 10)
    assert Area((5, 5), (5, 5)) == area_pattern.area

    area_pattern = AreaPattern(area = ((-1, -2), (-5, -4)), map_size = 10)
    assert Area((5, 6), (9, 8)) == area_pattern.area
