from enum import Enum


class OtherInfo(Enum):
    # SUGGEST: place the properties together for more convenient management.
    @property
    def ID(self):
        return self.value[0]

    @classmethod
    def from_id(cls, value: int):
        if type(value) is not int:
            raise TypeError(f"from_id expected int, got {type(value)}")
        if value == -1:
            raise ValueError("-1 is not a valid id value")
        for x in cls._member_map_.values():
            if x.value[0] == value:
                return x
        raise ValueError(f"{value} is not a valid id value")

    @property
    def ICON_ID(self):
        return self.value[1]

    @classmethod
    def from_icon_id(cls, value: int):
        # NOTE: Only return the first unit(member) of units who have the same icon id.
        if type(value) is not int:
            raise TypeError(f"from_icon_id expected int, got {type(value)}")
        if value == -1:
            raise ValueError("-1 is not a valid icon_id value")
        for x in cls._member_map_.values():
            if x.value[1] == value:
                return x
        raise ValueError(f"{value} is not a valid icon_id value")

    @property
    def DEAD_ID(self):
        return self.value[2]

    @classmethod
    def from_dead_id(cls, value: int):
        # NOTE: Only return the first unit(member) of units who have the same dead id.
        if type(value) is not int:
            raise TypeError(f"from_dead_id expected int, got {type(value)}")
        if value == -1:
            raise ValueError("-1 is not a valid dead_id value")
        for x in cls._member_map_.values():
            if x.value[2] == value:
                return x
        raise ValueError(f"{value} is not a valid dead_id value")

    @property
    def IS_GAIA_ONLY(self):
        return self.value[3]

    @staticmethod
    def gaia_only():
        result = []
        for x in OtherInfo:
            if x.IS_GAIA_ONLY:
                result.append(x)
        return result

    @staticmethod
    def non_gaia():
        result = []
        for x in OtherInfo:
            if not x.IS_GAIA_ONLY:
                result.append(x)
        return result

    FLARE = 274, -1, -1, False
