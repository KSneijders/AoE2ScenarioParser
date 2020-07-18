from AoE2ScenarioParser.pieces.aoe2_piece import AoE2Piece


class AoE2Object:
    def __init__(self, aoe2_piece):
        self.aoe2_piece = aoe2_piece
        if aoe2_piece is not None:
            for retriever in aoe2_piece.retrievers:
                setattr(self, retriever.name, self._get_data_as_obj(retriever.data))

    def _get_data_as_obj(self, data):
        if isinstance(data, list):
            return [self._get_data_as_obj(item) for item in data]

        if isinstance(data, AoE2Piece):
            if hasattr(data, 'HANDLER_TYPE'):
                return data.HANDLER_TYPE(data)
            return AoE2Object(data)

        return data

    def _save(self):
        for retriever in self.aoe2_piece.retrievers:
            retriever.data = self._save_data_as_obj(getattr(self, retriever.name))
            
    def _save_data_as_obj(self, attr):
        if isinstance(attr, list):
            return [self._save_data_as_obj(item) for item in attr]

        if isinstance(attr, AoE2Object):
            attr._save()
            return attr.aoe2_piece
            
        else:
            return attr

    def __repr__(self):
        return str(self.__class__.__name__) + ": " + str(self.__dict__)
