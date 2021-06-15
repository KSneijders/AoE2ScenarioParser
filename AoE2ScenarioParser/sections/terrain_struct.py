import re
from typing import List, Tuple, Union, Dict
from pandas import Series, DataFrame   # TODO: add to requirements.txt

from AoE2ScenarioParser.helper.helper import xy_to_i
from AoE2ScenarioParser.helper.bytes_conversions import parse_bytes_to_val
from AoE2ScenarioParser.helper.incremental_generator import IncrementalGenerator
from AoE2ScenarioParser.sections.aoe2_struct_model import AoE2StructModel

class TerrainStruct:
    def __init__(self, map_size, struct_model: AoE2StructModel):
        self.map_size = map_size
        self.tiles_count = map_size * map_size
        self.struct_model = struct_model
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


    def set_data_from_generator(self, igenerator: IncrementalGenerator):
        """Read, parse and store all Tiles data from igenerator into a DataFrame in one time."""
        bytes_list = self.read_and_parse_content(igenerator)
        all_tiles_df = DataFrame(bytes_list, columns=self.attrs_names)
        #    terrain_id elevation           unused        layer
        # 0     b'\x0f'   b'\x1a'  b'\xc6\xee\xcc'  b'\x10\x00'
        # 1     b'\x0f'   b'\x1a'  b'\xc6\xee\xcc'  b'\x10\x00'

        # For each Tile attribute column, execute the conversion of bytes→value
        for i, attr_name in enumerate(self.attrs_names):
            attr_type = self.attrs_types[i]
            attr_length = self.attrs_lengths[i]
            if attr_type == "data":
                continue
            # Select each column, and convert each cell within the column into a corresponding value
            all_tiles_df[attr_name] = all_tiles_df[attr_name].apply(self.bytes_to_value, args=(attr_type, attr_length))
            #    terrain_id  elevation           unused  layer
            # 0          15         26  b'\xc6\xee\xcc'     16
            # 1          15         26  b'\xc6\xee\xcc'     16

        self.data = all_tiles_df


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
            if type(value) is not type(self.data.at[index, attr_name]):
                raise ValueError(f"The given value's type {type(value)} is not in line with norm.")
            # TODO: verify datatype (int vs u8, etc.)

            self.data.at[index, attr_name] = value      # at[row_index, column_title]


    # TODO: Expand or shrink map size

    # TODO: Vertical table <-> X·Y Tiles matrix


    # --------------------------------------------------------
    #                     Helper Functions
    # --------------------------------------------------------

    def read_and_parse_content(self, igenerator: IncrementalGenerator) -> List[Tuple]:
        section_bytes = igenerator.get_bytes(self.tiles_count * self.each_tile_length)
        # 7 bytes as one Tile, split the data, make a DataFrame table
        re_rule = b""
        for length in self.attrs_lengths:
            re_rule += b"(.{%d})" % length      # b"(.{1})(.{1})(.{3})(.{2})"
        return re.findall(re_rule, section_bytes)

    def chech_if_xy_outside_map(self, x, y) -> int:
        index = xy_to_i(x, y, self.map_size)
        if index >= self.tiles_count:
            raise IndexError(f"The tile at (x={x}, y={y}) has been outside the map (size={self.map_size}).")
        else:
            return index


    # --------------------------------------------------------
    #                     Static Methods
    # --------------------------------------------------------

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
