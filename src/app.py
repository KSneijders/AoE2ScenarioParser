import resources.settings as settings
from src.scenario_file import AoE2Scenario

# (Outdated)? AoE2Scenario explanation: http://dderevjanik.github.io/agescx/formatscx/#about-scenario

# Open file and remove the not compressed header
scenario = AoE2Scenario(settings.file.get("name"))


# Todo: Fix method
# scenario.write_data_progress(write_in_bytes=False)
scenario.write_file("hd", write_in_bytes=False)

# https://stackoverflow.com/questions/3122145/zlib-error-error-3-while-decompressing-incorrect-header-check/22310760#22310760
# deflateObj = zlib.compressobj(9, zlib.DEFLATED, -zlib.MAX_WBITS)
# compressed = deflateObj.compress(decompressed) + deflateObj.flush()
#