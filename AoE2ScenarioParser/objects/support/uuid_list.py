from __future__ import annotations

from copy import deepcopy
from typing import Iterable, Sequence, TypeVar, List, Generic, Iterator, overload
from uuid import UUID

from typing_extensions import SupportsIndex

_T = TypeVar('_T')

NO_UUID = "<<NO_UUID>>"


class UuidList(list, Generic[_T]):
    def __init__(
            self,
            uuid: UUID,
            seq: Sequence[_T] = (),
            on_update_execute_entry=None,
            on_update_execute_list=None
    ) -> None:
        """
        Args:
            uuid: The UUID for the list
            seq: The starting sequence within this list
            on_update_execute_entry: The callback executed for each entry that is updated (added)
            on_update_execute_list: The callback executed on the entire list when a new entry is added
        """
        self._uuid = uuid
        self.on_update_execute_entry = on_update_execute_entry
        self.on_update_execute_list = on_update_execute_list

        if not isinstance(seq, Iterable):
            raise ValueError(f"Sequence object should be iterable. Got: {seq}")

        if seq:
            # Deepcopy the given list if the object's UUID isn't equal to the given UUID
            # Meaning the objects came from another scenario. Can cause reference issues!
            if hasattr(seq[0], '_uuid') and seq[0]._uuid != uuid and seq[0]._uuid != NO_UUID:
                seq = deepcopy(seq)

            seq = self._iter_to_uuid_list(seq, ignore_root_iter=True)
            self._update(seq)

        super().__init__(seq)

    def __iter__(self) -> Iterator[_T]:
        return super().__iter__()

    def __deepcopy__(self, memo):
        deepcopied_content = [deepcopy(e) for e in self]
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, getattr(self, k))
        result[:] = deepcopied_content
        return result

    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        self._uuid = value
        self._update(self)

    def append(self, __object: _T) -> None:
        """Append object to the end of the list."""
        __object = self._iter_to_uuid_list(__object)
        super().append(__object)
        self._update(__object)

    def extend(self, __iterable: Iterable[_T]) -> None:
        """Extend list by appending elements from the iterable."""
        __iterable = self._iter_to_uuid_list(__iterable, ignore_root_iter=True)
        super().extend(__iterable)
        self._update(__iterable)

    def insert(self, __index: int, __object: _T) -> None:
        """Insert object before index"""
        __object = self._iter_to_uuid_list(__object)
        super().insert(__index, __object)
        self._update(__object)

    def pop(self, __index: int = ...) -> _T:
        popped = super().pop(__index)
        self._callback(is_last_update=True)
        return popped

    def remove(self, __value: _T) -> None:
        super().remove(__value)
        self._callback(is_last_update=True)

    def reverse(self) -> None:
        super().reverse()
        self._callback(is_last_update=True)

    def sort(self: List, *, key: None = ..., reverse: bool = ...) -> None:
        super().sort(key=key, reverse=reverse)

    @overload
    def __getitem__(self, __i: SupportsIndex) -> _T: ...

    @overload
    def __getitem__(self, __s: slice) -> list[_T]: ...

    def __getitem__(self, __i):
        """Only overwritten because Python Generics are... 'Interesting'"""
        return super().__getitem__(__i)

    def __setitem__(self, i: SupportsIndex, o: _T | Iterable[_T]) -> None:
        """
        Set self[key] to value or set self[i:j] to slice.

        Args:
            i: The index or slice object
            o: The object to set or iterable with objects when slicing is used
        """
        o = self._iter_to_uuid_list(o, ignore_root_iter=isinstance(i, slice))
        super().__setitem__(i, o)
        self._update(o)

    def _iter_to_uuid_list(self, iterable: _T | Iterable[_T], ignore_root_iter=False) -> _T | Iterable[_T]:
        if ignore_root_iter:
            return list(map(self._iter_to_uuid_list, iterable))

        if not issubclass(iterable.__class__, Iterable):
            return iterable
        return UuidList(
            uuid=self.uuid,
            seq=iterable
        )

    def _update(self, o: _T | Iterable[_T]):
        """Checks if `o` is an iterable and calls function on each entry or on `o` if it's not an iterable"""
        if issubclass(o.__class__, Iterable):
            for element in o:
                if isinstance(element, UuidList):
                    element.uuid = self.uuid
                    continue
                self._update_object(element)
            self._callback(is_last_update=True)
        else:
            self._update_object(o, is_last_update=True)

    def _update_object(self, o: _T, is_last_update: bool = False):
        """
        Update the UUID of the object

        Args:
            o: an object to update
            is_last_update: If this entry is the last in a list
        """
        o._uuid = self.uuid
        self._callback(o, is_last_update)

    def _callback(self, o: _T = None, is_last_update: bool = False) -> None:
        """
        Executes given callbacks on `o` if given. If not given, execute list callback on entire list.

        Args:
            o: an object to call a callback on
            is_last_update: If this entry is the last in a list
        """
        if o is not None:
            if self.on_update_execute_entry is not None:
                self.on_update_execute_entry(o)
        if self.on_update_execute_list is not None and is_last_update:
            self.on_update_execute_list(self)
