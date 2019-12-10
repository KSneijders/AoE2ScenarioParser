import resources.settings as settings
from src.pieces.messagespiece import MessagesPiece
from src.scenario_file import AoE2Scenario
from src.pieces.file_header import FileHeaderPiece
from src.pieces.data_header import DataHeaderPiece

# (Outdated)? AoE2Scenario explanation: http://dderevjanik.github.io/agescx/formatscx/#about-scenario

# Open file and remove the not compressed header
scenario = AoE2Scenario(settings.file.get("name"))
header_generator = scenario.create_header_generator(settings.runtime.get("chunk_size"))
data_generator = scenario.create_data_generator(settings.runtime.get("chunk_size"))

header = FileHeaderPiece()
header.set_data_from_generator(header_generator)
print(header)

data_header = DataHeaderPiece()
data_header.set_data_from_generator(data_generator)
print(data_header)

messages = MessagesPiece()
messages.set_data_from_generator(data_generator)
print(messages)

scenario.write_data_progress()
scenario.write_file("d", write_in_bytes=False)

# print("\nFile Data Header:")
# print("\tNext unit ID to place:", retrieve_value(data_generator, "u32"))
# print("\tVersion 2:", retrieve_value(data_generator, "f32"))
# print("\tASCII player names:", retrieve_value(data_generator, "256", repeat=16))
# print("\tstring table player names:", retrieve_value(data_generator, "u32", repeat=16))
# print("\tPlayer Data#1 see sub-struct below:", retrieve_value(data_generator, "16", repeat=16))
# print("\tConquest Mode:", retrieve_value(data_generator, "u8"))
# missionItems = retrieve_value(data_generator, "u16")
# print("\tMission Items Counter:", missionItems)
# print("\tMission Available:", retrieve_value(data_generator, "u16"))
# print("\tMission Timeline:", retrieve_value(data_generator, "f32"))
# print("\tMission Item (each 30 bytes):", retrieve_value(data_generator, "30", repeat=missionItems))
# print("\tOriginal filename, created while first scenario save:", retrieve_value(data_generator, "str16"))
#
# print("\nPlayer Data#1:")
# print("\tBoolean: Active:", retrieve_value(data_generator, "u32"))
# print("\tBoolean: Human:", retrieve_value(data_generator, "u32"))
# print("\tCivilization, see IDs at this document:", retrieve_value(data_generator, "u32"))
# print("\tCTY Mode1:", retrieve_value(data_generator, "u32"))

# print("\nMessages:")
# print("\tString table, Instructions:", retrieve_value(data_generator, "u32"))
# print("\tString table, Hints:", retrieve_value(data_generator, "u32"))
# print("\tString table, Victory:", retrieve_value(data_generator, "u32"))
# print("\tString table, Loss:", retrieve_value(data_generator, "u32"))
# print("\tString table, History:", retrieve_value(data_generator, "u32"))
# print("\tString table, Scouts:", retrieve_value(data_generator, "u32"))
# print("\tASCII, Instructions:", retrieve_value(data_generator, "str16"))
# print("\tASCII, Hints:", retrieve_value(data_generator, "str16"))
# print("\tASCII, Victory:", retrieve_value(data_generator, "str16"))
# print("\tASCII, Loss:", retrieve_value(data_generator, "str16"))
# print("\tASCII, History:", retrieve_value(data_generator, "str16"))
# print("\tASCII, Scouts:", retrieve_value(data_generator, "str16"))

# https://stackoverflow.com/questions/3122145/zlib-error-error-3-while-decompressing-incorrect-header-check/22310760#22310760
# deflateObj = zlib.compressobj(9, zlib.DEFLATED, -zlib.MAX_WBITS)
# compressed = deflateObj.compress(decompressed) + deflateObj.flush()
# print(compressed)
