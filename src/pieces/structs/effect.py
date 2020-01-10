from src.helper.datatype import DataType
from src.helper.retriever import Retriever
import src.pieces.structs.aoe2_struct as structs


class EffectStruct(structs.Struct):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("Effect type", DataType("s32"), save_as="effect_type"),                               # CONFIRMED
            Retriever("Check, (46)", DataType("s32")),  # always 0x17, now 0x2e (46)?                       # CONFIRMED
            Retriever("AI script goal", DataType("s32")),                                                   # CONFIRMED
            Retriever("AA Quantity", DataType("u8"),
                      set_repeat="1 if {effect_type} == 31 or {effect_type} == 28 else 0"),                 # CONFIRMED
            Retriever("AA Armor/Attack Type", DataType("s24"),
                      set_repeat="1 if {effect_type} == 31 or {effect_type} == 28 else 0"),                 # CONFIRMED
            Retriever("Quantity", DataType("s32"),
                      set_repeat="1 if {effect_type} != 31 and {effect_type} != 28 else 0"),                # CONFIRMED
            Retriever("Tribute List", DataType("s32")),                                                     # CONFIRMED
            Retriever("Diplomacy", DataType("s32")),                                                        # CONFIRMED
            Retriever("Number of units selected", DataType("s32"), save_as="number_of_units_selected"),     # CONFIRMED
            Retriever("Unknown", DataType("s32")),                                                          # UNUSED
            Retriever("Object list unit ID", DataType("s32")),                                              # CONFIRMED
            Retriever("Player Source", DataType("s32")),                                                    # CONFIRMED
            Retriever("Player Target", DataType("s32")),                                                    # CONFIRMED
            Retriever("Technology", DataType("s32")),                                                       # CONFIRMED
            Retriever("String ID", DataType("s32")),                                                        # CONFIRMED
            Retriever("Unknown2", DataType("s32")),                                                         # UNUSED
            Retriever("Display Time (display instructions)", DataType("s32")),                              # CONFIRMED
            Retriever("Trigger ID (activate/deactivate)", DataType("s32")),                                 # CONFIRMED
            Retriever("Location X", DataType("s32")),                                                       # CONFIRMED
            Retriever("Location Y", DataType("s32")),                                                       # CONFIRMED
            Retriever("Area 1 X", DataType("s32")),                                                         # CONFIRMED
            Retriever("Area 1 Y", DataType("s32")),                                                         # CONFIRMED
            Retriever("Area 2 X", DataType("s32")),                                                         # CONFIRMED
            Retriever("Area 2 Y", DataType("s32")),                                                         # CONFIRMED
            Retriever("Object Group", DataType("s32")),                                                     # CONFIRMED
            Retriever("Object Type", DataType("s32")),                                                      # CONFIRMED
            Retriever("Instruction Panel Position", DataType("s32")),                                       # CONFIRMED
            Retriever("Attack Stance", DataType("s32")),                                                    # CONFIRMED
            Retriever("Time unit (second, minutes, years)", DataType("s32")),                               # CONFIRMED
            Retriever("Enabled/Victory", DataType("s32")),                                                  # CONFIRMED
            Retriever("Food", DataType("s32")),                                                             # CONFIRMED
            Retriever("Wood", DataType("s32")),                                                             # CONFIRMED
            Retriever("Stone", DataType("s32")),                                                            # CONFIRMED
            Retriever("Gold", DataType("s32")),                                                             # CONFIRMED
            Retriever("Item ID", DataType("s32")),                                                          # CONFIRMED
            Retriever("Flash Object", DataType("s32")),                                                     # CONFIRMED
            Retriever("Force Research Technology", DataType("s32")),                                        # CONFIRMED
            Retriever("Visibility State", DataType("s32")),                                                 # CONFIRMED
            Retriever("Scroll (Set view)", DataType("s32")),                                                # CONFIRMED
            Retriever("Operation", DataType("s32")),                                                        # CONFIRMED
            Retriever("Object list unit ID 2", DataType("s32")),                                            # CONFIRMED
            Retriever("Button Location", DataType("s32")),                                                  # CONFIRMED
            Retriever("AI signal Value", DataType("s32")),                                                  # CONFIRMED
            Retriever("Unknown3", DataType("s32")),                                                         # UNUSED
            Retriever("Object attributes", DataType("s32")),                                                # CONFIRMED
            Retriever("From Variable", DataType("s32")),                                                    # CONFIRMED
            Retriever("Variable/Timer", DataType("s32")),                                                   # CONFIRMED
            Retriever("Facet", DataType("s32")),                                                            # CONFIRMED
            Retriever("Unknown4", DataType("s32")),                                                         # UNUSED
            Retriever("Play Sound", DataType("s32")),                                                       # CONFIRMED
            Retriever("Message", DataType("str32")),                                                        # CONFIRMED
            Retriever("Sound (event) name", DataType("str32")),                                             # CONFIRMED
            Retriever("Selected Object(s) ID", DataType("s32"), set_repeat="{number_of_units_selected}"),   # CONFIRMED
        ]

        super().__init__("Effect", retrievers, parser_obj, data)
