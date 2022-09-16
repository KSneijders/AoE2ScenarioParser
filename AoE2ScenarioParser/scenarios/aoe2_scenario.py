from __future__ import annotations

import json
import uuid
import zlib
from pathlib import Path
from typing import Dict, Any, Type, TypeVar

import AoE2ScenarioParser.datasets.conditions as conditions
import AoE2ScenarioParser.datasets.effects as effects
from AoE2ScenarioParser import settings
from AoE2ScenarioParser.helper.exceptions import (
    InvalidScenarioStructureError, UnknownScenarioStructureError,
    UnknownStructureError
)
from AoE2ScenarioParser.helper.incremental_generator import IncrementalGenerator
from AoE2ScenarioParser.helper.printers import s_print
from AoE2ScenarioParser.helper.string_manipulations import create_textual_hex
from AoE2ScenarioParser.helper.version_check import python_version_check
from AoE2ScenarioParser.objects.aoe2_object_manager import AoE2ObjectManager
from AoE2ScenarioParser.objects.managers.map_manager import MapManager
from AoE2ScenarioParser.objects.managers.message_manager import MessageManager
from AoE2ScenarioParser.objects.managers.player_manager import PlayerManager
from AoE2ScenarioParser.objects.managers.trigger_manager import TriggerManager
from AoE2ScenarioParser.objects.managers.unit_manager import UnitManager
from AoE2ScenarioParser.scenarios.scenario_debug.compare import debug_compare
from AoE2ScenarioParser.scenarios.scenario_store import store
from AoE2ScenarioParser.scenarios.support.object_factory import ObjectFactory
from AoE2ScenarioParser.scenarios.support.scenario_actions import ScenarioActions
from AoE2ScenarioParser.sections.aoe2_file_section import AoE2FileSection

_ScenarioType = TypeVar('_ScenarioType', bound='AoE2Scenario')


