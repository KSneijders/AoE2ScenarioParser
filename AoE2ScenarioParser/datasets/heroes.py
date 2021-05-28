from enum import Enum


class HeroInfo(Enum):
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

    KHOSRAU = 1297, 172, 874
    LIEF_ERIKSON = 106, 118, -1
    RICHARD_THE_LIONHEART = 160, 92, 570
    THE_BLACK_PRINCE = 161, 343, 139
    FRIAR_TUCK = 163, 311, 134
    SHERIFF_OF_NOTTINGHAM = 164, 182, 180
    CHARLEMAGNE = 165, 160, 157
    ROLAND = 166, 320, 111
    BELISARIUS = 167, 187, 277
    THEODORIC_THE_GOTH = 168, 163, 62
    AETHELFRITH = 169, 161, 233
    SIEGFRIED = 170, 301, 568
    ERIK_THE_RED = 171, 118, 693
    TAMERLANE = 172, 261, 135
    KING_ARTHUR = 173, 301, 568
    LANCELOT = 174, 305, 570
    GAWAIN = 175, 343, 139
    MORDRED = 176, 305, 570
    ARCHBISHOP = 177, 311, 134
    VLAD_DRACULA = 193, 147, 1617
    KITABATAKE = 195, 307, 151
    MINAMOTO = 196, 126, 151
    ALEXANDER_NEVSKI = 197, 75, 139
    EL_CID = 198, 173, 568
    ROBIN_HOOD = 200, 326, 115
    VASCO_DA_GAMA = 203, 167, -1
    ALARIC_THE_GOTH = 223, 163, 1620
    KING_BELA_IV = 230, 323, 497
    CUAUHTEMOC = 307, 146, 1117
    HENRY_THE_LION = 418, 328, 111
    CHARLES_MARTEL = 424, 129, 157
    FRANCISCO_DE_ORELLANA = 425, 153, 772
    HAROLD_HARDRADA = 426, 118, 693
    GONZALO_PIZARRO = 427, 167, 772
    HROLF_THE_GANGER = 428, 302, 695
    FREDERICK_BARBAROSSA = 429, 154, 181
    JOAN_THE_MAID = 430, 52, 431
    WILLIAM_WALLACE = 432, 363, 433
    PRITHVIRAJ = 437, 176, 1627
    FRANCESCO_SFORZA = 439, 162, 1615
    ATAULF = 453, 163, 1624
    JOAN_OF_ARC = 629, 76, 630
    FRANKISH_PALADIN = 632, 62, 633
    SIEUR_DE_METZ = 634, 59, 111
    SIEUR_BERTRAND = 636, 61, 111
    DUKE_D_ALENASONN = 638, 65, 633
    LA_HIRE = 640, 51, 568
    LORD_DE_GRAVILLE = 642, 66, 496
    JEAN_DE_LORRAIN = 644, 67, 16
    CONSTABLE_RICHEMONT = 646, 343, 633
    GUY_JOSSELYNE = 648, 56, 570
    JEAN_BUREAU = 650, 68, 16
    SIR_JOHN_FASTOLF = 652, 69, 633
    REYNALD_DE_CHATILLON = 678, 70, 633
    MASTER_OF_THE_TEMPLAR = 680, 75, 633
    BAD_NEIGHBOR = 682, 94, 194
    GODS_OWN_SLING = 683, 94, 194
    ARCHER_OF_THE_EYES = 686, 77, 687
    SUBOTAI = 698, 53, 1618
    HUNTING_WOLF = 700, 340, 237
    KUSHLUK = 702, 81, 1638
    TOPA_YUPANQUI = 703, 327, 750
    SHAH = 704, 82, 1337
    SABOTEUR = 706, 58, -1
    ORNLU_THE_WOLF = 707, 145, 708
    GODS_OWN_SLING_PACKED = 729, 313, 735
    BAD_NEIGHBOR_PACKED = 730, 313, 735
    GENGHIS_KHAN = 731, 54, 135
    EMPEROR_IN_A_BARREL = 733, 57, 205
    CUSI_YUPANQUI = 749, 306, 1626
    ATTILA_THE_HUN = 777, 119, 1619
    BLEDA_THE_HUN = 779, 120, 1371
    POPE_LEO_I = 781, 130, 134
    SCYTHIAN_WILD_WOMAN = 783, 121, 431
    EL_CID_CAMPEADOR = 824, 173, 633
    KING_SANCHO = 838, 124, 497
    KING_ALFONSO = 840, 123, 497
    IMAM = 842, 324, 1326
    ADMIRAL_YI_SUN_SHIN = 844, 127, -1
    NOBUNAGA = 845, 126, 151
    HENRY_V = 847, 125, 570
    WILLIAM_THE_CONQUEROR = 849, 128, 633
    SCYTHIAN_SCOUT = 852, 321, 547
    MUSA_IBN_NUSAYR = 1034, 204, 1008
    SUNDJATA = 1035, 206, 1395
    TARIQ_IBN_ZIYAD = 1036, 207, 1616
    RICHARD_DE_CLARE = 1037, 210, 547
    TRISTAN = 1038, 322, 870
    PRINCESS_YODIT = 1039, 216, 1328
    HENRY_II = 1040, 325, 500
    YEKUNA_AMLAK = 1064, 208, 1017
    YODIT = 1066, 216, 1625
    ITZCOATL = 1067, 317, 1221
    MUSTAFA_PASHA = 1068, 318, 107
    PACAL_II = 1069, 314, 764
    BABUR = 1070, 316, 300
    ABRAHA_ELEPHANT = 1071, 310, 136
    GUGLIELMO_EMBRIACO = 1072, 312, 867
    SU_DINGFANG = 1073, 303, 28
    PACHACUTI = 1074, 319, 1633
    HUAYNA_CAPAC = 1075, 308, 186
    MIKLOS_TOLDI = 1076, 322, 870
    LITTLE_JOHN = 1077, 309, 140
    ZAWISZA_THE_BLACK = 1078, 315, 480
    SUMANGURU = 1080, 205, 1621
    DAGNAJAN = 1106, 209, 1108
    GIDAJAN = 1109, 245, 1110
    GAJAH_MADA = 1157, 220, 1190
    JAYANEGARA = 1158, 342, 732
    RADEN_WIJAYA = 1159, 222, 139
    SUNDA_ROYAL_FIGHTER = 1160, 234, 1161
    SURYAVARMAN_I = 1162, 239, 1154
    UDAYADITYAVARMAN_I = 1163, 241, 732
    JAYAVIRAVARMAN = 1164, 221, 1124
    BAYINNAUNG = 1165, 219, 1637
    TABINSHWEHTI = 1166, 223, 874
    LE_LOI = 1178, 243, 1623
    LE_LAI = 1180, 242, 1224
    LE_TRIEN = 1181, 237, 568
    LUU_NHAN_CHU = 1182, 238, 687
    BUI_BI = 1183, 235, 1329
    DINH_LE = 1184, 236, 1224
    WANG_TONG = 1185, 240, 1224
    ENVOY = 1186, 244, 1636
    TOKHTAMYSH_KHAN = 1262, 152, 1229
    IVAYLO = 1265, 257, 1290
    TSAR_KONSTANTIN = 1266, 254, 1286
    KOTYAN_KHAN = 1267, 259, 1287
    CUMAN_CHIEF = 1268, 255, 1288
    GIRGEN_KHAN = 1269, 256, 1289
    URUS_KHAN = 1276, 262, 1232
    VYTAUTAS_THE_GREAT = 1281, 260, 1278
    IVAYLO_DISMOUNTED = 1290, 257, 1630
    SANYOGITA = 1293, 170, 1328
    PRITHVI = 1294, 304, 26
    CHAND_BARDAI = 1295, 171, 1329
    SALADIN = 1296, 175, 44
    JARL = 1298, 188, 1628
    SAVAR = 1299, 181, 1401
    OSMAN = 1303, 180, 1632
    MOUNTED_SAMURAI = 1568, 103, 1569
    SOSSO_GUARD = 1574, 350, 1575
    THE_MIDDLEBROOK = 1631, 353, -1
