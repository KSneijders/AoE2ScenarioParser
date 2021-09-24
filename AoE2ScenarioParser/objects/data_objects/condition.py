from __future__ import annotations

from enum import IntEnum

from AoE2ScenarioParser.datasets import conditions
from AoE2ScenarioParser.helper.helper import raise_if_not_int_subclass
from AoE2ScenarioParser.helper.printers import warn
from AoE2ScenarioParser.helper.string_manipulations import add_tabs
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.support.attr_presentation import transform_condition_attr_value
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.sections.retrievers.support import Support


class Condition(AoE2Object):
    """Object for handling a condition."""

    _link_list = [
        RetrieverObjectLink("condition_type", "Triggers",
                            "trigger_data[__index__].condition_data[__index__].condition_type"),
        RetrieverObjectLink("quantity", "Triggers",
                            "trigger_data[__index__].condition_data[__index__].quantity"),
        RetrieverObjectLink("attribute", "Triggers",
                            "trigger_data[__index__].condition_data[__index__].attribute"),
        RetrieverObjectLink("unit_object", "Triggers",
                            "trigger_data[__index__].condition_data[__index__].unit_object"),
        RetrieverObjectLink("next_object", "Triggers",
                            "trigger_data[__index__].condition_data[__index__].next_object"),
        RetrieverObjectLink("object_list", "Triggers",
                            "trigger_data[__index__].condition_data[__index__].object_list"),
        RetrieverObjectLink("source_player", "Triggers",
                            "trigger_data[__index__].condition_data[__index__].source_player"),
        RetrieverObjectLink("technology", "Triggers",
                            "trigger_data[__index__].condition_data[__index__].technology"),
        RetrieverObjectLink("timer", "Triggers", "trigger_data[__index__].condition_data[__index__].timer"),
        RetrieverObjectLink("area_x1", "Triggers", "trigger_data[__index__].condition_data[__index__].area_x1"),
        RetrieverObjectLink("area_y1", "Triggers", "trigger_data[__index__].condition_data[__index__].area_y1"),
        RetrieverObjectLink("area_x2", "Triggers", "trigger_data[__index__].condition_data[__index__].area_x2"),
        RetrieverObjectLink("area_y2", "Triggers", "trigger_data[__index__].condition_data[__index__].area_y2"),
        RetrieverObjectLink("object_group", "Triggers",
                            "trigger_data[__index__].condition_data[__index__].object_group"),
        RetrieverObjectLink("object_type", "Triggers",
                            "trigger_data[__index__].condition_data[__index__].object_type"),
        RetrieverObjectLink("ai_signal", "Triggers", "trigger_data[__index__].condition_data[__index__].ai_signal"),
        RetrieverObjectLink("inverted", "Triggers", "trigger_data[__index__].condition_data[__index__].inverted"),
        RetrieverObjectLink("variable", "Triggers", "trigger_data[__index__].condition_data[__index__].variable"),
        RetrieverObjectLink("comparison", "Triggers",
                            "trigger_data[__index__].condition_data[__index__].comparison"),
        RetrieverObjectLink("target_player", "Triggers",
                            "trigger_data[__index__].condition_data[__index__].target_player"),
        RetrieverObjectLink("object_state", "Triggers",
                            "trigger_data[__index__].condition_data[__index__].object_state", Support(since=1.42)),
        RetrieverObjectLink("xs_function", "Triggers",
                            "trigger_data[__index__].condition_data[__index__].xs_function", Support(since=1.40)),
        RetrieverObjectLink("unit_ai_action", "Triggers",
                            "trigger_data[__index__].condition_data[__index__].unit_ai_action", Support(since=1.40)),
    ]

    def __init__(self,
                 condition_type: int = None,
                 quantity: int = None,
                 attribute: int = None,
                 unit_object: int = None,
                 next_object: int = None,
                 object_list: int = None,
                 source_player: IntEnum = None,
                 technology: IntEnum = None,
                 timer: int = None,
                 area_x1: int = None,
                 area_y1: int = None,
                 area_x2: int = None,
                 area_y2: int = None,
                 object_group: int = None,
                 object_type: int = None,
                 ai_signal: int = None,
                 inverted: int = None,
                 variable: int = None,
                 comparison: int = None,
                 target_player: IntEnum = None,
                 unit_ai_action: int = None,
                 object_state: int = None,
                 xs_function: str = None,
                 **kwargs
                 ):
        raise_if_not_int_subclass([object_list, technology])

        # QoL addition. When selecting a singular tile, no need for the second coords.
        if area_x2 == -1 and area_x1 != -1:
            area_x2 = area_x1
        if area_y2 == -1 and area_y1 != -1:
            area_y2 = area_y1

        # Fix, not allowed for x1 > x2 & y1 > y2
        if area_x1 > area_x2:
            area_x1, area_x2 = area_x2, area_x1
            warn("Swapping 'area_x1' and 'area_x2' values. Attribute 'area_x1' cannot be higher than 'area_x2'")
        if area_y1 > area_y2:
            area_y1, area_y2 = area_y2, area_y1
            warn("Swapping 'area_y1' and 'area_y2' values. Attribute 'area_y1' cannot be higher than 'area_y2'")

        self.condition_type: int = condition_type
        self.quantity: int = quantity
        self.attribute: int = attribute
        self.unit_object: int = unit_object
        self.next_object: int = next_object
        self.object_list: int = object_list
        self.source_player: int = source_player
        self.technology: int = technology
        self.timer: int = timer
        self.area_x1: int = area_x1
        self.area_y1: int = area_y1
        self.area_x2: int = area_x2
        self.area_y2: int = area_y2
        self.object_group: int = object_group
        self.object_type: int = object_type
        self.ai_signal: int = ai_signal
        self.inverted: int = inverted
        self.variable: int = variable
        self.comparison: int = comparison
        self.target_player: int = target_player
        self.unit_ai_action: int = unit_ai_action
        self.object_state: int = object_state
        self.xs_function: str = xs_function

        super().__init__(**kwargs)

    def get_content_as_string(self, include_effect_definition=False) -> str:
        if self.condition_type not in conditions.attributes:
            attributes_list = conditions.empty_attributes
        else:
            attributes_list = conditions.attributes[self.condition_type]

        return_string = ""
        for attribute in attributes_list:
            val = getattr(self, attribute)
            if attribute == "condition_type" or val in [[], [-1], [''], "", " ", -1]:
                continue

            value_string = transform_condition_attr_value(self.condition_type, attribute, val, self._host_uuid)
            return_string += f"{attribute}: {value_string}\n"

        if return_string == "":
            return "<< No Attributes >>\n"

        if include_effect_definition:
            return f"{conditions.condition_names[self.condition_type]}:\n{add_tabs(return_string, 1)}"

        return return_string

    def __str__(self):
        return f"[Condition] {self.get_content_as_string(include_effect_definition=True)}"
