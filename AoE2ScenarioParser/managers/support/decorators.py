from __future__ import annotations

from enum import IntEnum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Callable, Type


def no_gaia_property():
    """
    A decorator to create a property that enforces restrictions for GAIA.
    Retrieving the value will return None for GAIA, and setting the value will raise an AttributeError.

    Returns:
        Callable: The wrapped property function with enforced restrictions.
    """
    def wrapper(func: Callable):
        attr_name = f"_{func.__name__}"

        def getter(self):
            if self.index == 0:
                return None
            return func(self)

        def setter(self, value):
            if self.index == 0:
                raise AttributeError(f"GAIA does not support the {func.__name__} attribute")
            setattr(self, attr_name, value)

        return property(getter, setter)

    return wrapper


def dataset_property(dataset: Type[IntEnum]):
    """
    Decorator to create a property that applies the conversion from and to an IntEnum type. Does not enforce that the
    value is present in the dataset. Only when it is present it is converted to and from the dataset.

    Args:
        dataset: The IntEnum type to be associated with the property.

    Returns:
        Callable: The wrapped property function with the dataset transformation.
    """
    def wrapper(func):
        attr_name = f"_{func.__name__}"

        def getter(self):
            val = func(self)
            return dataset(val) if val in dataset else val

        def setter(self, value):
            if isinstance(value, dataset):
                value = value.value
            setattr(self, attr_name, value)

        return property(getter, setter)

    return wrapper
