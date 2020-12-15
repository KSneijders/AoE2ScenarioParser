from __future__ import annotations

from collections import OrderedDict

from AoE2ScenarioParser.helper import generator
from AoE2ScenarioParser.helper.helper import SimpleLogger
from AoE2ScenarioParser.helper.retriever import get_retriever_by_name
from AoE2ScenarioParser.objects.data_header_obj import DataHeaderObject
from AoE2ScenarioParser.objects.diplomacy_obj import DiplomacyObject
from AoE2ScenarioParser.objects.file_header_obj import FileHeaderObject
from AoE2ScenarioParser.objects.map_obj import MapObject
from AoE2ScenarioParser.objects.messages_obj import MessagesObject
from AoE2ScenarioParser.objects.options_obj import OptionsObject
from AoE2ScenarioParser.objects.player_object import PlayerObject
from AoE2ScenarioParser.objects.triggers_obj import TriggersObject
from AoE2ScenarioParser.objects.units_obj import UnitsObject
from AoE2ScenarioParser.pieces.aoe2_piece import AoE2Piece


class AoE2ObjectManager:
    def __init__(self, parsed_header, parsed_data, log_parsing=True):
        # Todo: Create a piece holder object or something to simplify this process
        self.pieces: OrderedDict[str, AoE2Piece] = OrderedDict(**parsed_header, **parsed_data)

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
            lgr.print("\tParsing " + obj.__name__ + "...", replace_line=True)
            self.objects[obj.__name__] = obj._construct(self.pieces)
            lgr.print("\tParsing " + obj.__name__ + " finished successfully.", replace_line=True)
            lgr.print()

        lgr.print("Parsing pieces and structs to objects finished successfully.")

        # self._objects = {
        #     # "FileHeaderObject": self._parse_file_header_object(),
        #     # "DataHeaderObject": self._parse_data_header_object(),
        #     # "PlayerObject": self._parse_player_object(),
        #     # "MessagesObject": self._parse_messages_object(),
        #     # "DiplomacyObject": self._parse_diplomacy_object(),
        #     # "OptionsObject": self._parse_options_object(),
        #     # "MapObject": self._parse_map_object(),
        #     "UnitsObject": UnitsObject.parse_object(self.parsed_data),
        #     "TriggersObject": TriggersObject.parse_object(self.parsed_data)
        # }

    def reconstruct(self, log_reconstructing=False):
        lgr = SimpleLogger(log_reconstructing)
        lgr.print("\nReconstructing pieces and structs from objects...")

        for obj in self.constructables:
            lgr.print("\tReconstructing " + obj.__name__ + "...", replace_line=True)
            self.objects[obj.__name__].commit(pieces=self.pieces)
            lgr.print("\tReconstructing " + obj.__name__ + " finished successfully.", replace_line=True)
            lgr.print()

        lgr.print("Reconstruction finished successfully.")

    # ################################################################################################ #
    #                           Todo: Move these functions to their objects.
    # ################################################################################################ #

    def _parse_options_object(self):
        object_piece = self.parsed_data['OptionsPiece']
        # ppnd: Per Player Number of Disabled
        ppnd_techs = get_retriever_by_name(object_piece.retrievers, "Per player number of disabled techs").data
        ppnd_units = get_retriever_by_name(object_piece.retrievers, "Per player number of disabled units").data
        ppnd_buildings = get_retriever_by_name(object_piece.retrievers, "Per player number of disabled buildings").data
        disabled_techs = generator.create_advanced_generator(
            get_retriever_by_name(object_piece.retrievers, "Disabled technology IDs in player order").data, 1
        )
        disabled_units = generator.create_advanced_generator(
            get_retriever_by_name(object_piece.retrievers, "Disabled unit IDs in player order").data, 1
        )
        disabled_buildings = generator.create_advanced_generator(
            get_retriever_by_name(object_piece.retrievers, "Disabled building IDs in player order").data, 1
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
            get_retriever_by_name(object_piece.retrievers, "All techs").data
        )

    def _parse_diplomacy_object(self):
        object_piece = self.parsed_data['DiplomacyPiece']
        diplomacy = get_retriever_by_name(object_piece.retrievers, "Per-player diplomacy").data

        diplomacies = []
        for player_id in range(0, 8):  # 0-7 Players
            diplomacies.append(get_retriever_by_name(diplomacy[player_id].retrievers, "Stance with each player").data)

        return DiplomacyObject(
            player_stances=diplomacies
        )

    def _parse_messages_object(self):
        object_piece = self.parsed_data['MessagesPiece']
        retrievers = object_piece.retrievers

        return MessagesObject(
            instructions=get_retriever_by_name(retrievers, "Instructions").data,
            hints=get_retriever_by_name(retrievers, "Hints").data,
            victory=get_retriever_by_name(retrievers, "Victory").data,
            loss=get_retriever_by_name(retrievers, "Loss").data,
            history=get_retriever_by_name(retrievers, "History").data,
            scouts=get_retriever_by_name(retrievers, "Scouts").data,
            ascii_instructions=get_retriever_by_name(retrievers, "ASCII Instructions").data,
            ascii_hints=get_retriever_by_name(retrievers, "ASCII Hints").data,
            ascii_victory=get_retriever_by_name(retrievers, "ASCII Victory").data,
            ascii_loss=get_retriever_by_name(retrievers, "ASCII Loss").data,
            ascii_history=get_retriever_by_name(retrievers, "ASCII History").data,
            ascii_scouts=get_retriever_by_name(retrievers, "ASCII Scouts").data,
        )

    def _parse_player_object(self):
        players = []

        data_header_piece = self.parsed_data['DataHeaderPiece']
        unit_piece = self.parsed_data['UnitsPiece']
        options_piece = self.parsed_data['OptionsPiece']
        starting_ages = get_retriever_by_name(options_piece.retrievers, "Per player starting age").data

        # Player Data >>> 0-7 Players & 8 Gaia <<<
        player_data_one = get_retriever_by_name(data_header_piece.retrievers, "Player data#1").data
        player_data_two = self.parsed_data['PlayerDataTwoPiece']
        resources = get_retriever_by_name(player_data_two.retrievers, "Resources").data
        # player_data_three = find_retriever(unit_piece.retrievers, "Player data #3").data
        player_data_four = get_retriever_by_name(unit_piece.retrievers, "Player data #4").data

        for player_id in range(0, 9):  # 0-7 Players & 8 Gaia:
            try:  # If gaia isn't saved. (PlayerDataThree and PlayerDataFour)
                pop_limit = get_retriever_by_name(player_data_four[player_id].retrievers, "Population limit").data
            except IndexError:
                pop_limit = -1

            players.append(PlayerObject(
                player_number=player_id,
                active=get_retriever_by_name(player_data_one[player_id].retrievers, "Active").data,
                human=get_retriever_by_name(player_data_one[player_id].retrievers, "Human").data,
                civilization=get_retriever_by_name(player_data_one[player_id].retrievers, "Civilization").data,
                gold=get_retriever_by_name(resources[player_id].retrievers, "Gold").data,
                wood=get_retriever_by_name(resources[player_id].retrievers, "Wood").data,
                food=get_retriever_by_name(resources[player_id].retrievers, "Food").data,
                stone=get_retriever_by_name(resources[player_id].retrievers, "Stone").data,
                color=get_retriever_by_name(resources[player_id].retrievers, "Player color").data,
                starting_age=starting_ages[player_id],
                pop_limit=pop_limit
            ))

        return players

    def _parse_data_header_object(self):
        object_piece = self.parsed_data['DataHeaderPiece']
        retrievers = object_piece.retrievers

        return DataHeaderObject(
            version=get_retriever_by_name(retrievers, "Version").data,
            filename=get_retriever_by_name(retrievers, "Filename").data
        )

    def _parse_file_header_object(self):
        object_piece = self.parsed_header['FileHeaderPiece']
        retrievers = object_piece.retrievers

        return FileHeaderObject(
            version=get_retriever_by_name(retrievers, "Version").data,
            timestamp=get_retriever_by_name(retrievers, "Timestamp of last save").data,
            instructions=get_retriever_by_name(retrievers, "Scenario instructions").data,
            player_count=get_retriever_by_name(retrievers, "Player count").data,
            creator_name=get_retriever_by_name(retrievers, "Creator name").data,
        )
