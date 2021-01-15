from typing import Dict

from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.retriever_dependency import RetrieverDependency, DependencyTarget, DependencyAction, \
    DependencyEval
from AoE2ScenarioParser.pieces.aoe2_file_part import AoE2FilePart


def _fill_dependencies(dependencies):
    for disabled_type in ["tech", "building", "unit"]:
        dependencies[f"per_player_number_of_disabled_{disabled_type}s"] = {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_VALUE,
                DependencyTarget(["self"] * 8,
                                 [f"disabled_{disabled_type}_ids_player_{p}" for p in range(1, 9)]),
                DependencyEval("[len(x) for x in [p1, p2, p3, p4, p5, p6, p7, p8]]",
                               values_as_variable=['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8'])
            )
        }
        for player in range(1, 9):
            dependencies[f"disabled_{disabled_type}_ids_player_{player}"] = {
                "on_refresh": RetrieverDependency(
                    DependencyAction.SET_REPEAT,
                    DependencyTarget("self", f"per_player_number_of_disabled_{disabled_type}s"),
                    DependencyEval(f"x[{player - 1}]")),
                "on_construct": RetrieverDependency(DependencyAction.REFRESH_SELF),
                "on_commit": RetrieverDependency(
                    DependencyAction.REFRESH,
                    DependencyTarget("self", f"per_player_number_of_disabled_{disabled_type}s")
                ) if player == 1 else None
            }


class OptionsPiece(AoE2FilePart):
    dependencies: Dict[str, Dict[str, RetrieverDependency]] = {
        'number_of_triggers': {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_VALUE, DependencyTarget("TriggersPiece", "trigger_data"),
                DependencyEval("len(x)")
            )
        }
    }
    _fill_dependencies(dependencies)

    def __init__(self):
        retrievers = []
        for disabled_type in ["tech", "building", "unit"]:
            retrievers.append(Retriever(f"per_player_number_of_disabled_{disabled_type}s", DataType("u32", repeat=16)))
            for player in range(1, 9):
                retrievers.append(Retriever(f"disabled_{disabled_type}_ids_player_{player}", DataType("u32")))
                # Unused: Players 9 - 16 can't have {disabled_type} technologies
            retrievers.append(Retriever(f"disabled_{disabled_type}_ids_player9-16", DataType("u32", repeat=0)))

        retrievers += [
            Retriever("combat_mode", DataType("u32")),
            Retriever("naval_mode", DataType("u32")),
            Retriever("all_techs", DataType("u32")),
            Retriever("per_player_starting_age", DataType("u32", repeat=16)),
            # 2: Dark 6 = Post | 1-8 players 9 GAIA
            Retriever("unknown", DataType("32")),
            Retriever("number_of_triggers", DataType("u32")),
        ]
        super().__init__("Options", retrievers)

    @staticmethod
    def defaults(pieces):
        defaults = {}
        for disabled_type in ["tech", "building", "unit"]:
            defaults[f'per_player_number_of_disabled_{disabled_type}s'] = [0] * 16
            for player in range(1, 9):
                defaults[f'disabled_{disabled_type}_ids_player_{player}'] = []
            defaults[f'disabled_{disabled_type}_ids_player9-16'] = []

        defaults = dict(**defaults, **{
            'combat_mode': 0,
            'naval_mode': 0,
            'all_techs': 0,
            'per_player_starting_age': [2] * 16,
            # 'unknown': b'\x9d\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            #            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00',
            # 'unknown': b'\x9d\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            #            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00',
            'unknown': b'\x9d\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                       b'\x00\x00\x00\x00\x00\x00\x00\x00\x00',

            'number_of_triggers': 0,
        })
        return defaults