class AoE2Scenario:
    """All scenario objects are derived from this class"""

    @property
    def trigger_manager(self) -> TriggerManager:
        """The trigger manager of the scenario"""
        return self._object_manager.managers['Trigger']

    @property
    def unit_manager(self) -> UnitManager:
        """The unit manager of the scenario"""
        return self._object_manager.managers['Unit']

    @property
    def map_manager(self) -> MapManager:
        """The map manager of the scenario"""
        return self._object_manager.managers['Map']

    @property
    def player_manager(self) -> PlayerManager:
        """The player manager of the scenario"""
        return self._object_manager.managers['Player']

    @property
    def message_manager(self) -> MessageManager:
        return self._object_manager.managers['Message']

    def __init__(self, source_location):
        self.source_location = source_location

        self.read_mode: str = "???"
        self.scenario_version: str = "???"
        self.game_version: str = "???"
        self.structure = {}
        self.sections: Dict[str, AoE2FileSection] = {}
        self._object_manager: AoE2ObjectManager | None = None

        # Used in debug functions
        self._file = None
        self._file_header = None
        self._decompressed_file_data = None

        self.uuid = uuid.uuid4()
        store.register_scenario(self)

        self.new = ObjectFactory(self.uuid)
        self.actions = ScenarioActions(self.uuid)

    @classmethod
    def from_file(cls: Type[_ScenarioType], filename: str, game_version: str) -> _ScenarioType:
        """
        Creates and returns an instance of the AoE2Scenario class from the given scenario file

        Args:
            filename: The path to the scenario file to create the object from
            game_version: The version of the game to create the object for

        Returns:
            An instance of the AoE2Scenario class (or any of its subclasses) which is the object representation of
            the given scenario file
        """
        python_version_check()

        s_print(f"\nReading file: '{filename}'", final=True, color="magenta")
        s_print("Reading scenario file...")
        igenerator = IncrementalGenerator.from_file(filename)
        s_print("Reading scenario file finished successfully.", final=True)

        scenario: _ScenarioType = cls(filename)
        scenario.read_mode = "from_file"
        scenario.game_version = game_version
        scenario.scenario_version = _get_file_version(igenerator)

        # Log game and scenario version
        s_print("\n############### Attributes ###############", final=True, color="blue")
        s_print(f">>> Game version: '{scenario.game_version}'", final=True, color="blue")
        s_print(f">>> Scenario version: {scenario.scenario_version}", final=True, color="blue")
        s_print("##########################################", final=True, color="blue")

        s_print(f"\nLoading scenario structure...")
        scenario._load_structure()
        _initialise_version_dependencies(scenario.game_version, scenario.scenario_version)
        s_print(f"Loading scenario structure finished successfully.", final=True)

        # scenario._initialize(igenerator)
        s_print("Parsing scenario file...", final=True)
        scenario._load_header_section(igenerator)
        scenario._load_content_sections(igenerator)
        s_print(f"Parsing scenario file finished successfully.", final=True)

        scenario._object_manager = AoE2ObjectManager(scenario.uuid)
        scenario._object_manager.setup()

        return scenario

    def _load_structure(self) -> None:
        """
        Loads the structure json for the scenario and game version specified into self.structure

        Raises:
            ValueError: if the game or scenario versions are not set
        """
        if self.game_version == "???" or self.scenario_version == "???":
            raise ValueError("Both game and scenario version need to be set to load structure")
        self.structure = _get_structure(self.game_version, self.scenario_version)

    def _load_header_section(self, raw_file_igenerator: IncrementalGenerator) -> None:
        """
        Reads and adds the header file section to the sections dict of the scenario.

        The header is stored decompressed and is the first thing in the scenario file. It is meta data for the scenario
        file and thus needs to be read before everything else (also the reason why its stored decompressed).

        Args:
            raw_file_igenerator: The generator to read the header section from
        """
        header = self._create_and_load_section('FileHeader', raw_file_igenerator)
        self._file_header = raw_file_igenerator.file_content[:raw_file_igenerator.progress]
        self._add_to_sections(header)

    def _load_content_sections(self, raw_file_igenerator: IncrementalGenerator) -> None:
        """
        Reads and adds all the remaining file sections from the structure file to the sections dict of the
        scenario.

        The sections after the header are compressed and are first decompressed using the -zlib.MAX_WBITS algorithm.

        Args:
            raw_file_igenerator: The generator to read the file sections from
        """
        self._decompressed_file_data = _decompress_bytes(raw_file_igenerator.get_remaining_bytes())

        data_igenerator = IncrementalGenerator(name='Scenario Data', file_content=self._decompressed_file_data)

        for section_name in self.structure.keys():
            if section_name == "FileHeader":
                continue
            try:
                section = self._create_and_load_section(section_name, data_igenerator)
                self._add_to_sections(section)
            except (ValueError, TypeError) as e:
                print(f"\n[{e.__class__.__name__}] AoE2Scenario.parse_file: \n\tSection: {section_name}\n")
                self.write_error_file(trail_generator=data_igenerator)
                raise e

    def _create_and_load_section(self, name: str, igenerator: IncrementalGenerator) -> AoE2FileSection:
        """
        Initialises a file section from its name and fills its retrievers with data from the given generator

        Args:
            name: The name of the file section
            igenerator: The generator to fill the data from

        Returns:
            An AoE2FileSection representing the given section name with its data initialised from the generator
        """
        s_print(f"\t🔄 Parsing {name}...", color="yellow")
        section = AoE2FileSection.from_structure(name, self.structure.get(name), self.uuid)
        s_print(f"\t🔄 Gathering {name} data...", color="yellow")
        section.set_data_from_generator(igenerator)
        s_print(f"\t✔ {name}", final=True, color="green")
        return section

    def _add_to_sections(self, section: AoE2FileSection) -> None:
        """
        Adds the given section to the sections dictionary

        Args:
            section: The section to add to the sections dictionary
        """
        self.sections[section.name] = section

    def remove_store_reference(self) -> None:
        """
        Removes the reference to this scenario object from the scenario store. Useful (~a must) when reading many
        scenarios in a row without needing earlier ones. Python likes to take up a lot of memory.
        Removing all references to an object will cause the memory to be cleared up.

        Warning: Remove all other references too!
            When using this function it's important to remove all other references to the scenario.
            So if save it in a dict or list, remove it from it.
            If you have variables referencing this scenario that you won't need anymore (and won't overwrite) delete
            them using: `del varname`.
        """
        store.remove_scenario(self.uuid)

    def commit(self) -> None:
        """Commit the changes to the retriever backend made within the managers."""
        self._object_manager.reconstruct()

    """ ##########################################################################################
    ####################################### Write functions ######################################
    ########################################################################################## """

    def write_to_file(self, filename: str, skip_reconstruction: bool = False) -> None:
        """
        Writes the scenario to a new file with the given filename

        Args:
            filename: The location to write the file to
            skip_reconstruction: If reconstruction should be skipped. If true, this will ignore all changes made
                using the managers (For example all changes made using trigger_manager).

        Raises:
            ValueError: if the setting DISABLE_ERROR_ON_OVERWRITING_SOURCE is not disabled and the source filename is
                the same as the filename being written to
        """
        self._write_from_structure(filename, skip_reconstruction)

    def _write_from_structure(self, filename: str, skip_reconstruction: bool = False) -> None:
        """
        Writes the scenario to a new file with the given filename

        Args:
            filename: The location to write the file to
            skip_reconstruction: If reconstruction should be skipped. If true, this will ignore all changes made
                using the managers (For example all changes made using trigger_manager).

        Raises:
            ValueError: if the setting DISABLE_ERROR_ON_OVERWRITING_SOURCE is not disabled and the source filename is
                the same as the filename being written to
        """
        if not settings.DISABLE_ERROR_ON_OVERWRITING_SOURCE and self.source_location == filename:
            raise ValueError(
                "Overwriting the source scenario file is disallowed. "
                "This behaviour can be changed through the settings."
            )
        if not skip_reconstruction:
            self.commit()

        s_print("\nFile writing from structure started...", final=True)
        binary = _get_file_section_data(self.sections.get('FileHeader'))

        binary_list_to_be_compressed = []
        for file_part in self.sections.values():
            if file_part.name == "FileHeader":
                continue
            binary_list_to_be_compressed.append(_get_file_section_data(file_part))

        compressed = _compress_bytes(b''.join(binary_list_to_be_compressed))

        with open(filename, 'wb') as f:
            f.write(binary + compressed)

        s_print("File writing finished successfully.", final=True)
        s_print(f"File successfully written to: '{filename}'", color="magenta", final=True)

    def write_error_file(self, filename: str = "error_file.txt", trail_generator: IncrementalGenerator = None) -> None:
        """
        Outputs the contents of the entire scenario file in a readable format. An example of the format is given below::

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

        Args:
            filename: The filename to write the error file to
            trail_generator: Write all the bytes remaining in this generator as a trail
        """
        self._debug_byte_structure_to_file(filename=filename, trail_generator=trail_generator)

    """ #############################################
    ################ Debug functions ################
    ############################################# """

    def _debug_compare(
            self,
            other: AoE2Scenario,
            filename: str = "differences.txt",
            commit: bool = False
    ) -> None:
        """
        Compare a scenario to a given scenario and report the differences found

        Args:
            other: The scenario to compare it to
            filename: The debug file to write the differences to (Defaults to "differences.txt")
            commit: If the scenarios need to commit their manager changes before comparing (Defaults to False)
        """
        debug_compare(self, other, filename, commit)

    def _debug_write_from_source(self, filename: str, datatype: str, write_bytes: bool = True) -> None:
        """
        Writes the decompressed scenario file as bytes or as hex text

        Args:
            filename: The filename to write to
            datatype: these are flags that indicate which parts of the file to include in the output. 'd' for
                decompressed file data, 'f' for the file, and 'h' for the header. Note: Only 'd' actually works at this
                time
            write_bytes: boolean to determine if the file needs to be written as bytes or hex text form
        """
        s_print("File writing from source started with attributes " + datatype + "...")
        file = open(filename, "wb" if write_bytes else "w")
        selected_parts = []
        for t in datatype:
            if t == "f":
                selected_parts.append(self._file)
            elif t == "h":
                selected_parts.append(self._file_header)
            elif t == "d":
                selected_parts.append(self._decompressed_file_data)
        parts = None
        for part in selected_parts:
            if parts is None:
                parts = part
                continue
            parts += part
        file.write(parts if write_bytes else create_textual_hex(parts.hex()))
        file.close()
        s_print("File writing finished successfully.")

    def _debug_byte_structure_to_file(self, filename, trail_generator: IncrementalGenerator = None, commit=False):
        """
        Outputs the contents of the entire scenario file in a readable format. An example of the format is given below::

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

        Args:
            filename: The filename to write the error file to
            trail_generator: Write all the bytes remaining in this generator as a trail
            commit: If the managers should commit their changes before writing this file.
        """
        if commit and hasattr(self, '_object_manager'):
            self.commit()

        s_print("\nWriting structure to file...", final=True)
        with open(filename, 'w', encoding=settings.MAIN_CHARSET) as f:
            result = []
            for section in self.sections.values():
                s_print(f"\t🔄 Writing {section.name}...")
                result.append(section.get_byte_structure_as_string())
                s_print(f"\t✔ {section.name}", final=True)

            if trail_generator is not None:
                s_print("\tWriting trail...")
                trail = trail_generator.get_remaining_bytes()

                result.append(f"\n\n{'#' * 27} TRAIL ({len(trail)})\n\n")
                result.append(create_textual_hex(trail.hex(), space_distance=2, enter_distance=24))
                s_print("\tWriting trail finished successfully.", final=True)

            f.write(''.join(result))
        s_print("Writing structure to file finished successfully.", final=True)


