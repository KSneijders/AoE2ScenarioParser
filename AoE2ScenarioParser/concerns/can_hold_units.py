import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from AoE2ScenarioParser.sections import Unit


class CanHoldUnits(abc.ABC):

    @abc.abstractmethod
    def _get_unit_references(self, key: str = '') -> tuple['Unit', ...]:
        raise Exception("Not implemented")

    @abc.abstractmethod
    def _remove_unit_reference(self, unit: 'Unit', key: str = '') -> None:
        raise Exception("Not implemented")

    @abc.abstractmethod
    def _add_unit_reference(self, unit: 'Unit', key: str = '') -> None:
        raise Exception("Not implemented")
