from enum import Enum


class UnitsBase(Enum):
    """Base class for all kinds of units, including Unit, Building, Here and Other, and inherited by 4 related subclasses.
    You can manage their shared properties and classmethods here, while informations are stored separately within 4 subclasses.
    """
    # Place the properties together for more convenient management.
    @property
    def ID(self):
        return self.value[0]

    @property
    def ICON_ID(self):
        return self.value[1]

    @property
    def DEAD_ID(self):
        return self.value[2]

    @property
    def IS_GAIA_ONLY(self):
        return self.value[3]

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

    @classmethod
    def gaia_only(cls):
        # EXPLAIN: When being called, subclass(UnitInfo etc.) will be passed as cls.
        #          I'd used @classmethod for subclasses' inheriting.
        # TEST:
        #      from AoE2ScenarioParser.datasets.units import UnitInfo
        #      from AoE2ScenarioParser.datasets.units_base import UnitsBase
        #      if issubclass(UnitInfo, UnitsBase):
        #          u0 = UnitInfo.from_id(0)
        #          ugaia = UnitInfo.gaia_only()
        # It works well~ XD
        result = []
        for x in cls:
            if x.IS_GAIA_ONLY:
                result.append(x)
        return result

    @classmethod
    def non_gaia(cls):
        result = []
        for x in cls:
            if not x.IS_GAIA_ONLY:
                result.append(x)
        return result
