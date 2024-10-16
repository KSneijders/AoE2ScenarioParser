from __future__ import annotations

from enum import Enum
from struct import error
from typing import Dict, List, TYPE_CHECKING
from uuid import UUID

from AoE2ScenarioParser.exceptions.asp_exceptions import UnknownErrorDuringReadingIterationError
from AoE2ScenarioParser.helper import bytes_parser
from AoE2ScenarioParser.helper.list_functions import listify
from AoE2ScenarioParser.helper.pretty_format import pretty_format_dict
from AoE2ScenarioParser.helper.string_manipulations import create_textual_hex, insert_char, add_suffix_chars, q_str, \
    trunc_string, add_tabs
from AoE2ScenarioParser.sections.aoe2_struct_model import AoE2StructModel, model_dict_from_structure
from AoE2ScenarioParser.sections.dependencies.dependency import handle_retriever_dependency
from AoE2ScenarioParser.sections.retrievers.retriever import Retriever, reset_retriever_map

if TYPE_CHECKING:
    from AoE2ScenarioParser.helper.incremental_generator import IncrementalGenerator


class SectionLevel(Enum):
    """This enum class indicates the section level of the structure"""
    TOP_LEVEL = 0
    STRUCT = 1


class SectionName(Enum):
    """This enum class indicates the different sections in the scenario file"""
    FILE_HEADER = "FileHeader"
    DATA_HEADER = "DataHeader"
    MESSAGES = "Messages"
    CINEMATICS = "Cinematics"
    BACKGROUND_IMAGE = "BackgroundImage"
    PLAYER_DATA_TWO = "PlayerDataTwo"
    GLOBAL_VICTORY = "GlobalVictory"
    DIPLOMACY = "Diplomacy"
    OPTIONS = "Options"
    MAP = "Map"
    UNITS = "Units"
    TRIGGERS = "Triggers"
    FILES = "Files"


