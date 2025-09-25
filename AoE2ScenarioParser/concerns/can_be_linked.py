import abc

from bfp_rs import BaseStruct


class CanBeLinked(abc.ABC):

    _struct: BaseStruct | None = None

    def _is_linked(self) -> bool:
        return self._struct is not None
