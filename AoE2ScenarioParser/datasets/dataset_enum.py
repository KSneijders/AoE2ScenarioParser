from enum import Enum, IntEnum, IntFlag, EnumMeta


class _DataSetMeta(EnumMeta):
    def __contains__(self, other):
        try:
            self(other)
        except ValueError:
            return False
        else:
            return True


class _DataSet(Enum, metaclass=_DataSetMeta):
    def attribute_presentation(self) -> str:
        raise NotImplemented("_DataSet.attribute_presentation has to be implemented")


class _DataSetIntEnums(_DataSet, IntEnum):
    def attribute_presentation(self) -> str:
        """
        Get the string representation of an enum entry. Uses `.name` when not overridden.
        Returns:
            The string representation of an enum entry.
        """
        return super().name


class _DataSetIntFlags(_DataSet, IntFlag):
    def attribute_presentation(self) -> str:
        """
        Get the string representation of an enum entry. Uses `.name` when not overridden.
        Returns:
            The string representation of an enum entry.
        """
        return super().name
