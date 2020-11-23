from __future__ import annotations

from AoE2ScenarioParser.aoe2_scenario import AoE2Scenario


class TestObject:
    scenario_folder: str
    file_name: str
    instance: TestObject

    @classmethod
    def get_instance(cls, scenario_folder="", file_name="default_scx"):
        if not hasattr(TestObject, "instance"):
            test_obj = cls()
            test_obj.scenario_folder = scenario_folder
            test_obj.file_name = file_name
            TestObject.instance = test_obj
            return test_obj
        return TestObject.instance

    def init_files(self):
        default_scenario = AoE2Scenario.create_default()
        read_scenario = AoE2Scenario.from_file(f"{self.scenario_folder}{self.file_name}.aoe2scenario")
        return {
            'default': default_scenario,
            'read': read_scenario
        }
