from __future__ import annotations

from AoE2ScenarioParser.objects.support.tile import Tile


class Area:
    """Represents an area selection on a map. An area is defined by two opposite corners of a map"""

    def __init__(self, corner1: tuple[int, int], corner2: tuple[int, int] = None):
        if corner2 is None:
            self.corner1 = self.corner2 = Tile(corner1[0], corner1[1])
            return
        x1, x2 = sorted((corner1[0], corner2[0]))
        y1, y2 = sorted((corner1[1], corner2[1]))
        self.corner1 = Tile(x1, y1)
        self.corner2 = Tile(x2, y2)

    def bound(self, map_size: int) -> Area:
        return Area(
            self.corner1.bound(map_size),
            self.corner2.bound(map_size),
        )

    @property
    def center(self) -> Tile:
        return self.corner1.mid_point(self.corner2)

    @property
    def width(self) -> int:
        return self.corner2.x - self.corner1.x + 1

    @property
    def height(self) -> int:
        return self.corner2.y - self.corner1.y + 1

    def contains(self, tile: tuple) -> bool:
        x, y = tile
        return (
            self.corner1.x <= x <= self.corner2.x
            and self.corner1.y <= y <= self.corner2.y
        )

    def __iter__(self) -> Tile:
        yield self.corner1
        yield self.corner2

    def __getitem__(self, item: int) -> Tile:
        return (self.corner1, self.corner2)[item]

    def __repr__(self) -> str:
        return f"Area({self.corner1}, {self.corner2})"
