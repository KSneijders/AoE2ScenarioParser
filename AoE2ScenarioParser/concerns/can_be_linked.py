import abc

from bfp_rs import BaseStruct

from AoE2ScenarioParser.exceptions.asp_exceptions import ObjectAlreadyLinkedError


class CanBeLinked(abc.ABC):

    _struct: BaseStruct | None = None

    def _is_linked(self) -> bool:
        return self._struct is not None

    def _is_unlinked(self) -> bool:
        return not self._is_linked()

    def _is_linked_to_same(self, other: 'CanBeLinked') -> bool:
        return self._struct is other._struct

    def _is_not_linked_to_same(self, other: 'CanBeLinked') -> bool:
        return not self._is_linked_to_same(other)

    def _validate_linkable_can_be_linked(self, other: 'CanBeLinked') -> None:
        """
        Validates if an object can be linked to this scenario.

        Args:
            other: The object to validate
        """
        # noinspection PyProtectedMember
        if other._is_linked():
            raise ObjectAlreadyLinkedError('Unable to add object that has already been linked to a scenario. Use an import function instead.')
