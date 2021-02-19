from typing import List

from AoE2ScenarioParser.helper.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.objects.data_objects.unit import Unit
from AoE2ScenarioParser.objects.managers.unit_manager import UnitManager


class UnitManagerDE(UnitManager):
    _link_list = [
        RetrieverObjectLink("units", "Units", "players_units[].units", process_as_object=Unit)
    ]

    def __init__(self, units: List[List[Unit]]):
        super().__init__(units)
