from src.helper.parser import Parser


class ScenarioPiece:
    def __init__(self, parser, piece_type, retrievers, data_list=None):
        self.parser = parser
        self.piece_type = piece_type
        self.retrievers = retrievers
        self.data_list = data_list

    def set_data(self, data_list):
        if len(data_list) == len(self.retrievers):
            self.data_list = data_list

            for i in range(0, len(data_list)):
                self.retrievers[i].on_success(data_list[i])
        else:
            ValueError("Data list isn't the same size as the DataType list")

    def set_data_from_generator(self, generator):
        self.data_list = list()
        for i, retriever in enumerate(self.retrievers):
            self.data_list.append(self.parser.retrieve_value(generator, retriever))

    def _entry_to_string(self, name, data, datatype):
        return "\t" + name + ": " + data + " (" + datatype + ")\n"

    def _to_string(self):
        represent = self.piece_type + ": \n"

        for i, val in enumerate(self.retrievers):
            if type(self.data_list[i]) is list and len(self.data_list[i]) > 0:
                if isinstance(self.data_list[i][0], ScenarioPiece):
                    represent += "\t" + val.name + ": [\n"
                    for x in self.data_list[i]:
                        represent += "\t\t" + str(x)
                    represent += "\t]\n"
            else:
                data = self.data_list[i] if self.data_list and self.data_list[i] is not None else "<Empty>"
                represent += self._entry_to_string(val.name, str(data), str(val.datatype.to_simple_string()))

        return represent

    def __repr__(self):
        return self._to_string()

    def __str__(self):
        return self._to_string()
