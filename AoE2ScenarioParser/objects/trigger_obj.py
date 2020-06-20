from typing import List

from AoE2ScenarioParser.datasets import effects, conditions
from AoE2ScenarioParser.datasets.conditions import Condition
from AoE2ScenarioParser.datasets.effects import Effect
from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper import parser
from AoE2ScenarioParser.helper.retriever import find_retriever
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.condition_obj import ConditionObject
from AoE2ScenarioParser.objects.effect_obj import EffectObject
from AoE2ScenarioParser.pieces.structs.trigger import TriggerStruct


class TriggerObject(AoE2Object):
    def __init__(self,
                 name: str,
                 description: str = "",
                 description_stid: int = -1,
                 display_as_objective: int = 0,
                 short_description: str = "",
                 short_description_stid: int = -1,
                 display_on_screen: int = 0,
                 description_order: int = 0,
                 enabled: int = 1,
                 looping: int = 0,
                 header: int = 0,
                 mute_objectives: int = 0,
                 conditions_list: List[ConditionObject] = None,
                 condition_order: List[int] = None,
                 effects_list: List[EffectObject] = None,
                 effect_order: List[int] = None,
                 trigger_id: int = -1,
                 ):

        if conditions_list is None:
            conditions_list = []
        if condition_order is None:
            condition_order = []
        if effects_list is None:
            effects_list = []
        if effect_order is None:
            effect_order = []

        self.name: str = name
        self.description: str = description
        self.description_stid: int = description_stid
        self.display_as_objective: int = display_as_objective
        self.short_description: str = short_description
        self.short_description_stid: int = short_description_stid
        self.display_on_screen: int = display_on_screen
        self.description_order: int = description_order
        self.enabled: int = enabled
        self.looping: int = looping
        self.header: int = header
        self.mute_objectives: int = mute_objectives
        self.conditions: List[ConditionObject] = conditions_list
        self.condition_order: List[int] = condition_order
        self.effects: List[EffectObject] = effects_list
        self.effect_order: List[int] = effect_order
        self.trigger_id: int = trigger_id

        self.trigger_id = trigger_id

        super().__init__()

    @property
    def conditions(self):
        return self._conditions

    @conditions.setter
    def conditions(self, val):
        self._conditions = val
        self.condition_order = list(range(0, len(val)))

    @property
    def effects(self):
        return self._effects

    @effects.setter
    def effects(self, val):
        self._effects = val
        self.effect_order = list(range(0, len(val)))

    def add_effect(self, effect_type: Effect) -> EffectObject:
        new_effect = EffectObject(**effects.default_attributes[effect_type.value])
        self.effects.append(new_effect)
        helper.update_order_array(self.effect_order, len(self.effects))
        return new_effect

    def add_condition(self, condition_type: Condition) -> ConditionObject:
        new_cond = ConditionObject(**conditions.default_attributes[condition_type.value])
        self.conditions.append(new_cond)
        helper.update_order_array(self.condition_order, len(self.conditions))
        return new_cond

    def get_content_as_string(self) -> str:
        return_string = ""
        data_tba = [
            ('enabled', self.enabled != 0),
            ('looping', self.looping != 0)
        ]

        if helper.del_str_trail(self.description) != "":
            data_tba.append(('description', "'" + helper.del_str_trail(self.description) + "'"))
        if self.description_stid != -1:
            data_tba.append(('description_stid', self.description_stid))
        if helper.del_str_trail(self.short_description) != "":
            data_tba.append(('short_description', "'" + helper.del_str_trail(self.short_description) + "'"))
        if self.short_description_stid != -1:
            data_tba.append(('short_description_stid', self.short_description_stid))
        if self.display_as_objective != 0:
            data_tba.append(('display_as_objective', self.display_as_objective != 0))
        if self.display_on_screen != 0:
            data_tba.append(('display_on_screen', self.display_on_screen != 0))
        if self.description_order != 0:
            data_tba.append(('description_order', self.description_order))
        if self.header != 0:
            data_tba.append(('header', self.header != 0))
        if self.mute_objectives != 0:
            data_tba.append(('mute_objectives', self.mute_objectives != 0))

        for data in data_tba:
            return_string += "\t\t" + data[0] + ": " + str(data[1]) + "\n"

        if len(self.condition_order) > 0:
            return_string += "\t\tconditions:\n"
            for c_display_order, condition_id in enumerate(self.condition_order):
                condition = self.conditions[condition_id]

                return_string += f"\t\t\t{conditions.condition_names[condition.condition_type]} " \
                                 f"[Index: {condition_id}, Display: {c_display_order}]:\n"
                return_string += condition.get_content_as_string()

        if len(self.effect_order) > 0:
            return_string += "\t\teffects:\n"
            for e_display_order, effect_id in enumerate(self.effect_order):
                effect = self.effects[effect_id]

                return_string += f"\t\t\t{effects.effect_names[effect.effect_type]} " \
                                 f"[Index: {effect_id}, Display: {e_display_order}]:\n"
                return_string += effect.get_content_as_string()

        return return_string

    def get_effect(self, effect_index: int = None, display_index: int = None) -> EffectObject:
        helper.evaluate_index_params(effect_index, display_index, "effect")

        if effect_index is None:
            effect_index = self.effect_order[display_index]

        return parser.listify(self.effects)[effect_index]

    def get_condition(self, condition_index: int = None, display_index: int = None) -> ConditionObject:
        helper.evaluate_index_params(condition_index, display_index, "condition")

        if condition_index is None:
            condition_index = self.condition_order[display_index]

        return parser.listify(self.conditions)[condition_index]

    def get_summary_as_string(self) -> str:
        pass

    def remove_effect(self, effect_index: int = None, display_index: int = None, effect: EffectObject = None) -> None:
        if effect is None:
            helper.evaluate_index_params(effect_index, display_index, "effect")
        else:
            effect_index = self.effects.index(effect)

        if effect_index is None:
            effect_index = self.effect_order[display_index]
        else:
            display_index = self.effect_order.index(effect_index)

        del self.effects[effect_index]
        del self.effect_order[display_index]

        self.effect_order = [x - 1 if x > effect_index else x for x in self.effect_order]

    def remove_condition(self, condition_index: int = None, display_index: int = None, condition: EffectObject = None) \
            -> None:
        if condition is None:
            helper.evaluate_index_params(condition_index, display_index, "condition")
        else:
            condition_index = self.conditions.index(condition)

        if condition_index is None:
            condition_index = self.condition_order[display_index]
        else:
            display_index = self.condition_order.index(condition_index)

        del self.conditions[condition_index]
        del self.condition_order[display_index]

        self.condition_order = [x - 1 if x > condition_index else x for x in self.condition_order]

    @staticmethod
    def _parse_object(parsed_data, **kwargs):  # Expected {trigger=triggerStruct, trigger_id=id}
        trigger = kwargs['trigger']

        effects_list = []
        effect_structs = parser.listify(find_retriever(trigger.retrievers, "Effect data").data)
        for effect_struct in effect_structs:
            effects_list.append(EffectObject._parse_object(parsed_data, effect=effect_struct))

        conditions_list = []
        condition_structs = parser.listify(find_retriever(trigger.retrievers, "Condition data").data)
        for condition_struct in condition_structs:
            conditions_list.append(ConditionObject._parse_object(parsed_data, condition=condition_struct))

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
            conditions_list=conditions_list,
            condition_order=parser.listify(find_retriever(trigger.retrievers, "Condition display order array").data),
            effects_list=effects_list,
            effect_order=parser.listify(find_retriever(trigger.retrievers, "Effect display order array").data),
            trigger_id=kwargs['trigger_id'],
        )

    @staticmethod
    def _reconstruct_object(parsed_header, parsed_data, objects, **kwargs):  # Expected {trigger=triggerStruct}
        trigger_data_retriever = find_retriever(parsed_data['TriggerPiece'].retrievers, "Trigger data")
        trigger = kwargs['trigger']
        trigger.effect_order = parser.listify(trigger.effect_order)
        trigger.condition_order = parser.listify(trigger.condition_order)

        effects_list = []
        for effect_obj in trigger.effects:
            EffectObject._reconstruct_object(parsed_header, parsed_data, objects, effect=effect_obj,
                                             effects=effects_list)

        helper.update_order_array(trigger.effect_order, len(trigger.effects))

        conditions_list = []
        for condition_obj in trigger.conditions:
            ConditionObject._reconstruct_object(parsed_header, parsed_data, objects, condition=condition_obj,
                                                conditions=conditions_list)

        helper.update_order_array(trigger.condition_order, len(trigger.conditions))

        trigger_data_retriever.data.append(
            TriggerStruct(data=[
                trigger.enabled,
                trigger.looping,
                trigger.description_stid,
                trigger.display_as_objective,
                trigger.description_order,
                trigger.header,
                trigger.short_description_stid,
                trigger.display_on_screen,
                b'\x00\x00\x00\x00\x00',  # Unknown
                trigger.mute_objectives,
                trigger.description,
                trigger.name,
                trigger.short_description,
                len(trigger.effects),
                effects_list,
                trigger.effect_order,
                len(trigger.conditions),
                conditions_list,
                trigger.condition_order,
            ])
        )
