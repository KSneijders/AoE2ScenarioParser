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
                 description,
                 description_stid,
                 display_as_objective,
                 short_description,
                 short_description_stid,
                 display_on_screen,
                 description_order,
                 enabled,
                 looping,
                 header,
                 mute_objectives,
                 conditions,
                 condition_order,
                 effects,
                 effect_order,
                 ):

        super().__init__(locals())

    @staticmethod
    def parse_object(parsed_data, **kwargs):  # Expected {trigger=triggerStruct}
        trigger = kwargs['trigger']

        effects = []
        effect_structs = parser.listify(find_retriever(trigger.retrievers, "Effect data").data)
        for effect_struct in effect_structs:
            effect_type = find_retriever(effect_struct.retrievers, "Effect type").data
            parameters = effect.parameters.get(effect_type)

            parameter_dict = copy.copy(effect.empty_parameters)
            for param in parameters:
                inverted_name = effect.naming_conversion.get(param)
                parameter_dict[inverted_name] = find_retriever(effect_struct.retrievers, param).data

            effects.append(EffectObject(
                **parameter_dict
            ))

        conditions = []
        condition_structs = parser.listify(find_retriever(trigger.retrievers, "Condition data").data)
        for condition_struct in condition_structs:
            condition_type = find_retriever(condition_struct.retrievers, "Condition type").data
            parameters = condition.parameters.get(condition_type)

            parameter_dict = copy.copy(condition.empty_parameters)
            for param in parameters:
                inverted_name = condition.naming_conversion.get(param)
                parameter_dict[inverted_name] = find_retriever(condition_struct.retrievers, param).data

            conditions.append(ConditionObject(
                **parameter_dict
            ))

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
