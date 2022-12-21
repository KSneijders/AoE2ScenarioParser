from enum import Enum


class AreaAttr(Enum):
    """Enum to show the supported attributes that can be edited using ``Area.attr(k, v)``"""
    X1 = "x1"
    Y1 = "y1"
    X2 = "x2"
    Y2 = "y2"
    GAP_SIZE = "gap_size"
    GAP_SIZE_X = "gap_size_x"
    GAP_SIZE_Y = "gap_size_y"
    LINE_WIDTH = "line_width"
    LINE_WIDTH_X = "line_width_x"
    LINE_WIDTH_Y = "line_width_y"
    AXIS = "axis"
    CORNER_SIZE = "corner_size"
    CORNER_SIZE_X = "corner_size_x"
    CORNER_SIZE_Y = "corner_size_y"
    BLOCK_SIZE = "block_size"
    BLOCK_SIZE_X = "block_size_x"
    BLOCK_SIZE_Y = "block_size_y"