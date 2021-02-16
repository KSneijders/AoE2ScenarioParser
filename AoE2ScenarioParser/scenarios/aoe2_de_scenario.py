from AoE2ScenarioParser.scenarios.aoe2_scenario import AoE2Scenario


class AoE2DEScenario(AoE2Scenario):
    @classmethod
    def from_file(cls, filename):
        return super().from_file("DE", filename)
