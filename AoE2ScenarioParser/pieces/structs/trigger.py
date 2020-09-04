from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.structs.aoe2_struct import AoE2Struct
from AoE2ScenarioParser.pieces.structs.condition import ConditionStruct
from AoE2ScenarioParser.pieces.structs.effect import EffectStruct


class TriggerStruct(AoE2Struct):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("enabled", DataType("u32")),
            Retriever("looping", DataType("s8")),
            Retriever("description_string_table_id", DataType("s32")),
            Retriever("display_as_objective", DataType("u8")),
            Retriever("objective_description_order", DataType("u32")),
            Retriever("make_header", DataType("u8")),
            Retriever("short_description_string_table_id", DataType("s32")),
            Retriever("display_on_screen", DataType("u8")),
            Retriever("unknown", DataType("5")),
            Retriever("mute_objectives", DataType("u8")),
            # Retriever("Trigger starting time", DataType("u32")),
            Retriever("trigger_description", DataType("str32")),
            Retriever("trigger_name", DataType("str32")),  # (max 44 characters in UI)
            Retriever("short_description", DataType("str32")),
            Retriever("number_of_effects", DataType("s32"), save_as="number_of_effects"),
            Retriever("effect_data", DataType(EffectStruct), set_repeat="{number_of_effects}"),
            Retriever("effect_display_order_array", DataType("s32"), set_repeat="{number_of_effects}"),
            Retriever("number_of_conditions", DataType("s32"), save_as="number_of_conditions"),
            Retriever("condition_data", DataType(ConditionStruct), set_repeat="{number_of_conditions}"),
            Retriever("condition_display_order_array", DataType("s32"), set_repeat="{number_of_conditions}"),
        ]

        super().__init__("Trigger", retrievers, parser_obj, data)
