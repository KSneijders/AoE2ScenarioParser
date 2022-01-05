from typing import Tuple, Union, TYPE_CHECKING, List, Optional, Iterator
from uuid import UUID

from AoE2ScenarioParser.helper.attr_dict import AttrDict
from AoE2ScenarioParser.helper.helper import values_are_valid
from AoE2ScenarioParser.objects.support.area import Area
from AoE2ScenarioParser.objects.support.tile import Tile
from AoE2ScenarioParser.scenarios.scenario_store import getters, actions

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.data_objects.condition import Condition
    from AoE2ScenarioParser.objects.data_objects.effect import Effect
    from AoE2ScenarioParser.objects.data_objects.trigger import Trigger


class TriggerMarkings:
    _scan_options: Tuple = ("area:", "tile:", "location:",)

    def __init__(self, uuid: UUID) -> None:
        super().__init__()

        self._uuid = uuid

        self.objects = AttrDict()
        self.areas = AttrDict()
        self.tiles = AttrDict()

    def discover(self, remove_template_triggers: bool) -> None:
        triggers = getters.get_triggers_by_prefix(self._uuid, self._scan_options)

        for trigger in triggers:
            tag = self._resolve_markings_name(trigger)
            for ce in loop_trigger_content(trigger):
                if trigger.name.startswith("area:"):
                    area = self._create_area(ce)
                    if area:
                        self.areas.setdefault(tag, []).append(area)

                elif trigger.name.startswith(("tile:", "location:")):
                    tiles = self._create_tiles(ce)
                    if tiles:
                        self.tiles.setdefault(tag, []).extend(tiles)

        if remove_template_triggers:
            actions.remove_triggers(self._uuid, [t.trigger_id for t in triggers])

    def _create_area(self, ce: Union['Condition', 'Effect']) -> Optional[Area]:
        if values_are_valid(ce.area_x1, ce.area_y1, ce.area_x2, ce.area_y2):
            return actions.new_area_object(self._uuid).select(ce.area_x1, ce.area_y1, ce.area_x2, ce.area_y2)

    def _create_tiles(self, ce: Union['Condition', 'Effect']) -> Optional[List[Tile]]:
        tiles = []
        try:
            # Only effects have a location value
            if values_are_valid(ce.location_x, ce.location_y):
                tiles.append(Tile(ce.location_x, ce.location_y))
        except AttributeError:
            pass
        area = self._create_area(ce)
        if area:
            tiles.extend(list(area.to_coords()))
        return tiles

    @staticmethod
    def _resolve_markings_name(trigger: 'Trigger'):
        return trigger.name[trigger.name.find(":") + 1:]


def loop_trigger_content(trigger: 'Trigger') -> Iterator[Union['Condition', 'Effect']]:
    for condition in trigger.conditions:
        yield condition
    for effect in trigger.effects:
        yield effect
