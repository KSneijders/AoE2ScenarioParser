from __future__ import annotations

from typing import List

from AoE2ScenarioParser.helper import generator
from AoE2ScenarioParser.helper.helper import SimpleLogger
from AoE2ScenarioParser.helper.retriever import find_retriever
from AoE2ScenarioParser.objects.triggers_obj import TriggersObject


class AoE2ObjectManager:
    def __init__(self, parser_header, parsed_data, log_parsing=True):
        lgr = SimpleLogger(should_log=log_parsing)
        lgr.print("\nParsing pieces and structs to objects...")
        self.parser_header = parser_header
        self.parsed_data = parsed_data
        self._objects = {}
        self._finished_new_structure = {
            "TriggersObject": TriggersObject
        }

        for key in self._finished_new_structure.keys():
            lgr.print("\tParsing " + key + "...")
            self._objects[key] = self._finished_new_structure[key]._parse_object(self.parsed_data)
            lgr.print("\tParsing " + key + " finished successfully.")

        lgr.print("Parsing pieces and structs to objects finished successfully.")

    @property
    def trigger_manager(self) -> TriggersObject:
        return self._objects['TriggersObject']

    def reconstruct(self, log_reconstructing=False):
        lgr = SimpleLogger(should_log=log_reconstructing)
        lgr.print("\nReconstructing pieces and structs from objects...")

        for key in self._finished_new_structure.keys():
            lgr.print("\tReconstructing " + key + "...")
            self._objects[key]._reconstruct_object(self.parser_header, self.parsed_data, self._objects)
            lgr.print("\tReconstructing " + key + " finished successfully.")

        lgr.print("Reconstruction finished successfully.")
