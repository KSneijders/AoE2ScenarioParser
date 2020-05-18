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
    IVAYLO = 1290
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
    106: "Lief Erikson",
    160: "Richard the Lionheart",
    161: "The Black Prince",
    163: "Friar Tuck",
    164: "Sheriff of Nottingham",
    165: "Charlemagne",
    166: "Roland",
    167: "Belisarius",
    168: "Theodoric the Goth",
    169: "Aethelfrith",
    170: "Siegfried",
    171: "Erik the Red",
    172: "Tamerlane",
    173: "King Arthur",
    174: "Lancelot",
    175: "Gawain",
    176: "Mordred",
    177: "Archbishop",
    193: "Vlad Dracula",
    195: "Kitabatake",
    196: "Minamoto",
    197: "Alexander Nevski",
    198: "El Cid",
    200: "Robin Hood",
    203: "Vasco da Gama",
    223: "Alaric the Goth",
    230: "King Bela IV",
    307: "Cuauhtemoc",
    418: "Henry the Lion",
    424: "Charles Martel",
    425: "Francisco de Orellana",
    426: "Harold Hardrada",
    427: "Gonzalo Pizarro",
    428: "Hrolf the Ganger",
    429: "Frederick Barbarossa",
    430: "Joan the Maid",
    432: "William Wallace",
    437: "Prithviraj",
    439: "Francesco Sforza",
    453: "Ataulf",
    629: "Joan of Arc",
    632: "Frankish Paladin",
    634: "Sieur de Metz",
    636: "Sieur Bertrand",
    638: "Duke D'AlenÃ§onn",
    640: "La Hire",
    642: "Lord de Graville",
    644: "Jean de Lorrain",
    646: "Constable Richemont",
    648: "Guy Josselyne",
    650: "Jean Bureau",
    652: "Sir John Fastolf",
    678: "Reynald de Chatillon",
    680: "Master of the Templar",
    682: "Bad Neighbor",
    683: "God's Own Sling",
    686: "Archer of the Eyes",
    698: "Subotai",
    700: "Hunting Wolf",
    702: "Kushluk",
    703: "Topa Yupanqui",
    704: "Shah",
    706: "Saboteur",
    707: "Ornlu the Wolf",
    729: "God's Own Sling (Packed)",
    730: "Bad Neighbor (Packed)",
    731: "Genghis Khan",
    733: "Emperor in a Barrel",
    749: "Cusi Yupanqui",
    777: "Attila the Hun",
    779: "Bleda the Hun",
    781: "Pope Leo I",
    783: "Scythian Wild Woman",
    824: "El Cid Campeador",
    838: "King Sancho",
    840: "King Alfonso",
    842: "Imam",
    844: "Admiral Yi Sun-shin",
    845: "Nobunaga",
    847: "Henry V",
    849: "William the Conqueror",
    852: "Scythian Scout",
    1034: "Musa ibn Nusayr",
    1035: "Sundjata",
    1036: "Tariq ibn Ziyad",
    1037: "Richard de Clare",
    1038: "Tristan",
    1039: "Princess Yodit",
    1040: "Henry II",
    1064: "Yekuna Amlak",
    1066: "Yodit",
    1067: "Itzcoatl",
    1068: "Mustafa Pasha",
    1069: "Pacal II",
    1070: "Babur",
    1071: "Abraha Elephant",
    1072: "Guglielmo Embriaco",
    1073: "Su Dingfang",
    1074: "Pachacuti",
    1075: "Huayna Capac",
    1076: "Miklos Toldi",
    1077: "Little John",
    1078: "Zawisza the Black",
    1080: "Sumanguru",
    1106: "Dagnajan",
    1109: "Gidajan",
    1157: "Gajah Mada",
    1158: "Jayanegara",
    1159: "Raden Wijaya",
    1160: "Sunda Royal Fighter",
    1162: "Suryavarman I",
    1163: "Udayadityavarman I",
    1164: "Jayaviravarman",
    1165: "Bayinnaung",
    1166: "Tabinshwehti",
    1178: "Le Loi",
    1180: "Le Lai",
    1181: "Le Trien",
    1182: "Luu Nhan Chu",
    1183: "Bui Bi",
    1184: "Dinh Le",
    1185: "Wang Tong",
    1186: "Envoy",
    1262: "Tokhtamysh Khan",
    1265: "Ivaylo",
    1266: "Tsar Konstantin",
    1267: "Kotyan Khan",
    1268: "Cuman Chief",
    1269: "Girgen Khan",
    1276: "Urus Khan",
    1281: "Vytautas the Great",
    # 1290: "Ivaylo",  Todo: 2 same names?
    1293: "Sanyogita",
    1294: "Prithvi",
    1295: "Chand Bardai",
    1296: "Saladin",
    1297: "Khosrau",
    1298: "Jarl",
    1299: "Savar",
    1303: "Osman",
    1568: "Mounted Samurai",
    1574: "Sosso Guard",
    1631: "The Middlebrook",
})