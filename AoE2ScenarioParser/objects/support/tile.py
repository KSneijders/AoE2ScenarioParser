from typing import NamedTuple, Dict


class Tile(NamedTuple):
    """NamedTuple for tiles. use tile.x or tile.y for coord access"""
    x: int
    y: int

    def to_dict(self, prefix: str = "location_") -> Dict[str, int]:
        """
        Converts the coordinates of the tile to keys for use in effects etc.
        This can be used by adding double stars (**) before this function.

        Usage:
            The coordinate: ``(4, 6)`` would result in a dict that looks like:
                ``{'location_x': 4, 'location_y': 6}``
            Then do: ``**tile.to_dict()`` in a function that accepts tiles

        Args:
            prefix: The prefix of the string before 'x' (e.g. prefix="coord_" will result in: "coord_x" as key)

        Returns:
            A dict with ``location_x``, ``location_y`` as keys and their respective values (if prefix is unchanged).
        """
        return {f"{prefix}{key}": getattr(self, key) for key in ['x', 'y']}
