from __future__ import annotations

import json
import time
import zlib
from pathlib import Path
from typing import Union, Dict, TYPE_CHECKING
from uuid import uuid4, UUID

import AoE2ScenarioParser.datasets.conditions as conditions
import AoE2ScenarioParser.datasets.effects as effects
from AoE2ScenarioParser import settings
from AoE2ScenarioParser.helper.exceptions import InvalidScenarioStructureError, UnknownScenarioStructureError, \
    UnknownStructureError
from AoE2ScenarioParser.helper.incremental_generator import IncrementalGenerator
from AoE2ScenarioParser.helper.printers import s_print, color_string
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

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


class AoE2Scenario:
    @property
    def trigger_manager(self) -> TriggerManager:
        return self._object_manager.managers['Trigger']

    @property
    def unit_manager(self) -> UnitManager:
        return self._object_manager.managers['Unit']

    @property
    def map_manager(self) -> MapManager:
        return self._object_manager.managers['Map']

    @property
    def player_manager(self) -> PlayerManager:
        return self._object_manager.managers['Player']

    @property
    def message_manager(self) -> MessageManager:
        return self._object_manager.managers['Message']

    def __init__(self, game_version: str, scenario_version: str, source_location: str, name: str):
        # Scenario meta info
        self.game_version = game_version
        self.scenario_version = scenario_version
        self.source_location = source_location
        self._time_start = time.time()

        # Actual scenario content
        self.structure = {}
        self.sections: Dict[str, AoE2FileSection] = {}
        self._object_manager: Union[AoE2ObjectManager, None] = None

        # For Scenario Store functionality
        self.name = name
        self.uuid = uuid4()
        store.register_scenario(self)

        # Actions through the scenario
        self.new = ObjectFactory(self.uuid)
        self.actions = ScenarioActions(self.uuid)

        # Used in debug functions
        self._file = None
        self._file_header = None
        self._decompressed_file_data = None

    @classmethod
    def from_file(cls, path: str, game_version, name: str = ""):
        python_version_check()

        filepath = Path(path)
        if not filepath.is_file():
            raise ValueError(f"Unable to read file from path '{filepath}'")

        name = name or filepath.stem

        s_print(f"Reading file: " + color_string(f"'{path}'", "magenta"), final=True, time=True, newline=True)
        s_print("Reading scenario file...")
        igenerator = IncrementalGenerator.from_file(path)
        s_print("Reading scenario file finished successfully.", final=True, time=True)

        scenario_version = get_file_version(igenerator)
        scenario = cls(game_version, scenario_version, source_location=path, name=name)

        # Log game and scenario version
        s_print("\n############### Attributes ###############", final=True, color="blue")
        s_print(f">>> Game version: '{scenario.game_version}'", final=True, color="blue")
        s_print(f">>> Scenario version: {scenario.scenario_version}", final=True, color="blue")
        s_print("##########################################", final=True, color="blue")

        s_print(f"Loading scenario structure...", time=True, newline=True)
        scenario._load_structure()
        initialise_version_dependencies(scenario.game_version, scenario.scenario_version)
        s_print(f"Loading scenario structure finished successfully.", final=True, time=True)

        # scenario._initialize(igenerator)
        s_print("Parsing scenario file...", final=True, time=True)
        scenario._load_header_section(igenerator)
        scenario._load_content_sections(igenerator)
        s_print(f"Parsing scenario file finished successfully.", final=True, time=True)

        scenario._object_manager = AoE2ObjectManager(scenario.uuid)
        scenario._object_manager.setup()

        return scenario

    @staticmethod
    def get_scenario(
        uuid: UUID = None,
        obj: 'AoE2Object' = None,
        name: str = None
    ) -> AoE2Scenario:
        """
        Get scenario through a UUID, a related object or the name of a scenario.

        Args:
            uuid: The UUID of the scenario
            obj: An object related to a scenario
            name: The name of a scenario

        Raises

        Returns:
            The scenario based on the given identifier, or `None`
        """
        # Todo: Add return type from api-docs branch when merged :)
        return store.get_scenario(uuid=uuid, obj=obj, name=name)

    def _load_structure(self):
        if self.game_version == "???" or self.scenario_version == "???":
            raise ValueError("Both game and scenario version need to be set to load structure")
        self.structure = get_structure(self.game_version, self.scenario_version)

    def _load_header_section(self, raw_file_igenerator: IncrementalGenerator):
        header = self._create_and_load_section('FileHeader', raw_file_igenerator)
        self._file_header = raw_file_igenerator.file_content[:raw_file_igenerator.progress]
        self._add_to_sections(header)

    def _load_content_sections(self, raw_file_igenerator: IncrementalGenerator):
        self._decompressed_file_data = decompress_bytes(raw_file_igenerator.get_remaining_bytes())

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

    def _create_and_load_section(self, name, igenerator) -> AoE2FileSection:
        s_print(f"\t🔄 Parsing {name}...", color="yellow")
        section = AoE2FileSection.from_structure(name, self.structure.get(name), self.uuid)
        s_print(f"\t🔄 Gathering {name} data...", color="yellow")
        section.set_data_from_generator(igenerator)
        s_print(f"\t✔ {name}", final=True, color="green")
        return section

    def _add_to_sections(self, section) -> None:
        self.sections[section.name] = section

    def remove_store_reference(self) -> None:
        """
        Removes the reference to this scenario object from the scenario store. Useful (~a must) when reading many
        scenarios in a row without needing earlier ones. Python likes to take up a lot of memory.
        Removing all references to an object will cause the memory to be cleared up.

        **Please note:** When using this function it's important to remove all other references to the scenario.
        So if save it in a dict or list, remove it from it.
        If you have variables referencing this scenario that you won't need anymore (and won't overwrite) delete them
        using: `del varname`.
        """
        store.remove_scenario(self.uuid)

    def commit(self) -> None:
        """Commit the changes to the retriever backend made within the managers."""
        self._object_manager.reconstruct()

    """ ##########################################################################################
    ####################################### Write functions ######################################
    ########################################################################################## """

    def write_to_file(self, filename, skip_reconstruction=False):
        """
        Write the scenario to a new file

        Args:
            filename (str): The location to write the file to
            skip_reconstruction (bool): If reconstruction should be skipped. If true, this will ignore all changes made
                using the managers (For example all changes made using trigger_manager).
        """
        self._write_from_structure(filename, skip_reconstruction)

    def _write_from_structure(self, filename, skip_reconstruction=False):
        if not settings.DISABLE_ERROR_ON_OVERWRITING_SOURCE and self.source_location == filename:
            raise ValueError("Overwriting the source scenario file is disallowed. "
                             "This behaviour can be disabled in the settings file.")
        if not skip_reconstruction:
            self.commit()

        s_print("File writing from structure started...", final=True, time=True, newline=True)
        binary = _get_file_section_data(self.sections.get('FileHeader'))

        binary_list_to_be_compressed = []
        for file_part in self.sections.values():
            if file_part.name == "FileHeader":
                continue
            binary_list_to_be_compressed.append(_get_file_section_data(file_part))

        compressed = compress_bytes(b''.join(binary_list_to_be_compressed))

        with open(filename, 'wb') as f:
            f.write(binary + compressed)

        etime = round(time.time() - self._time_start, 2)
        s_print("File writing finished successfully.", final=True, time=True)
        s_print(f"File successfully written to: " + color_string(f"'{filename}'", "magenta"), final=True, time=True)
        s_print(f"Execution time from scenario read: {etime}s", final=True, time=True)

    def write_error_file(self, filename="error_file.txt", trail_generator=None):
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

    def _debug_write_from_source(self, filename, datatype, write_bytes=True):
        """This function is used as a test debugging writing. It writes parts of the read file to the filesystem."""
        print("File writing from source started with attributes " + datatype + "...")
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
        print("File writing finished successfully.")

    def _debug_byte_structure_to_file(self, filename, trail_generator: IncrementalGenerator = None, commit=False):
        """ Used for debugging - Writes structure from read file to the filesystem in an easily readable manner. """
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


