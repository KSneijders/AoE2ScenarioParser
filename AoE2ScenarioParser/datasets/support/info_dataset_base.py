from __future__ import annotations

from enum import Enum
from typing import List


class InfoDatasetBase(Enum):
    """
    This enum class is the base class for the UnitInfo, BuildingInfo, HeroInfo and OtherInfo datasets. It provides the
    properties and functions common to all the mentioned classes

    **Methods**
    
    >>> InfoDatasetBase.from_id()
    >>> InfoDatasetBase.from_dead_id()
    >>> InfoDatasetBase.from_icon_id()
    >>> InfoDatasetBase.from_hotkey_id()
    >>> InfoDatasetBase.gaia_only()
    >>> InfoDatasetBase.non_gaia()
    """

    @staticmethod
    def _id_map() -> dict:
        """
        Returns:
            A dict that maps the names of the properties to their index in the info tuple
        """
        return {'id': 0, 'icon_id': 1, 'dead_id': 2, 'hotkey_id': 3, 'gaia_only': 4}

    def _get_property(self, name: str) -> int | bool:
        """
        Get the specified property by its name from an object of this (or its derived) class

        Args:
            name: the name of the property to get

        Returns:
        """
        return self.value[self._id_map()[name]]

    @property
    def ID(self) -> int:
        """
        Returns:
            The ID of the specified unit
        """
        return self._get_property('id')

    @property
    def ICON_ID(self) -> int:
        """
        Returns:
            The Icon ID of the specified unit
        """
        return self._get_property('icon_id')

    @property
    def DEAD_ID(self) -> int:
        """
        Returns:
            The Dead Unit ID of the specified unit
        """
        return self._get_property('dead_id')

    @property
    def HOTKEY_ID(self) -> int:
        """
        Returns:
            The HotKey ID of the specified unit
        """
        return self._get_property('hotkey_id')

    @property
    def IS_GAIA_ONLY(self) -> bool:
        """
        Returns:
            A boolean value indicating if the specified unit is a gaia only unit (e.g. Deer)
        """
        return self._get_property('gaia_only')

    @classmethod
    def _from_id(cls, id_type: str, value: int) -> InfoDatasetBase:
        """
        Finds and returns the member object that uses the given value for the specified property (id_type)

        Args:
            id_type: the property of member objects that should match the value specified
            value: the value of the property to search for

        Returns:
            An InfoDatasetBase member object which uses the given value for the specified property (id_type
        """
        index = cls._id_map()[id_type]

        if type(value) is not int:
            raise TypeError(f"from_id expected int, got {type(value)}")
        if value < 0:
            raise ValueError(f"{value} is not a valid id value")

        for member in cls._member_map_.values():
            if member.value[index] == value:
                return member

        raise KeyError(f"A unit with {id_type} = {value} was not found in the dataset")

    @classmethod
    def from_id(cls, unit_id: int) -> InfoDatasetBase:
        """
        Finds and returns the unit with the given unit ID

        Args:
            unit_id: the unit ID to search for

        Returns:
            A unit with the given unit I
        """
        return cls._from_id('id', unit_id)

    @classmethod
    def from_icon_id(cls, icon_id: int) -> InfoDatasetBase:
        """
        Finds and returns the unit with the given icon ID

        Args:
            icon_id: the icon ID to search for

        Returns:
            A unit with the given icon ID
        """
        return cls._from_id('icon_id', icon_id)

    @classmethod
    def from_dead_id(cls, dead_id: int) -> InfoDatasetBase:
        """
        Finds and returns the unit with the given dead unit ID

        Args:
            dead_id: the dead unit ID to search for

        Returns:
            A unit with the given dead unit ID
        """
        return cls._from_id('dead_id', dead_id)

    @classmethod
    def from_hotkey_id(cls, hotkey_id: int) -> InfoDatasetBase:
        """
        Finds and returns the unit with the given hotkey ID. Note that there may be multiple units that
        use the same hotkey ID, currently only one is returned!

        Args:
            hotkey_id: the hotkey ID to search for

        Returns:
            A unit with the given hotkey ID
        """
        return cls._from_id('hotkey_id', hotkey_id)

    @classmethod
    def gaia_only(cls) -> List[InfoDatasetBase]:
        """
        Returns:
            A list of all the gaia only units (e.g. Deer)
        """
        return cls._gaia_filter(gaia_only=True)

    @classmethod
    def non_gaia(cls) -> List[InfoDatasetBase]:
        """
        Returns:
            A list of all the units excluding gaia only units (e.g. militia)
        """
        return cls._gaia_filter(gaia_only=False)

    @classmethod
    def _gaia_filter(cls, gaia_only: bool) -> List[InfoDatasetBase]:
        """
        Args:
            gaia_only: if set to true, lists all gaia only units. If set to `False`, lists all units except gaia only units

        Returns:
            A list of either all gaia only units or a list of all units excluding gaia only units
        """
        result = []
        for x in cls:
            if x.IS_GAIA_ONLY == gaia_only:
                result.append(x)
        return result
