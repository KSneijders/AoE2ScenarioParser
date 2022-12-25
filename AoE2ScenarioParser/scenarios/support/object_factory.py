from uuid import UUID

from AoE2ScenarioParser.objects.support.area import AreaPattern


class ObjectFactory:
    def __init__(self, uuid: UUID) -> None:
        super().__init__()

        self._uuid = uuid

    def area_pattern(self) -> AreaPattern:
        """Return an area_pattern map linked to the corresponding scenario"""
        return AreaPattern(uuid=self._uuid)
