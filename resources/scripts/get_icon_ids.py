def main():
    import json

    from AoE2ScenarioParser.datasets.buildings import BuildingInfo
    from AoE2ScenarioParser.datasets.heroes import HeroInfo
    from AoE2ScenarioParser.datasets.other import OtherInfo
    from AoE2ScenarioParser.datasets.units import UnitInfo

    #
    # Written by Alian713
    #

    with open("./full.json") as file:
        dataset = json.load(file)

    _icon_ids = {}

    _unit_icon = {}
    for obj in UnitInfo:
        for unit in dataset["Civs"][0]["Units"]:
            if unit["ID"] == obj.ID:
                _unit_icon[str(obj.ID).split(".")[1]] = unit["IconID"]

    _icon_ids["_unit_icon"] = _unit_icon

    _building_icon = {}
    for obj in BuildingInfo:
        for unit in dataset["Civs"][0]["Units"]:
            if unit["ID"] == obj.ID:
                _building_icon[str(obj.ID).split(".")[1]] = unit["IconID"]

    _icon_ids["_building_icon"] = _building_icon

    # _gaia_unit_icon = {}
    # for obj in GaiaUnitId:
    #     for unit in dataset["Civs"][0]["Units"]:
    #         if unit["ID"] == obj:
    #             _gaia_unit_icon[str(obj).split(".")[1]] = unit["IconID"]
    #
    # _icon_ids["_gaia_unit_icon"] = _gaia_unit_icon

    # _gaia_building_icon = {}
    # for obj in GaiaBuildingId:
    #     for unit in dataset["Civs"][0]["Units"]:
    #         if unit["ID"] == obj:
    #             _gaia_building_icon[str(obj).split(".")[1]] = unit["IconID"]
    #
    # _icon_ids["_gaia_building_icon"] = _gaia_building_icon

    _unit_other = {}
    for obj in OtherInfo:
        for unit in dataset["Civs"][0]["Units"]:
            if unit["ID"] == obj.ID:
                _unit_other[str(obj.ID).split(".")[1]] = unit["IconID"]

    _icon_ids["_unit_other"] = _unit_other

    # _gaia_unit_other_icon = {}
    # for obj in GaiaUnitOtherId:
    #     for unit in dataset["Civs"][0]["Units"]:
    #         if unit["ID"] == obj:
    #             _gaia_unit_other_icon[str(obj).split(".")[1]] = unit["IconID"]
    #
    # _icon_ids["_gaia_unit_other_icon"] = _gaia_unit_other_icon

    _hero_icon = {}
    for obj in HeroInfo:
        for unit in dataset["Civs"][0]["Units"]:
            if unit["ID"] == obj.ID:
                _hero_icon[str(obj.ID).split(".")[1]] = unit["IconID"]

    _icon_ids["_hero_icon"] = _hero_icon

    with open("./icons.json", "w") as file:
        json.dump(_icon_ids, file, indent=4)

    # Change json to print Python code

    with open('./icons.json', 'r') as f:
        js = json.loads(f.read())

        for header in js:
            print(f"class {header}(IntEnum):")
            for key, v in js.get(header).items():
                print(f"    {key} = {v}")

            input("Press Enter to continue...")


if __name__ == '__main__':
    main()