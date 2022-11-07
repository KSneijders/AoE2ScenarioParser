from typing import List

from AoE2ScenarioParser.objects.data_objects.units.player_units import PlayerUnits
from AoE2ScenarioParser.objects.managers.unit_manager import UnitManager


class UnitManagerDE(UnitManager):
    """Manager of all DE unit related features"""

    def __init__(self, _player_units: List[PlayerUnits], **kwargs):
        super().__init__(_player_units, **kwargs)
