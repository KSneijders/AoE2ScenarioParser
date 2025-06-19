from AoE2ScenarioParser.datasets.effects import EffectId
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario


def main():
    dir = "/Users/mindaugasa/Applications/Age of Empires 2 Definitive Ed.app/Contents/SharedSupport/prefix/drive_c/users/Wineskin/Games/Age of Empires 2 DE/76561198027295783/resources/_common/scenario/t.aoe2scenario"
    scenario = AoE2DEScenario.from_file(dir)
    tm = scenario.trigger_manager
    triggers = tm.triggers
    scenario._debug_byte_structure_to_file("output.txt")
    ids = [int(e) for e in EffectId]
    for t in triggers:
        for e in t.effects:
            if e.effect_type >= 90:
                print(e.effect_type, e)
    # 90 - create decision
    # 98 - disable unit attackable
    # 99 - enable unit attackable
    # 100 - modify variable by variable
    # 101 - count units into variable

if __name__ == '__main__':
    main()