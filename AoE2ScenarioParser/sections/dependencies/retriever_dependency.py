from __future__ import annotations

from typing import Type

from AoE2ScenarioParser.sections.dependencies.dependency_action import DependencyAction
from AoE2ScenarioParser.sections.dependencies.dependency_eval import DependencyEval
from AoE2ScenarioParser.sections.dependencies.dependency_target import DependencyTarget


class RetrieverDependency:
    """
    Provides for objects used to handle dependencies between retrievers
    """
    def __init__(
            self,
            dependency_action: Type[DependencyAction],
            dependency_target: DependencyTarget | None = None,
            dependency_eval: DependencyEval | None = None
    ):
        """
        Args:
            dependency_action: The type of action taken.
            dependency_target: The target of the action.
            dependency_eval: Eval code to execute for action.

        Raises:
            ValueError: if the parameter 'dependency_target' is None and the 'dependency_action' is anything other than
                REFRESH_SELF
        """
        if dependency_action != DependencyAction.REFRESH_SELF and dependency_target is None:
            raise ValueError(f"Parameter dependency_target cannot be None when action is {dependency_action.name}")

        self.dependency_action = dependency_action
        self.dependency_target = dependency_target

        if dependency_action in [DependencyAction.SET_REPEAT, DependencyAction.SET_VALUE] and dependency_eval is None:
            # Get name of first (and only) target, must define eval if using more than one target
            dependency_eval = DependencyEval(dependency_target.targets[0][1])

        self.dependency_eval = dependency_eval

    @classmethod
    def from_structure(cls, structure: dict) -> RetrieverDependency:
        """
        Creates a RetrieverDependency object from the given dependency structure.

        Args:
            structure: This is a dictionary that contains the action to perform, the target retriever to perform the
                action on and the relevant code to execute

        Returns:
            A RetrieverDependency instance created from the given dependency structure
        """
        return cls(
            dependency_action=DependencyAction[structure.get('action')],
            dependency_target=DependencyTarget.instance_or_none(structure.get('target')),
            dependency_eval=DependencyEval.instance_or_none(structure.get('eval')),
        )

    def __repr__(self):
        repr_string = f"\n[RetrieverDependency] {self.dependency_action}"
        if self.dependency_target:
            repr_string += f"\n\tTarget: {self.dependency_target}"
        if self.dependency_eval:
            repr_string += f"\n\tEval: {self.dependency_eval.eval_code}"
        return repr_string
