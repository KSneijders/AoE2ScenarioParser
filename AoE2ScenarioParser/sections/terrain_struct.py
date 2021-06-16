import re
from math import sqrt
from typing import List, Tuple, Union, Dict
from pandas import Series, DataFrame   # TODO: add to requirements.txt

from AoE2ScenarioParser.helper.helper import xy_to_i
from AoE2ScenarioParser.helper.bytes_conversions import parse_bytes_to_val
from AoE2ScenarioParser.helper.incremental_generator import IncrementalGenerator
from AoE2ScenarioParser.sections.aoe2_struct_model import AoE2StructModel


DTypeMap = {
    'c': '|S',
    'u': 'uint',
    's': 'int',
    'str': 'str',
    'data': '|S',   # numpy.bytes_, A byte string. (When used in arrays, this type strips trailing null bytes)
    'f': 'float',
}
"""Custom data types -> pandas.dtype or numpy.dtype (prefix only)"""


class TerrainStruct:
    def __init__(self, tiles_count, struct_model: AoE2StructModel):
        self.map_size = int(sqrt(tiles_count))
        self.tiles_count = tiles_count
        assert (self.map_size ** 2 == tiles_count), \
            f"Square of map_size {self.map_size} not equals to tiles_count {tiles_count}."
        self.struct_model = struct_model
        self.byte_length: int = -1

        # Prepare attrs lists.
        self.attrs_names = []       # ['terrain_id', 'elevation', 'unused', 'layer']
        self.attrs_types = []       # ['u', 'u', 'data', 's']
        self.attrs_lengths = []     # [1, 1, 3, 2]
        for name, retriever in struct_model.retriever_map.items():
            var_type, var_len = retriever.datatype.type_and_length
            self.attrs_names.append(name)
            self.attrs_types.append(var_type)
            self.attrs_lengths.append(var_len)
        self.each_tile_length = sum(self.attrs_lengths)      # Each tile's bytes length. Normally is 7.

        self.data = DataFrame()
        """You can locate one tile by `get_tile_by_xy(x, y)`, or by `data.loc[index]`."""

    # --------------------------------------------------------
    #                     Internal Methods
    # --------------------------------------------------------

    def set_data_from_generator(self, igenerator: IncrementalGenerator):
        """Read, parse and store all Tiles data from igenerator into a DataFrame in one time."""
        bytes_list, bytes_length = self.read_and_split_content(igenerator)
        all_tiles_df = DataFrame(bytes_list, columns=self.attrs_names)
        #    terrain_id elevation           unused        layer
        # 0     b'\x0f'   b'\x1a'  b'\xc6\xee\xcc'  b'\x10\x00'
        # 1     b'\x0f'   b'\x1a'  b'\xc6\xee\xcc'  b'\x10\x00'

        for i, attr_name in enumerate(self.attrs_names):
            attr_type = self.attrs_types[i]
            attr_length = self.attrs_lengths[i]
            # Select each column, and convert each cell within the column into a corresponding value
            all_tiles_df[attr_name] = all_tiles_df[attr_name].apply(self.bytes_to_value, args=(attr_type, attr_length))
            #    terrain_id  elevation           unused  layer
            # 0          15         26  b'\xc6\xee\xcc'     16
            # 1          15         26  b'\xc6\xee\xcc'     16

            # Limit values to fixed type and length (currently useless because it can't lock type when editing value).
            # all_tiles_df[attr_name] = all_tiles_df[attr_name].astype(self.type_to_dtype(attr_type, attr_length))
        self.data = all_tiles_df
        self.byte_length = bytes_length


    # TODO: Write methods, to be compatible with AoE2Scenario.write_to_file()


    # --------------------------------------------------------
    #                     API Methods
    # --------------------------------------------------------

    def get_tile_by_xy(self, x, y, as_dict=True) -> Union[Dict, Series]:
        """Get certain Tile's data by x-y coordinates.
        Args:
            x: ↘ direction in map.
            y: ↗ direction in map.
            as_dict: `True` (default), returns a dict with attributes and values.
                     `False` will returns a `Series` in which you can access value by x[index] or x['attr_name'].
        """
        index = self.chech_if_xy_outside_map(x, y)
        if as_dict:
            return dict(self.data.loc[index])
        else:
            return self.data.loc[index]


    def edit_tile_by_xy(self, x, y, attrs_values: Dict):
        """Edit certain Tile's data by x-y coordinates.
        Args:
            x: ↘ direction in map.
            y: ↗ direction in map.
            attrs_values: such as {'terrain_id': 4, ...}, You can input not only one attributes.
        """
        index = self.chech_if_xy_outside_map(x, y)
        for attr_name, value in attrs_values.items():
            if attr_name not in self.attrs_names:
                raise KeyError(f"The given attribute '{attr_name}'  is not existed in tile's attributes.")
            # TODO: verify datatype (int vs u8, etc.)
            previous_type = type(self.data.at[index, attr_name])

            self.data.at[index, attr_name] = value      # at[row_index, column_title]

            new_type = type(self.data.at[index, attr_name])
            if new_type != previous_type:
                raise TypeError(f"The type of new value should be {previous_type}, but got: {new_type}.")


    # TODO: Expand or shrink map size

    # TODO: Vertical table <-> X·Y Tiles matrix


    # --------------------------------------------------------
    #                     Helper Functions
    # --------------------------------------------------------

    def read_and_split_content(self, igenerator: IncrementalGenerator) -> Tuple[List[Tuple], int]:
        """Read all bytes of all tiles, split them into List[(attr1, attr2 ...)], and returns the length of all
        bytes by the way."""
        section_bytes = igenerator.get_bytes(self.tiles_count * self.each_tile_length)
        # 7 bytes as one Tile, split the data, make a DataFrame table
        re_rule = b""
        for length in self.attrs_lengths:
            re_rule += b"(.{%d})" % length      # b"(.{1})(.{1})(.{3})(.{2})"
        bytes_list = re.findall(re_rule, section_bytes)
        bytes_length = len(section_bytes)
        return bytes_list, bytes_length

    def chech_if_xy_outside_map(self, x, y) -> int:
        index = xy_to_i(x, y, self.map_size)
        if index >= self.tiles_count:
            raise IndexError(f"The tile at (x={x}, y={y}) has been outside the map (size={self.map_size}).")
        else:
            return index


    @staticmethod
    def bytes_to_value(cell_data, type_, length_):
        """
        cell_data: (e.g: b'\x0f'). Each single cell in a vertical DataFrame column (Series).
        type_: (e.g: 'u')
        length_: (e.g: 8)
        """
        if type_ == "u":
            return int.from_bytes(cell_data, "little", signed=False)
        elif type_ == "s":
            return int.from_bytes(cell_data, "little", signed=True)
        # elif type_ == "data":
        #     return cell_data
        else:
            return parse_bytes_to_val(None, cell_data, type_, length_)

    @staticmethod
    def type_to_dtype(type_, length_) -> str:
        """Custom data type -> pandas.dtype / numpy.dtype"""
        if type_ in ['u', 's', 'f']:
            dtype_prefix = DTypeMap[type_]
            return dtype_prefix + str(length_ * 8)
        elif type_ in ['data', 'c']:
            return 'bytes'
        elif type_ == 'str':
            return type_
        else:
            raise ValueError(f"Unknown type: ({type_})")


    # --------------------------------------------------------
    #                     Debug Methods
    # --------------------------------------------------------

    # TODO: Write debug methods according to AoE2FileSection.get_byte_structure_as_string() and
