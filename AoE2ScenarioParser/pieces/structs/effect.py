from typing import Dict

from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.retriever_dependency import RetrieverDependency, DependencyAction, DependencyTarget, \
    DependencyEval
from AoE2ScenarioParser.pieces.aoe2_file_part import AoE2FilePart


class EffectStruct(AoE2FilePart):
    dependencies: Dict[str, Dict[str, RetrieverDependency]] = {
        "effect_type": {
            "on_commit": RetrieverDependency(
                DependencyAction.REFRESH,
                DependencyTarget(['self', 'self', 'self'], ['aa_quantity', 'aa_armor_or_attack_type', 'quantity'])
            )
        },
        "aa_quantity": {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_REPEAT,
                DependencyTarget('self', 'effect_type'),
                DependencyEval('1 if x in [28, 31] else 0')
            ),
            "on_construct": RetrieverDependency(DependencyAction.REFRESH_SELF)
        },
        "aa_armor_or_attack_type": {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_REPEAT,
                DependencyTarget('self', 'effect_type'),
                DependencyEval('1 if x in [28, 31] else 0')
            ),
            "on_construct": RetrieverDependency(DependencyAction.REFRESH_SELF)
        },
        "quantity": {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_REPEAT,
                DependencyTarget('self', 'effect_type'),
                DependencyEval('1 if x not in [28, 31] else 0')
            ),
            "on_construct": RetrieverDependency(DependencyAction.REFRESH_SELF)
        },
        "number_of_units_selected": {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_VALUE,
                DependencyTarget('self', 'selected_object_ids'),
                DependencyEval('len(x) if len(x) != 0 else -1')
            )
        },
        "selected_object_ids": {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_REPEAT,
                DependencyTarget("self", "number_of_units_selected"),
            ),
            "on_construct": RetrieverDependency(DependencyAction.REFRESH_SELF),
            "on_commit": RetrieverDependency(
                DependencyAction.REFRESH,
                DependencyTarget("self", "number_of_units_selected")
            )
        },
        # "player_color": {
        #     "on_refresh": RetrieverDependency(
        #         DependencyAction.SET_REPEAT,
        #         DependencyTarget('FileHeaderPiece', 'version'),
        #         DependencyEval('1 if x in [\'1.40\'] else 0')
        #     ),
        #     "on_construct": RetrieverDependency(DependencyAction.REFRESH_SELF)
        # },
    }

    def __init__(self):
        retrievers = [
            Retriever("effect_type", DataType("s32")),
            Retriever("static_value_46", DataType("s32")),  # always 0x17, now 0x30 (48)?
            Retriever("ai_script_goal", DataType("s32")),
            Retriever("aa_quantity", DataType("u8")),
            Retriever("aa_armor_or_attack_type", DataType("s24")),
            Retriever("quantity", DataType("s32")),
            Retriever("tribute_list", DataType("s32")),
            Retriever("diplomacy", DataType("s32")),
            Retriever("number_of_units_selected", DataType("s32")),
            Retriever("unknown", DataType("s32")),
            Retriever("object_list_unit_id", DataType("s32")),
            Retriever("source_player", DataType("s32")),
            Retriever("target_player", DataType("s32")),
            Retriever("technology", DataType("s32")),
            Retriever("string_id", DataType("s32")),
            Retriever("unknown_2", DataType("s32")),
            Retriever("display_time", DataType("s32")),
            Retriever("trigger_id", DataType("s32")),
            Retriever("location_x", DataType("s32")),
            Retriever("location_y", DataType("s32")),
            Retriever("area_1_x", DataType("s32")),
            Retriever("area_1_y", DataType("s32")),
            Retriever("area_2_x", DataType("s32")),
            Retriever("area_2_y", DataType("s32")),
            Retriever("object_group", DataType("s32")),
            Retriever("object_type", DataType("s32")),
            Retriever("instruction_panel_position", DataType("s32")),
            Retriever("attack_stance", DataType("s32")),
            Retriever("time_unit", DataType("s32")),
            Retriever("enabled_or_victory", DataType("s32")),
            Retriever("food", DataType("s32")),
            Retriever("wood", DataType("s32")),
            Retriever("stone", DataType("s32")),
            Retriever("gold", DataType("s32")),
            Retriever("item_id", DataType("s32")),
            Retriever("flash_object", DataType("s32")),
            Retriever("force_research_technology", DataType("s32")),
            Retriever("visibility_state", DataType("s32")),
            Retriever("scroll", DataType("s32")),
            Retriever("operation", DataType("s32")),
            Retriever("object_list_unit_id_2", DataType("s32")),
            Retriever("button_location", DataType("s32")),
            Retriever("ai_signal_value", DataType("s32")),
            Retriever("unknown_3", DataType("s32")),
            Retriever("object_attributes", DataType("s32")),
            Retriever("from_variable", DataType("s32")),
            Retriever("variable_or_timer", DataType("s32")),
            Retriever("facet", DataType("s32")),
            Retriever("location_object_reference", DataType("s32")),
            Retriever("play_sound", DataType("s32")),
            Retriever("player_color", DataType("s32")),
            Retriever("unknown_4", DataType("s32")),
            Retriever("message", DataType("str32")),
            Retriever("sound_name", DataType("str32")),
            Retriever("selected_object_ids", DataType("s32")),
        ]

        super().__init__("Effect", retrievers)

    @staticmethod
    def defaults(pieces):
        defaults = {
            'effect_type': 0,
            'static_value_46': 48,
            'ai_script_goal': -1,
            'quantity': -1,
            'aa_quantity': -1,
            'aa_armor_or_attack_type': -1,
            'tribute_list': -1,
            'diplomacy': -1,
            'number_of_units_selected': -1,
            'unknown': -1,
            'object_list_unit_id': -1,
            'source_player': -1,
            'target_player': -1,
            'technology': -1,
            'string_id': -1,
            'unknown_2': -1,
            'display_time': -1,
            'trigger_id': -1,
            'location_x': -1,
            'location_y': -1,
            'area_1_x': -1,
            'area_1_y': -1,
            'area_2_x': -1,
            'area_2_y': -1,
            'object_group': -1,
            'object_type': -1,
            'instruction_panel_position': -1,
            'attack_stance': -1,
            'time_unit': -1,
            'enabled_or_victory': -1,
            'food': -1,
            'wood': -1,
            'stone': -1,
            'gold': -1,
            'item_id': -1,
            'flash_object': -1,
            'force_research_technology': -1,
            'visibility_state': -1,
            'scroll': -1,
            'operation': -1,
            'object_list_unit_id_2': -1,
            'button_location': -1,
            'ai_signal_value': -1,
            'unknown_3': -1,
            'object_attributes': -1,
            'from_variable': -1,
            'variable_or_timer': -1,
            'facet': -1,
            'location_object_reference': -1,
            'play_sound': -1,
            'player_color': -1,
            'unknown_4': -1,
            'message': '',
            'sound_name': '',
            'selected_object_ids': [],
        }
        return defaults
