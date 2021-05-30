from enum import Enum
import json

with open("./unit_projectile_info.json") as file:
    unit_projectile_info = json.load(file)

class ProjectileInfo(Enum):

    @property
    def ID(self):
        return self.value[0]

    @property
    def PROJECTILE_OF(self):
        return self.value[1]

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

    @staticmethod
    def get_projectile_of(unit_const: int, has_chemistry: bool = False, secondary: bool = False):
        if type(unit_const) is not int:
            raise TypeError(f"unit id expected int, got {type(unit_const)}")
        if unit_const == -1:
            raise ValueError("-1 is not a valid unit constant")
        
        if type(has_chemistry) is not bool:
            raise TypeError(f"has_chemistry expected bool, got {type(has_chemistry)}")
        
        if type(secondary) is not bool:
            raise TypeError(f"has_chemistry expected bool, got {type(secondary)}")

        fire = "_fire" if has_chemistry else ""
        projectile = "secondary" if secondary else "primary"

        return unit_projectile_info.get(str(unit_const), {}).get(projectile+fire, -1)

    ARROW = 9, ()
    VOL = 54, (71, 109, 141, 142, 484, 597, 617, 621)
    ARROW1 = 97, ()
    SLINGER = 187, (185, 1075)
    CATST = 242, ()
    CATSF = 244, ()
    BOLTX = 245, ()
    BOLTF = 246, ()
    ARROW2 = 312, ()
    TREBST = 313, ()
    MANGST = 314, ()
    ARROW3 = 315, ()
    ARROW4 = 316, ()
    ARROW5 = 317, ()
    ARROW6 = 318, ()
    ARROW7 = 319, ()
    ARROW8 = 320, ()
    ARROW9 = 321, ()
    ARROW10 = 322, ()
    CATST1 = 323, ()
    CATST2 = 324, ()
    CATST3 = 325, ()
    CATST4 = 326, ()
    CATST5 = 327, ()
    VOL_FIRE = 328, (71, 109, 141, 142, 484, 597, 617, 621)
    ARW_FLM = 360, ()
    ARC = 363, (4, 158, 571)
    CROSSBOWMAN = 364, (24, 493, 866, 868, 873, 875, 926, 930, 1072, 1106, 1166, 1294, 1297)
    CRS = 365, (7,)
    HCS = 366, (6, 583, 596, 1010, 1012, 1036, 1079, 1155)
    SCORPION = 367, (279,)
    BOMBARD_CANNON = 368, (36, 644, 650)
    MANGONEL_SECONDARY = 369, (280, 550, 588)
    TREBUCHET = 371, (42, 682, 683, 1690)
    GAL = 372, (21,)
    WAR_GALLEY = 373, (442, 827, 829)
    CANNON_GALLEON = 374, (420, 691)
    COM_FIRE = 375, (24, 493, 866, 868, 873, 875, 926, 930, 1072, 1106, 1166, 1294, 1297)
    CRS_FIRE = 376, (7,)
    HCS_FIRE = 377, (6, 583, 596, 1010, 1012, 1036, 1079, 1155)
    SCORPION_FIRE = 378, (279,)
    GUNPOWDER_PRIMARY = 380, (5, 46, 52, 203, 425, 427, 557, 748, 771, 773, 1001, 1003, 1068)
    BOLTXF = 381, ()
    BOLTF1 = 385, ()
    MNG_FLM = 462, ()
    ARC_FIRE = 466, (4, 158, 571)
    MANGONEL_SECONDARY_FIRE = 468, (280, 550, 588)
    TREBUCHET_FIRE = 469, (42, 682, 683, 1690)
    GALLEY_FIRE = 470, (21,)
    WAR_GALLEY_FIRE = 471, (442, 827, 829)
    HAR_FIRE = 475, (11, 39, 172, 561, 577, 731, 1007, 1009, 1034, 1231, 1233, 1259, 1260, 1261, 1269, 1275, 1276)
    HHA_FIRE = 476, (437, 474, 698, 943, 1267, 1303)
    HAR = 477, (11, 39, 172, 561, 577, 731, 1007, 1009, 1034, 1231, 1233, 1259, 1260, 1261, 1269, 1275, 1276)
    HHA = 478, (437, 474, 698, 943, 1267, 1303)
    T_ARO = 485, ()
    WTN = 503, ()
    ARROW_GUARD_TOWER = 504, (79, 234, 235, 566, 785, 1665)
    KEP = 505, (79, 234, 235, 684, 685, 785, 1102, 1665)
    BTW = 506, (236,)
    ACA = 507, (492, 642, 686, 1182)
    AHX = 508, ()
    VIL = 509, (122, 216)
    CKN = 510, (73, 559, 1073, 1231, 1233, 1260)
    LONGBOWMAN = 511, (8, 200, 530, 763, 765, 850, 1069, 1129, 1131)
    LBT = 512, (45, 47, 51, 106, 133, 250, 533, 778, 885, 1189)
    MSU = 513, ()
    MPC = 514, ()
    TAX = 515, (165, 281, 424, 426, 531, 931, 1298)
    WTN_FIRE = 516, ()
    GTW_FIRE = 517, (79, 234, 235, 566, 785, 1665)
    KEP_FIRE = 518, (79, 234, 235, 684, 685, 785, 1102, 1665)
    ACA_FIRE = 519, (492, 642, 686, 1182)
    AHX_FIRE = 520, ()
    VIL_FIRE = 521, (122, 216)
    CKN_FIRE = 522, (73, 559, 1073, 1231, 1233, 1260)
    LBM_FIRE = 523, (8, 200, 530, 763, 765, 850, 1069, 1129, 1131)
    LBT_FIRE = 524, (45, 47, 51, 106, 133, 250, 533, 778, 885, 1189)
    MPC_FIRE = 525, ()
    MSU_FIRE = 526, ()
    FRG = 537, ()
    HFG = 538, ()
    SGY = 540, (539,)
    SGY_FIRE = 541, (539,)
    ONAGER = 551, ()
    ONAGER_FIRE = 552, ()
    HEAVY_SCORPION = 627, (542,)
    HEAVY_SCORPION_FIRE = 628, (542,)
    MANGONEL_PRIMARY = 656, (280, 550, 588)
    GP1 = 657, ()
    MANGONEL_PRIMARY_FIRE = 658, (280, 550, 588)
    FIRE_SHIP = 676, (188, 190, 529, 532, 938, 1103, 1302)
    MLK = 736, (282, 556, 929, 1296)
    CST = 746, (33, 82, 445, 1251)
    CST_FIRE = 747, (33, 82, 445, 1251)
    CGX = 767, (831, 832, 844, 1631)
    STW = 786, ()
    STW_FIRE = 787, ()
    KNIFE = 1055, (1013, 1015, 1066)
    CVB = 1057, (1004, 1006)
    CVB_FIRE = 1058, (1004, 1006)
    LBOL = 1111, ()
    LBOL_FIRE = 1112, ()
    HEAVY_SCORPION_UNUSED = 1113, ()
    HEAVY_SCORPION_FIRE_UNUSED = 1114, ()
    GUNPOWDER_SECONDARY = 1119, (203, 1001, 1003)
    BALLISTA_ELEPHANT = 1167, (1120, 1122)
    BALLISTA_ELEPHANT_FIRE = 1168, (1120, 1122)
    ARAMBAI = 1169, (1126, 1128)
    ARAMBAI_FIRE = 1170, (1126, 1128)
    SHCOW = 1223, ()
    LASER = 1595, (1222, 1577)
