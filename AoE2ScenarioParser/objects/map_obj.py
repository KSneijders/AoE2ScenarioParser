from __future__ import annotations

from typing import List

from AoE2ScenarioParser.helper.alias import Alias

class MapObject():
    def __init__(self, pieces):
        self._map_piece = pieces['MapPiece']

    _map_height = Alias('_map_piece', 'map_height')
    _map_width  = Alias('_map_piece', 'map_width')
    terrain_data = Alias('_map_piece', 'terrain_data')

    def dump_raw_data(self, required_attr = ['terrain_id', 'elevation', 'layer']) -> []:
        """
        @param required_attr: list of attribute names that we want to use in the final concatenated list
        @return: terrain attribute values concatenated in a single list
        """
        # Put the required attributes as a list in a list
        raw_attrs = [[getattr(tile, attr) for attr in required_attr] for tile in self.terrain_data]
        # Flatten the list of lists into a simple list
        return [attr for tile in raw_attrs for attr in tile]

    def create_hill(self, x_begin, y_begin, x_end, y_end, elevation):
        """
        Function that takes the coordinates and the height of a plateau and applies it to the map
        by also setting the surrounding slopes so that it is smooth
        """
        # Clamped coordinates
        for x in range(max(0, x_begin - elevation), min(self.map_size, x_end + elevation)):
            for y in range(max(0, y_begin - elevation), min(self.map_size, y_end + elevation)):
                intended_elevation = 0
                if x >= x_begin and x <= x_end and y >= y_begin and y <= y_end:
                    intended_elevation = elevation
                else:
                    distance_to_hill = max(x_begin - x, x - x_end, y_begin - y, y - y_end)
                    intended_elevation = elevation - distance_to_hill

                self.terrain_data[x * self.map_size + y].elevation = max(intended_elevation, self.terrain_data[x * self.map_size + y].elevation)

    @property
    def map_size(self) -> int:
        if self._map_height == self._map_width:
            return self._map_height
        else:
            raise ValueError("Map is not a square. Use the attributes 'map_width' and 'map_height' instead.")

    @map_size.setter
    def map_size(self, val: int):
        self._map_width = val
        self._map_height = val

    @property
    def map_width(self) -> int:
        return self._map_width

    @property
    def map_height(self) -> int:
        return self._map_height
