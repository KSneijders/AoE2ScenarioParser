from enum import IntEnum

from bidict import bidict


class Hero(IntEnum):
    LIEF_ERIKSON = 106
    RICHARD_THE_LIONHEART = 160
    THE_BLACK_PRINCE = 161
    FRIAR_TUCK = 163
    SHERIFF_OF_NOTTINGHAM = 164
    CHARLEMAGNE = 165
    ROLAND = 166
    BELISARIUS = 167
    THEODORIC_THE_GOTH = 168
    AETHELFRITH = 169
    SIEGFRIED = 170
    ERIK_THE_RED = 171
    TAMERLANE = 172
    KING_ARTHUR = 173
    LANCELOT = 174
    GAWAIN = 175
    MORDRED = 176
    ARCHBISHOP = 177
    VLAD_DRACULA = 193
    KITABATAKE = 195
    MINAMOTO = 196
    ALEXANDER_NEVSKI = 197
    EL_CID = 198
    ROBIN_HOOD = 200
    VASCO_DA_GAMA = 203
    ALARIC_THE_GOTH = 223
    KING_BELA_IV = 230
    CUAUHTEMOC = 307
    HENRY_THE_LION = 418
    CHARLES_MARTEL = 424
    FRANCISCO_DE_ORELLANA = 425
    HAROLD_HARDRADA = 426
    GONZALO_PIZARRO = 427
    HROLF_THE_GANGER = 428
    FREDERICK_BARBAROSSA = 429
    JOAN_THE_MAID = 430
    WILLIAM_WALLACE = 432
    PRITHVIRAJ = 437
    FRANCESCO_SFORZA = 439
    ATAULF = 453
    JOAN_OF_ARC = 629
    FRANKISH_PALADIN = 632
    SIEUR_DE_METZ = 634
    SIEUR_BERTRAND = 636
    DUKE_D_ALENASONN = 638
    LA_HIRE = 640
    LORD_DE_GRAVILLE = 642
    JEAN_DE_LORRAIN = 644
    CONSTABLE_RICHEMONT = 646
    GUY_JOSSELYNE = 648
    JEAN_BUREAU = 650
    SIR_JOHN_FASTOLF = 652
    REYNALD_DE_CHATILLON = 678
    MASTER_OF_THE_TEMPLAR = 680
    BAD_NEIGHBOR = 682
    GODS_OWN_SLING = 683
    ARCHER_OF_THE_EYES = 686
    SUBOTAI = 698
    HUNTING_WOLF = 700
    KUSHLUK = 702
    TOPA_YUPANQUI = 703
    SHAH = 704
    SABOTEUR = 706
    ORNLU_THE_WOLF = 707
    GODS_OWN_SLING_PACKED = 729
    BAD_NEIGHBOR_PACKED = 730
    GENGHIS_KHAN = 731
    EMPEROR_IN_A_BARREL = 733
    CUSI_YUPANQUI = 749
    ATTILA_THE_HUN = 777
    BLEDA_THE_HUN = 779
    POPE_LEO_I = 781
    SCYTHIAN_WILD_WOMAN = 783
    EL_CID_CAMPEADOR = 824
    KING_SANCHO = 838
    KING_ALFONSO = 840
    IMAM = 842
    ADMIRAL_YI_SUN_SHIN = 844
    NOBUNAGA = 845
    HENRY_V = 847
    WILLIAM_THE_CONQUEROR = 849
    SCYTHIAN_SCOUT = 852
    MUSA_IBN_NUSAYR = 1034
    SUNDJATA = 1035
    TARIQ_IBN_ZIYAD = 1036
    RICHARD_DE_CLARE = 1037
    TRISTAN = 1038
    PRINCESS_YODIT = 1039
    HENRY_II = 1040
    YEKUNA_AMLAK = 1064
    YODIT = 1066
    ITZCOATL = 1067
    MUSTAFA_PASHA = 1068
    PACAL_II = 1069
    BABUR = 1070
    ABRAHA_ELEPHANT = 1071
    GUGLIELMO_EMBRIACO = 1072
    SU_DINGFANG = 1073
    PACHACUTI = 1074
    HUAYNA_CAPAC = 1075
    MIKLOS_TOLDI = 1076
    LITTLE_JOHN = 1077
    ZAWISZA_THE_BLACK = 1078
    SUMANGURU = 1080
    DAGNAJAN = 1106
    GIDAJAN = 1109
    GAJAH_MADA = 1157
    JAYANEGARA = 1158
    RADEN_WIJAYA = 1159
    SUNDA_ROYAL_FIGHTER = 1160
    SURYAVARMAN_I = 1162
    UDAYADITYAVARMAN_I = 1163
    JAYAVIRAVARMAN = 1164
    BAYINNAUNG = 1165
    TABINSHWEHTI = 1166
    LE_LOI = 1178
    LE_LAI = 1180
    LE_TRIEN = 1181
    LUU_NHAN_CHU = 1182
    BUI_BI = 1183
    DINH_LE = 1184
    WANG_TONG = 1185
    ENVOY = 1186
    TOKHTAMYSH_KHAN = 1262
    IVAYLO = 1265
    TSAR_KONSTANTIN = 1266
    KOTYAN_KHAN = 1267
    CUMAN_CHIEF = 1268
    GIRGEN_KHAN = 1269
    URUS_KHAN = 1276
    VYTAUTAS_THE_GREAT = 1281
    IVAYLO_DISMOUNTED = 1290
    SANYOGITA = 1293
    PRITHVI = 1294
    CHAND_BARDAI = 1295
    SALADIN = 1296
    KHOSRAU = 1297
    JARL = 1298
    SAVAR = 1299
    OSMAN = 1303
    MOUNTED_SAMURAI = 1568
    SOSSO_GUARD = 1574
    THE_MIDDLEBROOK = 1631


