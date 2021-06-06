from __future__ import annotations

from enum import Enum
from typing import Dict

from AoE2ScenarioParser.helper import bytes_parser, string_manipulations
from AoE2ScenarioParser.helper.incremental_generator import IncrementalGenerator
from AoE2ScenarioParser.helper.list_functions import listify
from AoE2ScenarioParser.helper.pretty_format import pretty_format_list
from AoE2ScenarioParser.helper.string_manipulations import create_textual_hex, insert_char
from AoE2ScenarioParser.sections.aoe2_struct_model import AoE2StructModel, model_dict_from_structure
from AoE2ScenarioParser.sections.dependencies.dependency import handle_retriever_dependency
from AoE2ScenarioParser.sections.retrievers.retriever import Retriever, duplicate_retriever_map, reset_retriever_map


class SectionLevel(Enum):
    TOP_LEVEL = 0
    STRUCT = 1


class AoE2FileSection:
    def __init__(self, name, retriever_map, struct_models=None, level=SectionLevel.TOP_LEVEL):
        if struct_models is None:
            struct_models = {}

        self.name: str = name
        self.retriever_map = retriever_map
        self.byte_length: int = -1
        self.struct_models: Dict[str, AoE2StructModel] = struct_models
        self.level: SectionLevel = level

    @classmethod
    def from_model(cls, model, set_defaults=False) -> AoE2FileSection:
        """
        Create a copy (what was called struct before) from a model.

        Args:
            model (AoE2StructModel): The model to copy from
            set_defaults (bool): If retrievers need to be set to the default values

        Returns:
            An AoE2FileSection instance based on the model
        """
        duplicate_rmap = duplicate_retriever_map(model.retriever_map)
        if set_defaults:
            reset_retriever_map(duplicate_rmap)

        return cls(
            name=model.name,
            retriever_map=duplicate_rmap,
            struct_models=model.structs,
            level=SectionLevel.STRUCT
        )

    @classmethod
    def from_structure(cls, section_name, structure):
        retriever_map = {}
        for name, attr in structure.get('retrievers').items():
            retriever_map[name] = Retriever.from_structure(name, attr)

        structs = model_dict_from_structure(structure)
        return cls(section_name, retriever_map, structs)

    def get_data_as_bytes(self):
        result = []
        retriever: Retriever
        for retriever in self.retriever_map.values():
            result.append(retriever.get_data_as_bytes())
        return b''.join(result)

    def set_data_from_generator(self, igenerator: IncrementalGenerator, sections: Dict[str, AoE2FileSection]) -> None:
        """
        Fill data from all retrievers with data from the given generator. Generator is expected to return bytes.
        Bytes will be parsed based on the retrievers. The total length of bytes read to fill this section is also stored
        in this section as `byte_length`.

        Args:
            igenerator: A generator from a binary scenario file
            sections: A list of sections to reference when the retrievers have
                dependencies to or from them.
        """
        total_length = 0
        for retriever in self.retriever_map.values():
            try:
                handle_retriever_dependency(retriever, "construct", self, sections)
                if retriever.datatype.type == "struct":
                    retriever.data = []
                    struct_name = retriever.datatype.var[7:]  # 7 == len("struct:") >> Removing struct naming prefix
                    for _ in range(retriever.datatype.repeat):
                        model = self.struct_models.get(struct_name)
                        if model is None:
                            raise ValueError(f"Model '{struct_name}' not found. Likely not defined in structure.")

                        struct = AoE2FileSection.from_model(model)
                        struct.set_data_from_generator(igenerator, sections)
                        retriever.data.append(struct)

                        total_length += struct.byte_length
                else:
                    retrieved_bytes = bytes_parser.retrieve_bytes(igenerator, retriever)
                    retriever.set_data_from_bytes(retrieved_bytes)

                    total_length += sum([len(raw_bytes) for raw_bytes in retrieved_bytes])
            except (TypeError, ValueError) as e:
                if retriever.datatype.type == "struct":
                    print(struct.get_byte_structure_as_string(sections))
                print(f"\n\n[{e.__class__.__name__}] Occurred while setting data in:\n\t{retriever}")
                raise e

        self.byte_length = total_length

    def set_data(self, data, sections):
        retrievers = self.retriever_map.values()

        if len(data) == len(retrievers):
            for i in range(len(data)):
                retrievers[i].data = data[i]

                if hasattr(retrievers[i], 'on_construct'):
                    handle_retriever_dependency(retrievers[i], "construct", self, sections)
        else:
            print(f"\nError in: {self.__class__.__name__}")
            print(f"Data: (len: {len(data)}) "
                  f"{pretty_format_list([f'{i}: {str(x)}' for i, x in enumerate(data)])}")
            print(f"Retrievers: (len: {len(retrievers)}) "
                  f"{pretty_format_list([f'{i}: {str(x)}' for i, x in enumerate(self.retriever_map.values())])}")
            raise ValueError("Data list isn't the same size as the DataType list")

    def __getattr__(self, item):
        """Providing a default way to access retriever data labeled 'name'"""
        if 'retriever_map' not in self.__dict__:
            return super().__getattribute__(item)
        else:
            retriever = self.retriever_map[item]
            if retriever is None:
                return super().__getattribute__(item)
            else:
                return retriever.data

    def __setattr__(self, name, value):
        """Trying to edit retriever data labeled 'name' if available"""
        if 'retriever_map' not in self.__dict__:
            super().__setattr__(name, value)
        else:
            try:
                self.retriever_map[name].data = value
            except KeyError:
                super().__setattr__(name, value)

    def _entry_to_string(self, name, data, datatype):
        prefix = "\t"
        if self.level == SectionLevel.STRUCT:
            prefix = "\t\t\t"
        if 'str' in datatype:
            data = string_manipulations.q_str(data)
        return f"{prefix}{name}: {data} ({datatype})\n"

    def get_header_string(self):
        if self.level == SectionLevel.TOP_LEVEL:
            return "######################## " + self.name + " ######################## [SECTION]"
        elif self.level == SectionLevel.STRUCT:
            return "############ " + self.name + " ############  [STRUCT]"

    def get_byte_structure_as_string(self, sections, skip_retrievers=None):
        if skip_retrievers is None:
            skip_retrievers = []

        byte_structure = "\n" + self.get_header_string()

        for key, retriever in self.retriever_map.items():
            if key in skip_retrievers:
                continue
            byte_structure += "\n"

            listed_retriever_data = listify(retriever.data)
            struct_header_set = False
            for struct in listed_retriever_data:
                if isinstance(struct, AoE2FileSection):
                    if not struct_header_set:
                        byte_structure += f"\n{'#' * 27} {key} ({retriever.datatype.to_simple_string()})"
                        struct_header_set = True
                    byte_structure += struct.get_byte_structure_as_string(sections)
            # Struct Header was set. Retriever was struct, data retrieved using recursion. Next retriever.
            if struct_header_set:
                byte_structure += f"{'#' * 27} End of: {key} ({retriever.datatype.to_simple_string()})\n"
                continue

            retriever_data_bytes = retriever.get_data_as_bytes()
            if retriever_data_bytes is None:
                return byte_structure
            else:
                retriever_data_bytes = retriever_data_bytes.hex()

            retriever_short_string: str = retriever.get_short_str()
            retriever_hex = create_textual_hex(retriever_data_bytes, space_distance=2, enter_distance=24)

            split_hex = retriever_hex.split("\n")
            split_hex_length = len(split_hex)

            split_data_string = retriever_short_string.replace('\x00', ' ').splitlines()
            data_lines = []
            for x in split_data_string:
                if len(x) > 120:
                    data_lines += [f'\t{x}' for x in insert_char(x, '\r\n', 120).splitlines()]
                else:
                    data_lines.append(x)
            split_data_length = len(data_lines)

            lines = max(split_hex_length, split_data_length)

            combined_strings = []
            for i in range(0, lines):
                hex_part = split_hex[i] if i < split_hex_length else ""
                data_part = data_lines[i] if i < split_data_length else ""
                combined_strings.append(
                    string_manipulations.add_suffix_chars(hex_part, " ", 28) + data_part)

            byte_structure += "\n".join(combined_strings)

        return byte_structure + "\n"

    def __str__(self):
        represent = self.name + ": \n"

        for retriever in self.retriever_map.values():
            if type(retriever.data) is list and len(retriever.data) > 0:
                if isinstance(retriever.data[0], AoE2FileSection):
                    represent += "\t" + retriever.name + ": [\n"
                    for x in retriever.data:
                        represent += "\t\t" + str(x)
                    represent += "\t]\n"
                else:
                    represent += self._entry_to_string(
                        retriever.name,
                        str(retriever.data),
                        str(retriever.datatype.to_simple_string())
                    )
            else:
                data = retriever.data or "None"
                represent += self._entry_to_string(
                    retriever.name, str(data), str(retriever.datatype.to_simple_string())
                )

        return represent

    def __repr__(self):
        return f"<AoE2FileSection> {self.name}"
