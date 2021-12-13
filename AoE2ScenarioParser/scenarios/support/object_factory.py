from uuid import UUID

from AoE2ScenarioParser.objects.support.area import Area


class ObjectFactory:
    def __init__(self, uuid: UUID) -> None:
        super().__init__()

        self.uuid = uuid

    def area(self):
        """Return an area map linked to the corresponding scenario"""
        return Area(uuid=self.uuid)
