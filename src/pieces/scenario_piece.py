import src.helper.parser as parser


class ScenarioPiece:
    def __init__(self, parser, piece_type, retrievers, data=None):
        self.parser = parser
        self.piece_type = piece_type
        self.retrievers = retrievers
        if data is not None:
            self.set_data(data)

    def get_length(self):
        total_length = 0
        for i in range(0, len(self.retrievers)):
            datatype, length = parser.datatype_to_type_length(self.retrievers[i].datatype.var)

            if datatype == "struct":
                if type(self.retrievers[i].data) == list:
                    for continues_struct in self.retrievers[i].data:
                        length += continues_struct.get_length()
                else:
                    length = self.retrievers[i].data.get_length()
            elif datatype == "str":
                length = len(self.retrievers[i].data)
            total_length += length

        return total_length

    def set_data(self, data):
        if len(data) == len(self.retrievers):
            for i in range(0, len(data)):
                self.retrievers[i].set_data(data[i])
        else:
            ValueError("Data list isn't the same size as the DataType list")

    def set_data_from_generator(self, generator):
        for i, retriever in enumerate(self.retrievers):
            retriever.set_data(self.parser.retrieve_value(generator, retriever))

    def _entry_to_string(self, name, data, datatype):
        return "\t" + name + ": " + data + " (" + datatype + ")\n"

    def _to_string(self):
        represent = self.piece_type + ": \n"

        for i, val in enumerate(self.retrievers):
            if type(self.retrievers[i].data) is list and len(self.retrievers[i].data) > 0:
                if isinstance(self.retrievers[i].data[0], ScenarioPiece):
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
                    data = "<Empty>"
                represent += self._entry_to_string(val.name, str(data), str(val.datatype.to_simple_string()))

        return represent

    def __repr__(self):
        return self._to_string()

    def __str__(self):
        return self._to_string()
