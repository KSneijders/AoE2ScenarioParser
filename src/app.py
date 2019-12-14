import resources.settings as settings
from src.scenario_file import AoE2Scenario

from src.pieces.player_data_three import PlayerDataThreePiece
from src.pieces.units import UnitsPiece
from src.pieces.background_image import BackgroundImagePiece
from src.pieces.cinematics import CinematicsPiece
from src.pieces.diplomacy import DiplomacyPiece
from src.pieces.disables import DisablesPiece
from src.pieces.global_victory import GlobalVictoryPiece
from src.pieces.map import MapPiece
from src.pieces.messages import MessagesPiece
from src.pieces.player_data_two import PlayerDataTwoPiece
from src.pieces.file_header import FileHeaderPiece
from src.pieces.data_header import DataHeaderPiece
from src.pieces.triggers import TriggerPiece

# (Outdated)? AoE2Scenario explanation: http://dderevjanik.github.io/agescx/formatscx/#about-scenario

# Open file and remove the not compressed header
scenario = AoE2Scenario(settings.file.get("name"))
header_generator = scenario.create_header_generator(settings.runtime.get("chunk_size"))
data_generator = scenario.create_data_generator(settings.runtime.get("chunk_size"))
parser = scenario.parser

header = FileHeaderPiece(parser)
header.set_data_from_generator(header_generator)
print(header)

data_header = DataHeaderPiece(parser)
data_header.set_data_from_generator(data_generator)
print(data_header)

messages = MessagesPiece(parser)
messages.set_data_from_generator(data_generator)
print(messages)

cinematics = CinematicsPiece(parser)
cinematics.set_data_from_generator(data_generator)
print(cinematics)

backgroundImage = BackgroundImagePiece(parser)
backgroundImage.set_data_from_generator(data_generator)
print(backgroundImage)

playerDataTwo = PlayerDataTwoPiece(parser)
playerDataTwo.set_data_from_generator(data_generator)
print(playerDataTwo)

globalVictory = GlobalVictoryPiece(parser)
globalVictory.set_data_from_generator(data_generator)
print(globalVictory)

diplomacyPiece = DiplomacyPiece(parser)
diplomacyPiece.set_data_from_generator(data_generator)
print(diplomacyPiece)

disablesPiece = DisablesPiece(parser)
disablesPiece.set_data_from_generator(data_generator)
print(disablesPiece)

map = MapPiece(parser)
map.set_data_from_generator(data_generator)
print(map)

units = UnitsPiece(parser)
units.set_data_from_generator(data_generator)
print(units)

playerDataThree = PlayerDataThreePiece(parser)
playerDataThree.set_data_from_generator(data_generator)
print(playerDataThree)

triggers = TriggerPiece(parser)
triggers.set_data_from_generator(data_generator)
print(triggers)

# Todo: Fix method
# scenario.write_data_progress(write_in_bytes=False)
scenario.write_file("hd", write_in_bytes=False)

# https://stackoverflow.com/questions/3122145/zlib-error-error-3-while-decompressing-incorrect-header-check/22310760#22310760
# deflateObj = zlib.compressobj(9, zlib.DEFLATED, -zlib.MAX_WBITS)
# compressed = deflateObj.compress(decompressed) + deflateObj.flush()
# print(compressed)
