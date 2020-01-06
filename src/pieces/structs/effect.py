from src.helper.datatype import DataType
from src.helper.retriever import Retriever
import src.pieces.structs.aoe2_struct as structs


class EffectStruct(structs.Struct):
    def __init__(self, parser_obj, data=None):
        retrievers = [
            Retriever("Effect type", DataType("s32"), save_as="effect_type"),                               # CONFIRMED
            Retriever("Check, (46)", DataType("s32")),  # always 0x17, now 0x2e (46)?                       # CONFIRMED
            Retriever("AI script goal", DataType("s32")),                                                   # CONFIRMED
            Retriever("Quantity", DataType("u8"), set_repeat="1 if {effect_type} == 31 else 0"),            # CONFIRMED
            Retriever("Armor/Attack Type", DataType("s24"), set_repeat="1 if {effect_type} == 31 else 0"),  # CONFIRMED
            Retriever("Quantity", DataType("s32"), set_repeat="1 if {effect_type} != 31 else 0"),           # CONFIRMED
            # Retriever("Armor/Attack Type", DataType("s24")),                                              # CONFIRMED
            Retriever("Resource type/Tribute item", DataType("s32")),                                       # CONFIRMED
            Retriever("Diplomacy, state for change", DataType("s32")),                                      # CONFIRMED
            Retriever("Number of units selected", DataType("s32"), save_as="number_of_units_selected"),     # CONFIRMED
            Retriever("Unit ID", DataType("s32")),                                                          # ?
            Retriever("Object list unit ID", DataType("s32")),                                              # CONFIRMED
            Retriever("Player Source", DataType("s32")),                                                    # CONFIRMED
            Retriever("Player Target", DataType("s32")),                                                    # CONFIRMED
            Retriever("Technology", DataType("s32")),                                                       # CONFIRMED
            Retriever("String ID", DataType("s32")),                                                        # CONFIRMED
            Retriever("Sound resource ID", DataType("s32")),                                                # ?
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
            Retriever("Attack Stance", DataType("s32")),  # o:Instruction Text (str32)                      # CONFIRMED
            Retriever("Time unit (second, minutes, years)", DataType("s32")),                               # CONFIRMED
            Retriever("Enabled (enable/disable objects/units/techs)", DataType("s32")),                     # CONFIRMED
            Retriever("Victory (win or lose)", DataType("s32")),                                            # CONFIRMED
            Retriever("Food", DataType("s32")),                                                             # CONFIRMED
            Retriever("Wood", DataType("s32")),                                                             # CONFIRMED
            Retriever("Gold", DataType("s32")),                                                             # CONFIRMED
            # Stores IDs in many effects. (Possible bugs)                                                   # #########
            Retriever("Stone", DataType("s32")),                                                            # CONFIRMED
            Retriever("Flash Object", DataType("s32")),                                                     # CONFIRMED
            Retriever("Force Research Technology", DataType("s32")),                                        # CONFIRMED
            Retriever("Visibility State", DataType("s32")),                                                 # CONFIRMED
            Retriever("Scroll (Set view)", DataType("s32")),                                                # CONFIRMED
            # Stores "Operation" in effect "Modify attribute and Modify resource (by var..)" (Possible bug) # #########
            Retriever("Operation 2?", DataType("s32")),                                                     # CONFIRMED
            # Stores "Target Object list ID" in effect "Create garrisoned/Replace Object" (Possible bug)    # #########
            Retriever("Operation", DataType("s32")),                                                        # CONFIRMED
            Retriever("Target Object list ID", DataType("s32")),                                            # CONFIRMED
            Retriever("Button location (for researches)", DataType("s32")),                                 # CONFIRMED
            Retriever("AI Signal Value", DataType("s32")),                                                  # CONFIRMED
            Retriever("Object attributes", DataType("s32")),                                                # CONFIRMED
            Retriever("From Variable", DataType("s32")),                                                    # CONFIRMED
            Retriever("Variable/Timer", DataType("s32")),                                                   # CONFIRMED
            Retriever("Clear timer", DataType("s32")),                                                      # CONFIRMED
            Retriever("Facet", DataType("s32")),                                                            # CONFIRMED
            Retriever("Play Sound", DataType("s32")),                                                       # CONFIRMED
            # Stores "Message" in effect "Display Instructions" (Possible bug)                              # #########
            Retriever("Message", DataType("str32")),                                                        # CONFIRMED
            # Stores "Sound (event) name" in effect "Play sound & Send chat" (Possible bug)                 # #########
            Retriever("CivName/Message/Variable", DataType("str32")),                                       # CONFIRMED
            # Stores "Sound (event) name" in effect "Display Instructions" (Possible bug)                   # #########
            Retriever("Selected Object(s) ID", DataType("s32"), set_repeat="{number_of_units_selected}"),   # CONFIRMED
        ]

        super().__init__(parser_obj, "Effect", retrievers, data)