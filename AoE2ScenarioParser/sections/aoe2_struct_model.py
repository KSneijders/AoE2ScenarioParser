from __future__ import annotations

from typing import List, Dict

from AoE2ScenarioParser.helper.pretty_format import pretty_format_list
from AoE2ScenarioParser.sections.retrievers.retriever import Retriever


class AoE2StructModel:
    def __init__(self, name: str, retrievers: List[Retriever], structs: Dict[AoE2StructModel]):
        self.name = name
        self.retrievers = retrievers
        self.structs = structs

    @classmethod
    def from_structure(cls, name, structure) -> AoE2StructModel:
        retrievers = []
        for retriever_name, attr in structure.get('retrievers').items():
            retrievers.append(Retriever.from_structure(retriever_name, attr))
        structs = model_dict_from_structure(structure)

        return cls(name, retrievers, structs)

    def __str__(self):
        return_string = f"[AoE2StructModel] {self.name} -> retrievers: " + pretty_format_list(self.retrievers)
        return return_string


def model_dict_from_structure(structure) -> Dict[AoE2StructModel]:
    models = {}
    for name, attr in structure.get('structs', {}).items():
        # Create struct model
        models[name] = AoE2StructModel.from_structure(name, attr)
    return models
