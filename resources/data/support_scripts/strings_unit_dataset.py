vils = """
    @staticmethod
    def vils():
        return [
            UnitInfo.VILLAGER_MALE, UnitInfo.VILLAGER_FEMALE, UnitInfo.VILLAGER_MALE_BUILDER,
            UnitInfo.VILLAGER_FEMALE_BUILDER, UnitInfo.VILLAGER_MALE_FARMER, UnitInfo.VILLAGER_FEMALE_FARMER,
            UnitInfo.VILLAGER_MALE_FISHERMAN, UnitInfo.VILLAGER_FEMALE_FISHERMAN, UnitInfo.VILLAGER_MALE_FORAGER,
            UnitInfo.VILLAGER_FEMALE_FORAGER, UnitInfo.VILLAGER_MALE_GOLD_MINER, UnitInfo.VILLAGER_FEMALE_GOLD_MINER,
            UnitInfo.VILLAGER_MALE_HUNTER, UnitInfo.VILLAGER_FEMALE_HUNTER, UnitInfo.VILLAGER_MALE_LUMBERJACK,
            UnitInfo.VILLAGER_FEMALE_LUMBERJACK, UnitInfo.VILLAGER_MALE_REPAIRER, UnitInfo.VILLAGER_FEMALE_REPAIRER,
            UnitInfo.VILLAGER_MALE_SHEPHERD, UnitInfo.VILLAGER_FEMALE_SHEPHERD, UnitInfo.VILLAGER_MALE_STONE_MINER,
            UnitInfo.VILLAGER_FEMALE_STONE_MINER,
        ]\n"""
unique_units = """
    @staticmethod
    def unique_units():
        return [
            UnitInfo.LONGBOWMAN, UnitInfo.MANGUDAI, UnitInfo.TEUTONIC_KNIGHT, UnitInfo.CATAPHRACT, UnitInfo.HUSKARL,
            UnitInfo.JANISSARY, UnitInfo.ROYAL_JANISSARY, UnitInfo.CHU_KO_NU, UnitInfo.CONDOTTIERO_PLACEHOLDER,
            UnitInfo.SLINGER, UnitInfo.WOAD_RAIDER, UnitInfo.WAR_ELEPHANT, UnitInfo.LONGBOAT, UnitInfo.THROWING_AXEMAN,
            UnitInfo.MAMELUKE, UnitInfo.SAMURAI, UnitInfo.ELITE_LONGBOWMAN, UnitInfo.ELITE_THROWING_AXEMAN,
            UnitInfo.ELITE_LONGBOAT, UnitInfo.ELITE_WOAD_RAIDER, UnitInfo.ELITE_CATAPHRACT,
            UnitInfo.ELITE_TEUTONIC_KNIGHT, UnitInfo.ELITE_HUSKARL, UnitInfo.ELITE_MAMELUKE, UnitInfo.ELITE_JANISSARY,
            UnitInfo.ELITE_WAR_ELEPHANT, UnitInfo.ELITE_CHU_KO_NU, UnitInfo.ELITE_SAMURAI, UnitInfo.ELITE_MANGUDAI,
            UnitInfo.BERSERK, UnitInfo.ELITE_BERSERK, UnitInfo.JAGUAR_WARRIOR, UnitInfo.ELITE_JAGUAR_WARRIOR,
            UnitInfo.TARKAN, UnitInfo.ELITE_TARKAN, UnitInfo.HUSKARL_BARRACKS, UnitInfo.ELITE_HUSKARL_BARRACKS,
            UnitInfo.PLUMED_ARCHER, UnitInfo.ELITE_PLUMED_ARCHER, UnitInfo.CONQUISTADOR, UnitInfo.ELITE_CONQUISTADOR,
            UnitInfo.MISSIONARY, UnitInfo.WAR_WAGON, UnitInfo.ELITE_WAR_WAGON, UnitInfo.TURTLE_SHIP,
            UnitInfo.ELITE_TURTLE_SHIP, UnitInfo.GENOESE_CROSSBOWMAN, UnitInfo.ELITE_GENOESE_CROSSBOWMAN,
            UnitInfo.MAGYAR_HUSZAR, UnitInfo.ELITE_MAGYAR_HUSZAR, UnitInfo.ELEPHANT_ARCHER,
            UnitInfo.ELITE_ELEPHANT_ARCHER, UnitInfo.BOYAR, UnitInfo.ELITE_BOYAR, UnitInfo.KAMAYUK,
            UnitInfo.ELITE_KAMAYUK, UnitInfo.CONDOTTIERO, UnitInfo.TARKAN_STABLE, UnitInfo.ELITE_TARKAN_STABLE,
            UnitInfo.ORGAN_GUN, UnitInfo.ELITE_ORGAN_GUN, UnitInfo.CARAVEL, UnitInfo.ELITE_CARAVEL,
            UnitInfo.CAMEL_ARCHER, UnitInfo.ELITE_CAMEL_ARCHER, UnitInfo.GENITOUR, UnitInfo.ELITE_GENITOUR,
            UnitInfo.GBETO, UnitInfo.ELITE_GBETO, UnitInfo.SHOTEL_WARRIOR, UnitInfo.ELITE_SHOTEL_WARRIOR,
            UnitInfo.BALLISTA_ELEPHANT, UnitInfo.ELITE_BALLISTA_ELEPHANT, UnitInfo.KARAMBIT_WARRIOR,
            UnitInfo.ELITE_KARAMBIT_WARRIOR, UnitInfo.ARAMBAI, UnitInfo.ELITE_ARAMBAI, UnitInfo.RATTAN_ARCHER,
            UnitInfo.ELITE_RATTAN_ARCHER, UnitInfo.KONNIK, UnitInfo.ELITE_KONNIK, UnitInfo.KESHIK,
            UnitInfo.ELITE_KESHIK, UnitInfo.KIPCHAK, UnitInfo.ELITE_KIPCHAK, UnitInfo.LEITIS, UnitInfo.ELITE_LEITIS,
            UnitInfo.KONNIK_DISMOUNTED, UnitInfo.ELITE_KONNIK_DISMOUNTED, UnitInfo.KONNIK_KREPOST,
            UnitInfo.ELITE_KONNIK_KREPOST, UnitInfo.ELITE_KIPCHAK_CUMAN_MERCENARIES, UnitInfo.FLAMING_CAMEL,
            UnitInfo.COUSTILLIER, UnitInfo.ELITE_COUSTILLIER, UnitInfo.SERJEANT, UnitInfo.ELITE_SERJEANT,
            UnitInfo.SERJEANT_DONJON, UnitInfo.ELITE_SERJEANT_DONJON, UnitInfo.FLEMISH_MILITIA_MALE,
            UnitInfo.FLEMISH_MILITIA_FEMALE, UnitInfo.FLEMISH_MILITIA,
        ]\n"""
from_id = """
    @classmethod
    def from___NAME__(cls, value: int):
        if type(value) is not int:
            raise TypeError(f"from___NAME__ expected int, got {type(value)}")
        if value == -1:
            raise ValueError("-1 is not a valid __NAME__ value")
        for x in cls._member_map_.values():
            if x.value[__VALUE__] == value:
                return x
        raise ValueError(f"{value} is not a valid __NAME__ value")\n"""
non_gaia = """
    @staticmethod
    def non_gaia():
        result = []
        for x in __CLASSNAME__Info:
            if not x.IS_GAIA:
                result.append(x)
        return result\n"""
gaia_only = """
    @staticmethod
    def gaia_only():
        result = []
        for x in __CLASSNAME__Info:
            if x.IS_GAIA:
                result.append(x)
        return result\n"""