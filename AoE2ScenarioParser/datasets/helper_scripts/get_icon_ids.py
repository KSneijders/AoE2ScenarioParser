import json

from AoE2ScenarioParser.datasets.buildings import Building, GaiaBuilding
from AoE2ScenarioParser.datasets.heroes import Hero
from AoE2ScenarioParser.datasets.other import GaiaUnitOther
from AoE2ScenarioParser.datasets.units import Unit, GaiaUnit


#
# Written by Alian713
#


with open("./full.json") as file:
    dataset = json.load(file)

iconIDs = {}

UnitIcon = {}
for obj in Unit:
    for unit in dataset["Civs"][0]["Units"]:
        if unit["ID"] == obj:
            UnitIcon[str(obj).split(".")[1]] = unit["IconID"]

iconIDs["UnitIcon"] = UnitIcon

BuildingIcon = {}
for obj in Building:
    for unit in dataset["Civs"][0]["Units"]:
        if unit["ID"] == obj:
            BuildingIcon[str(obj).split(".")[1]] = unit["IconID"]

iconIDs["BuildingIcon"] = BuildingIcon

GaiaUnitIcon = {}
for obj in GaiaUnit:
    for unit in dataset["Civs"][0]["Units"]:
        if unit["ID"] == obj:
            GaiaUnitIcon[str(obj).split(".")[1]] = unit["IconID"]

iconIDs["GaiaUnitIcon"] = GaiaUnitIcon

GaiaBuildingIcon = {}
for obj in GaiaBuilding:
    for unit in dataset["Civs"][0]["Units"]:
        if unit["ID"] == obj:
            GaiaBuildingIcon[str(obj).split(".")[1]] = unit["IconID"]

iconIDs["GaiaBuildingIcon"] = GaiaBuildingIcon

UnitOther = {}
for obj in UnitOther:
    for unit in dataset["Civs"][0]["Units"]:
        if unit["ID"] == obj:
            UnitOther[str(obj).split(".")[1]] = unit["IconID"]

iconIDs["UnitOther"] = UnitOther

GaiaUnitOtherIcon = {}
for obj in GaiaUnitOther:
    for unit in dataset["Civs"][0]["Units"]:
        if unit["ID"] == obj:
            GaiaUnitOtherIcon[str(obj).split(".")[1]] = unit["IconID"]

iconIDs["GaiaUnitOtherIcon"] = GaiaUnitOtherIcon

HeroIcon = {}
for obj in Hero:
    for unit in dataset["Civs"][0]["Units"]:
        if unit["ID"] == obj:
            HeroIcon[str(obj).split(".")[1]] = unit["IconID"]

iconIDs["HeroIcon"] = HeroIcon

with open("./icons.json", "w") as file:
    json.dump(iconIDs, file, indent=4)


# Change json to print Python code


with open('icons.json', 'r') as f:
    js = json.loads(f.read())

    for header in js:
        print(f"class {header}(IntEnum):")
        for k, v in js.get(header).items():
            print(f"    {k} = {v}")

        input("Press Enter to continue...")