import math
from typing import List, TYPE_CHECKING
from uuid import UUID

from AoE2ScenarioParser.scenarios.scenario_store import getters
from AoE2ScenarioParser.sections.dependencies.dependency_action import DependencyAction

if TYPE_CHECKING:
    from AoE2ScenarioParser.sections.retrievers.retriever import Retriever
    from AoE2ScenarioParser.sections.dependencies.retriever_dependency import RetrieverDependency
    from AoE2ScenarioParser.sections.aoe2_file_section import AoE2FileSection


def refresh_targets(retriever_event: 'RetrieverDependency', section: 'AoE2FileSection', uuid: UUID) -> None:
    """
    Calls the execute_refresh_action on every target in the target list of the given retriever

    Args:
        retriever_event: The RetrieverDependency object that contains the target retrievers for the dependency action
        section: The AoE2FileSection object containing the given retriever
        uuid: The universally unique identifier for the scenario containing this file section
    """
    for target in retriever_event.dependency_target.targets:
        selected_retriever = select_retriever(target, section, uuid)
        execute_refresh_action(selected_retriever, section, uuid)


def execute_refresh_action(retriever: 'Retriever', section: 'AoE2FileSection', uuid: UUID) -> None:
    """
    Calls handle_retriever_dependency with the same retriever section and host, but changes the state to refresh.

    Args:
        retriever: The retriever to refresh
        section: The AoE2FileSection object containing the given retriever
        uuid: The universally unique identifier for the scenario containing this file section
    """
    handle_retriever_dependency(retriever, "refresh", section, uuid)


def handle_retriever_dependency(
        retriever: 'Retriever',
        state: str,
        section: 'AoE2FileSection',
        uuid: UUID
) -> None:
    """
    Checks if the given retriever has a dependency action for the specified state. If it does, then that action is
    carried out in this function.

    Args:
        retriever: The retriever to check the dependency for
        state: The state for which the dependency needs to be checked
        section: The AoE2FileSection object containing the given retriever
        uuid: The universally unique identifier for the scenario containing this file section
    """
    on_x = f'on_{state}'
    if not hasattr(retriever, on_x):
        return

    retriever_event = getattr(retriever, on_x)  # construct, push or refresh

    action = retriever_event.dependency_action

    if action == DependencyAction.REFRESH_SELF:
        execute_refresh_action(retriever, section, uuid)
    elif action == DependencyAction.REFRESH:
        refresh_targets(retriever_event, section, uuid)
    elif action in [DependencyAction.SET_VALUE, DependencyAction.SET_REPEAT]:
        value = execute_dependency_eval(retriever_event, section, uuid)
        if action == DependencyAction.SET_VALUE:
            retriever.set_data(value, affect_dirty=False)
        elif action == DependencyAction.SET_REPEAT:
            retriever.datatype.repeat = value


def execute_dependency_eval(retriever_event: 'RetrieverDependency', section: 'AoE2FileSection', uuid: UUID) -> int:
    """
    Runs the python code specified in a retriever dependency eval

    Args:
        retriever_event: The RetrieverDependency object that contains the eval
        section: The AoE2FileSection object containing the given retriever
        uuid: The universally unique identifier for the scenario containing this file section

    Returns:
        The result of the eval code in the given retriever dependency object
    """
    eval_code = retriever_event.dependency_eval.eval_code
    eval_locals = retriever_event.dependency_eval.eval_locals
    targets = retriever_event.dependency_target.targets

    values = []
    for target in targets:
        values.append(select_retriever(target, section, uuid).data)

    for index, target in enumerate(targets):
        eval_locals[target[1]] = values[index]
    eval_locals['math'] = math

    return eval(eval_code, {}, eval_locals)


def select_retriever(target: List[str], section: 'AoE2FileSection', uuid: UUID) -> 'Retriever':
    """
    Returns the retriever being targeted by a dependency action

    Args:
        target: A list containing the section and the name of the retriever
        section: The AoE2FileSection object containing the given retriever
        uuid: The universally unique identifier of the scenario containing the given file section

    Returns:
        The given retriever of the specified section (first element of target)
    """
    if target[0] == "self":
        return section.retriever_map[target[1]]
    else:
        sections = getters.get_sections(uuid)
        return sections[target[0]].retriever_map[target[1]]
