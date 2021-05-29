from enum import Enum
from typing import List


class InfoDatasetBase(Enum):
    @staticmethod
    def _id_map():
        return {'id': 0, 'icon_id': 1, 'dead_id': 2, 'hotkey_id': 3, 'gaia_only': 4}

    def _get_property(self, name):
        return self.value[self._id_map()[name]]

    @property
    def ID(self):
        return self._get_property('id')

    @property
    def ICON_ID(self):
        return self._get_property('icon_id')

    @property
    def DEAD_ID(self):
        return self._get_property('dead_id')

    @property
    def HOTKEY_ID(self):
        return self._get_property('hotkey_id')

    @property
    def IS_GAIA_ONLY(self):
        return self._get_property('gaia_only')

    @classmethod
    def _from_id(cls, id_type, value):
        index = cls._id_map()[id_type]
        if type(value) is not int:
            raise TypeError(f"from_id expected int, got {type(value)}")
        if value == -1:
            raise ValueError("-1 is not a valid id value")
        for member in cls._member_map_.values():
            if member.value[index] == value:
                return member
        return None

    @classmethod
    def from_id(cls, value: int):
        return cls._from_id('id', value)

    @classmethod
    def from_icon_id(cls, value: int):
        return cls._from_id('icon_id', value)

    @classmethod
    def from_dead_id(cls, value: int):
        return cls._from_id('dead_id', value)

    @classmethod
    def gaia_only(cls) -> List:
        return cls._gaia_filter(gaia_only=True)

    @classmethod
    def non_gaia(cls) -> List:
        return cls._gaia_filter(gaia_only=False)

    @classmethod
    def _gaia_filter(cls, gaia_only: bool) -> List:
        result = []
        for x in cls:
            if x.IS_GAIA_ONLY == gaia_only:
                result.append(x)
        return result
