from __future__ import annotations

from collections import OrderedDict

from AoE2ScenarioParser.helper.helper import SimpleLogger
from AoE2ScenarioParser.objects.map_obj import MapObject
from AoE2ScenarioParser.objects.triggers_obj import TriggersObject
from AoE2ScenarioParser.objects.units_obj import UnitsObject
from AoE2ScenarioParser.pieces.aoe2_file_part import AoE2FilePart


class AoE2ObjectManager:
    def __init__(self, parsed_header, parsed_data, log_parsing=True):
        # Todo: Create a piece holder object or something to simplify this process
        self.pieces: OrderedDict[str, AoE2FilePart] = OrderedDict(**parsed_header, **parsed_data)

        lgr = SimpleLogger(log_parsing)
        lgr.print("\nParsing pieces and structs to objects...")
        self.parsed_header = parsed_header
        self.parsed_data = parsed_data

        self.constructables = [
            MapObject,
            TriggersObject,
            UnitsObject,
        ]
        self.objects = {}

        for obj in self.constructables:
            lgr.print("\tParsing " + obj.__name__ + "...", replace=True)
            self.objects[obj.__name__] = obj._construct(self.pieces)
            lgr.print("\tParsing " + obj.__name__ + " finished successfully.", replace=True)
            lgr.print()

        lgr.print("Parsing pieces and structs to objects finished successfully.")

    def reconstruct(self, log_reconstructing=False):
        lgr = SimpleLogger(log_reconstructing)
        lgr.print("\nReconstructing pieces and structs from objects...")

        for obj in self.constructables:
            lgr.print("\tReconstructing " + obj.__name__ + "...", replace=True)
            self.objects[obj.__name__].commit(pieces=self.pieces)
            lgr.print("\tReconstructing " + obj.__name__ + " finished successfully.", replace=True)
            lgr.print()

        lgr.print("Reconstruction finished successfully.")
