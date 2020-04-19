from __future__ import annotations

from typing import List
from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper import parser
from AoE2ScenarioParser.helper.retriever import find_retriever
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.trigger_obj import TriggerObject


def _evaluate_index_params(trigger_id, display_index):
    if trigger_id is None and display_index is None:
        raise ValueError("Please choose 'trigger_id' or 'display_index' as identification for the wanted trigger")
    if trigger_id is not None and display_index is not None:
        raise ValueError("Please identify a trigger using 'trigger_id' or 'display_index' but not both")


class TriggersObject(AoE2Object):
    def __init__(self,
                 trigger_data,
                 trigger_display_order
                 ):

        self.trigger_data = trigger_data
        self.trigger_display_order = trigger_display_order

        super().__init__()

    def add_trigger(self, name) -> TriggerObject:
        new_trigger = TriggerObject(name=name, trigger_id=len(self.trigger_data))
        self.trigger_data.append(new_trigger)
        helper.update_order_array(self.trigger_display_order, len(self.trigger_data))
        return new_trigger

    @staticmethod
    def _parse_object(parsed_data, **kwargs) -> TriggersObject:  # Expected {}
        display_order = parser.listify(
            find_retriever(parsed_data['TriggerPiece'].retrievers, "Trigger display order array").data)
        trigger_data = parser.listify(
            find_retriever(parsed_data['TriggerPiece'].retrievers, "Trigger data").data)

        triggers = []
        for index, trigger in enumerate(trigger_data):
            triggers.append(TriggerObject._parse_object(parsed_data, trigger=trigger, trigger_id=index))

        return TriggersObject(
            trigger_data=triggers,
            trigger_display_order=display_order
        )

    @staticmethod
    def _reconstruct_object(parsed_data, objects, **kwargs) -> None:  # Expected {}
        number_of_triggers_retriever = find_retriever(parsed_data['TriggerPiece'].retrievers, "Number of triggers")
        trigger_data_retriever = find_retriever(parsed_data['TriggerPiece'].retrievers, "Trigger data")
        display_order_retriever = find_retriever(parsed_data['TriggerPiece'].retrievers, "Trigger display order array")

        trigger_data_retriever.data = []
        for trigger in objects["TriggersObject"].trigger_data:
            TriggerObject._reconstruct_object(parsed_data, objects, trigger=trigger)

        assert len(trigger_data_retriever.data) == len(objects["TriggersObject"].trigger_data)
        trigger_count = len(trigger_data_retriever.data)
        number_of_triggers_retriever.data = trigger_count
        # Currently not necessary due to the parser changing the 'repeated' value equal to the len(list)
        # trigger_data_retriever.datatype.repeat = trigger_count
        # display_order_retriever.datatype.repeat = trigger_count
        helper.update_order_array(parser.listify(display_order_retriever.data), trigger_count)

    def get_summary_as_string(self) -> str:
        return_string = "Trigger Summary:\n"

        triggers = parser.listify(self.trigger_data)
        display_order = parser.listify(self.trigger_display_order)

        longest_trigger_name = -1
        for trigger_id in display_order:
            trigger_name = helper.del_str_trail(triggers[trigger_id].name)
            longest_trigger_name = max(longest_trigger_name, len(trigger_name))

        longest_trigger_name += 3
        for display, trigger_id in enumerate(display_order):
            trigger = triggers[trigger_id]
            trigger_name = helper.del_str_trail(trigger.name)

            buffer = longest_trigger_name - len(trigger_name)
            return_string += "\t" + trigger_name + (" " * buffer)
            return_string += " [Index: " + str(trigger_id) + ", Display: " + str(display) + "]"

            return_string += "\t(conditions: " + str(len(parser.listify(trigger.conditions))) + ", "
            return_string += " effects: " + str(len(parser.listify(trigger.effects))) + ")\n"

        return return_string

    def get_content_as_string(self) -> str:
        return_string = "Triggers:\n"

        triggers = parser.listify(self.trigger_data)
        display_order = parser.listify(self.trigger_display_order)

        if len(triggers) == 0:
            return return_string + "\t<<No triggers>>"

        for trigger_id in display_order:
            return_string += self.get_trigger_as_string(trigger_id) + "\n"

        return return_string

    def get_trigger_as_string(self, trigger_id=None, display_index=None) -> str:
        _evaluate_index_params(trigger_id, display_index)

        if trigger_id is None:
            trigger_id = self._get_trigger_id_by_display_index(display_index)

        trigger = parser.listify(self.trigger_data)[trigger_id]
        display = parser.listify(self.trigger_display_order).index(trigger_id)

        return_string = ""

        return_string += "\t'" + helper.del_str_trail(trigger.name) + "'"
        return_string += " [Index: " + str(trigger_id) + ", Display: " + str(display) + "]" + ":\n"

        return_string += trigger.get_content_as_string()

        return return_string

    def get_trigger(self, trigger_id=None, display_index=None) -> TriggerObject:
        _evaluate_index_params(trigger_id, display_index)

        if trigger_id is None:
            trigger_id = self._get_trigger_id_by_display_index(display_index)

        return parser.listify(self.trigger_data)[trigger_id]

    def get_triggers(self) -> List[TriggerObject]:
        return parser.listify(self.trigger_data)

    def delete_trigger(self, trigger_id=None, display_index=None) -> None:
        _evaluate_index_params(trigger_id, display_index)

        if trigger_id is None:
            trigger_id = self._get_trigger_id_by_display_index(display_index)
        else:
            display_index = self.trigger_display_order.index(trigger_id)

        del self.trigger_data[trigger_id]
        del self.trigger_display_order[display_index]

        self.trigger_display_order = \
            [x - 1 if x > trigger_id else x for x in self.trigger_display_order]

    def _get_trigger_id_by_display_index(self, display_index) -> int:
        return self.trigger_display_order[display_index]