hero_names = bidict({
    106: "lief_erikson",
    160: "richard_the_lionheart",
    161: "the_black_prince",
    163: "friar_tuck",
    164: "sheriff_of_nottingham",
    165: "charlemagne",
    166: "roland",
    167: "belisarius",
    168: "theodoric_the_goth",
    169: "aethelfrith",
    170: "siegfried",
    171: "erik_the_red",
    172: "tamerlane",
    173: "king_arthur",
    174: "lancelot",
    175: "gawain",
    176: "mordred",
    177: "archbishop",
    193: "vlad_dracula",
    195: "kitabatake",
    196: "minamoto",
    197: "alexander_nevski",
    198: "el_cid",
    200: "robin_hood",
    203: "vasco_da_gama",
    223: "alaric_the_goth",
    230: "king_bela_iv",
    307: "cuauhtemoc",
    418: "henry_the_lion",
    424: "charles_martel",
    425: "francisco_de_orellana",
    426: "harold_hardrada",
    427: "gonzalo_pizarro",
    428: "hrolf_the_ganger",
    429: "frederick_barbarossa",
    430: "joan_the_maid",
    432: "william_wallace",
    437: "prithviraj",
    439: "francesco_sforza",
    453: "ataulf",
    629: "joan_of_arc",
    632: "frankish_paladin",
    634: "sieur_de_metz",
    636: "sieur_bertrand",
    638: "duke_d'alenã§onn",
    640: "la_hire",
    642: "lord_de_graville",
    644: "jean_de_lorrain",
    646: "constable_richemont",
    648: "guy_josselyne",
    650: "jean_bureau",
    652: "sir_john_fastolf",
    678: "reynald_de_chatillon",
    680: "master_of_the_templar",
    682: "bad_neighbor",
    683: "god's_own_sling",
    686: "archer_of_the_eyes",
    698: "subotai",
    700: "hunting_wolf",
    702: "kushluk",
    703: "topa_yupanqui",
    704: "shah",
    706: "saboteur",
    707: "ornlu_the_wolf",
    729: "god's_own_sling_(packed)",
    730: "bad_neighbor_(packed)",
    731: "genghis_khan",
    733: "emperor_in_a_barrel",
    749: "cusi_yupanqui",
    777: "attila_the_hun",
    779: "bleda_the_hun",
    781: "pope_leo_i",
    783: "scythian_wild_woman",
    824: "el_cid_campeador",
    838: "king_sancho",
    840: "king_alfonso",
    842: "imam",
    844: "admiral_yi_sun-shin",
    845: "nobunaga",
    847: "henry_v",
    849: "william_the_conqueror",
    852: "scythian_scout",
    1034: "musa_ibn_nusayr",
    1035: "sundjata",
    1036: "tariq_ibn_ziyad",
    1037: "richard_de_clare",
    1038: "tristan",
    1039: "princess_yodit",
    1040: "henry_ii",
    1064: "yekuna_amlak",
    1066: "yodit",
    1067: "itzcoatl",
    1068: "mustafa_pasha",
    1069: "pacal_ii",
    1070: "babur",
    1071: "abraha_elephant",
    1072: "guglielmo_embriaco",
    1073: "su_dingfang",
    1074: "pachacuti",
    1075: "huayna_capac",
    1076: "miklos_toldi",
    1077: "little_john",
    1078: "zawisza_the_black",
    1080: "sumanguru",
    1106: "dagnajan",
    1109: "gidajan",
    1157: "gajah_mada",
    1158: "jayanegara",
    1159: "raden_wijaya",
    1160: "sunda_royal_fighter",
    1162: "suryavarman_i",
    1163: "udayadityavarman_i",
    1164: "jayaviravarman",
    1165: "bayinnaung",
    1166: "tabinshwehti",
    1178: "le_loi",
    1180: "le_lai",
    1181: "le_trien",
    1182: "luu_nhan_chu",
    1183: "bui_bi",
    1184: "dinh_le",
    1185: "wang_tong",
    1186: "envoy",
    1262: "tokhtamysh_khan",
    1265: "ivaylo",
    1266: "tsar_konstantin",
    1267: "kotyan_khan",
    1268: "cuman_chief",
    1269: "girgen_khan",
    1276: "urus_khan",
    1281: "vytautas_the_great",
    1290: "ivaylo_dismounted",
    1293: "sanyogita",
    1294: "prithvi",
    1295: "chand_bardai",
    1296: "saladin",
    1297: "khosrau",
    1298: "jarl",
    1299: "savar",
    1303: "osman",
    1568: "mounted_samurai",
    1574: "sosso_guard",
    1631: "the_middlebrook",
})
