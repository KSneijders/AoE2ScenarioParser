from src.helper.retriever import find_retriever
from src.objects.aoe2_object import AoE2Object


class PlayerObject(AoE2Object):
    def __init__(self):
        super().__init__()

    def set_from_pieces(self, file_header_piece):
        retrievers = file_header_piece.retrievers
        data_dict = dict()

        player_data_one = {
            "Active": "active",
            "Human": "human",
            "Civilization": "civilization"
        }

        for attribute in player_data_one.keys():
            data_dict[player_data_one[attribute]] = find_retriever(retrievers, attribute).data

        self.data_dict = data_dict
