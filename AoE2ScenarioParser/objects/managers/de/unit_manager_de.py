from typing import List

from AoE2ScenarioParser.objects.data_objects.unit import Unit
from AoE2ScenarioParser.objects.managers.unit_manager import UnitManager
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink


class UnitManagerDE(UnitManager):
    _link_list = [
        RetrieverObjectLink("units", "Units", "players_units[].units", process_as_object=Unit)
    ]

    def __init__(self, units: List[List[Unit]], **kwargs):
        super().__init__(units, **kwargs)
