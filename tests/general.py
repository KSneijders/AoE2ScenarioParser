from AoE2ScenarioParser.scenarios.aoe2_scenario import AoE2Scenario


def write_to_file(scx_type: str, scx: AoE2Scenario):
    scx.write_to_file(f"./results/{scx_type}/test_{scx_type[0]}_no_edits.aoe2scenario")


def read_ai_file(scx_name: str):
    scx = AoE2Scenario.from_file(scx_name)
    scx.write_to_file(f"./results/read/test_ai_file.aoe2scenario")
