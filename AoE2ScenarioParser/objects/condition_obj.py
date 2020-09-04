from __future__ import annotations

from enum import IntEnum

from AoE2ScenarioParser.datasets import conditions
from AoE2ScenarioParser.helper.retriever import RetrieverObjectLink
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


class ConditionObject(AoE2Object):
    """Object for handling a condition."""

    _link_list = [
        RetrieverObjectLink("condition_type",
                            "TriggerPiece.trigger_data[__index__].condition_data[__index__].condition_type"),
        RetrieverObjectLink("amount_or_quantity",
                            "TriggerPiece.trigger_data[__index__].condition_data[__index__].amount_or_quantity"),
        RetrieverObjectLink("resource_type_or_tribute_list",
                            "TriggerPiece.trigger_data[__index__].condition_data[__index__]"
                            ".resource_type_or_tribute_list"),
        RetrieverObjectLink("unit_object",
                            "TriggerPiece.trigger_data[__index__].condition_data[__index__].unit_object"),
        RetrieverObjectLink("next_object",
                            "TriggerPiece.trigger_data[__index__].condition_data[__index__].next_object"),
        RetrieverObjectLink("object_list",
                            "TriggerPiece.trigger_data[__index__].condition_data[__index__].object_list"),
        RetrieverObjectLink("source_player",
                            "TriggerPiece.trigger_data[__index__].condition_data[__index__].source_player"),
        RetrieverObjectLink("technology", "TriggerPiece.trigger_data[__index__].condition_data[__index__].technology"),
        RetrieverObjectLink("timer", "TriggerPiece.trigger_data[__index__].condition_data[__index__].timer"),
        RetrieverObjectLink("area_1_x", "TriggerPiece.trigger_data[__index__].condition_data[__index__].area_1_x"),
        RetrieverObjectLink("area_1_y", "TriggerPiece.trigger_data[__index__].condition_data[__index__].area_1_y"),
        RetrieverObjectLink("area_2_x", "TriggerPiece.trigger_data[__index__].condition_data[__index__].area_2_x"),
        RetrieverObjectLink("area_2_y", "TriggerPiece.trigger_data[__index__].condition_data[__index__].area_2_y"),
        RetrieverObjectLink("object_group",
                            "TriggerPiece.trigger_data[__index__].condition_data[__index__].object_group"),
        RetrieverObjectLink("object_type",
                            "TriggerPiece.trigger_data[__index__].condition_data[__index__].object_type"),
        RetrieverObjectLink("ai_signal", "TriggerPiece.trigger_data[__index__].condition_data[__index__].ai_signal"),
        RetrieverObjectLink("inverted", "TriggerPiece.trigger_data[__index__].condition_data[__index__].inverted"),
        RetrieverObjectLink("variable", "TriggerPiece.trigger_data[__index__].condition_data[__index__].variable"),
        RetrieverObjectLink("comparison", "TriggerPiece.trigger_data[__index__].condition_data[__index__].comparison"),
        RetrieverObjectLink("target_player",
                            "TriggerPiece.trigger_data[__index__].condition_data[__index__].target_player"),
    ]

    def __init__(self,
                 condition_type: int,
                 amount_or_quantity: int,
                 resource_type_or_tribute_list: int,
                 unit_object: int,
                 next_object: int,
                 object_list: int,
                 source_player: IntEnum,
                 technology: IntEnum,
                 timer: int,
                 area_1_x: int,
                 area_1_y: int,
                 area_2_x: int,
                 area_2_y: int,
                 object_group: int,
                 object_type: int,
                 ai_signal: int,
                 inverted: int,
                 variable: int,
                 comparison: int,
                 target_player: IntEnum
                 ):

        self.condition_type: int = condition_type
        self.amount_or_quantity: int = amount_or_quantity
        self.resource_type_or_tribute_list: int = resource_type_or_tribute_list
        self.unit_object: int = unit_object
        self.next_object: int = next_object
        self.object_list: int = object_list
        self.source_player: IntEnum = source_player
        self.technology: IntEnum = technology
        self.timer: int = timer
        self.area_1_x: int = area_1_x
        self.area_1_y: int = area_1_y
        self.area_2_x: int = area_2_x
        self.area_2_y: int = area_2_y
        self.object_group: int = object_group
        self.object_type: int = object_type
        self.ai_signal: int = ai_signal
        self.inverted: int = inverted
        self.variable: int = variable
        self.comparison: int = comparison
        self.target_player: IntEnum = target_player

        super().__init__()

    def get_content_as_string(self) -> str:
        attributes_list = conditions.attributes[self.condition_type]

        return_string = ""
        for attribute in attributes_list:
            attr = getattr(self, attribute)
            if attribute == "condition_type" or attr == [] or attr == "" or attr == " " or attr == -1:
                continue
            return_string += "\t\t\t\t" + attribute + ": " + str(attr) + "\n"

        if return_string == "":
            return "\t\t\t\t<< No Attributes >>\n"

        return return_string
