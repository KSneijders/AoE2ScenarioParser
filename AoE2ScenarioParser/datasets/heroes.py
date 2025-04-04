from AoE2ScenarioParser.datasets.support.info_dataset_base import InfoDatasetBase


class HeroInfo(InfoDatasetBase):
    """
    This enum class provides information about most of the heroes in the game. Information about the following
    properties of a hero is found in this class:

     - Unit ID
     - Icon ID
     - Dead Unit ID
     - HotKey ID
     - If the hero is a gaia only unit

    **Inherited Methods from class InfoDatasetBase**

    >>> InfoDatasetBase.from_id()
    >>> InfoDatasetBase.from_dead_id()
    >>> InfoDatasetBase.from_icon_id()
    >>> InfoDatasetBase.from_hotkey_id()
    >>> InfoDatasetBase.gaia_only()
    >>> InfoDatasetBase.non_gaia()

    **Examples**

    >>> HeroInfo.WILLIAM_WALLACE.ID
    >>> 432

    >>> HeroInfo.WILLIAM_WALLACE.ICON_ID
    >>> 363

    >>> HeroInfo.WILLIAM_WALLACE.DEAD_ID
    >>> 433

    >>> HeroInfo.WILLIAM_WALLACE.HOTKEY_ID
    >>> 16299

    >>> HeroInfo.WILLIAM_WALLACE.IS_GAIA_ONLY
    >>> False
    """
    KHOSRAU = 1297, 172, 874, 16311, False
    LEIF_ERIKSON = 106, 118, -1, 16457, False
    RICHARD_THE_LIONHEART = 160, 92, 570, 16633, False
    THE_BLACK_PRINCE = 161, 343, 139, 16622, False
    FRIAR_TUCK = 163, 311, 134, 16626, False
    SHERIFF_OF_NOTTINGHAM = 164, 182, 180, 16635, False
    CHARLEMAGNE = 165, 160, 157, 16623, False
    ROLAND = 166, 320, 111, 16634, False
    BELISARIUS = 167, 187, 277, 16621, False
    THEODORIC_THE_GOTH = 168, 163, 62, 16638, False
    AETHELFRITH = 169, 161, 233, 16619, False
    SIEGFRIED = 170, 301, 568, 16636, False
    ERIK_THE_RED = 171, 118, 693, 16625, False
    TAMERLANE = 172, 261, 135, 16637, False
    KING_ARTHUR = 173, 301, 568, 16628, False
    LANCELOT = 174, 305, 570, 16630, False
    GAWAIN = 175, 343, 139, 16627, False
    MORDRED = 176, 305, 570, 16632, False
    ARCHBISHOP = 177, 311, 134, 16620, False
    VLAD_DRACULA = 193, 147, 1617, 16101, False
    KITABATAKE = 195, 307, 151, 16629, False
    MINAMOTO = 196, 126, 151, 16631, False
    ALEXANDER_NEVSKI = 197, 75, 139, 16639, False
    EL_CID = 198, 173, 568, 16624, False
    ROBIN_HOOD = 200, 326, 115, 16640, False
    VASCO_DA_GAMA = 203, 167, -1, 16106, False
    ALARIC_THE_GOTH = 223, 163, 1620, 16638, False
    KING_BELA_IV = 230, 323, 497, 16738, False
    CUAUHTEMOC = 307, 146, 1117, 16673, False
    HENRY_THE_LION = 418, 328, 111, 16531, False
    CHARLES_MARTEL = 424, 129, 157, 16291, False
    FRANCISCO_DE_ORELLANA = 425, 153, 772, 16689, False
    HARALD_HARDRADA = 426, 118, 693, 16293, False
    GONZALO_PIZARRO = 427, 167, 772, 16689, False
    HROLF_THE_GANGER = 428, 302, 695, 16295, False
    FREDERICK_BARBAROSSA = 429, 154, 181, 16462, False
    JOAN_THE_MAID = 430, 52, 431, 16297, False
    WILLIAM_WALLACE = 432, 363, 433, 16299, False
    PRITHVIRAJ = 437, 176, 1627, 16412, False
    FRANCESCO_SFORZA = 439, 162, 1615, 16679, False
    ATAULF = 453, 163, 1624, 16638, False
    JOAN_OF_ARC = 629, 76, 630, 16526, False
    FRANKISH_PALADIN = 632, 62, 633, 16529, False
    SIEUR_DE_METZ = 634, 59, 111, 16531, False
    SIEUR_BERTRAND = 636, 61, 111, 16533, False
    DUKE_D_ALENCON = 638, 65, 633, 16535, False
    LA_HIRE = 640, 51, 568, 16537, False
    LORD_DE_GRAVILLE = 642, 66, 496, 16539, False
    JEAN_DE_LORRAIN = 644, 67, 16, 16541, False
    CONSTABLE_RICHEMONT = 646, 343, 633, 16543, False
    GUY_JOSSELYNE = 648, 56, 570, 16545, False
    JEAN_BUREAU = 650, 68, 16, 16547, False
    SIR_JOHN_FASTOLF = 652, 69, 633, 16549, False
    REYNALD_DE_CHATILLON = 678, 70, 633, 16560, False
    MASTER_OF_THE_TEMPLAR = 680, 75, 633, 16562, False
    BAD_NEIGHBOR = 682, 94, 194, 16564, False
    GODS_OWN_SLING = 683, 94, 194, 16565, False
    ARCHER_OF_THE_EYES = 686, 77, 687, 16568, False
    SUBOTAI = 698, 53, 1618, 16580, False
    HUNTING_WOLF = 700, 340, 237, 16582, False
    KUSHLUK = 702, 81, 1638, 16584, False
    TOPA_YUPANQUI = 703, 327, 750, 16669, False
    SHAH = 704, 82, 1337, 16586, False
    SABOTEUR = 706, 58, -1, 16588, False
    ORNLU_THE_WOLF = 707, 145, 708, 16589, False
    GODS_OWN_SLING_PACKED = 729, 313, 735, 16611, False
    BAD_NEIGHBOR_PACKED = 730, 313, 735, 16612, False
    GENGHIS_KHAN = 731, 54, 135, 16613, False
    EMPEROR_IN_A_BARREL = 733, 57, 205, 16615, False
    CUSI_YUPANQUI = 749, 306, 1626, 16671, False
    ATTILA_THE_HUN = 777, 119, 1619, 16695, False
    BLEDA_THE_HUN = 779, 120, 1371, 16697, False
    POPE_LEO_I = 781, 130, 134, 16699, False
    SCYTHIAN_WILD_WOMAN = 783, 121, 431, 16701, False
    EL_CID_CAMPEADOR = 824, 173, 633, 16724, False
    KING_SANCHO = 838, 124, 497, 16738, False
    KING_ALFONSO = 840, 123, 497, 16740, False
    IMAM = 842, 324, 1326, 16742, False
    ADMIRAL_YI_SUN_SHIN = 844, 127, -1, 16744, False
    NOBUNAGA = 845, 126, 151, 16745, False
    HENRY_V = 847, 125, 570, 16747, False
    WILLIAM_THE_CONQUEROR = 849, 128, 633, 16749, False
    SCYTHIAN_SCOUT = 852, 321, 547, 16752, False
    MUSA_IBN_NUSAYR = 1034, 204, 1008, 16101, False
    SUNDJATA = 1035, 206, 1395, 16777, False
    TARIQ_IBN_ZIYAD = 1036, 207, 1616, 16415, False
    RICHARD_DE_CLARE = 1037, 210, 547, 16778, False
    TRISTAN = 1038, 322, 870, 16779, False
    PRINCESS_YODIT = 1039, 216, 1328, 16781, False
    HENRY_II = 1040, 325, 500, 16780, False
    YEKUNO_AMLAK = 1064, 208, 1017, 16799, False
    YODIT = 1066, 216, 1625, 16220, False
    ITZCOATL = 1067, 317, 1221, 16206, False
    MUSTAFA_PASHA = 1068, 318, 107, 16207, False
    PACAL_II = 1069, 314, 764, 16208, False
    BABUR = 1070, 316, 300, 16209, False
    ABRAHA_ELEPHANT = 1071, 310, 136, 16210, False
    GUGLIELMO_EMBRIACO = 1072, 312, 867, 16211, False
    SU_DINGFANG = 1073, 303, 28, 16212, False
    PACHACUTI = 1074, 319, 1633, 16213, False
    HUAYNA_CAPAC = 1075, 308, 186, 16214, False
    MIKLOS_TOLDI = 1076, 322, 870, 16215, False
    LITTLE_JOHN = 1077, 309, 140, 16216, False
    ZAWISZA_THE_BLACK = 1078, 315, 480, 16217, False
    SUMANGURU = 1080, 205, 1621, 16218, False
    DAGNAJAN = 1106, 209, 1108, 16232, False
    GIDAJAN = 1109, 245, 1110, 16101, False
    GAJAH_MADA = 1157, 220, 1190, 16469, False
    JAYANEGARA = 1158, 342, 732, 16301, False
    RADEN_WIJAYA = 1159, 222, 139, 16070, False
    SUNDA_ROYAL_FIGHTER = 1160, 234, 1161, 16101, False
    SURYAVARMAN_I = 1162, 239, 1154, 16459, False
    UDAYADITYAVARMAN_I = 1163, 241, 732, 16301, False
    JAYAVIRAVARMAN = 1164, 221, 1124, 16101, False
    BAYINNAUNG = 1165, 219, 1637, 16459, False
    TABINSHWEHTI = 1166, 223, 874, 16101, False
    LE_LOI = 1178, 243, 1623, 16299, False
    LE_LAI = 1180, 242, 1224, 16633, False
    LE_TRIEN = 1181, 237, 568, 16299, False
    LUU_NHAN_CHU = 1182, 238, 687, 16568, False
    BUI_BI = 1183, 235, 1329, 16742, False
    DINH_LE = 1184, 236, 1224, 16633, False
    WANG_TONG = 1185, 240, 1224, 16218, False
    ENVOY = 1186, 244, 1636, 16777, False
    TOKHTAMYSH_KHAN = 1262, 152, 1229, 16101, False
    IVAYLO = 1265, 257, 1290, 16101, False
    TSAR_KONSTANTIN = 1266, 254, 1286, 16101, False
    KOTYAN_KHAN = 1267, 259, 1287, 16580, False
    CUMAN_CHIEF = 1268, 255, 1288, 16533, False
    GIRGEN_KHAN = 1269, 256, 1289, 16085, False
    URUS_KHAN = 1276, 262, 1232, 16108, False
    VYTAUTAS_THE_GREAT = 1281, 260, 1278, 16405, False
    IVAYLO_DISMOUNTED = 1290, 257, 1630, 16101, False
    SANYOGITA = 1293, 170, 1328, 16307, False
    PRITHVI = 1294, 304, 26, 16308, False
    CHAND_BARDAI = 1295, 171, 1329, 16742, False
    SALADIN = 1296, 175, 44, 16453, False
    JARL = 1298, 188, 1628, 16416, False
    SOGDIAN_CATAPHRACT = 1299, 181, 1401, 16451, False
    OSMAN = 1303, 180, 1632, 16412, False
    MOUNTED_SAMURAI = 1568, 103, 1569, 16661, False
    SOSSO_GUARD = 1574, 350, 1575, 16101, False
    THE_MIDDLEBROOK = 1631, 353, -1, 16457, False
    EDWARD_LONGSHANKS = 1669, 358, 1670, 16724, False
    GILBERT_DE_CLARE = 1671, 364, 1672, 16724, False
    JOHN_THE_FEARLESS = 1673, 359, 1674, 16724, False
    PHILIP_THE_GOOD = 1675, 360, 1676, 16724, False
    ROBERT_GUISCARD = 1677, 361, 1678, 16724, False
    ROGER_BOSSO = 1679, 362, 1680, 16724, False
    BOHEMOND = 1681, 357, 1682, 16724, False
    LLYWELYN_AP_GRUFFYDD = 1683, 368, 1684, 16619, False
    DAFYDD_AP_GRUFFYDD = 1685, 366, 1686, 16619, False
    BERNARD_D_ARMAGNAC = 1687, 365, 1688, 16724, False
    WARWOLF_TREBUCHET = 1690, 94, 194, 16097, False
    WARWOLF_TREBUCHET_PACKED = 1691, 313, 735, 16381, False
    JACQUELINE_OF_HAINAUT = 1692, 367, 1328, 16307, False
    STOERTEBEKER = 114, 88, -1, 16703, False
    JAN_ZIZKA = 1713, 373, 1714, 16724, False
    JADWIGA = 1715, 374, 1716, 16691, False
    JOGAILA = 1718, 375, 1719, 16724, False
    KESTUTIS = 1721, 376, 1722, 16724, False
    ALGIRDAS = 1725, 378, 1726, 16724, False
    ULRICH_VON_JUNGINGEN = 1727, 379, 1728, 16562, False
    EMPEROR_SIGISMUND = 1729, 380, 633, 16562, False
    DMITRY_OF_MOSCOW = 1730, 381, 139, 16639, False
    MIKHAIL_OF_TVER = 1731, 382, 877, 16639, False
    YOUNG_JADWIGA = 1732, 383, 431, 16297, False
    MIHIRA_BHOJA = 1762, 396, 870, 16779, False
    AMOGHAVARSHA = 1763, 397, 1736, 16779, False
    RAJENDRA_CHOLA = 1764, 398, 1765, 16633, False
    GENERAL_ARAIYAN = 1766, 399, 1767, 16218, False
    YOUNG_BABUR = 1768, 400, 495, 16218, False
    QUTLUGH = 1769, 401, 1770, 16637, False
    IBRAHIM_LODI = 1771, 402, 1277, 16458, False
    SHAYBANI_KHAN = 1772, 403, 1289, 16458, False
    SHAH_ISMAIL = 1815, 411, 1816, 16639, False
    ISMAIL = 1815, 411, 1816, 16639, False
    SELIM_THE_GRIM = 1820, 419, 1814, 16471, False
    THOROS = 1821, 413, 1848, 16639, False
    TAMAR = 1822, 414, 1823, 16691, False
    YURY = 1824, 421, 1630, 16101, False
    IVANE = 1825, 417, 27, 16471, False
    ZAKARE = 1826, 422, 1812, 16691, False
    STEPHAN = 1827, 420, 1812, 16691, False
    MLEH = 1828, 418, 568, 16537, False
    POLEMARCH = 2162, 2163, 622, 416014, False
    POLEMARCH_2 = 2164, 2163, 622, 416014, False
    POLEMARCH_3 = 2165, 2163, 622, 416014, False
    POLEMARCH_4 = 2166, 2163, 622, 416014, False
    POLEMARCH_3_WITH_EPHORATE = 2167, 2163, 622, 416014, False
    POLEMARCH_4_WITH_EPHORATE = 2270, 2163, 622, 416014, False
    POLEMARCH_3_WITH_MORAI = 2171, 2163, 622, 416014, False
    POLEMARCH_4_WITH_MORAI = 2272, 2163, 622, 416014, False
    ARTAPHERNES = 2308, 2363, 645, 16412, False
    DATIS = 2309, 2364, 631, 16444, False
    ARISTAGORAS = 2310, 2370, 653, 16724, False
    DIONYSUS = 2311, -1, 632, 416011, False
    ARTEMISIA = 2312, -1, 646, 416008, False
    ARISTIDES = 2313, 2376, 644, 416013, False
    MILTIADES = 2314, 2163, 654, 16070, False
    THEMISTOCLES = 2315, 2360, 642, 16104, False
    LEONIDAS = 2316, 2109, 634, 16104, False
    BRASIDAS = 2317, 2359, 648, 416014, False
    LYSANDER = 2318, 2371, 635, 16104, False
    POLYCRITUS = 2319, -1, 640, 416012, False
    THEMISTOCLES_WARSHIP = 2339, -1, 642, 416008, False
    CLEON = 2346, 2106, 649, 16104, False
    DARIUS = 2347, 2303, 651, -1, False
