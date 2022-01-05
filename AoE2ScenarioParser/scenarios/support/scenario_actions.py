from typing import Dict, List, Union, TYPE_CHECKING
from uuid import UUID

from AoE2ScenarioParser.helper.helper import values_are_valid
from AoE2ScenarioParser.objects.support.area import Area
from AoE2ScenarioParser.objects.support.tile import Tile
from AoE2ScenarioParser.scenarios.scenario_store import getters, actions

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.data_objects.condition import Condition
    from AoE2ScenarioParser.objects.data_objects.effect import Effect


class ScenarioActions:
    def __init__(self, uuid: UUID) -> None:
        super().__init__()

        self.uuid = uuid

    def discover_locations(self, remove_template_triggers=True) -> Dict[str, List[Union[Area, Tile]]]:
        """

        Args:
            remove_template_triggers:

        Returns:

        """
        def create_object(ce: Union['Condition', 'Effect'], trigger_name: str) -> Union[Area, List[Tile]]:
            def create_area(ce_: Union['Condition', 'Effect']) -> Area:
                return actions.new_area_object(self.uuid).select(ce_.area_x1, ce_.area_y1, ce_.area_x2, ce_.area_y2)

            if trigger_name.startswith("area:"):
                if values_are_valid(ce.area_x1, ce.area_y1, ce.area_x2, ce.area_y2):
                    return create_area(ce)
            else:
                tiles = []
                try:
                    # Only effects have a location value
                    if values_are_valid(ce.location_x, ce.location_y):
                        tiles.append(Tile(ce.location_x, ce.location_y))
                except AttributeError:
                    pass
                if values_are_valid(ce.area_x1, ce.area_y1, ce.area_x2, ce.area_y2):
                    tiles.extend(list(create_area(ce).to_coords()))
                return tiles

        locations: Dict[str, List[Union[Area, Tile]]] = {}
        triggers = getters.get_triggers_by_prefix(self.uuid, ("area:", "tile:", "location:"))
        for trigger in triggers:
            tag = trigger.name[trigger.name.find(":") + 1:]
            for ces in [trigger.effects, trigger.conditions]:
                for cond_or_eff in ces:
                    obj = create_object(cond_or_eff, trigger.name)
                    if obj is not None:
                        if isinstance(obj, list):
                            locations.setdefault(tag, []).extend(obj)
                        else:
                            locations.setdefault(tag, []).append(obj)

        if remove_template_triggers:
            actions.remove_triggers(self.uuid, [t.trigger_id for t in triggers])

        return locations
