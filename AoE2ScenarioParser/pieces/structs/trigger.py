from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
import AoE2ScenarioParser.pieces.structs.aoe2_struct as structs
from AoE2ScenarioParser.pieces.structs.condition import ConditionStruct
from AoE2ScenarioParser.pieces.structs.effect import EffectStruct


class TriggerStruct(structs.Struct):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("Enabled", DataType("u32")),
            Retriever("Looping", DataType("s8")),
            Retriever("Description string Table ID", DataType("s32")),
            Retriever("Act as objective", DataType("u8")),
            Retriever("Description order (in objectives)", DataType("u32")),
            Retriever("Make header", DataType("u8")),
            Retriever("Short description string Table ID", DataType("s32")),
            Retriever("Display on screen", DataType("u8")),
            Retriever("Unknown", DataType("5")),
            Retriever("Mute objectives", DataType("u8")),
            # Retriever("Trigger starting time", DataType("u32")),
            Retriever("Trigger description", DataType("str32")),
            Retriever("Trigger name", DataType("str32")),  # (max 44 characters in UI)
            Retriever("Short description", DataType("str32")),
            Retriever("Number of effects", DataType("s32"), save_as="number_of_effects"),
            Retriever("Effect data", DataType(EffectStruct), set_repeat="{number_of_effects}"),
            Retriever("Effect display order array", DataType("s32"), set_repeat="{number_of_effects}"),
            Retriever("Number of conditions", DataType("s32"), save_as="number_of_conditions"),
            Retriever("Condition data", DataType(ConditionStruct), set_repeat="{number_of_conditions}"),
            Retriever("Condition display order array", DataType("s32"), set_repeat="{number_of_conditions}"),
        ]

        super().__init__("Trigger", retrievers, parser_obj, data)
