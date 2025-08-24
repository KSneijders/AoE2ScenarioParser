from __future__ import annotations

from typing import TYPE_CHECKING

from AoE2ScenarioParser.objects.support import TerrainData, TerrainDataRow
from AoE2ScenarioParser.objects.support.enums.direction import Direction
from AoE2ScenarioParser.sections import TerrainTile

if TYPE_CHECKING:
    from AoE2ScenarioParser.managers.map_manager import MapManager


class TerrainDataSupport:
    def __init__(self, map_manager: 'MapManager'):
        """
        A support object used for resizing terrain data

        Args:
            map_manager: A MapManager object to use for terrain retrieval and calculations
        """
        self.map_manager = map_manager
        self.terrain_template = None

    def compute_resized_terrain_data(
        self,
        new_map_size: int,
        direction: Direction,
        terrain_template: TerrainTile | None = None
    ) -> TerrainData:
        """
        Computes the resized terrain data based on the given arguments

        Args:
            new_map_size: The new map size
            direction: The direction where the adjustments are calculated from
            terrain_template: The terrain template to use when creating new terrain tiles on expansion

        Returns:
            The new terrain data
        """
        self.terrain_template = terrain_template

        diff = new_map_size - self.map_manager.map_size
        is_expansion = diff > 0
        abs_diff = abs(diff)

        terrain_2d = self.map_manager.terrain
        if is_expansion:
            terrain_2d = self.add_rows(terrain_2d, abs_diff, in_front = direction in (Direction.NORTH, Direction.WEST))
            terrain_2d = self.add_cols(terrain_2d, abs_diff, in_front = direction in (Direction.SOUTH, Direction.WEST))
        else:
            terrain_2d = self.slice_rows(terrain_2d, abs_diff, from_front = direction in (Direction.NORTH, Direction.WEST))
            terrain_2d = self.slice_cols(terrain_2d, abs_diff, from_front = direction in (Direction.SOUTH, Direction.WEST))

        return terrain_2d

    def create_tile(self) -> TerrainTile:
        terrain_template = self.terrain_template

        if terrain_template is None:
            return TerrainTile()

        return TerrainTile(
            type = terrain_template.type,
            elevation = terrain_template.elevation,
            zone = terrain_template.zone,
            mask_type = terrain_template.mask_type,
            layer_type = terrain_template.layer_type,
        )

    def create_tiles(self, size: int) -> TerrainDataRow:
        return tuple(self.create_tile() for _ in range(size))

    def create_tile_rows(self, amount: int, size: int) -> TerrainData:
        return tuple(self.create_tiles(size) for _ in range(amount))

    def add_rows(self, terrain: TerrainData, num_rows: int, in_front: bool) -> TerrainData:
        new_rows = self.create_tile_rows(num_rows, size = len(terrain))
        return (new_rows + terrain) if in_front else (terrain + new_rows)

    def add_cols(self, terrain: TerrainData, num_cols: int, in_front: bool) -> TerrainData:
        return tuple(
            (self.create_tiles(num_cols) + row) if in_front else (row + self.create_tiles(num_cols))
                for row in terrain
        )

    def slice_rows(self, terrain: TerrainData, num_rows: int, from_front: bool):
        if from_front:
            return terrain[num_rows:]
        else:
            return terrain[:-num_rows]

    def slice_cols(self, terrain: TerrainData, num_cols: int, from_front: bool):
        return tuple(row[num_cols:] if from_front else row[:-num_cols] for row in terrain)
