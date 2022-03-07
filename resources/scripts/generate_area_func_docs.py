from typing import List

# DISCLAIMER: PLEASE DON'T USE THIS (Except for it's intended use)
# IT'S MEANT AS A PLACEHOLDER FOR THE ACTUAL API DOCS WHICH WILL COME SOON :tm:
# And yes, I know this code is horrendous 1111

"""
import regex

string = ""  # Read file
indent = 4
r_functions = rf"(?:\n\s{{{indent}}}@(.+?))?\n\s{{{indent}}}def\s+(\w+)\((.+?)?\)(?:\s+->\s+(.+?))?:(?:\n\s{{{4+indent}}}\"\"\"(.+?)\"\"\")?"
regex_findall_result = regex.findall(r_functions, string, regex.DOTALL)
"""

regex_findall_result = [
    ('', 'associate_scenario', 'self, scenario: AoE2Scenario', 'None',
     '\n        Associate area with scenario. Saves scenario UUID in this area object.\n\n        Args:\n            scenario: The scenario to associate with\n        '),
    ('', 'to_coords', 'self, as_terrain: bool = False', "OrderedSet[Tile | 'TerrainTile']",
     '\n        Converts the selection to an OrderedSet of (x, y) coordinates\n\n        Args:\n            as_terrain: If the returning coordinates should be Tile objects or Terrain Tiles. If True the coordinates\n                are returned as TerrainTiles.\n\n        Returns:\n            An OrderedSet of Tiles ((x, y) named tuple) of the selection.\n\n        Examples:\n            The selection: ``((3,3), (5,5))`` would result in an OrderedSet with a length of 9::\n\n                [\n                    (3,3), (4,3)  ...,\n                    ...,   ...,   ...,\n                    ...,   (4,5), (5,5)\n                ]\n        '),
    ('', 'to_chunks',
     '\n            self,\n            as_terrain: bool = False,\n            separate_by_id: bool = True\n    ',
     "List[OrderedSet[Tile | 'TerrainTile']]",
     "\n        Converts the selection to a list of OrderedSets with Tile NamedTuples with (x, y) coordinates.\n        The separation between chunks is based on if they're connected to each other.\n        So the tiles must share an edge (i.e. they should be non-diagonal).\n\n        Args:\n            as_terrain: If the returning coordinates should be Tile objects or Terrain Tiles. If True the coordinates\n                are returned as TerrainTiles.\n            separate_by_id: Take chunk ids into account when separating chunks. When this is true, separate 'chunks'\n                will not be combined into one when they touch each other. For example, with a line pattern and\n                gap_size=0 when this is False, this will result in one 'chunk' as the lines touch each other.\n\n        Returns:\n            A list of OrderedSets of Tiles ((x, y) named tuple) of the selection.\n        "),
    ('', 'to_dict', 'self, prefix:str="area_"', 'Dict[str, int]',
     '\n        Converts the 2 corners of the selection to area keys for use in effects etc.\n        This can be used by adding double stars (**) before this function.\n\n        Usage:\n            The selection: ``((3,3), (5,5))`` would result in a dict that looks like:\n                ``{\'area_x1\': 3, \'area_y1\': 3, \'area_x2\': 5, \'area_y2\': 5}``\n            Then do: ``**area.to_dict()`` in a function that accepts area tiles\n\n        Args:\n            prefix: The prefix of the string before \'x1\' (e.g. prefix="coord_" will result in: "coord_x1" as key)\n\n        Returns:\n            A dict with area_x1, area_y1, area_x2, area_y2 as keys and their respective values.\n        '),
    ('', 'get_selection', 'self', 'Tuple[Tuple[int, int], Tuple[int, int]]',
     'Get the four values of the selection as: ((x1, y1), (x2, y2))'),
    ('', 'get_center', 'self', 'Tuple[float, float]', 'Get center of current selection'),
    ('', 'get_center_int', 'self', 'Tuple[int, int]',
     'Get center of current selection, coords can only be integers. If even length, the value is floored'),
    ('', 'get_range_x', 'self', 'range', 'Returns a range object for the x coordinates.'),
    ('', 'get_range_y', 'self', 'range', 'Returns a range object for the y coordinates.'),
    ('', 'get_width', 'self', 'int', 'Returns the length of the x side of the selection.'),
    ('', 'get_height', 'self', 'int', 'Returns the length of the y side of the selection.'),
    ('', 'use_full', 'self', 'Area', 'Sets the area object to use the entire selection'),
    ('', 'use_only_edge', 'self, line_width: int = None, line_width_x: int = None, line_width_y: int = None', 'Area',
     '\n        Sets the area object to only use the edge of the selection\n\n        Args:\n            line_width: The width of the x & y edge line\n            line_width_x: The width of the x edge line\n            line_width_y: The width of the y edge line\n\n        Returns:\n            This area object\n        '),
    ('', 'use_only_corners', 'self, corner_size: int = None, corner_size_x: int = None, corner_size_y: int = None',
     'Area',
     '\n        Sets the area object to only use the corners pattern within the selection.\n\n        Args:\n            corner_size: The size along both the x and y axis of the corner areas\n            corner_size_x: The size along the x axis of the corner areas\n            corner_size_y: The size along the y axis of the corner areas\n\n        Returns:\n            This area object\n        '),
    ('', 'use_pattern_grid',
     '\n            self,\n            block_size: int = None,\n            gap_size: int = None,\n            block_size_x: int = None,\n            block_size_y: int = None,\n            gap_size_x: int = None,\n            gap_size_y: int = None\n    ',
     'Area',
     '\n        Sets the area object to use a grid pattern within the selection.\n\n        Args:\n            block_size: The size of the gaps between lines\n            gap_size: The width of the grid lines\n            block_size_x: The size of the x gaps between lines\n            block_size_y: The size of the y gaps between lines\n            gap_size_x: The width of the x grid lines\n            gap_size_y: The width of the y grid lines\n\n        Returns:\n            This area object\n        '),
    ('', 'use_pattern_lines', 'self, axis: str = None, gap_size: int = None, line_width: int = None', 'Area',
     '\n        Sets the area object to use a lines pattern within the selection.\n\n        Args:\n            axis: The axis the lines should follow. Can either be "x" or "y"\n            gap_size: The size of the gaps between lines\n            line_width: The width of the x & y lines\n\n        Returns:\n            This area object\n        '),
    ('', 'invert', 'self', 'Area',
     '\n        Inverts the inverted boolean. Causes the `to_coords` to return the inverted selection. (Especially useful for\n        the grid state. Not as useful for the edge which would be the same as shrinking the selection. When used with\n        the fill state an empty set is returned.\n\n        **Please note:** This inverts the INTERNAL selection. Tiles OUTSIDE of the selection will NOT be returned.\n        '),
    ('', 'along_axis', 'self, axis: str', 'Area', 'Sets the axis. Can be either "x" or "y". '),
    ('', 'attr', 'self, key: str | AreaAttr, value: int', 'Area',
     'Sets the attribute to the given value. AreaAttr or str can be used as key'),
    ('', 'attrs',
     '\n            self,\n            x1: int = None,\n            y1: int = None,\n            x2: int = None,\n            y2: int = None,\n            gap_size: int = None,\n            gap_size_x: int = None,\n            gap_size_y: int = None,\n            line_width: int = None,\n            line_width_x: int = None,\n            line_width_y: int = None,\n            axis: str = None,\n            corner_size: int = None,\n            corner_size_x: int = None,\n            corner_size_y: int = None,\n            block_size: int = None,\n            block_size_x: int = None,\n            block_size_y: int = None,\n    ',
     'Area',
     '\n        Sets multiple attributes to the corresponding values.\n\n        Returns:\n            This area object\n        '),
    ('', 'size', 'self, n: int', 'Area',
     '\n        Sets the selection to a size around the center. If center is (4,4) with a size of 3 the selection will become\n        ``((3,3), (5,5))``\n        '),
    ('', 'height', 'self, n: int', 'Area',
     "\n        Sets the height (y axis) of the selection. Shrinks/Expands both sides equally.\n        If the expansion hits the edge of the map, it'll expand on the other side.\n        "),
    ('', 'width', 'self, n: int', 'Area',
     "\n        Sets the width (x axis) of the selection. Shrinks/Expands both sides equally.\n        If the expansion hits the edge of the map, it'll expand on the other side.\n        "),
    ('', 'center', 'self, x: int, y: int', 'Area',
     '\n        Moves the selection center to a given position. When the given center forces the selection of the edge of the\n        map, the selection is moved to that position and all tiles that are out of the map are removed from the\n        selection, effectively decreasing the selection size.\n\n        If you want to limit moving the center without changing the selection box size, use: ``center_bounded``\n        '),
    ('', 'center_bounded', 'self, x: int, y: int', 'Area',
     '\n        Moves the selection center to a given position on the map. This function makes sure it cannot go over the edge\n        of the map. The selection will be forced against the edge of the map but the selection will not be decreased.\n        '),
    ('', 'select_entire_map', 'self', 'Area', 'Sets the selection to the entire map'),
    ('', 'select', 'self, x1: int, y1: int, x2: int = None, y2: int = None', 'Area',
     'Sets the selection to the given coordinates'),
    ('', 'select_centered', 'self, x: int, y: int, dx: int = 1, dy: int = 1', 'Area',
     'Sets the selection to the given coordinates'),
    ('', 'shrink', 'self, n: int', 'Area', 'Shrinks the selection from all sides'),
    ('', 'shrink_x1', 'self, n: int', 'Area', 'Shrinks the selection from the first corner on the X axis by n'),
    ('', 'shrink_y1', 'self, n: int', 'Area', 'Shrinks the selection from the first corner on the Y axis by n'),
    ('', 'shrink_x2', 'self, n: int', 'Area', 'Shrinks the selection from the second corner on the X axis by n'),
    ('', 'shrink_y2', 'self, n: int', 'Area', 'Shrinks the selection from the second corner on the Y axis by n'),
    ('', 'expand', 'self, n: int', 'Area', 'Expands the selection from all sides'),
    ('', 'expand_x1', 'self, n: int', 'Area', 'Expands the selection from the first corner on the X axis by n'),
    ('', 'expand_y1', 'self, n: int', 'Area', 'Expands the selection from the first corner on the Y axis by n'),
    ('', 'expand_x2', 'self, n: int', 'Area', 'Expands the selection from the second corner on the X axis by n'),
    ('', 'expand_y2', 'self, n: int', 'Area', 'Expands the selection from the second corner on the Y axis by n'),
    ('', 'is_within_selection', 'self, x: int = -1, y: int = -1, tile: Tile = None', 'bool',
     '\n        If a given (x,y) location is within the selection.\n\n        Args:\n            x: The X coordinate\n            y: The Y coordinate\n            tile: A Tile object, replacing the x & y coordinates\n\n        Returns:\n            True if (x,y) is within the selection, False otherwise\n        '),
    ('', 'copy', 'self', 'Area',
     "\n        Copy this instance of an Area. Useful for when you want to do multiple extractions (to_...) from the same source\n        with small tweaks.\n\n        Examples:\n\n            Get a grid and the edge around it::\n\n                area = Area.select(10,10,20,20)\n                edge = area.copy().expand(1).use_only_edge().to_coords()\n                # Without copy you'd have to undo all changes above. In this case that'd be: `.shrink(1)`\n                grid = area.use_pattern_grid().to_coords()\n\n        Returns:\n            A copy of this Area object\n        "),
]

