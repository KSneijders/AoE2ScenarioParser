from binary_file_parser import Retriever

from AoE2ScenarioParser.sections import MapData, ScenarioSections


class MockScenarioSections(ScenarioSections):
    map_data: MapData         = Retriever(MapData, default_factory = lambda version: MapData(struct_ver = version, width = 5, height = 5))
