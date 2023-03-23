from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct
from binary_file_parser.types import bool8, Bytes, uint32, str16

from AoE2ScenarioParser.sections.bfp.map.terrain import Terrain
from AoE2ScenarioParser.sections.bfp.map.view import View


class MapData(BaseStruct):
    @staticmethod
    def set_terrain_data_repeat(_, instance: MapData):
        MapData.tiles.set_repeat(instance, instance.width * instance.height)

    @staticmethod
    def update_script_file_path(_, instance: MapData):
        instance.parent.file_data.script_file_path = instance.script_name + ".xs" if instance.script_name else ""

    @staticmethod
    def update_width_height(_, instance: MapData):
        instance.width = instance.height = int(len(instance.tiles) ** 0.5)

    # formatter:off
    string_starter1: bytes         = Retriever(Bytes[2],                    default=b"\x60\x0a")
    water_definition: str          = Retriever(str16,                       default="")
    string_starter2: bytes         = Retriever(Bytes[2],                    default=b"\x60\x0a")
    colour_mood: str               = Retriever(str16,                       default="Empty")
    string_starter3: bytes         = Retriever(Bytes[2], (1, 40),           default=b"\x60\x0a")
    script_name: str               = Retriever(str16,    (1, 40),           default="", on_write=[update_script_file_path])
    lock_coop_alliances_1_41: bool = Retriever(bool8,    (1, 41), (1, 41),  default=False)
    collide_and_correct: bool      = Retriever(bool8,                       default=False)
    villager_force_drop: bool      = Retriever(bool8,    (1, 37),           default=False)
    player_views: list[View]       = Retriever(View, (1, 40), default=View(), repeat=16)
    lock_coop_alliances_1_42: bool = Retriever(bool8,    (1, 42),           default=False)
    ai_map_type: int               = Retriever(uint32,   (1, 42), (1, 46),  default=0)
    population_caps: list[int]     = Retriever(uint32,   (1, 44),           default=200, repeat=16)
    secondary_game_mode            = Retriever(Bytes[4], (1, 45),           default=b"\x00\x00\x00\x00")
    unknown3                       = Retriever(Bytes[4],                    default=b"\x0d\xf0\xad\xde")
    unknown4                       = Retriever(Bytes[4],                    default=b"\x02\x00\x00\x00")
    no_waves_on_shore: bool        = Retriever(bool8,                       default=False)
    width: int                     = Retriever(uint32,                      default=120, on_set=[set_terrain_data_repeat], on_write=[update_width_height])
    height: int                    = Retriever(uint32,                      default=120, on_set=[set_terrain_data_repeat])
    tiles: list[Terrain]           = Retriever(Terrain, default=Terrain(), repeat=14_400)
    # formatter:on

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)
