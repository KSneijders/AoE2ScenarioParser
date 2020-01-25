from AoE2ScenarioParser.datasets.conditions import condition_identifier_conversion
from AoE2ScenarioParser.datasets.effects import effect_identifier_conversion
from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper import parser
from AoE2ScenarioParser.helper.retriever import find_retriever
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.condition_obj import ConditionObject
from AoE2ScenarioParser.objects.effect_obj import EffectObject
from AoE2ScenarioParser.pieces.structs.condition import ConditionStruct
from AoE2ScenarioParser.pieces.structs.trigger import TriggerStruct


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

        # Adding expected (by DE) ending character
        name += "\x00"

        if conditions is None:
            conditions = []
        if condition_order is None:
            condition_order = []
        if effects is None:
            effects = []
        if effect_order is None:
            effect_order = []

        super().__init__(locals())

    def get_content_as_string(self):
        return_string = ""
        data_tba = [
            ('enabled', self.data_dict['enabled'] != 0),
            ('looping', self.data_dict['looping'] != 0)
        ]

        if helper.del_str_trail(self.data_dict['description']) != "":
            data_tba.append(('description', "'" + helper.del_str_trail(self.data_dict['description']) + "'"))
        if self.data_dict['description_stid'] != 0:
            data_tba.append(('description_stid', self.data_dict['description_stid']))
        if helper.del_str_trail(self.data_dict['short_description']) != "":
            data_tba.append(('short_description', "'" + helper.del_str_trail(self.data_dict['short_description']) + "'"))
        if self.data_dict['short_description_stid'] != 0:
            data_tba.append(('short_description_stid', self.data_dict['short_description_stid']))
        if self.data_dict['display_as_objective'] != 0:
            data_tba.append(('display_as_objective', self.data_dict['display_as_objective'] != 0))
        if self.data_dict['display_on_screen'] != 0:
            data_tba.append(('display_on_screen', self.data_dict['display_on_screen'] != 0))
        if self.data_dict['description_order'] != 0:
            data_tba.append(('description_order', self.data_dict['description_order']))
        if self.data_dict['header'] != 0:
            data_tba.append(('header', self.data_dict['header'] != 0))
        if self.data_dict['mute_objectives'] != 0:
            data_tba.append(('mute_objectives', self.data_dict['mute_objectives'] != 0))

        for data in data_tba:
            return_string += "\t\t" + data[0] + ": " + str(data[1]) + "\n"

        if len(self.data_dict['condition_order']) > 0:
            return_string += "\t\tconditions:\n"
            for c_display_order, condition_id in enumerate(self.data_dict['condition_order']):
                condition = self.data_dict['conditions'][condition_id]

                return_string += "\t\t\t" + condition_identifier_conversion[condition.data_dict['condition_type']] + ":\n"
                return_string += condition.get_content_as_string()

        if len(self.data_dict['effect_order']) > 0:
            return_string += "\t\teffects:\n"
            for e_display_order, effect_id in enumerate(self.data_dict['effect_order']):
                effect = self.data_dict['effects'][effect_id]

                return_string += "\t\t\t" + effect_identifier_conversion[effect.data_dict['effect_type']] + ":\n"
                return_string += effect.get_content_as_string()

        return return_string

    def add_effect(self, effect_type):
        new_effect = EffectObject(effect_type)
        self.data_dict['effects'].append(new_effect)
        return new_effect

    def add_condition(self, condition_type):
        new_cond = ConditionObject(condition_type)
        self.data_dict['conditions'].append(new_cond)
        return new_cond

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
            condition_order=parser.listify(find_retriever(trigger.retrievers, "Condition display order array").data),
            effects=effects,
            effect_order=parser.listify(find_retriever(trigger.retrievers, "Effect display order array").data),
        )

    @staticmethod
    def reconstruct_object(parsed_data, objects, **kwargs):  # Expected {trigger=triggerStruct}
        trigger_data_retriever = find_retriever(parsed_data['TriggerPiece'].retrievers, "Trigger data")
        trigger = kwargs['trigger']

        effects = []
        for effect_obj in trigger.data_dict['effects']:
            EffectObject.reconstruct_object(parsed_data, objects, effect=effect_obj, effects=effects)

        helper.update_order_array(
            parser.listify(trigger.data_dict['effect_order']), len(trigger.data_dict['effects']))

        conditions = []
        for condition_obj in trigger.data_dict['conditions']:
            data_list = list(condition_obj.data_dict.values())
            data_list.insert(1, 21)  # Check, (21)
            data_list.insert(10, -1)  # Unknown
            data_list.insert(19, -1)  # Unknown (3)
            conditions.append(ConditionStruct(data=data_list))

        helper.update_order_array(
            parser.listify(trigger.data_dict['condition_order']), len(trigger.data_dict['conditions']))

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
        self.data_dict['name'] = val + "\x00"

    def set_description(self, val):
        self.data_dict['description'] = val + "\x00"

    def set_description_stid(self, val):
        self.data_dict['description_stid'] = val

    def set_display_as_objective(self, val):
        self.data_dict['display_as_objective'] = val

    def set_short_description(self, val):
        self.data_dict['short_description'] = val + "\x00"

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
