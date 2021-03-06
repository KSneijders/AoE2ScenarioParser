import json
import zlib
from collections import OrderedDict
from typing import Union

from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper.exceptions import InvalidScenarioStructure, UnknownScenarioStructure
from AoE2ScenarioParser.helper.helper import create_textual_hex
from AoE2ScenarioParser.helper.incremental_generator import IncrementalGenerator
from AoE2ScenarioParser.objects.aoe2_object_manager import AoE2ObjectManager
from AoE2ScenarioParser.objects.managers.map_manager import MapManager
from AoE2ScenarioParser.objects.managers.trigger_manager import TriggerManager
from AoE2ScenarioParser.objects.managers.unit_manager import UnitManager
from AoE2ScenarioParser.sections.aoe2_file_section import AoE2FileSection


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

    def __init__(self):
        self.read_mode = None
        self.scenario_version = "???"
        self.game_version = "???"
        self.structure = {}
        self.sections: OrderedDict[str, AoE2FileSection] = OrderedDict()
        self._object_manager: Union[AoE2ObjectManager, None] = None

        # Used in debug functions
        self._file = None
        self._file_header = None
        self._decompressed_file_data = None

    @classmethod
    def from_file(cls, game_version, filename):
        print(f"\nSelected file: '{filename}'")
        helper.rprint("Reading scenario file...")
        igenerator = IncrementalGenerator.from_file(filename)
        helper.rprint("Reading scenario file finished successfully.", final=True)

        scenario = cls()
        scenario.read_mode = "from_file"
        scenario.game_version = game_version
        scenario.scenario_version = get_file_version(igenerator)

        # Log game and scenario version
        print("\n############### Attributes ###############")
        print(f">>> Game version: '{scenario.game_version}'")
        print(f">>> Scenario version: {scenario.scenario_version}")
        print("##########################################")

        helper.rprint(f"\nLoading scenario structure...")
        scenario.load_structure()
        helper.rprint(f"Loading scenario structure finished successfully.", final=True)

        # scenario._initialize(igenerator)
        helper.rprint("Parsing scenario file...", final=True)
        scenario._load_header_section(igenerator)
        scenario._load_content_sections(igenerator)
        helper.rprint(f"Parsing scenario file finished successfully.", final=True)

        scenario._object_manager = AoE2ObjectManager(
            sections=scenario.sections,
            game_version=scenario.game_version,
            scenario_version=scenario.scenario_version
        )
        scenario._object_manager.setup()

        return scenario

    def load_structure(self):
        if self.game_version == "???" or self.scenario_version == "???":
            raise ValueError("Both game and scenario version need to be set to load structure")
        self.structure = get_structure(self.game_version, self.scenario_version)

    def _load_header_section(self, raw_file_igenerator: IncrementalGenerator):
        header = self._create_and_load_section('FileHeader', raw_file_igenerator)
        self._add_to_sections(header)

    def _load_content_sections(self, raw_file_igenerator: IncrementalGenerator):
        data_igenerator = IncrementalGenerator(
            name='Scenario Data',
            file_content=decompress_bytes(raw_file_igenerator.get_remaining_bytes())
        )

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

    def _create_and_load_section(self, name, igenerator):
        helper.rprint(f"\t🔄 Parsing {name}...")
        section = AoE2FileSection.from_structure(name, self.structure.get(name))
        helper.rprint(f"\t🔄 Gathering {name} data...")
        section.set_data_from_generator(igenerator, self.sections)
        helper.rprint(f"\t✔ {name}", final=True)
        return section

    def _add_to_sections(self, section):
        self.sections[section.name] = section

    """ ##########################################################################################
    ####################################### Write functions ######################################
    ########################################################################################## """

    def write_to_file(self, filename):
        self._write_from_structure(filename)

    def _write_from_structure(self, filename):
        self._object_manager.reconstruct()

        helper.rprint("\nFile writing from structure started...", final=True)
        binary = self._get_file_section_data(self.sections.get('FileHeader'))

        binary_list_to_be_compressed = []
        for file_part in self.sections.values():
            if file_part.name == "FileHeader":
                continue
            binary_list_to_be_compressed.append(self._get_file_section_data(file_part))
        compressed = compress_bytes(b''.join(binary_list_to_be_compressed))

        with open(filename, 'wb') as f:
            f.write(binary + compressed)

        helper.rprint("File writing finished successfully.", final=True)

    def _get_file_section_data(self, file_section: AoE2FileSection):
        helper.rprint(f"\t🔄 Reconstructing {file_section.name}...")
        value = file_section.get_data_as_bytes()
        helper.rprint(f"\t✔ {file_section.name}", final=True)
        return value

    def write_error_file(self, filename="error_file.txt", trail_generator=None):
        self._debug_byte_structure_to_file(filename=filename, trail_generator=trail_generator)

    """ #############################################
    ################ Debug functions ################
    ############################################# """

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

    def _retrieve_byte_structure(self, file_part):
        helper.rprint(f"\t🔄 Writing {file_part.name}...")
        value = file_part.get_byte_structure_as_string(self.sections)
        helper.rprint(f"\t✔ {file_part.name}", final=True)
        return value

    def _debug_byte_structure_to_file(self, filename, trail_generator: IncrementalGenerator = None, commit=False):
        """ Used for debugging - Writes structure from read file to the filesystem in a easily readable manner. """
        if commit and hasattr(self, '_object_manager'):
            self._object_manager.reconstruct()

        helper.rprint("\nWriting structure to file...", final=True)
        with open(filename, 'w', encoding="utf-8") as f:
            result = []
            for section in self.sections.values():
                result.append(self._retrieve_byte_structure(section))

            if trail_generator is not None:
                helper.rprint("\tWriting trail...")
                trail = trail_generator.get_remaining_bytes()

                result.append(f"\n\n{'#' * 27} TRAIL ({len(trail)})\n\n")
                result.append(helper.create_textual_hex(trail.hex(), space_distance=2, enter_distance=24))
                helper.rprint("\tWriting trail finished successfully.", final=True)

            f.write(''.join(result))
        helper.rprint("Writing structure to file finished successfully.", final=True)


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


def get_structure(game_version, scenario_version) -> dict:
    try:
        structure_file = open(f"./versions/{game_version}/v{scenario_version}/structure.json", 'r')
    except FileNotFoundError:  # Unsupported version
        v = f"{game_version}:{scenario_version}"
        raise UnknownScenarioStructure(f"The version {v} is not supported by AoE2ScenarioParser. :(") from None

    structure = json.loads(structure_file.read())

    if "FileHeader" not in structure.keys():
        raise InvalidScenarioStructure(f"First section in structure should always be FileHeader.")
    return structure
