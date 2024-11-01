from typing import List

from AoE2ScenarioParser.helper.printers import warn
from AoE2ScenarioParser.objects.data_objects.terrain_tile import TerrainTile
from AoE2ScenarioParser.objects.managers.map_manager import MapManager
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.sections.retrievers.retriever_object_link_group import RetrieverObjectLinkGroup
from AoE2ScenarioParser.sections.retrievers.support import Support


class MapManagerDE(MapManager):
    """Manager of all DE map related features"""
    _link_list = [
        RetrieverObjectLinkGroup("Map", group=[
            RetrieverObjectLink("map_color_mood"),
            RetrieverObjectLink("collide_and_correct"),
            RetrieverObjectLink("villager_force_drop", support=Support(since=1.37)),
            RetrieverObjectLink("map_width"),
            RetrieverObjectLink("map_height"),
            RetrieverObjectLink("terrain", link="terrain_data", process_as_object=TerrainTile),
        ])
    ]

    def __init__(self,
                 map_color_mood: str,
                 collide_and_correct: bool,
                 villager_force_drop: bool,
                 map_width: int,
                 map_height: int,
                 terrain: List[TerrainTile],
                 **kwargs,
                 ):
        super().__init__(map_width, map_height, terrain, **kwargs)

        self.map_color_mood: str = map_color_mood
        self.collide_and_correct: bool = collide_and_correct
        self.villager_force_drop: bool = villager_force_drop

    @property
    def collide_and_correct(self):
        warn("Moved to the OptionManager. Use: `option_manager.collide_and_correct` instead", DeprecationWarning)
        return self._collide_and_correct

    @collide_and_correct.setter
    def collide_and_correct(self, value):
        warn("Moved to the OptionManager. Use: `option_manager.collide_and_correct` instead", DeprecationWarning)
        self._collide_and_correct = value

    @property
    def villager_force_drop(self):
        warn("Moved to the OptionManager. Use: `option_manager.villager_force_drop` instead", DeprecationWarning)
        return self._villager_force_drop

    @villager_force_drop.setter
    def villager_force_drop(self, value):
        warn("Moved to the OptionManager. Use: `option_manager.villager_force_drop` instead", DeprecationWarning)
        self._villager_force_drop = value
