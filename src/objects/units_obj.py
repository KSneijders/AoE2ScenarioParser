from src.objects.aoe2_object import AoE2Object
from src.helper.retriever import find_retriever
from src.objects.unit_obj import UnitObject


class UnitsObject(AoE2Object):
    def __init__(self,
                 units
                 ):

        super().__init__(locals())

    @staticmethod
    def parse_object(parsed_data, **kwargs):
        object_piece = parsed_data['UnitsPiece']
        units_per_player = find_retriever(object_piece.retrievers, "Player Units").data

        player_units = []

        for player_id in range(0, 9):  # 0 Gaia & 1-8 Players:
            player_units.append([])
            units = find_retriever(units_per_player[player_id].retrievers, "Units").data

            for unit in units:
                player_units[player_id].append(
                    UnitObject.parse_object(parsed_data, unit=unit)
                )

        return UnitsObject(
            units=player_units
        )

    @staticmethod
    def reconstruct_object(parsed_data, objects, **kwargs):
        pass
