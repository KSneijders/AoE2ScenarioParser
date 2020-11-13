import abc

from AoE2ScenarioParser.helper import parser
from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper.retriever import get_retriever_by_name


class AoE2Piece:
    dependencies = {}

    def __init__(self, piece_type, retrievers, parser_obj=None, data=None):
        self.piece_type = piece_type
        self.retrievers = retrievers
        self.parser = parser_obj
        if data:
            self.set_data(data)

        for retriever in retrievers:
            if retriever.name in self.__class__.dependencies.keys():
                for key, value in self.__class__.dependencies[retriever.name].items():
                    setattr(retriever, key, value)

    @staticmethod
    @abc.abstractmethod
    def defaults():
        return {}

    def __getattr__(self, name):
        """
        Providing a default way to access retriever data labeled 'name'
        """
        try:
            return get_retriever_by_name(self.retrievers, name).data
        except:
            raise AttributeError("No attribute retriever named \'" + name + "\' in piece \'" + str(type(self)) + "\'")

    def __setattr__(self, name, value):
        """
        Trying to edit retriever data labeled 'name' if available
        """
        if 'retrievers' not in self.__dict__:
            super().__setattr__(name, value)
        else:
            retriever = get_retriever_by_name(self.retrievers, name)
            if retriever is None:
                super().__setattr__(name, value)
            else:
                retriever.data = value

    def set_data(self, data):
        if len(data) == len(self.retrievers):
            for i in range(0, len(data)):
                self.retrievers[i].data = data[i]
        else:
            print(f"\nError in: {self.__class__.__name__}")
            print(f"Data: ({len(data)}) "
                  f"{helper.pretty_print_list([f'{i}: {str(x)}' for i, x in enumerate(data)])}")
            print(f"Retrievers: ({len(self.retrievers)}) "
                  f"{helper.pretty_print_list([f'{i}: {str(x)}' for i, x in enumerate(self.retrievers)])}")
            raise ValueError("Data list isn't the same size as the DataType list")

    def get_value(self, retriever_key):
        return get_retriever_by_name(self.retrievers, retriever_key).data

    def get_length(self):
        total_length = 0
        try:
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
        except TypeError:
            print(self.retrievers)
        return total_length

    def set_data_from_generator(self, generator, pieces=None):
        if self.parser:
            for i, retriever in enumerate(self.retrievers):
                try:
                    retriever.data, status = self.parser.retrieve_value(generator, retriever, self.retrievers, pieces)
                    if status is not None:
                        raise status
                except Exception as e:
                    print(f"[{e.__class__.__name__}] AoE2Piece.set_data_from_generator: \n\tRetriever: {retriever}\n")
                    raise e

    def _entry_to_string(self, name, data, datatype):
        return "\t" + name + ": " + data + " (" + datatype + ")\n"

    def get_header_string(self):
        return "######################## " + self.piece_type + " ######################## [PIECE]"

    def get_byte_structure_as_string(self, skip_retrievers=None):
        if skip_retrievers is None:
            skip_retrievers = []

        byte_structure = "\n" + self.get_header_string()

        for retriever in self.retrievers:
            if retriever.name in skip_retrievers:
                continue
            byte_structure += "\n"

            listed_retriever_data = parser.listify(retriever.data)
            struct_header_set = False
            for struct in listed_retriever_data:
                if isinstance(struct, AoE2Piece):
                    if not struct_header_set:
                        byte_structure += f"\n{'#'*27} {retriever.name} ({retriever.datatype.to_simple_string()})"
                        struct_header_set = True
                    byte_structure += struct.get_byte_structure_as_string()
            # Struct Header was set. Retriever was struct, data retrieved using recursion. Next retriever.
            if struct_header_set:
                byte_structure += f"{'#'*27} End of: {retriever.name} ({retriever.datatype.to_simple_string()})\n"
                continue

            retriever_data_bytes = parser.retriever_to_bytes(retriever)
            if retriever_data_bytes is None:
                return byte_structure
            else:
                retriever_data_bytes = retriever_data_bytes.hex()

            retriever_short_string = retriever.get_short_str()
            retriever_data_hex = helper.create_textual_hex(retriever_data_bytes, space_distance=2,
                                                           enter_distance=24)

            if "\n" in retriever_data_hex:
                split_hex = retriever_data_hex.split("\n")
                if "\r\n" in retriever_short_string:
                    split_data_string = retriever_short_string.split("\r\n")

                    split_hex_length = len(split_hex)
                    split_data_string_length = len(split_data_string)
                    lines = max(split_hex_length, split_data_string_length)

                    combined_strings = []
                    for i in range(0, lines):
                        combined_strings.append(
                            helper.add_suffix_chars(split_hex[i] if i < split_hex_length else "", " ", 28) +
                            (split_data_string[i] if i < split_data_string_length else "")
                        )

                    byte_structure += "\n".join(combined_strings)
                else:
                    split_hex[0] = helper.add_suffix_chars(split_hex[0], " ", 28) + retriever_short_string
                    byte_structure += "\n".join(split_hex)
            else:
                byte_structure += helper.add_suffix_chars(retriever_data_hex, " ", 28) + retriever_short_string

        return byte_structure + "\n"

    def __str__(self):
        represent = self.piece_type + ": \n"

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
