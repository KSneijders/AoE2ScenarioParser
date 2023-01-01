from __future__ import annotations

from enum import Enum, IntEnum, IntFlag, EnumMeta
from typing import Type


class _DataSetMeta(EnumMeta):
    """Meta class for the dataset enums"""
    def __contains__(self, other):
        try:
            self(other)
        except ValueError:
            return False
        else:
            return True


class _DataSet(Enum, metaclass=_DataSetMeta):
    """Enum super class for all datasets to force the mandatory functions for all subclasses."""
    def attribute_presentation(self) -> str:
        """
        Get the string representation of an enum entry. Uses `.name` when not overridden.

        Returns:
            The string representation of an enum entry.
        """
        raise NotImplemented("_DataSet.attribute_presentation has to be implemented")


class _DataSetIntEnums(_DataSet, IntEnum):
    """IntEnum super class for all int based datasets."""
    def attribute_presentation(self) -> str:
        """
        Get the string representation of an enum entry. Uses `.name` when not overridden.

        Returns:
            The string representation of an enum entry.
        """
        return super().name


class _DataSetIntFlags(_DataSet, IntFlag):
    """IntFlag super class for all int flag based datasets."""
    def attribute_presentation(self) -> str:
        """
        Get the string representation of an enum entry. Uses `.name` when not overridden.

        Returns:
            The string representation of an enum entry.
        """
        return super().name


def dataset_or_value(enum: Type[_DataSet], value: int | str) -> _DataSet | int | str:
    """
    Return the value in the enum used to create the enum, or if it failed, returns just the value

    Args:
        enum: The enum to create with the given value
        value: The value to use in the enum

    Returns:
        The enum with the given value if it exists, the value itself otherwise
    """
    try:
        return enum(value)
    except ValueError:
        return value
