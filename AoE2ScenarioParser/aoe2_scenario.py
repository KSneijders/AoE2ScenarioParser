import time

from AoE2ScenarioParser.helper.printers import warn
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

_deprecation_msg = '\n'.join([
    "", "",
    "The AoE2Scenario class from AoE2ScenarioParser.aoe2_scenario is deprecated and will be removed in the future.",
    "Please use the AoE2DEScenario from AoE2ScenarioParser.scenarios.aoe2_de_scenario instead.",
    "For other changes please check: https://github.com/KSneijders/AoE2ScenarioParser/blob/master/changelog.md",
    "Using:",
    "\tfrom AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario",
    "\tscenario = AoE2DEScenario.from_file(...)",
    ""
])


class AoE2Scenario:

    @staticmethod
    def from_file(filename) -> AoE2DEScenario:
        warn(_deprecation_msg)

        # Making sure there's time to see the warning.
        # Also good incentive to switch :)
        time.sleep(2)

        return AoE2DEScenario.from_file(filename)