for decorator, name, definition, return_type, doc_str in regex_findall_result:
    definition: str = ''.join(map(lambda s: s.strip(), definition.splitlines()))
    definition = definition.removeprefix("self,").removeprefix("self")
    definition = definition.strip().replace(', ', ',')

    split_def: List[str] = [s for s in definition.split(',') if s]

    param_names: List[str] = []
    f_param_table_start: str = ""
    f_param_table_end: List[List[str]] = []
    f_param_table_end_string: str = ""

    if "\n\n" in doc_str:
        func_doc = [s.strip() for s in doc_str.split("\n\n")][0]
        args_etc = doc_str.removeprefix(func_doc)
    else:
        func_doc = doc_str
        args_etc = ""

    func_doc = f"\n\n{' '.join(s.strip() for s in func_doc.splitlines())}"

    if len(split_def):
        f_param_table_start = '\n'.join([
            f"", f"",
            f"|Parameter|Type|Default|Description|",
            f"|-|-|-|-|",
        ])

        for string in split_def:
            assert ':' in string

            param_name, right_side = string.split(':')
            param_names.append(param_name)

            if "=" in right_side:
                param_type, param_def = right_side.split('=')
            else:
                param_type, param_def = right_side, '-'

            param_type = param_type.replace('|', '\\|')

            f_param_table_end.append([param_name, param_type, param_def, ""])

        if "Args:" in args_etc:
            args_etc = args_etc[args_etc.find("Args:"):]
            for index, entry in enumerate(f_param_table_end):
                if index < len(f_param_table_end) - 1:
                    entry[3] = args_etc[
                               args_etc.find(f"{entry[0]}:"):args_etc.find(f"{f_param_table_end[index + 1][0]}:")].strip()
                else:
                    end = min([x for x in [
                        args_etc.find("Returns:"),
                        args_etc.find("Examples:")
                    ] if x != -1] or [-1])
                    entry[3] = args_etc[args_etc.find(entry[0]):end].strip()
                entry[3] = ''.join(s.strip() for s in entry[3].removeprefix(f"{entry[0]}:").splitlines())

        for entry in f_param_table_end:
            if not entry[3]:
                entry[3] = "-"
            f_param_table_end_string += f"\n|{'|'.join(entry)}|"

    f_string_definition = '\n'.join([
        f"---", f"",
        f".{name}({', '.join(param_names)})",
    ])

    assert return_type

    f_return_definition = '\n'.join([
        f"", f"",
        f"Returns: `{return_type}`",
        f"",
    ])
    nl = "\n"
    print(f"{f_string_definition}{func_doc}{f_param_table_start}{f_param_table_end_string}{f_return_definition}")


# Expected result:
"""
---

**.to_coords**

|Parameter|Type|Default|Description|
|-|-|-|-|
|as_terrain|`bool`|`False`|If the returning coordinates should be Tile objects or Terrain Tiles. If True the coordinates are returned as TerrainTiles|

Returns: `OrderedSet[Tile | TerrainTile]`

---

**.to_chunks**

|Parameter|Type|Default|Description|
|-|-|-|-|
|as_terrain|`bool`|`False`|If the returning coordinates should be Tile objects or Terrain Tiles. If True the coordinates are returned as TerrainTiles|
|separate_by_id|`bool`|`True`|Take chunk ids into account when separating chunks. When this is true, separate 'chunks' will not be combined into one when they touch each other. For example, with a line pattern and gap_size=0 when this is False, this will result in one 'chunk' as the lines touch each other|

Returns: `List[OrderedSet[Tile | TerrainTile]]`

---
"""


