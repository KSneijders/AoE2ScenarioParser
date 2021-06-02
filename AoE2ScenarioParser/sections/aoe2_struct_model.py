from __future__ import annotations

from typing import Dict

from AoE2ScenarioParser.helper.pretty_format import pretty_format_dict
from AoE2ScenarioParser.sections.retrievers.retriever import Retriever


class AoE2StructModel:
    def __init__(self, name: str, retriever_map: Dict[str, Retriever], structs: Dict[AoE2StructModel]):
        self.name = name
        self.retriever_map = retriever_map
        self.structs = structs

    @classmethod
    def from_structure(cls, name, structure) -> AoE2StructModel:
        retriever_map = {}
        for retriever_name, attr in structure.get('retrievers').items():
            retriever_map[retriever_name] = Retriever.from_structure(retriever_name, attr)
        structs = model_dict_from_structure(structure)

        return cls(name, retriever_map, structs)

    def __str__(self):
        return f"[AoE2StructModel] {self.name} -> retrievers: " + pretty_format_dict(self.retriever_map)


def model_dict_from_structure(structure) -> Dict[AoE2StructModel]:
    models = {}
    for name, attr in structure.get('structs', {}).items():
        # Create struct model
        models[name] = AoE2StructModel.from_structure(name, attr)
    return models
