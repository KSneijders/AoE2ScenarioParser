import abc

from bfp_rs import BaseStruct


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
