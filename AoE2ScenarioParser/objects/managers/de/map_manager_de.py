from typing import List

from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.objects.data_objects.terrain_tile import TerrainTile
from AoE2ScenarioParser.objects.managers.map_manager import MapManager
from AoE2ScenarioParser.sections.retrievers.support import Support


class MapManagerDE(MapManager):

    _link_list = [
        RetrieverObjectLink("water_definition", "Map", "water_definition"),
        RetrieverObjectLink("map_color_mood", "Map", "map_color_mood"),
        RetrieverObjectLink("block_humanity_team_change", "Map", "block_humanity_team_change", Support(since=1.41)),
        RetrieverObjectLink("collide_and_correct", "Map", "collide_and_correct"),
        RetrieverObjectLink("villager_force_drop", "Map", "villager_force_drop"),
        RetrieverObjectLink("map_width", "Map", "map_width"),
        RetrieverObjectLink("map_height", "Map", "map_height"),
        RetrieverObjectLink("no_waves_on_shore", "Map", "no_waves_on_shore"),   # TODO: Or `AI Type` of the map?
        RetrieverObjectLink("terrain", "Map", "terrain_data", process_as_object=TerrainTile),
        RetrieverObjectLink("script_name", "Map", "script_name", Support(since=1.40)),
    ]

    def __init__(self,
                 water_definition: str,
                 map_color_mood: str,
                 block_humanity_team_change: int,
                 collide_and_correct: bool,
                 villager_force_drop: bool,
                 no_waves_on_shore: bool,
                 map_width: int,
                 map_height: int,
                 terrain: List[TerrainTile],
                 script_name: str
                 ):

        self.water_definition = water_definition
        self.map_color_mood = map_color_mood
        self.block_humanity_team_change = block_humanity_team_change
        self.collide_and_correct = collide_and_correct
        self.villager_force_drop = villager_force_drop
        self.no_waves_on_shore = no_waves_on_shore
        self.script_name = script_name

        super().__init__(map_width, map_height, terrain)
