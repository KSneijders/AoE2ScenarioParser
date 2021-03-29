from enum import Enum


class OtherInfo(Enum):
    @property
    def ID(self):
        return self.value[0]

    @classmethod
    def from_id(cls, value):
        if value == -1:
            raise ValueError("-1 is not a valid id value")
        for x in cls._member_map_.values():
            if x.value[0] == value:
                return x

    @property
    def ICON_ID(self):
        return self.value[1]

    @classmethod
    def from_icon_id(cls, value):
        if value == -1:
            raise ValueError("-1 is not a valid icon_id value")
        for x in cls._member_map_.values():
            if x.value[1] == value:
                return x

    @property
    def DEAD_ID(self):
        return self.value[2]

    @classmethod
    def from_dead_id(cls, value):
        if value == -1:
            raise ValueError("-1 is not a valid dead_id value")
        for x in cls._member_map_.values():
            if x.value[2] == value:
                return x

    @property
    def IS_GAIA_ONLY(self):
        return self.value[3]

    @staticmethod
    def gaia_only():
        result = []
        for x in OtherInfo:
            if x.IS_GAIA:
                result.append(x)
        return result

    @staticmethod
    def non_gaia():
        result = []
        for x in OtherInfo:
            if not x.IS_GAIA:
                result.append(x)
        return result


    FLARE = 274, -1, -1, False
