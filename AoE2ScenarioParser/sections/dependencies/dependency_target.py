from __future__ import annotations

from typing import List, Union

from AoE2ScenarioParser.exceptions.asp_exceptions import InvalidScenarioStructureError
from AoE2ScenarioParser.helper.pretty_format import pretty_format_list
from AoE2ScenarioParser.helper.string_manipulations import add_tabs


class DependencyTarget:
    """
    Provides the objects for targeting a specific retriever based on it's section name (or 'self') and the retriever
    name.
    """

    def __init__(self, targets: List[List[str]]):
        """
        Args:
            targets: a list of lists which specify the targets of the dependency. Each sublist consists of two elements,
                the first element is the name of the section in which the target retriever lives and the second element
                is the name of the retriever within that section
        """
        self.targets = targets

    @classmethod
    def instance_or_none(cls, target: Union[str, List[str]]) -> DependencyTarget | None:
        """
        Takes in a string or a list of strings indicating the target retriever(s)

        Args:
            target: a string or list of strings representing the target retriever(s). Each string is in the format
                'SectionName:RetrieverName'.

        Returns:
            A DependencyTarget instance

        Raises:
            InvalidScenarioStructureError: if the parameter 'target' is set to anything other than a string or a list
                of strings
        """
        if target is None:
            return None

        if type(target) is str:
            return cls([target.split(":")])
        elif type(target) is list:
            return cls([entry.split(':') for entry in target])
        else:
            raise InvalidScenarioStructureError("Target defined using unknown type. "
                                                "For single targets use a string, else use a list of strings")

    def __repr__(self) -> str:
        return f"[DependencyTarget] {add_tabs(pretty_format_list(self.targets).strip(), 1)}"
