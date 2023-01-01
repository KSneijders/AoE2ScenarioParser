from __future__ import annotations

from enum import IntEnum
from typing import Any

from AoE2ScenarioParser.datasets import conditions
from AoE2ScenarioParser.datasets.conditions import ConditionId
from AoE2ScenarioParser.helper.helper import raise_if_not_int_subclass, validate_coords
from AoE2ScenarioParser.helper.string_manipulations import add_tabs
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.support.attr_presentation import transform_condition_attr_value
from AoE2ScenarioParser.objects.support.trigger_object import TriggerComponent
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.sections.retrievers.retriever_object_link_group import RetrieverObjectLinkGroup
from AoE2ScenarioParser.sections.retrievers.support import Support


class Condition(AoE2Object, TriggerComponent):
    """Object for handling a condition."""
    hidden_attribute = 'condition_type'

    _link_list = [
        RetrieverObjectLinkGroup("Triggers", "trigger_data[__index__].condition_data[__index__]", group=[
            RetrieverObjectLink("condition_type"),
            RetrieverObjectLink("quantity"),
            RetrieverObjectLink("attribute"),
            RetrieverObjectLink("unit_object"),
            RetrieverObjectLink("next_object"),
            RetrieverObjectLink("object_list"),
            RetrieverObjectLink("source_player"),
            RetrieverObjectLink("technology"),
            RetrieverObjectLink("timer"),
            RetrieverObjectLink("area_x1"),
            RetrieverObjectLink("area_y1"),
            RetrieverObjectLink("area_x2"),
            RetrieverObjectLink("area_y2"),
            RetrieverObjectLink("object_group"),
            RetrieverObjectLink("object_type"),
            RetrieverObjectLink("ai_signal"),
            RetrieverObjectLink("inverted"),
            RetrieverObjectLink("variable"),
            RetrieverObjectLink("comparison"),
            RetrieverObjectLink("target_player"),
            RetrieverObjectLink("unit_ai_action", support=Support(since=1.40)),
            RetrieverObjectLink("object_state", support=Support(since=1.42)),
            RetrieverObjectLink("timer_id", support=Support(since=1.46)),
            RetrieverObjectLink("victory_timer_type", support=Support(since=1.46)),
            RetrieverObjectLink("include_changeable_weapon_objects", support=Support(since=1.46)),
            RetrieverObjectLink("xs_function", support=Support(since=1.40)),
        ])
    ]

    def __init__(
            self,
            condition_type: int = None,
            quantity: int = None,
            attribute: int = None,
            unit_object: int = None,
            next_object: int = None,
            object_list: int = None,
            source_player: int | IntEnum = None,
            technology: int | IntEnum = None,
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
            target_player: int | IntEnum = None,
            unit_ai_action: int = None,
            object_state: int = None,
            timer_id: int = None,
            victory_timer_type: int = None,
            include_changeable_weapon_objects: int = None,
            xs_function: str = None,
            **kwargs
    ):
        raise_if_not_int_subclass([object_list, technology])
        area_x1, area_y1, area_x2, area_y2 = validate_coords(area_x1, area_y1, area_x2, area_y2)

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
        self.timer_id: int = timer_id
        self.victory_timer_type: int = victory_timer_type
        self.include_changeable_weapon_objects: int = include_changeable_weapon_objects
        self.xs_function: str = xs_function

        super().__init__(**kwargs)

    def _should_be_displayed(self, attr: str, val: Any) -> bool:
        # Include the only exception to the -1 == invalid rule
        if self.condition_type == ConditionId.DIFFICULTY_LEVEL and attr == 'quantity' and val == -1:
            return True

        return super()._should_be_displayed(attr, val)

    def get_content_as_string(self, include_condition_definition: bool = False) -> str:
        """
        Create a human-readable string showcasing all content of this condition.

        This is also the function that is called when doing: `print(condition)`

        Args:
            include_condition_definition: If the condition meta-data should be added by this function

        Returns:
            The created string
        """
        if self.condition_type not in conditions.attributes:
            attributes_list = conditions.empty_attributes
        else:
            attributes_list = conditions.attributes[self.condition_type]

        return_string = ""
        for attribute in attributes_list:
            val = getattr(self, attribute)
            if not self._should_be_displayed(attribute, val):
                continue

            value_string = transform_condition_attr_value(self.condition_type, attribute, val, self._uuid)
            return_string += f"{attribute}: {value_string}\n"

        if return_string == "":
            return "<< No Attributes >>\n"

        if include_condition_definition:
            return f"{conditions.condition_names[self.condition_type]}:\n{add_tabs(return_string, 1)}"

        return return_string

    def __str__(self):
        return f"[Condition] {self.get_content_as_string(include_condition_definition=True)}"
