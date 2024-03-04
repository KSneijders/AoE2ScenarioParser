from __future__ import annotations

from typing import Dict

from AoE2ScenarioParser.helper.pretty_format import pretty_format_dict
from AoE2ScenarioParser.sections.retrievers.retriever import Retriever


class AoE2StructModel:
    """
    Multiple retrievers containing related data are grouped together in scenario files under structs. This class is used
    to recursively build all retrievers and sub-structures inside a structure.

    Note that this class is just a model that represents each possible structure in a scenario file, hence it does NOT
    actually contain any data. Rather it acts as a "mold" to copy from and create multiple of structures that are
    repeated many times in a scenario. Thus, these struct models are actually always the same for a given version of a
    scenario. The actual data is held in file sections which are unique to each scenario file read.
    """
    def __init__(self, name: str, retriever_map: Dict[str, Retriever], structs: Dict[str, AoE2StructModel]):
        """
        Args:
            name: The name of the structure being built
            retriever_map: A dict of retrievers that constitute this structure
            structs: A dict of sub-structures inside this structure
        """
        self.name = name
        self.retriever_map = retriever_map
        self.structs = structs

    @classmethod
    def from_structure(cls, name: str, structure: Dict[str, Dict]) -> AoE2StructModel:
        """
        Recursively constructs all retrievers and sub-structures inside a given structure from its dictionary
        representation.

        Args:
            name (str): The name of the structure being constructed
            structure (Dict[str, Dict]): A dictionary representation of the structure containing the information about
            substructures and retrievers

        Returns:
            An AoE2StructModel instance representing the given structure
        """
        retriever_map = {}
        log_all_retrievers = structure.get('log', False)
        for retriever_name, attr in structure.get('retrievers').items():
            if log_all_retrievers:
                attr['log'] = True
            retriever_map[retriever_name] = Retriever.from_structure(retriever_name, attr)
        structs = model_dict_from_structure(structure)

        return cls(name, retriever_map, structs)

    def __str__(self):
        return f"[AoE2StructModel] {self.name} -> retrievers: " + pretty_format_dict(self.retriever_map)


def model_dict_from_structure(structure: Dict[str, Dict]) -> Dict[str, AoE2StructModel]:
    """
    Constructs all the structures in a given file section

    Args:
        structure: The dictionary representation of the file section

    Returns:
        A dictionary containing all the structures (AoE2StructModel objects) as key value pairs
    """
    models = {}
    for name, attr in structure.get('structs', {}).items():
        # Create struct model
        models[name] = AoE2StructModel.from_structure(name, attr)
    return models
