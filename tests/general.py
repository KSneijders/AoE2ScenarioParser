from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario


def write_to_file(scx_type: str, scx: AoE2DEScenario):
    scx.write_to_file(f"./results/{scx_type}/test_{scx_type[0]}_no_edits.aoe2scenario")


def read_ai_file(scx_name: str):
    scx = AoE2DEScenario.from_file(scx_name)
    scx.write_to_file(f"./results/read/test_ai_file.aoe2scenario")
