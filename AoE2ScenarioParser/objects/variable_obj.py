from __future__ import annotations

from AoE2ScenarioParser.helper.retriever import find_retriever
from AoE2ScenarioParser.pieces.structs.variable import VariableStruct


class VariableObject():
    def __init__(self,
                 variable_id,
                 name
                 ):
        self.variable_id = variable_id
        self.name = name

    @staticmethod
    def _parse_object(parsed_data, **kwargs) -> VariableObject:
        # Expected {variable=VariableStruct}
        variable = kwargs['variable']

        return VariableObject(
            variable_id=find_retriever(variable.retrievers, "variable_id").data,
            name=find_retriever(variable.retrievers, "name").data
        )

    @staticmethod
    def _reconstruct_object(parsed_header, parsed_data, objects, **kwargs) -> None:
        # Expected {variable=VariableObject, variables=variables_list}
        variable_obj = kwargs['variable']
        variables_list = kwargs['variables']

        variables_list.append(VariableStruct(
            data=[variable_obj.variable_id, variable_obj.name]
        ))
