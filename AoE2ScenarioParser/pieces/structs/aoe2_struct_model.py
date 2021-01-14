from typing import List

from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever


class AoE2StructModel:
    def __init__(self, name: str, retrievers: List[Retriever]):
        self.name = name
        self.retrievers = retrievers

    @classmethod
    def from_structure(cls, name, structure):
        retrievers = []
        for name, attr in structure.get('retrievers', {}).items():
            datatype = DataType(var=attr.get('type'), repeat=attr.get('repeat', 1))
            retrievers.append(Retriever(
                name=name,
                datatype=datatype
            ))
        return cls(name, retrievers)
