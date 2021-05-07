from enum import Enum


class HeroInfo(Enum):
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
        if type(value) is not int:
            raise TypeError(f"from_dead_id expected int, got {type(value)}")
        if value == -1:
            raise ValueError("-1 is not a valid dead_id value")
        for x in cls._member_map_.values():
            if x.value[2] == value:
                return x
        raise ValueError(f"{value} is not a valid dead_id value")

    @property
    def HOTKEY_ID(self):
        return self.value[3]

    @classmethod
    def from_hotkey_id(cls, value: int):
        if type(value) is not int:
            raise TypeError(f"from_hotkey_id expected int, got {type(value)}")
        if value == -1:
            raise ValueError("-1 is not a valid hotkey_id value")
        for x in cls._member_map_.values():
            if x.value[3] == value:
                return x
        raise ValueError(f"{value} is not a valid hotkey_id value")

    KHOSRAU = 1297, 172, 874, -1
    LIEF_ERIKSON = 106, 118, -1, -1
    RICHARD_THE_LIONHEART = 160, 92, 570, -1
    THE_BLACK_PRINCE = 161, 343, 139, -1
    FRIAR_TUCK = 163, 311, 134, -1
    SHERIFF_OF_NOTTINGHAM = 164, 182, 180, -1
    CHARLEMAGNE = 165, 160, 157, -1
    ROLAND = 166, 320, 111, -1
    BELISARIUS = 167, 187, 277, -1
    THEODORIC_THE_GOTH = 168, 163, 62, -1
    AETHELFRITH = 169, 161, 233, -1
    SIEGFRIED = 170, 301, 568, -1
    ERIK_THE_RED = 171, 118, 693, -1
    TAMERLANE = 172, 261, 135, -1
    KING_ARTHUR = 173, 301, 568, -1
    LANCELOT = 174, 305, 570, -1
    GAWAIN = 175, 343, 139, -1
    MORDRED = 176, 305, 570, -1
    ARCHBISHOP = 177, 311, 134, -1
    VLAD_DRACULA = 193, 147, 1617, -1
    KITABATAKE = 195, 307, 151, -1
    MINAMOTO = 196, 126, 151, -1
    ALEXANDER_NEVSKI = 197, 75, 139, -1
    EL_CID = 198, 173, 568, -1
    ROBIN_HOOD = 200, 326, 115, -1
    VASCO_DA_GAMA = 203, 167, -1, -1
    ALARIC_THE_GOTH = 223, 163, 1620, -1
    KING_BELA_IV = 230, 323, 497, -1
    CUAUHTEMOC = 307, 146, 1117, -1
    HENRY_THE_LION = 418, 328, 111, -1
    CHARLES_MARTEL = 424, 129, 157, -1
    FRANCISCO_DE_ORELLANA = 425, 153, 772, -1
    HAROLD_HARDRADA = 426, 118, 693, -1
    GONZALO_PIZARRO = 427, 167, 772, -1
    HROLF_THE_GANGER = 428, 302, 695, -1
    FREDERICK_BARBAROSSA = 429, 154, 181, -1
    JOAN_THE_MAID = 430, 52, 431, -1
    WILLIAM_WALLACE = 432, 363, 433, -1
    PRITHVIRAJ = 437, 176, 1627, -1
    FRANCESCO_SFORZA = 439, 162, 1615, -1
    ATAULF = 453, 163, 1624, -1
    JOAN_OF_ARC = 629, 76, 630, -1
    FRANKISH_PALADIN = 632, 62, 633, -1
    SIEUR_DE_METZ = 634, 59, 111, -1
    SIEUR_BERTRAND = 636, 61, 111, -1
    DUKE_D_ALENASONN = 638, 65, 633, -1
    LA_HIRE = 640, 51, 568, -1
    LORD_DE_GRAVILLE = 642, 66, 496, -1
    JEAN_DE_LORRAIN = 644, 67, 16, -1
    CONSTABLE_RICHEMONT = 646, 343, 633, -1
    GUY_JOSSELYNE = 648, 56, 570, -1
    JEAN_BUREAU = 650, 68, 16, -1
    SIR_JOHN_FASTOLF = 652, 69, 633, -1
    REYNALD_DE_CHATILLON = 678, 70, 633, -1
    MASTER_OF_THE_TEMPLAR = 680, 75, 633, -1
    BAD_NEIGHBOR = 682, 94, 194, -1
    GODS_OWN_SLING = 683, 94, 194, -1
    ARCHER_OF_THE_EYES = 686, 77, 687, -1
    SUBOTAI = 698, 53, 1618, -1
    HUNTING_WOLF = 700, 340, 237, -1
    KUSHLUK = 702, 81, 1638, -1
    TOPA_YUPANQUI = 703, 327, 750, -1
    SHAH = 704, 82, 1337, -1
    SABOTEUR = 706, 58, -1, -1
    ORNLU_THE_WOLF = 707, 145, 708, -1
    GODS_OWN_SLING_PACKED = 729, 313, 735, -1
    BAD_NEIGHBOR_PACKED = 730, 313, 735, -1
    GENGHIS_KHAN = 731, 54, 135, -1
    EMPEROR_IN_A_BARREL = 733, 57, 205, -1
    CUSI_YUPANQUI = 749, 306, 1626, -1
    ATTILA_THE_HUN = 777, 119, 1619, -1
    BLEDA_THE_HUN = 779, 120, 1371, -1
    POPE_LEO_I = 781, 130, 134, -1
    SCYTHIAN_WILD_WOMAN = 783, 121, 431, -1
    EL_CID_CAMPEADOR = 824, 173, 633, -1
    KING_SANCHO = 838, 124, 497, -1
    KING_ALFONSO = 840, 123, 497, -1
    IMAM = 842, 324, 1326, -1
    ADMIRAL_YI_SUN_SHIN = 844, 127, -1, -1
    NOBUNAGA = 845, 126, 151, -1
    HENRY_V = 847, 125, 570, -1
    WILLIAM_THE_CONQUEROR = 849, 128, 633, -1
    SCYTHIAN_SCOUT = 852, 321, 547, -1
    MUSA_IBN_NUSAYR = 1034, 204, 1008, -1
    SUNDJATA = 1035, 206, 1395, -1
    TARIQ_IBN_ZIYAD = 1036, 207, 1616, -1
    RICHARD_DE_CLARE = 1037, 210, 547, -1
    TRISTAN = 1038, 322, 870, -1
    PRINCESS_YODIT = 1039, 216, 1328, -1
    HENRY_II = 1040, 325, 500, -1
    YEKUNA_AMLAK = 1064, 208, 1017, -1
    YODIT = 1066, 216, 1625, -1
    ITZCOATL = 1067, 317, 1221, -1
    MUSTAFA_PASHA = 1068, 318, 107, -1
    PACAL_II = 1069, 314, 764, -1
    BABUR = 1070, 316, 300, -1
    ABRAHA_ELEPHANT = 1071, 310, 136, -1
    GUGLIELMO_EMBRIACO = 1072, 312, 867, -1
    SU_DINGFANG = 1073, 303, 28, -1
    PACHACUTI = 1074, 319, 1633, -1
    HUAYNA_CAPAC = 1075, 308, 186, -1
    MIKLOS_TOLDI = 1076, 322, 870, -1
    LITTLE_JOHN = 1077, 309, 140, -1
    ZAWISZA_THE_BLACK = 1078, 315, 480, -1
    SUMANGURU = 1080, 205, 1621, -1
    DAGNAJAN = 1106, 209, 1108, -1
    GIDAJAN = 1109, 245, 1110, -1
    GAJAH_MADA = 1157, 220, 1190, -1
    JAYANEGARA = 1158, 342, 732, -1
    RADEN_WIJAYA = 1159, 222, 139, -1
    SUNDA_ROYAL_FIGHTER = 1160, 234, 1161, -1
    SURYAVARMAN_I = 1162, 239, 1154, -1
    UDAYADITYAVARMAN_I = 1163, 241, 732, -1
    JAYAVIRAVARMAN = 1164, 221, 1124, -1
    BAYINNAUNG = 1165, 219, 1637, -1
    TABINSHWEHTI = 1166, 223, 874, -1
    LE_LOI = 1178, 243, 1623, -1
    LE_LAI = 1180, 242, 1224, -1
    LE_TRIEN = 1181, 237, 568, -1
    LUU_NHAN_CHU = 1182, 238, 687, -1
    BUI_BI = 1183, 235, 1329, -1
    DINH_LE = 1184, 236, 1224, -1
    WANG_TONG = 1185, 240, 1224, -1
    ENVOY = 1186, 244, 1636, -1
    TOKHTAMYSH_KHAN = 1262, 152, 1229, -1
    IVAYLO = 1265, 257, 1290, -1
    TSAR_KONSTANTIN = 1266, 254, 1286, -1
    KOTYAN_KHAN = 1267, 259, 1287, -1
    CUMAN_CHIEF = 1268, 255, 1288, -1
    GIRGEN_KHAN = 1269, 256, 1289, -1
    URUS_KHAN = 1276, 262, 1232, -1
    VYTAUTAS_THE_GREAT = 1281, 260, 1278, -1
    IVAYLO_DISMOUNTED = 1290, 257, 1630, -1
    SANYOGITA = 1293, 170, 1328, -1
    PRITHVI = 1294, 304, 26, -1
    CHAND_BARDAI = 1295, 171, 1329, -1
    SALADIN = 1296, 175, 44, -1
    JARL = 1298, 188, 1628, -1
    SAVAR = 1299, 181, 1401, -1
    OSMAN = 1303, 180, 1632, -1
    MOUNTED_SAMURAI = 1568, 103, 1569, -1
    SOSSO_GUARD = 1574, 350, 1575, -1
    THE_MIDDLEBROOK = 1631, 353, -1, -1
