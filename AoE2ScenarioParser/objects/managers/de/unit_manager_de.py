from typing import List

from AoE2ScenarioParser.objects.data_objects.unit import Unit
from AoE2ScenarioParser.objects.managers.unit_manager import UnitManager


class UnitManagerDE(UnitManager):

    def __init__(self, units: List[List[Unit]], **kwargs):
        super().__init__(units, **kwargs)