class AoE2FileSection:
    """
    Multiple retrievers and structures containing related data are grouped together under one file section. This class
    is used to construct, manage and commit all the retrievers and structures inside a file section.

    Utilises the AoE2StructModel to create multiple of the same structure. These copies are what is used to store the
    data from a scenario file
    """

    def __init__(
            self,
            name: str,
            retriever_map: Dict[str, 'Retriever'],
            uuid: UUID,
            struct_models: Dict[str, 'AoE2StructModel'] = None,
            level: SectionLevel = SectionLevel.TOP_LEVEL
    ):
        """
        Args:
            name: The name of the file section
            retriever_map: A dict containing all the retrievers for this file section
            uuid: The universally unique identifier for the scenario that this file section belongs to
            struct_models: A dict containing all the structures for this file section
            level: This variable tells if a structure or file section is at the top level of the scenario or a struct.
        """
        if struct_models is None:
            struct_models = {}

        self.name: str = name
        self.retriever_map: Dict[str, 'Retriever'] = retriever_map
        self._uuid = uuid
        self.byte_length: int = -1
        self.struct_models: Dict[str, AoE2StructModel] = struct_models
        self.level: SectionLevel = level

    def find_struct_model_by_retriever(self, retriever: 'Retriever') -> AoE2StructModel:
        prefix = "struct:"

        struct_datatype = retriever.datatype.var
        if not struct_datatype.startswith(prefix):
            raise ValueError(f"Unable to retrieve model '{struct_datatype}' from file section. "
                             f"Possible model names: {self.struct_models.keys()}")

        struct_name = struct_datatype[len(prefix):]
        return self.struct_models[struct_name]

    @classmethod
    def from_model(cls, model: AoE2StructModel, uuid: UUID, set_defaults: bool = False) -> AoE2FileSection:
        """
        Create a file section based on the given AoE2StructModel.

        Args:
            model: The model to copy from
            uuid: The universally unique identifier of the scenario
            set_defaults: If retrievers need to be set to the default values

        Returns:
            An AoE2FileSection instance based on the model
        """
        duplicate_rmap = {k: e.duplicate() for k, e in model.retriever_map.items()}

        if set_defaults:
            reset_retriever_map(duplicate_rmap)

        return cls(
            name=model.name,
            retriever_map=duplicate_rmap,
            uuid=uuid,
            struct_models=model.structs,
            level=SectionLevel.STRUCT
        )

    @classmethod
    def from_structure(cls, section_name: str, structure: Dict[str, Dict], uuid: UUID) -> 'AoE2FileSection':
        """
        Constructs all retrievers and structures from the given file section (dict)

        Args:
            section_name (str): This is the name of the file section
            structure (Dict[str, Dict]): The dict representation of the file section to build
            uuid (UUID): The universally unique identifier of the scenario that this file section belongs to

        Returns:
            An AoE2FileSection instance representing the given file section structure
        """
        retriever_map = {}
        log_all_retrievers = structure.get('log', False)
        for name, attr in structure.get('retrievers').items():
            if log_all_retrievers:
                attr['log'] = True
            retriever_map[name] = Retriever.from_structure(name, attr)

        structs = model_dict_from_structure(structure)
        return cls(section_name, retriever_map, uuid, structs)

    def get_data_as_bytes(self) -> bytes:
        """
        Converts the data of a file section into bytes

        Returns:
            The bytes representing the file section
        """
        result: List[bytes] = []
        for retriever in self.retriever_map.values():
            result.append(retriever.get_data_as_bytes())
        return b''.join(result)

    def set_data_from_generator(self, igenerator: 'IncrementalGenerator') -> None:
        """
        Sets all the data for the retrievers and structures of the file section from the given generator
        (bytes of the scenario file). Each retriever (and retrieves inside structures) parses a set number of bytes
        based on its datatype. The total number of bytes parsed is then stored in the self.bytes_length variable

        Args:
            igenerator: A generator from a binary scenario file

        Raises:
            ValueError: if a structure inside a model is not defined
        """
        total_length = 0
        for retriever in self.retriever_map.values():
            try:
                handle_retriever_dependency(retriever, "construct", self, self._uuid)
                if retriever.datatype.type == "struct":
                    struct_name = retriever.datatype.get_struct_name()

                    structs: List['AoE2FileSection'] = []
                    for i in range(retriever.datatype.repeat):
                        try:
                            model = self.struct_models.get(struct_name)
                            if model is None:
                                raise ValueError(f"Model '{struct_name}' not found. Likely not defined in structure.")

                            struct = self._create_struct(model, igenerator)
                            structs.append(struct)

                            total_length += struct.byte_length
                        except Exception as e:
                            if len(structs) == 0:
                                raise e

                            print("#" * 100)
                            print(" " * 33 + "CURRENT PROGRESS STRUCTURE CONTENT")
                            print("#" * 100 + '\n\n')

                            length = len(structs) - 1
                            for index, struct in enumerate(structs):
                                print(f"[Index: {index}/{length}] " + struct.get_byte_structure_as_string().lstrip())

                            raise e

                    retriever.set_data(structs, affect_dirty=False)
                else:
                    retrieved_bytes = bytes_parser.retrieve_bytes(igenerator, retriever)
                    self._fill_retriever_with_bytes(retriever, retrieved_bytes)

                    total_length += sum([len(raw_bytes) for raw_bytes in retrieved_bytes])

            except Exception as e:
                print("\nCurrent Struct Progress: ")
                print(add_tabs(self.get_byte_structure_as_string(), 1))
                print("\n\n")
                raise e

        self.byte_length = total_length

    def _fill_retriever_with_bytes(self, retriever: 'Retriever', retrieved_bytes: List[bytes]) -> None:
        """
        With the given bytes, sets the data of the provided retriever.

        If setting the data fails and a ValueError is raised, this function deals with the error logging (and re-raises
        the error).

        Args:
            retriever: The retriever to set the data for
            retrieved_bytes: The bytes to set the data from

        Raises:
            ValueError: if the bytes given cannot be used to set the data of the retriever provided
        """
        try:
            retriever.set_data_from_bytes(retrieved_bytes)
        except Exception as e:
            print("\n\n" + "#" * 120)
            print(f"[{e.__class__.__name__}] Occurred while setting data in:\n\t{retriever}")
            print("#" * 120)
            # print(trunc_string(self.get_byte_structure_as_string(), length=10000))
            print(self.get_byte_structure_as_string())
            raise e

    def _create_struct(self, model: 'AoE2StructModel', igenerator: 'IncrementalGenerator') -> 'AoE2FileSection':
        """
        Creates an AoE2FileSection from the given model using data from the provided generator

        If setting the data fails and a ValueError is raised, this function deals with the error logging (and re-raises
        the error).

        Args:
            model: The model to make the AoE2FileSection from
            igenerator: The generator to set the data for the file section from

        Returns:
            An AoE2FileSection object created from the given model with its data set according to the given generator
        """
        struct = AoE2FileSection.from_model(model, uuid=self._uuid)

        try:
            struct.set_data_from_generator(igenerator)
        except Exception as exception:
            print("\n" + "#" * 120)
            print(f"[{exception.__class__.__name__}] Occurred while setting data in: {struct.name}"
                  f"\n\tContent of {self.name}:")
            print("#" * 120)
            # print(trunc_string(self.get_byte_structure_as_string(), length=10000))
            print(self.get_byte_structure_as_string())
            raise exception

        return struct

    def __getattr__(self, item):
        """Providing a default way to access retriever data labeled 'name'"""
        if 'retriever_map' not in self.__dict__:
            return super().__getattribute__(item)
        elif item.startswith("__"):
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

    def _entry_to_string(self, name: str, data: str, datatype: str) -> str:
        """
        Formats the given data into a string. Example::

            version: 1.45 (1 * c4)

        Args:
            name: The name of the value
            data: The value itself
            datatype: The datatype of the value

        Returns:
            Formatted string representation of the given data
        """
        prefix = "\t"
        if self.level == SectionLevel.STRUCT:
            prefix = "\t\t\t"
        if 'str' in datatype:
            data = q_str(data)
        return f"{prefix}{name}: {data} ({datatype})\n"

    def get_header_string(self) -> str:
        """
        Returns:
            The name of the header for the file section
        """
        if self.level == SectionLevel.TOP_LEVEL:
            return f"######################## {self.name} ######################## [SECTION]"
        elif self.level == SectionLevel.STRUCT:
            return f"############ {self.name} ############  [STRUCT]"

    def get_byte_structure_as_string(self):
        """
        Recursively converts the retrievers of a file section and their data into a readable format. An
        example with this format is shown below::

            ########################### units (1954 * struct:UnitStruct)
            ############ UnitStruct ############  [STRUCT]
            00 00 70 42                 x (1 * f32): 60.0
            00 00 70 42                 y (1 * f32): 60.0
            00 00 00 00                 z (1 * f32): 0.0
            52 05 00 00                 reference_id (1 * s32): 1362
            89 02                       unit_const (1 * u16): 649
            02                          status (1 * u8): 2
            00 00 00 00                 rotation (1 * f32): 0.0
            00 00                       initial_animation_frame (1 * u16): 0
            ff ff ff ff                 garrisoned_in_id (1 * s32): -1

        Returns:
            A string showing the data in each retriever of the file section
        """
        byte_structure = "\n" + self.get_header_string()

        for key, retriever in self.retriever_map.items():
            byte_structure += "\n"

            listed_retriever_data = listify(retriever.data)
            struct_header_set = False
            for struct in listed_retriever_data:
                if isinstance(struct, AoE2FileSection):
                    if not struct_header_set:
                        byte_structure += f"\n{'#' * 27} {key} ({retriever.datatype.to_simple_string()})"
                        struct_header_set = True
                    byte_structure += struct.get_byte_structure_as_string()
            # Struct Header was set. Retriever was struct, data retrieved using recursion. Next retriever.
            if struct_header_set:
                byte_structure += f"{'#' * 27} End of: {key} ({retriever.datatype.to_simple_string()})\n"
                continue

            retriever_data_bytes = retriever.get_data_as_bytes().hex()
            retriever_hex = create_textual_hex(retriever_data_bytes, space_distance=2, enter_distance=24)

            split_hex = retriever_hex.split("\n")
            split_hex_length = len(split_hex)

            retriever_short_string: str = retriever.get_short_str()
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
                combined_strings.append(add_suffix_chars(hex_part, " ", 28) + data_part)

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