def _initialise_version_dependencies(game_version: str, scenario_version: str) -> None:
    """
    Initialises the data for the condition and effect objects (IDs, defaults, etc.) for the given scenario
    and game versions

    Args:
        game_version: The version of the game to initialise the dependencies for
        scenario_version: The version of the scenario to initialise the dependencies for
    """
    condition_json = _get_version_dependant_structure_file(game_version, scenario_version, "conditions")

    for condition_id, structure in condition_json.items():
        condition_id = int(condition_id)

        if condition_id == -1:
            conditions.attribute_presentation[condition_id] = structure['attribute_presentation']
            continue

        conditions.condition_names[condition_id] = structure['name']
        conditions.default_attributes[condition_id] = structure['default_attributes']
        conditions.attributes[condition_id] = structure['attributes']
        conditions.attribute_presentation[condition_id] = structure.get('attribute_presentation', {})

    effect_json = _get_version_dependant_structure_file(game_version, scenario_version, "effects")

    for effect_id, structure in effect_json.items():
        effect_id = int(effect_id)

        if effect_id == -1:
            effects.attribute_presentation[effect_id] = structure['attribute_presentation']
            continue

        effects.effect_names[effect_id] = structure['name']
        effects.default_attributes[effect_id] = structure['default_attributes']
        effects.attributes[effect_id] = structure['attributes']
        effects.attribute_presentation[effect_id] = structure.get('attribute_presentation', {})