def initialise_version_dependencies(game_version, scenario_version):
    condition_json = get_version_dependant_structure_file(game_version, scenario_version, "conditions")

    for condition_id, structure in condition_json.items():
        condition_id = int(condition_id)

        if condition_id == -1:
            conditions.attribute_presentation[condition_id] = structure['attribute_presentation']
            continue

        conditions.condition_names[condition_id] = structure['name']
        conditions.default_attributes[condition_id] = structure['default_attributes']
        conditions.attributes[condition_id] = structure['attributes']
        conditions.attribute_presentation[condition_id] = structure.get('attribute_presentation', {})

    effect_json = get_version_dependant_structure_file(game_version, scenario_version, "effects")

    for effect_id, structure in effect_json.items():
        effect_id = int(effect_id)

        if effect_id == -1:
            effects.attribute_presentation[effect_id] = structure['attribute_presentation']
            continue

        effects.effect_names[effect_id] = structure['name']
        effects.default_attributes[effect_id] = structure['default_attributes']
        effects.attributes[effect_id] = structure['attributes']
        effects.attribute_presentation[effect_id] = structure.get('attribute_presentation', {})


def _get_file_section_data(file_section: AoE2FileSection):
    s_print(f"\t🔄 Reconstructing {file_section.name}...", color="yellow")
    value = file_section.get_data_as_bytes()
    s_print(f"\t✔ {file_section.name}", final=True, color="green")
    return value


def get_file_version(generator: IncrementalGenerator):
    """Get first 4 bytes of a file, which contains the version of the scenario"""
    return generator.get_bytes(4, update_progress=False).decode('ASCII')


def decompress_bytes(file_content):
    return zlib.decompress(file_content, -zlib.MAX_WBITS)


def compress_bytes(file_content):
    # https://stackoverflow.com/questions/3122145/zlib-error-error-3-while-decompressing-incorrect-header-check/22310760#22310760
    deflate_obj = zlib.compressobj(9, zlib.DEFLATED, -zlib.MAX_WBITS)
    compressed = deflate_obj.compress(file_content) + deflate_obj.flush()
    return compressed


def get_version_directory_path() -> Path:
    return Path(__file__).parent.parent / 'versions'


def get_version_dependant_structure_file(game_version: str, scenario_version: str, name: str) -> dict:
    try:
        vdir = get_version_directory_path()
        with (vdir / game_version / f'v{scenario_version}' / f'{name}.json').open() as structure_file:
            return json.load(structure_file)
    except FileNotFoundError:  # Unsupported version
        v = f"{game_version}:{scenario_version}"
        raise UnknownStructureError(f"The structure {name} could not be found with: {v}")


def get_structure(game_version, scenario_version) -> dict:
    try:
        vdir = get_version_directory_path()
        with (vdir / game_version / f'v{scenario_version}' / 'structure.json').open() as structure_file:
            structure = json.load(structure_file)

            if "FileHeader" not in structure.keys():
                raise InvalidScenarioStructureError(f"First section in structure should always be FileHeader.")
            return structure
    except FileNotFoundError:  # Unsupported version
        v = f"{game_version}:{scenario_version}"
        raise UnknownScenarioStructureError(f"The version {v} is not supported by AoE2ScenarioParser. :(") from None
