from binary_file_parser import BaseStruct, Retriever

from AoE2ScenarioParser.sections import MapData, Settings


class MockScxSecTestMM(BaseStruct):
    settings: Settings        = Retriever(Settings, default_factory = Settings)
    map_data: MapData         = Retriever(MapData,  default_factory = lambda version: MapData(version, width = 5, height = 5))
