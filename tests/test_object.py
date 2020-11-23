from __future__ import annotations

from AoE2ScenarioParser.aoe2_scenario import AoE2Scenario


class TestObject:
    scenario_folder: str
    file_name: str
    instance: TestObject

    def init_files(self):
        if not hasattr(self, "scenario_folder") or not hasattr(self, "file_name"):
            raise ValueError("Path and filename bv")
        default_scenario = AoE2Scenario.create_default()
        read_scenario = AoE2Scenario.from_file(f"{self.scenario_folder}{self.file_name}.aoe2scenario")
        return {
            'default': default_scenario,
            'read': read_scenario
        }

    @staticmethod
    def get_instance():
        if not hasattr(TestObject, "instance"):
            return TestObject()
        return TestObject.instance

    @staticmethod
    def init(scenario_folder="./", file_name="default_scx"):
        test_obj = TestObject()
        test_obj.scenario_folder = scenario_folder
        test_obj.file_name = file_name
        TestObject.instance = test_obj
