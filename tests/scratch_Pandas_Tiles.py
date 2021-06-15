import time
from AoE2ScenarioParser.helper.bytes_conversions import parse_bytes_to_val  # NOTE: edited!!
from AoE2ScenarioParser.helper.incremental_generator import IncrementalGenerator
from AoE2ScenarioParser.sections.terrain_struct import TerrainStruct
from AoE2ScenarioParser.sections.aoe2_struct_model import AoE2StructModel

map_size = 200
file_context = b'\x0f\x1a\xc6\xee\xcc\x10\x00' * 45668      # random
terrrain_struct_json = {
    "retrievers":{
        "terrain_id":{
            "type":"u8",
            "default":0
        },
        "elevation":{
            "type":"u8",
            "default":0
        },
        "unused":{
            "type":"3",
            "default":"00ffff"
        },
        "layer":{
            "type":"s16",
            "default":-1
        }
    }
}
terrainStructModel = AoE2StructModel.from_structure("terrain_struct", terrrain_struct_json)     # prepare model
igenerator = IncrementalGenerator('test', file_context, 0)
igenerator.get_bytes(350)   # random progress


start_time = time.time()
# Get all Tiles' source data (bytes).
terrainStruct = TerrainStruct(map_size, terrainStructModel)
terrainStruct.set_data_from_generator(igenerator)

end_time = time.time()
print(f"Time: {round(end_time - start_time, 3)} s")
