from abc import ABC

from AoE2ScenarioParser.pieces.aoe2_file_part import AoE2FilePart


class AoE2Piece(AoE2FilePart, ABC):

    def __init__(self, name, retrievers):
        super().__init__(name, retrievers)

    def get_header_string(self):
        return "######################## " + self.name + " ######################## [PIECE]"

    def __str__(self):
        represent = self.name + ": \n"

        for i, val in enumerate(self.retrievers):
            if type(self.retrievers[i].data) is list and len(self.retrievers[i].data) > 0:
                if isinstance(self.retrievers[i].data[0], AoE2Piece):
                    represent += "\t" + val.name + ": [\n"
                    for x in self.retrievers[i].data:
                        represent += "\t\t" + str(x)
                    represent += "\t]\n"
                else:
                    represent += self._entry_to_string(
                        val.name,
                        str(self.retrievers[i].data),
                        str(val.datatype.to_simple_string())
                    )
            else:
                if self.retrievers[i].data is not None:
                    data = self.retrievers[i].data
                else:
                    data = "None"
                represent += self._entry_to_string(val.name, str(data), str(val.datatype.to_simple_string()))

        return represent

    def __repr__(self):
        return type(self).__name__
