import abc
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from AoE2ScenarioParser.sections import Condition, Effect

    TriggerArtifacts = Effect | Condition


class CanBeReferencedByTriggerArtifacts(abc.ABC):

    @abc.abstractmethod
    def _get_trigger_artifact_references(self) -> tuple['TriggerArtifacts', ...]:
        raise Exception("Not implemented")

    @abc.abstractmethod
    def _remove_trigger_artifact_reference(self, trigger_artifact: 'TriggerArtifacts') -> None:
        raise Exception("Not implemented")

    @abc.abstractmethod
    def _add_trigger_artifact_reference(self, trigger_artifact: 'TriggerArtifacts') -> None:
        raise Exception("Not implemented")
