from AoE2ScenarioParser.helper.retriever import RetrieverObjectLink
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


class TerrainObject(AoE2Object):
    _link_list = [
        RetrieverObjectLink("terrain_id", "data.MapPiece.terrain_data[__index__].terrain_id"),
        RetrieverObjectLink("elevation", "data.MapPiece.terrain_data[__index__].elevation"),
        RetrieverObjectLink("layer", "data.MapPiece.terrain_data[__index__].layer"),
    ]

    terrain_id: int
    elevation: int
    layer: int

    def __init__(self, parsed_header, parsed_data, instance_number: int = -1):
        self._parsed_header = parsed_header
        self._parsed_data = parsed_data
        self._instance_number = instance_number

        self.construct(self._parsed_header, self._parsed_data, self._instance_number)

        super().__init__()

    def construct(self, parser_header, parsed_data, instance_number: int = -1):
        for link in self._link_list:
            self.__setattr__(link.name, link.retrieve(parser_header, parsed_data, instance_number))

    def commit(self):
        for link in self._link_list:
            link.commit(self._parsed_header, self._parsed_data, self.__getattribute__(link.name))

    @staticmethod
    def _parse_object(parsed_data, **kwargs):
        pass

    @staticmethod
    def _reconstruct_object(parsed_header, parsed_data, objects, **kwargs):
        pass
