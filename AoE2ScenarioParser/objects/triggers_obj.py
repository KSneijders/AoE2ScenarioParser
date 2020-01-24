from AoE2ScenarioParser.datasets.conditions import condition_identifier_conversion
from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper import parser
from AoE2ScenarioParser.helper.retriever import find_retriever
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.trigger_obj import TriggerObject


class TriggersObject(AoE2Object):
    def __init__(self,
                 trigger_data,
                 trigger_display_order
                 ):

        super().__init__(locals())

    def add_trigger(self, name):
        new_trigger = TriggerObject(name=name)
        self.data_dict['trigger_data'].append(new_trigger)
        helper.update_order_array(self.data_dict['trigger_display_order'], len(self.data_dict['trigger_data']))
        return new_trigger

    @staticmethod
    def parse_object(parsed_data, **kwargs):  # Expected {}
        display_order = parser.listify(
            find_retriever(parsed_data['TriggerPiece'].retrievers, "Trigger display order array").data)
        trigger_data = parser.listify(
            find_retriever(parsed_data['TriggerPiece'].retrievers, "Trigger data").data)

        triggers = []
        for trigger in trigger_data:
            triggers.append(TriggerObject.parse_object(parsed_data, trigger=trigger))

        return TriggersObject(
            trigger_data=triggers,
            trigger_display_order=display_order
        )

    @staticmethod
    def reconstruct_object(parsed_data, objects, **kwargs):  # Expected {}
        number_of_triggers_retriever = find_retriever(parsed_data['TriggerPiece'].retrievers, "Number of triggers")
        trigger_data_retriever = find_retriever(parsed_data['TriggerPiece'].retrievers, "Trigger data")
        display_order_retriever = find_retriever(parsed_data['TriggerPiece'].retrievers, "Trigger display order array")

        trigger_data_retriever.data = []
        for trigger in objects["TriggersObject"].data_dict['trigger_data']:
            TriggerObject.reconstruct_object(parsed_data, objects, trigger=trigger)

        assert len(trigger_data_retriever.data) == len(objects["TriggersObject"].data_dict['trigger_data'])
        trigger_count = len(trigger_data_retriever.data)
        number_of_triggers_retriever.data = trigger_count
        # Currently not necessary due to the parser setting repeated equal to list length
        # trigger_data_retriever.datatype.repeat = trigger_count
        # display_order_retriever.datatype.repeat = trigger_count
        display_order_retriever.data = parser.listify(display_order_retriever.data)
        helper.update_order_array(display_order_retriever.data, trigger_count)

    def get_content_as_string(self):
        return_string = "Triggers:\n"

        triggers = parser.listify(self.data_dict['trigger_data'])
        display_order = parser.listify(self.data_dict['trigger_display_order'])

        if len(triggers) == 0:
            return_string += "No triggers"
            return return_string

        for display_order, trigger_id in enumerate(display_order):
            return_string += self.get_trigger_as_string(trigger_id) + "\n"

        return return_string

    def get_trigger_as_string(self, trigger_id):
        trigger = parser.listify(self.data_dict['trigger_data'])[trigger_id]
        display = parser.listify(self.data_dict['trigger_display_order']).index(trigger_id)
        trigger_data = trigger.data_dict

        return_string = ""

        return_string += "\t'" + helper.del_str_trail(trigger_data['name']) + "'"
        return_string += " [Index: " + str(trigger_id) + ", Display: " + str(display) + "]" + ":\n"

        return_string += trigger.get_content_as_string()

        return return_string


"""
to = TriggerObject(
    name="TEST\x00",
    description="TEST DESCRIPTION\x00",
    description_stid=4,
    display_as_objective=0,
    short_description="TEST SHORT DESCRIPTION\x00",
    short_description_stid=2,
    display_on_screen=1,
    description_order=0,
    enabled=1,
    looping=1,
    header=1,
    mute_objectives=0,
    conditions=[],
    condition_order=[],
    effects=[],
    effect_order=[],
)
objects["TriggersObject"].data_dict['trigger_data'].append(to)
"""
