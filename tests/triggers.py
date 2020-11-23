from AoE2ScenarioParser.aoe2_scenario import AoE2Scenario
from tests.test_object import TestObject


def write_to_file(key: str, scx: AoE2Scenario):
    scx.write_to_file(f"./results/{key}/{key[0]}_no_edits.aoe2scenario")


if __name__ == "__main__":
    tests = [
        write_to_file
    ]

    for test_function in tests:
        scenarios = TestObject.get_instance().init_files()

        for key, scenario in scenarios.items():
            test_function(key, scenario)
