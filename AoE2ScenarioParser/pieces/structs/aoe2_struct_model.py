from __future__ import annotations

from typing import List, Dict

from AoE2ScenarioParser.helper.retriever import Retriever


class AoE2StructModel:
    def __init__(self, name: str, retrievers: List[Retriever], structs: Dict[AoE2StructModel]):
        self.name = name
        self.retrievers = retrievers
        self.structs = structs

    @classmethod
    def from_structure(cls, name, structure) -> AoE2StructModel:
        retrievers = []
        for retriever_name, attr in structure.get('retrievers', {}).items():
            retrievers.append(Retriever.from_structure(retriever_name, attr))
        structs = model_dict_from_structure(structure)

        return cls(name, retrievers, structs)


def model_dict_from_structure(structure) -> Dict[AoE2StructModel]:
    models = {}
    for name, attr in structure.get('structs', {}).items():
        # Create struct model
        models[name] = AoE2StructModel.from_structure(name, attr)
    return models
