from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

_deprecation_msg = '\n'.join([
    "", "",
    "The AoE2Scenario class from AoE2ScenarioParser.aoe2_scenario is deprecated and will be removed in the future.",
    "Please use the AoE2DEScenario from AoE2ScenarioParser.scenarios.aoe2_de_scenario instead.",
    "Using:",
    "\tfrom AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario",
    "\tscenario = AoE2DEScenario.from_file(...)",
    "From:"
])


class AoE2Scenario:

    @staticmethod
    def from_file(filename) -> AoE2DEScenario:
        from warnings import warn
        warn(_deprecation_msg)
        return AoE2DEScenario.from_file(filename)
