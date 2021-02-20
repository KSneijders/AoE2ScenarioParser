import math
from typing import List

from AoE2ScenarioParser.sections.dependencies.dependency_action import DependencyAction
from AoE2ScenarioParser.sections.retrievers.retriever import Retriever
from AoE2ScenarioParser.sections.retrievers.retriever import get_retriever_by_name


def refresh_targets(retriever_event, self_list, sections):
    for target in retriever_event.dependency_target.targets:
        retriever_list = select_retriever_list(target, self_list, sections)
        selected_retriever = get_retriever_by_name(retriever_list, target[1])
        execute_refresh_action(selected_retriever, retriever_list, sections)


def execute_refresh_action(retriever, self_list, sections):
    handle_retriever_dependency(retriever, "refresh", self_list, sections)


def handle_retriever_dependency(retriever: Retriever, state, self_list: List[Retriever], sections):
    on_x = f'on_{state}'
    if not hasattr(retriever, on_x):
        return
    retriever_event = getattr(retriever, on_x)  # construct, commit or refresh

    # Todo: Action could be list (Catch exception?), check if list in catch - throw again if not
    action = retriever_event.dependency_action

    if action == DependencyAction.REFRESH_SELF:
        execute_refresh_action(retriever, self_list, sections)
    elif action == DependencyAction.REFRESH:
        refresh_targets(retriever_event, self_list, sections)
    elif action in [DependencyAction.SET_VALUE, DependencyAction.SET_REPEAT]:
        value = execute_dependency_eval(retriever_event, self_list, sections)
        if action == DependencyAction.SET_VALUE:
            retriever.data = value
        elif action == DependencyAction.SET_REPEAT:
            retriever.datatype.repeat = value


def execute_dependency_eval(retriever_event, self_list, sections):
    eval_code = retriever_event.dependency_eval.eval_code
    eval_locals = retriever_event.dependency_eval.eval_locals
    targets = retriever_event.dependency_target.targets

    values = []
    for target in targets:
        retriever_list = select_retriever_list(target, self_list, sections)
        values.append(get_retriever_by_name(retriever_list, target[1]).data)

    for index, target in enumerate(targets):
        eval_locals[target[1]] = values[index]
    eval_locals['math'] = math

    return eval(eval_code, {}, eval_locals)


def select_retriever_list(target, retrievers, sections):
    if target[0] == "self":
        return retrievers
    else:
        return sections[target[0]].retrievers
