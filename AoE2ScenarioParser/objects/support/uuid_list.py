from typing import Iterable, Sequence, Callable, Union, TypeVar

from typing_extensions import SupportsIndex

T = TypeVar('T')


class UuidList(list):
    def __init__(self, uuid: str, seq: Sequence[T] = (), callable_: Callable = None, uuid_list_depth=1) -> None:
        self.callable_ = callable_
        self._uuid = uuid
        self.uuid_list_depth = uuid_list_depth

        self._update(seq)
        super().__init__(seq)

    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        self._uuid = value
        self._update(self)

    def append(self, __object: T) -> None:
        """Append object to the end of the list."""
        __object = self._iter_to_uuid_list(__object)
        self._update(__object)
        super().append(__object)

    def extend(self, __iterable: Iterable[T]) -> None:
        """Extend list by appending elements from the iterable."""
        __iterable = self._iter_to_uuid_list(__iterable, normal_top_iter=True)
        self._update(__iterable)
        super().extend(__iterable)

    def insert(self, __index: int, __object: T) -> None:
        """Insert object before index"""
        __object = self._iter_to_uuid_list(__object)
        self._update(__object)
        super().insert(__index, __object)

    def __setitem__(self, i: SupportsIndex, o: Union[T, Iterable[T]]) -> None:
        """
        Set self[key] to value or set self[i:j] to slice.

        Args:
            i: The index
            o: The object to set or iterable with objects when slicing is used
        """
        o = self._iter_to_uuid_list(o, normal_top_iter=True)
        self._update(o)
        super().__setitem__(i, o)

    def _iter_to_uuid_list(self, iterable: Union[T, Iterable[T]], normal_top_iter=False) -> Union[T, Iterable[T]]:
        if normal_top_iter:
            return list(map(self._iter_to_uuid_list, iterable))

        if not issubclass(iterable.__class__, Iterable) or self.uuid_list_depth == 1:
            return iterable
        return UuidList(
            uuid=self.uuid,
            seq=iterable,
            uuid_list_depth=self.uuid_list_depth - 1
        )

    def _update(self, o: Union[T, Iterable[T]]):
        """Checks if `o` is an iterable and calls function on each entry or on `o` if it's not an iterable"""
        if issubclass(o.__class__, Iterable):
            for element in o:
                if isinstance(element, UuidList):
                    element.uuid = self.uuid
                    continue
                self._update_object(element)
        else:
            self._update_object(o)

    def _update_object(self, o: T):
        """
        Update the UUID of the object and call a custom function if the callable has been set

        Args:
            o (T): an object to update
        """
        o._host_uuid = self.uuid
        if self.callable_ is not None:
            self.callable_(o)
