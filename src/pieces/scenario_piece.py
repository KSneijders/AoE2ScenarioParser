from src.helper.parser import datatype_to_type_length


class ScenarioPiece:
    def __init__(self, parser, piece_type, retrievers, data=None):
        self.parser = parser
        self.piece_type = piece_type
        self.retrievers = retrievers
        self.data = data

    def get_length(self):
        total_length = 0
        for i in range(0, len(self.retrievers)):
            datatype, length = datatype_to_type_length(self.retrievers[i].datatype.var)
            total_length += length
            if datatype == "str":
                total_length += len(self.data[i])
        return total_length

    def set_data(self, data):
        if len(data) == len(self.retrievers):
            self.data = data

            for i in range(0, len(data)):
                self.retrievers[i].on_success(data[i])
        else:
            ValueError("Data list isn't the same size as the DataType list")

    def set_data_from_generator(self, generator):
        self.data = list()
        for i, retriever in enumerate(self.retrievers):
            self.data.append(self.parser.retrieve_value(generator, retriever))

    def _entry_to_string(self, name, data, datatype):
        return "\t" + name + ": " + data + " (" + datatype + ")\n"

    def _to_string(self):
        represent = self.piece_type + ": \n"

        for i, val in enumerate(self.retrievers):
            if type(self.data[i]) is list and len(self.data[i]) > 0:
                if isinstance(self.data[i][0], ScenarioPiece):
                    represent += "\t" + val.name + ": [\n"
                    for x in self.data[i]:
                        represent += "\t\t" + str(x)
                    represent += "\t]\n"
                else:
                    represent += self._entry_to_string(val.name, str(self.data[i]), str(val.datatype.to_simple_string()))
            else:
                data = self.data[i] if self.data and self.data[i] is not None else "<Empty>"
                represent += self._entry_to_string(val.name, str(data), str(val.datatype.to_simple_string()))

        return represent

    def __repr__(self):
        return self._to_string()

    def __str__(self):
        return self._to_string()
