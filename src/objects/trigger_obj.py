import copy
from src.objects.aoe2_object import AoE2Object
from src.helper.retriever import find_retriever
from src.helper import parser
from src.helper import helper
from src.datasets import effect
from src.datasets import condition
from src.objects.condition_obj import ConditionObject
from src.objects.effect_obj import EffectObject
from src.pieces.structs.condition import ConditionStruct
from src.pieces.structs.effect import EffectStruct
from src.pieces.structs.trigger import TriggerStruct


class TriggerObject(AoE2Object):
    def __init__(self,
                 name,
                 description="",
                 description_stid=0,
                 display_as_objective=0,
                 short_description="",
                 short_description_stid=0,
                 display_on_screen=0,
                 description_order=0,
                 enabled=1,
                 looping=0,
                 header=0,
                 mute_objectives=0,
                 conditions=None,
                 condition_order=None,
                 effects=None,
                 effect_order=None,
                 ):

        if conditions is None:
            conditions = []
        if condition_order is None:
            condition_order = []
        if effects is None:
            effects = []
        if effect_order is None:
            effect_order = []

        super().__init__(locals())

    # def add_trigger(self, name):
    #     new_trigger = TriggerObject(name=name)
    #     self.data_dict['trigger_data'].append(new_trigger)
    #     return new_trigger

    def add_effect(self, effect_type):
        pass

    def add_condition(self, condition_type):
        pass

    @staticmethod
    def parse_object(parsed_data, **kwargs):  # Expected {trigger=triggerStruct}
        trigger = kwargs['trigger']

        effects = []
        effect_structs = parser.listify(find_retriever(trigger.retrievers, "Effect data").data)
        for effect_struct in effect_structs:
            effects.append(EffectObject.parse_object(parsed_data, effect=effect_struct))

        conditions = []
        condition_structs = parser.listify(find_retriever(trigger.retrievers, "Condition data").data)
        for condition_struct in condition_structs:
            conditions.append(ConditionObject.parse_object(parsed_data, condition=condition_struct))

        return TriggerObject(
            name=find_retriever(trigger.retrievers, "Trigger name").data,
            description=find_retriever(trigger.retrievers, "Trigger description").data,
            description_stid=find_retriever(trigger.retrievers, "Description string Table ID").data,
            display_as_objective=find_retriever(trigger.retrievers, "Act as objective").data,
            short_description=find_retriever(trigger.retrievers, "Short description").data,
            short_description_stid=find_retriever(trigger.retrievers, "Short description string Table ID").data,
            display_on_screen=find_retriever(trigger.retrievers, "Display on screen").data,
            description_order=find_retriever(trigger.retrievers, "Description order (in objectives)").data,
            enabled=find_retriever(trigger.retrievers, "Enabled").data,
            looping=find_retriever(trigger.retrievers, "Looping").data,
            header=find_retriever(trigger.retrievers, "Make header").data,
            mute_objectives=find_retriever(trigger.retrievers, "Mute objectives").data,
            conditions=conditions,
            condition_order=find_retriever(trigger.retrievers, "Condition display order array").data,
            effects=effects,
            effect_order=find_retriever(trigger.retrievers, "Effect display order array").data,
        )

    @staticmethod
    def reconstruct_object(parsed_data, objects, **kwargs):  # Expected {trigger=triggerStruct}
        trigger_data_retriever = find_retriever(parsed_data['TriggerPiece'].retrievers, "Trigger data")
        trigger = kwargs['trigger']

        effects = []
        for effect_obj in trigger.data_dict['effects']:
            data_list = list(effect_obj.data_dict.values())
            data_list.insert(1, 46)  # Check, (46)
            data_list.insert(9, 0)   # Unknown
            data_list.insert(15, 0)  # Unknown2
            data_list.insert(43, 0)  # Unknown3
            data_list.insert(48, 0)  # Unknown4

            effects.append(EffectStruct(data=data_list))

        helper.update_order_array(trigger.data_dict['effect_order'], len(trigger.data_dict['effects']))

        conditions = []
        for condition_obj in trigger.data_dict['conditions']:
            data_list = list(condition_obj.data_dict.values())
            data_list.insert(1, 21)  # Check, (21)
            data_list.insert(10, 0)  # Unknown
            data_list.insert(19, 0)  # Unknown (3)
            conditions.append(ConditionStruct(data=data_list))

        helper.update_order_array(trigger.data_dict['condition_order'], len(trigger.data_dict['conditions']))

        trigger_data_retriever.data.append(TriggerStruct(data=[
            trigger.data_dict['enabled'],
            trigger.data_dict['looping'],
            trigger.data_dict['description_stid'],
            trigger.data_dict['display_as_objective'],
            trigger.data_dict['description_order'],
            trigger.data_dict['header'],
            trigger.data_dict['short_description_stid'],
            trigger.data_dict['display_on_screen'],
            b'\x00\x00\x00\x00\x00',  # Unknown
            trigger.data_dict['mute_objectives'],
            trigger.data_dict['description'],
            trigger.data_dict['name'],
            trigger.data_dict['short_description'],
            len(trigger.data_dict['effects']),
            effects,
            trigger.data_dict['effect_order'],
            len(trigger.data_dict['conditions']),
            conditions,
            trigger.data_dict['condition_order'],
        ]))

    def set_name(self, val):
        self.data_dict['name'] = val

    def set_description(self, val):
        self.data_dict['description'] = val

    def set_description_stid(self, val):
        self.data_dict['description_stid'] = val

    def set_display_as_objective(self, val):
        self.data_dict['display_as_objective'] = val

    def set_short_description(self, val):
        self.data_dict['short_description'] = val

    def set_short_description_stid(self, val):
        self.data_dict['short_description_stid'] = val

    def set_display_on_screen(self, val):
        self.data_dict['display_on_screen'] = val

    def set_description_order(self, val):
        self.data_dict['description_order'] = val

    def set_enabled(self, val):
        self.data_dict['enabled'] = val

    def set_looping(self, val):
        self.data_dict['looping'] = val

    def set_header(self, val):
        self.data_dict['header'] = val

    def set_mute_objectives(self, val):
        self.data_dict['mute_objectives'] = val

    def set_conditions(self, val):
        self.data_dict['conditions'] = val

    def set_condition_order(self, val):
        self.data_dict['condition_order'] = val

    def set_effects(self, val):
        self.data_dict['effects'] = val

    def set_effect_order(self, val):
        self.data_dict['effect_order'] = val
