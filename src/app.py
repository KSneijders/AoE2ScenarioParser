import resources.settings as settings
from src.aoe2_scenario import AoE2Scenario

# (Outdated)? AoE2Scenario explanation: http://dderevjanik.github.io/agescx/formatscx/#about-scenario

# Open file and remove the not compressed header
scenario = AoE2Scenario(settings.file.get("name"))
