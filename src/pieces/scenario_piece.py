from src.helper.parser import Parser


class ScenarioPiece:
    def __init__(self, piece_type, data, data_list=None):
        self.piece_type = piece_type
        self.data = data
        self.data_list = data_list

    def set_data(self, data_list):
        if len(data_list) == len(self.data):
            self.data_list = data_list
        else:
            ValueError("Data list isn't the same size as the DataType list")

    def set_data_from_generator(self, generator):
        parser = Parser()
        self.data_list = list()
        for i, retriever in enumerate(self.data):
            self.data_list.append(parser.retrieve_value(generator, retriever))

    def _to_string(self):
        represent = self.piece_type + ": \n"

        for i, val in enumerate(self.data):
            data = self.data_list[i] if self.data_list and self.data_list[i] is not None else "<Empty>"
            represent += "\t" + val.name + ": " + str(data) + " (" + str(val.datatype.to_simple_string()) + ")\n"

        return represent

    def __repr__(self):
        return self._to_string()

    def __str__(self):
        return self._to_string()
