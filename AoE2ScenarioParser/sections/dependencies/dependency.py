import math
from typing import List, TYPE_CHECKING
from uuid import UUID

from AoE2ScenarioParser.scenarios.scenario_store import getters

if TYPE_CHECKING:
    from AoE2ScenarioParser.sections.retrievers.retriever import Retriever
    from AoE2ScenarioParser.sections.dependencies.retriever_dependency import RetrieverDependency
    from AoE2ScenarioParser.sections.aoe2_file_section import AoE2FileSection
    from AoE2ScenarioParser.sections.dependencies.dependency_action import DependencyAction


def refresh_targets(retriever_event: 'RetrieverDependency', section: 'AoE2FileSection', host_uuid: UUID) -> None:
    """
    This function calls the execute_refresh_action on every target in the target list of the given retriever

    Args:
        retriever_event (RetrieverDependency): The RetrieverDependency object that contains the target retrievers for
            the dependency action
        section (AoE2FileSection): The AoE2FileSection object containing the given retriever
        host_uuid (UUID): The universally unique identifier for the scenario containing this file section
    """
    for target in retriever_event.dependency_target.targets:
        selected_retriever = select_retriever(target, section, host_uuid)
        # selected_retriever = get_retriever_by_name(retriever_list, target[1])
        # selected_retriever = section.retriever_map[target[1]]
        execute_refresh_action(selected_retriever, section, host_uuid)


def execute_refresh_action(retriever: 'Retriever', section: 'AoE2FileSection', host_uuid: UUID) -> None:
    """
    This function just calls handle_retriever_dependency with the same retriever section and host, but changes the state
    to refresh.

    Args:
        retriever (Retriever): The retriever to refresh
        section (AoE2FileSection): The AoE2FileSection object containing the given retriever
        host_uuid (UUID): The universally unique identifier for the scenario containing this file section
    """
    handle_retriever_dependency(retriever, "refresh", section, host_uuid)


def handle_retriever_dependency(retriever: 'Retriever', state: str, section: 'AoE2FileSection', host_uuid: UUID) \
        -> None:
    """
    This function checks if the given retriever has a dependency action for the specified state. If it does, then that
    action is carried out in this function.

    Args:
        retriever (Retriever): The retriever to check the dependency for
        state (str): The state for which the dependency needs to be checked
        section (AoE2FileSection): The AoE2FileSection object containing the given retriever
        host_uuid (UUID): The universally unique identifier for the scenario containing this file section
    """
    on_x = f'on_{state}'
    if not hasattr(retriever, on_x):
        return

    retriever_event = getattr(retriever, on_x)  # construct, commit or refresh

    action = retriever_event.dependency_action

    if action == DependencyAction.REFRESH_SELF:
        execute_refresh_action(retriever, section, host_uuid)
    elif action == DependencyAction.REFRESH:
        refresh_targets(retriever_event, section, host_uuid)
    elif action in [DependencyAction.SET_VALUE, DependencyAction.SET_REPEAT]:
        value = execute_dependency_eval(retriever_event, section, host_uuid)
        if action == DependencyAction.SET_VALUE:
            retriever.data = value
        elif action == DependencyAction.SET_REPEAT:
            retriever.datatype.repeat = value


def execute_dependency_eval(retriever_event: 'RetrieverDependency', section: 'AoE2FileSection', host_uuid: UUID) -> int:
    """
    This function runs the python code specified in a retriever dependency eval

    Args:
        retriever_event (RetrieverDependency): The RetrieverDependency object that contains the eval
        section (AoE2FileSection): The AoE2FileSection object containing the given retriever
        host_uuid (UUID): The universally unique identifier for the scenario containing this file section

    Returns:
        This function returns the result of the eval code in the given retriever dependency object
    """
    eval_code = retriever_event.dependency_eval.eval_code
    eval_locals = retriever_event.dependency_eval.eval_locals
    targets = retriever_event.dependency_target.targets

    values = []
    for target in targets:
        # retriever_list = select_retriever_list(target, self_list, sections)
        # values.append(get_retriever_by_name(retriever_list, target[1]).data)
        values.append(select_retriever(target, section, host_uuid).data)

    for index, target in enumerate(targets):
        eval_locals[target[1]] = values[index]
    eval_locals['math'] = math

    return eval(eval_code, {}, eval_locals)


def select_retriever(target: List[str], section: 'AoE2FileSection', host_uuid: UUID) -> 'Retriever':
    """
    This function returns the retriever being targeted by a dependency action
    Args:
        target: A list containing the section and the name of the retriever
        section:
        host_uuid: The universally unique identifier of the scenario containing the given file section

    Returns:
        returns the given retriever of the specified section (first element of target)
    """
    if target[0] == "self":
        return section.retriever_map[target[1]]
    else:
        sections = getters.get_sections(host_uuid)
        return sections[target[0]].retriever_map[target[1]]
