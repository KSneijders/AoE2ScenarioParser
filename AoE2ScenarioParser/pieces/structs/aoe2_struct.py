import copy
from typing import List

from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.aoe2_file_part import AoE2FilePart


class AoE2Struct(AoE2FilePart):

    def __init__(self, name, retrievers):
        super().__init__(name, retrievers)

    def _entry_to_string(self, name, data, datatype):
        return "\t\t" + super()._entry_to_string(name, data, datatype)

    def get_header_string(self):
        return "############ " + self.name + " ############  [STRUCT]"

    def __str__(self):
        """ Remove Terrain and EyeCandy Units from the __str__ representation. As it'd mostly be considered spam. """
        if self.name in ["asd"]:  # Terrain
            return "."  # Recommended to keep as '.' due to the amount of tiles in a map (Tiny map = 14400) or units.
        elif self.name in ["Unit"]:
            if self.retrievers[4].data == 1358:  # Eye Candy (eg. Fake plants)
                return "."
        return super().__str__()


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

    def clone_as_struct(self):
        return AoE2Struct(
            self.name,
            copy.deepcopy(self.retrievers)
        )
