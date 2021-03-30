from typing import List

from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper.exceptions import InvalidScenarioStructureError


class DependencyTarget:
    def __init__(self, targets: List[List[str]]):
        """
        Object for targeting a specific retriever based on it's section name (or 'self') and the retriever name.

        Args:
            targets: a list of lists referencing a target according to: "('self' or {section}):{attribute_path}"
        """
        self.targets = targets

    @classmethod
    def instance_or_none(cls, target):
        if target is None:
            return None

        if type(target) is str:
            return cls([target.split(":")])
        elif type(target) is list:
            return cls([entry.split(':') for entry in target])
        else:
            raise InvalidScenarioStructureError(
                "Target defined using unknown type. For single targets, use str else list"
            )

    def __repr__(self) -> str:
        return f"[DependencyTarget] {helper.add_tabs(helper.pretty_print_list(self.targets).strip(), 1)}"
