from __future__ import annotations

from typing import List

from AoE2ScenarioParser.helper import generator
from AoE2ScenarioParser.helper.helper import SimpleLogger
from AoE2ScenarioParser.helper.retriever import find_retriever
from AoE2ScenarioParser.objects.file_header_obj import FileHeaderObject
from AoE2ScenarioParser.objects.options_obj import OptionsObject
from AoE2ScenarioParser.objects.player_object import PlayerObject
from AoE2ScenarioParser.objects.triggers_obj import TriggersObject
from AoE2ScenarioParser.objects.units_obj import UnitsObject


class AoE2ObjectManager:
    def __init__(self, parser_header, parsed_data, log_parsing=True):
        lgr = SimpleLogger(should_log=log_parsing)
        lgr.print("\nParsing pieces and structs to objects...")
        self.parser_header = parser_header
        self.parsed_data = parsed_data
        self._objects = {}
        self._finished_new_structure = {
            "UnitsObject": UnitsObject,
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

    @property
    def unit_manager(self) -> UnitsObject:
        return self._objects['UnitsObject']

    def reconstruct(self, log_reconstructing=False):
        lgr = SimpleLogger(should_log=log_reconstructing)
        lgr.print("\nReconstructing pieces and structs from objects...")

        for key in self._finished_new_structure.keys():
            lgr.print("\tReconstructing " + key + "...")
            self._objects[key]._reconstruct_object(self.parser_header, self.parsed_data, self._objects)
            lgr.print("\tReconstructing " + key + " finished successfully.")

        lgr.print("Reconstruction finished successfully.")

    # ################################################################################################ #
    #                           Todo: Move these functions to their objects.
    # ################################################################################################ #

    def _parse_options_object(self):
        object_piece = self.parsed_data['OptionsPiece']
        # ppnd: Per Player Number of Disabled
        ppnd_techs = find_retriever(object_piece.retrievers, "Per player number of disabled techs").data
        ppnd_units = find_retriever(object_piece.retrievers, "Per player number of disabled units").data
        ppnd_buildings = find_retriever(object_piece.retrievers, "Per player number of disabled buildings").data
        disabled_techs = generator.create_generator(
            find_retriever(object_piece.retrievers, "Disabled technology IDs in player order").data, 1
        )
        disabled_units = generator.create_generator(
            find_retriever(object_piece.retrievers, "Disabled unit IDs in player order").data, 1
        )
        disabled_buildings = generator.create_generator(
            find_retriever(object_piece.retrievers, "Disabled building IDs in player order").data, 1
        )

        disables = list()
        for player_id in range(0, 8):  # 0-7 Players
            nd_techs = ppnd_techs[player_id]
            nd_units = ppnd_units[player_id]
            nd_buildings = ppnd_buildings[player_id]
            player_disabled_techs = generator.repeat_generator(
                disabled_techs, nd_techs, return_bytes=False)
            player_disabled_units = generator.repeat_generator(
                disabled_units, nd_units, return_bytes=False)
            player_disabled_buildings = generator.repeat_generator(
                disabled_buildings, nd_buildings, return_bytes=False)

            disables.append({
                'techs': player_disabled_techs,
                'units': player_disabled_units,
                'buildings': player_disabled_buildings,
            })

        return OptionsObject(
            disables,
            find_retriever(object_piece.retrievers, "All techs").data
        )

    def _parse_player_object(self):
        players = []

        data_header_piece = self.parsed_data['DataHeaderPiece']
        unit_piece = self.parsed_data['UnitsPiece']
        options_piece = self.parsed_data['OptionsPiece']
        starting_ages = find_retriever(options_piece.retrievers, "Per player starting age").data

        # Player Data
        player_data_one = find_retriever(data_header_piece.retrievers, "Player data#1").data  # 0-7 Players & 8 Gaia
        player_data_two = self.parsed_data['PlayerDataTwoPiece']  # 0-7 Players & 8 Gaia
        resources = find_retriever(player_data_two.retrievers, "Resources").data
        # player_data_three = find_retriever(unit_piece.retrievers, "Player data #3").data  # 0-7 Players
        player_data_four = find_retriever(unit_piece.retrievers, "Player data #4").data  # 0-7 Players

        for player_id in range(0, 9):  # 0-7 Players & 8 Gaia:
            try:  # If gaia isn't saved. (PlayerDataThree and PlayerDataFour)
                pop_limit = find_retriever(player_data_four[player_id].retrievers, "Population limit").data
            except IndexError:
                pop_limit = -1

            players.append(PlayerObject(
                player_number=player_id,
                active=find_retriever(player_data_one[player_id].retrievers, "Active").data,
                human=find_retriever(player_data_one[player_id].retrievers, "Human").data,
                civilization=find_retriever(player_data_one[player_id].retrievers, "Civilization").data,
                gold=find_retriever(resources[player_id].retrievers, "Gold").data,
                wood=find_retriever(resources[player_id].retrievers, "Wood").data,
                food=find_retriever(resources[player_id].retrievers, "Food").data,
                stone=find_retriever(resources[player_id].retrievers, "Stone").data,
                color=find_retriever(resources[player_id].retrievers, "Player color").data,
                starting_age=starting_ages[player_id],
                pop_limit=pop_limit
            ))

        return players

    def _parse_file_header_object(self):
        object_piece = self.parser_header['FileHeaderPiece']
        retrievers = object_piece.retrievers

        return FileHeaderObject(
            version=find_retriever(retrievers, "Version").data,
            timestamp=find_retriever(retrievers, "Timestamp of last save").data,
            instructions=find_retriever(retrievers, "Scenario instructions").data,
            player_count=find_retriever(retrievers, "Player count").data,
            creator_name=find_retriever(retrievers, "Creator name").data,
        )
