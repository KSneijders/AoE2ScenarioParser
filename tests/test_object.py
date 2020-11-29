from __future__ import annotations

from typing import Tuple, List, Callable

from AoE2ScenarioParser.aoe2_scenario import AoE2Scenario
from tests import general


class TestObject:
    scenario_folder: str
    file_name: str
    instance: TestObject

    def init_files(self):
        if not hasattr(self, "scenario_folder") or not hasattr(self, "file_name"):
            raise ValueError("Path and filename need to be initialised using TestObject.init()")
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


def print_section(name, section_length=90):
    f_length = len(name)
    half = int(section_length / 2) - int(f_length / 2) - 1
    print("\n" + "\n".join([
        "#" * section_length,
        f"{'#' * half} {name} {'#' * (half - (1 if f_length % 2 == 1 else 0))}",
        "#" * section_length,
    ]))


if __name__ == "__main__":
    change_default_scenarios_tests = [
        general.write_to_file
    ]
    other_scenarios_tests: List[Tuple[Callable, List[str]]] = [
        (general.read_ai_file, ["ai_scx.aoe2scenario"])
    ]

    TestObject.init("./source/")

    for test_function in change_default_scenarios_tests:
        print_section(test_function.__name__)
        scenarios = TestObject.get_instance().init_files()

        for key, scenario in scenarios.items():
            print_section(f"{test_function.__name__}->{key}", section_length=70)
            test_function(key, scenario)

    for function, scx_names in other_scenarios_tests:
        print_section(f"{function.__name__}")
        for name in scx_names:
            print_section(f"{function.__name__}->{name}", section_length=70)
            function(f"{TestObject.get_instance().scenario_folder}{name}")
