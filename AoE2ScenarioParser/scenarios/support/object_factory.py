from uuid import UUID

from AoE2ScenarioParser.objects.support.area import TilePattern


class ObjectFactory:
    def __init__(self, uuid: UUID) -> None:
        super().__init__()

        self._uuid = uuid

    def tile_pattern(self) -> TilePattern:
        """Return an tile_pattern map linked to the corresponding scenario"""
        return TilePattern(uuid=self._uuid)
