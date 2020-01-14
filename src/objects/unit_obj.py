from src.helper.retriever import find_retriever
from src.objects.aoe2_object import AoE2Object


class UnitObject(AoE2Object):
    def __init__(self,
                 x,
                 y,
                 z,
                 id_on_map,
                 unit_id,
                 status,
                 rotation,
                 animation_frame,
                 garrisoned_in_id
                 ):

        super().__init__(locals())

    @staticmethod
    def parse_object(parsed_data, **kwargs):  # Expected {unit=unitStruct}
        unit = kwargs['unit']

        return UnitObject(
            x=find_retriever(unit.retrievers, "X position").data,
            y=find_retriever(unit.retrievers, "Y position").data,
            z=find_retriever(unit.retrievers, "Z position").data,
            id_on_map=find_retriever(unit.retrievers, "ID").data,
            unit_id=find_retriever(unit.retrievers, "Unit 'constant'").data,
            status=find_retriever(unit.retrievers, "Status").data,
            rotation=find_retriever(unit.retrievers, "Rotation, in radians").data,
            animation_frame=find_retriever(unit.retrievers, "Initial animation frame").data,
            garrisoned_in_id=find_retriever(unit.retrievers, "Garrisoned in: ID").data,
        )

    @staticmethod
    def reconstruct_object(parsed_data, objects, **kwargs):
        pass
