from src.helper.retriever import find_retriever
from src.objects.aoe2_object import AoE2Object


class FileHeaderObject(AoE2Object):

    attribute_mapping = {
        # Name In Piece: Name in Object
        "Version": "version",
        "Savable": "savable",
        "Timestamp of Last Save": "timestamp",
        "Scenario Instructions": "scenario_instr",
        "Player Count": "player_count",
        "Steam name": "steam_name"
    }

    def __init__(self):
        super().__init__()

    def set_from_pieces(self, file_header_piece):
        retrievers = file_header_piece.retrievers
        data_dict = dict()

        for attribute in self.attribute_mapping.keys():
            data_dict[self.attribute_mapping[attribute]] = find_retriever(retrievers, attribute).data

        self.data_dict = data_dict
