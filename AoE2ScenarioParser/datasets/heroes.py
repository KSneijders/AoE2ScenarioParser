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

    KHOSRAU = 1297, 172, 874, False
    LIEF_ERIKSON = 106, 118, -1, False
    RICHARD_THE_LIONHEART = 160, 92, 570, False
    THE_BLACK_PRINCE = 161, 343, 139, False
    FRIAR_TUCK = 163, 311, 134, False
    SHERIFF_OF_NOTTINGHAM = 164, 182, 180, False
    CHARLEMAGNE = 165, 160, 157, False
    ROLAND = 166, 320, 111, False
    BELISARIUS = 167, 187, 277, False
    THEODORIC_THE_GOTH = 168, 163, 62, False
    AETHELFRITH = 169, 161, 233, False
    SIEGFRIED = 170, 301, 568, False
    ERIK_THE_RED = 171, 118, 693, False
    TAMERLANE = 172, 261, 135, False
    KING_ARTHUR = 173, 301, 568, False
    LANCELOT = 174, 305, 570, False
    GAWAIN = 175, 343, 139, False
    MORDRED = 176, 305, 570, False
    ARCHBISHOP = 177, 311, 134, False
    VLAD_DRACULA = 193, 147, 1617, False
    KITABATAKE = 195, 307, 151, False
    MINAMOTO = 196, 126, 151, False
    ALEXANDER_NEVSKI = 197, 75, 139, False
    EL_CID = 198, 173, 568, False
    ROBIN_HOOD = 200, 326, 115, False
    VASCO_DA_GAMA = 203, 167, -1, False
    ALARIC_THE_GOTH = 223, 163, 1620, False
    KING_BELA_IV = 230, 323, 497, False
    CUAUHTEMOC = 307, 146, 1117, False
    HENRY_THE_LION = 418, 328, 111, False
    CHARLES_MARTEL = 424, 129, 157, False
    FRANCISCO_DE_ORELLANA = 425, 153, 772, False
    HAROLD_HARDRADA = 426, 118, 693, False
    GONZALO_PIZARRO = 427, 167, 772, False
    HROLF_THE_GANGER = 428, 302, 695, False
    FREDERICK_BARBAROSSA = 429, 154, 181, False
    JOAN_THE_MAID = 430, 52, 431, False
    WILLIAM_WALLACE = 432, 363, 433, False
    PRITHVIRAJ = 437, 176, 1627, False
    FRANCESCO_SFORZA = 439, 162, 1615, False
    ATAULF = 453, 163, 1624, False
    JOAN_OF_ARC = 629, 76, 630, False
    FRANKISH_PALADIN = 632, 62, 633, False
    SIEUR_DE_METZ = 634, 59, 111, False
    SIEUR_BERTRAND = 636, 61, 111, False
    DUKE_D_ALENASONN = 638, 65, 633, False
    LA_HIRE = 640, 51, 568, False
    LORD_DE_GRAVILLE = 642, 66, 496, False
    JEAN_DE_LORRAIN = 644, 67, 16, False
    CONSTABLE_RICHEMONT = 646, 343, 633, False
    GUY_JOSSELYNE = 648, 56, 570, False
    JEAN_BUREAU = 650, 68, 16, False
    SIR_JOHN_FASTOLF = 652, 69, 633, False
    REYNALD_DE_CHATILLON = 678, 70, 633, False
    MASTER_OF_THE_TEMPLAR = 680, 75, 633, False
    BAD_NEIGHBOR = 682, 94, 194, False
    GODS_OWN_SLING = 683, 94, 194, False
    ARCHER_OF_THE_EYES = 686, 77, 687, False
    SUBOTAI = 698, 53, 1618, False
    HUNTING_WOLF = 700, 340, 237, False
    KUSHLUK = 702, 81, 1638, False
    TOPA_YUPANQUI = 703, 327, 750, False
    SHAH = 704, 82, 1337, False
    SABOTEUR = 706, 58, -1, False
    ORNLU_THE_WOLF = 707, 145, 708, False
    GODS_OWN_SLING_PACKED = 729, 313, 735, False
    BAD_NEIGHBOR_PACKED = 730, 313, 735, False
    GENGHIS_KHAN = 731, 54, 135, False
    EMPEROR_IN_A_BARREL = 733, 57, 205, False
    CUSI_YUPANQUI = 749, 306, 1626, False
    ATTILA_THE_HUN = 777, 119, 1619, False
    BLEDA_THE_HUN = 779, 120, 1371, False
    POPE_LEO_I = 781, 130, 134, False
    SCYTHIAN_WILD_WOMAN = 783, 121, 431, False
    EL_CID_CAMPEADOR = 824, 173, 633, False
    KING_SANCHO = 838, 124, 497, False
    KING_ALFONSO = 840, 123, 497, False
    IMAM = 842, 324, 1326, False
    ADMIRAL_YI_SUN_SHIN = 844, 127, -1, False
    NOBUNAGA = 845, 126, 151, False
    HENRY_V = 847, 125, 570, False
    WILLIAM_THE_CONQUEROR = 849, 128, 633, False
    SCYTHIAN_SCOUT = 852, 321, 547, False
    MUSA_IBN_NUSAYR = 1034, 204, 1008, False
    SUNDJATA = 1035, 206, 1395, False
    TARIQ_IBN_ZIYAD = 1036, 207, 1616, False
    RICHARD_DE_CLARE = 1037, 210, 547, False
    TRISTAN = 1038, 322, 870, False
    PRINCESS_YODIT = 1039, 216, 1328, False
    HENRY_II = 1040, 325, 500, False
    YEKUNA_AMLAK = 1064, 208, 1017, False
    YODIT = 1066, 216, 1625, False
    ITZCOATL = 1067, 317, 1221, False
    MUSTAFA_PASHA = 1068, 318, 107, False
    PACAL_II = 1069, 314, 764, False
    BABUR = 1070, 316, 300, False
    ABRAHA_ELEPHANT = 1071, 310, 136, False
    GUGLIELMO_EMBRIACO = 1072, 312, 867, False
    SU_DINGFANG = 1073, 303, 28, False
    PACHACUTI = 1074, 319, 1633, False
    HUAYNA_CAPAC = 1075, 308, 186, False
    MIKLOS_TOLDI = 1076, 322, 870, False
    LITTLE_JOHN = 1077, 309, 140, False
    ZAWISZA_THE_BLACK = 1078, 315, 480, False
    SUMANGURU = 1080, 205, 1621, False
    DAGNAJAN = 1106, 209, 1108, False
    GIDAJAN = 1109, 245, 1110, False
    GAJAH_MADA = 1157, 220, 1190, False
    JAYANEGARA = 1158, 342, 732, False
    RADEN_WIJAYA = 1159, 222, 139, False
    SUNDA_ROYAL_FIGHTER = 1160, 234, 1161, False
    SURYAVARMAN_I = 1162, 239, 1154, False
    UDAYADITYAVARMAN_I = 1163, 241, 732, False
    JAYAVIRAVARMAN = 1164, 221, 1124, False
    BAYINNAUNG = 1165, 219, 1637, False
    TABINSHWEHTI = 1166, 223, 874, False
    LE_LOI = 1178, 243, 1623, False
    LE_LAI = 1180, 242, 1224, False
    LE_TRIEN = 1181, 237, 568, False
    LUU_NHAN_CHU = 1182, 238, 687, False
    BUI_BI = 1183, 235, 1329, False
    DINH_LE = 1184, 236, 1224, False
    WANG_TONG = 1185, 240, 1224, False
    ENVOY = 1186, 244, 1636, False
    TOKHTAMYSH_KHAN = 1262, 152, 1229, False
    IVAYLO = 1265, 257, 1290, False
    TSAR_KONSTANTIN = 1266, 254, 1286, False
    KOTYAN_KHAN = 1267, 259, 1287, False
    CUMAN_CHIEF = 1268, 255, 1288, False
    GIRGEN_KHAN = 1269, 256, 1289, False
    URUS_KHAN = 1276, 262, 1232, False
    VYTAUTAS_THE_GREAT = 1281, 260, 1278, False
    IVAYLO_DISMOUNTED = 1290, 257, 1630, False
    SANYOGITA = 1293, 170, 1328, False
    PRITHVI = 1294, 304, 26, False
    CHAND_BARDAI = 1295, 171, 1329, False
    SALADIN = 1296, 175, 44, False
    JARL = 1298, 188, 1628, False
    SAVAR = 1299, 181, 1401, False
    OSMAN = 1303, 180, 1632, False
    MOUNTED_SAMURAI = 1568, 103, 1569, False
    SOSSO_GUARD = 1574, 350, 1575, False
    THE_MIDDLEBROOK = 1631, 353, -1, False