def _get_file_section_data(file_section: AoE2FileSection) -> bytes:
    """
    Converts the data of the given file section into bytes, and also prints that the conversion is happening to the
    console.

    Args:
        file_section: The file section to convert to bytes

    Returns:
        Bytes for all the data in the given file section
    """
    s_print(f"\t🔄 Reconstructing {file_section.name}...", color="yellow")
    value = file_section.get_data_as_bytes()
    s_print(f"\t✔ {file_section.name}", final=True, color="green")
    return value


def _get_file_version(generator: IncrementalGenerator):
    """
    Get first 4 bytes of a file, which contains the version of the scenario
    
    Args:
        generator: An IncrementalGenerator object of a scenario file

    Returns:
        A string which is the version of the scenario file
    """
    return generator.get_bytes(4, update_progress=False).decode('ASCII')


def _decompress_bytes(file_content: bytes) -> bytes:
    """
    Decompress the given bytes using the -zlib.MAX_WBITS algorithm

    Args:
        file_content: The bytes to decompress

    Returns:
        The decompressed bytes
    """
    return zlib.decompress(file_content, -zlib.MAX_WBITS)


def _compress_bytes(file_content: bytes) -> bytes:
    """
    Compress the given bytes using the -zlib.MAX_WBITS algorithm. View this link for additional information:
    https://stackoverflow.com/questions/3122145/zlib-error-error-3-while-decompressing-incorrect-header-check/22310760#22310760

    Args:
        file_content: The bytes to compress

    Returns:
        The compressed bytes
    """
    deflate_obj = zlib.compressobj(9, zlib.DEFLATED, -zlib.MAX_WBITS)
    compressed = deflate_obj.compress(file_content) + deflate_obj.flush()
    return compressed


def _get_version_directory_path() -> Path:
    """
    Get the path of the AoE2ScenarioParser/versions directory. Simply '../../versions' is not used as that is not OS
    friendly.

    Returns:
        The full path of the AoE2ScenarioParser/versions directory.
    """
    return Path(__file__).parent.parent / 'versions'


def _get_version_dependant_structure_file(game_version: str, scenario_version: str, name: str) -> dict:
    """
    Returns a structure file dependant on the version of the scenario (AND game version).
    Files are retrieved based on the game and scenario version given.

    Args:
        game_version: The version of the game to return the structure file for
        scenario_version: The scenario version to return the structure file for
        name: The name of the structure file being requested

    Returns:
        a dict representation of the structure file requested

    Raises:
        UnknownStructureError: if a json associated with the name and versions specified is not found
    """
    try:
        vdir = _get_version_directory_path()
        with (vdir / game_version / f'v{scenario_version}' / f'{name}.json').open() as structure_file:
            return json.load(structure_file)
    except FileNotFoundError:  # Unsupported version
        v = f"{game_version}:{scenario_version}"
        raise UnknownStructureError(f"The structure {name} could not be found with: {v}")


def _get_structure(game_version: str, scenario_version: str) -> Dict[str, Any]:
    """
    Get the structure file of the given game and scenario version

    Args:
        game_version: The game version to get the structure file for
        scenario_version: The scenario version to get the structure file for

    Returns:
        The dictionary representation of the scenario for the specified versions

    Raises:
        InvalidScenarioStructureError: If the FileHeader section is not present in the loaded structure file
        UnknownScenarioStructureError: If the structure for the specified game/scenario version is not found
    """
    try:
        vdir = _get_version_directory_path()
        with (vdir / game_version / f'v{scenario_version}' / 'structure.json').open() as structure_file:
            structure = json.load(structure_file)

            if "FileHeader" not in structure.keys():
                raise InvalidScenarioStructureError(f"First section in structure should always be FileHeader.")
            return structure
    except FileNotFoundError:  # Unsupported version
        v = f"{game_version}:{scenario_version}"
        raise UnknownScenarioStructureError(f"The version {v} is not supported by AoE2ScenarioParser. :(") from None
