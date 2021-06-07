from __future__ import annotations

from typing import List

from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.data_objects.player_data import PlayerFeatures, PlayerResourcesColor, PlayerAIFileText,\
    PlayerMiscSettings, PlayerResources2Population, PlayerDiplomacy
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink


class PlayerManager(AoE2Object):
    """Manager of the everything player related."""

    _link_list = [
        RetrieverObjectLink("player_count", "FileHeader", "player_count"),

        RetrieverObjectLink("_player_names", "DataHeader", "player_names"),
        RetrieverObjectLink("_player_names_string_table", "DataHeader", "string_table_player_names"),

        RetrieverObjectLink("_players_features", "DataHeader", "player_data_1", process_as_object=PlayerFeatures),
        RetrieverObjectLink("players_misc_settings", "Units", "player_data_3", process_as_object=PlayerMiscSettings),

        RetrieverObjectLink("_players_resources_color", "PlayerDataTwo", "resources",
                            process_as_object=PlayerResourcesColor),
        RetrieverObjectLink("players_resources2_population", "Units", "player_data_4",
                            process_as_object=PlayerResources2Population),

        RetrieverObjectLink("_ai_files_names", "PlayerDataTwo", "ai_names"),
        RetrieverObjectLink("_ai_files_texts", "PlayerDataTwo", "ai_files", process_as_object=PlayerAIFileText),
        RetrieverObjectLink("_ai_types", "PlayerDataTwo", "ai_type"),

        RetrieverObjectLink("_diplomacies", "Diplomacy", "per_player_diplomacy",
                            process_as_object=PlayerDiplomacy),
        RetrieverObjectLink("_allied_victories", "Diplomacy", "per_player_allied_victory"),
        RetrieverObjectLink("_starting_ages", "Options", "per_player_starting_age"),
        RetrieverObjectLink("_individual_victories", "Diplomacy", "individual_victories"),

        RetrieverObjectLink("_disabled_techs_p1", "Options", "disabled_tech_ids_player_1"),
        RetrieverObjectLink("_disabled_techs_p2", "Options", "disabled_tech_ids_player_2"),
        RetrieverObjectLink("_disabled_techs_p3", "Options", "disabled_tech_ids_player_3"),
        RetrieverObjectLink("_disabled_techs_p4", "Options", "disabled_tech_ids_player_4"),
        RetrieverObjectLink("_disabled_techs_p5", "Options", "disabled_tech_ids_player_5"),
        RetrieverObjectLink("_disabled_techs_p6", "Options", "disabled_tech_ids_player_6"),
        RetrieverObjectLink("_disabled_techs_p7", "Options", "disabled_tech_ids_player_7"),
        RetrieverObjectLink("_disabled_techs_p8", "Options", "disabled_tech_ids_player_8"),
        RetrieverObjectLink("_disabled_buildings_p1", "Options", "disabled_building_ids_player_1"),
        RetrieverObjectLink("_disabled_buildings_p2", "Options", "disabled_building_ids_player_2"),
        RetrieverObjectLink("_disabled_buildings_p3", "Options", "disabled_building_ids_player_3"),
        RetrieverObjectLink("_disabled_buildings_p4", "Options", "disabled_building_ids_player_4"),
        RetrieverObjectLink("_disabled_buildings_p5", "Options", "disabled_building_ids_player_5"),
        RetrieverObjectLink("_disabled_buildings_p6", "Options", "disabled_building_ids_player_6"),
        RetrieverObjectLink("_disabled_buildings_p7", "Options", "disabled_building_ids_player_7"),
        RetrieverObjectLink("_disabled_buildings_p8", "Options", "disabled_building_ids_player_8"),
        RetrieverObjectLink("_disabled_units_p1", "Options", "disabled_unit_ids_player_1"),
        RetrieverObjectLink("_disabled_units_p2", "Options", "disabled_unit_ids_player_2"),
        RetrieverObjectLink("_disabled_units_p3", "Options", "disabled_unit_ids_player_3"),
        RetrieverObjectLink("_disabled_units_p4", "Options", "disabled_unit_ids_player_4"),
        RetrieverObjectLink("_disabled_units_p5", "Options", "disabled_unit_ids_player_5"),
        RetrieverObjectLink("_disabled_units_p6", "Options", "disabled_unit_ids_player_6"),
        RetrieverObjectLink("_disabled_units_p7", "Options", "disabled_unit_ids_player_7"),
        RetrieverObjectLink("_disabled_units_p8", "Options", "disabled_unit_ids_player_8")
    ]

    def __init__(self,
                 player_count: int,
                 _player_names: List[str],
                 _player_names_string_table: List[int],
                 _players_features: List[PlayerFeatures],
                 players_misc_settings: List[PlayerMiscSettings],
                 _players_resources_color: List[PlayerResourcesColor],
                 players_resources2_population: List[PlayerResources2Population],
                 _ai_files_names: List[str],
                 _ai_files_texts: List[PlayerAIFileText],
                 _ai_types: List[int],
                 _diplomacies: List[PlayerDiplomacy],
                 _allied_victories: List[int],
                 _starting_ages: List[int],
                 _individual_victories: List[bytes],
                 _disabled_techs_p1, _disabled_techs_p2, _disabled_techs_p3, _disabled_techs_p4,    # List
                 _disabled_techs_p5, _disabled_techs_p6, _disabled_techs_p7, _disabled_techs_p8,    # List
                 _disabled_buildings_p1, _disabled_buildings_p2, _disabled_buildings_p3, _disabled_buildings_p4,  # List
                 _disabled_buildings_p5, _disabled_buildings_p6, _disabled_buildings_p7, _disabled_buildings_p8,  # List
                 _disabled_units_p1, _disabled_units_p2, _disabled_units_p3, _disabled_units_p4,    # List
                 _disabled_units_p5, _disabled_units_p6, _disabled_units_p7, _disabled_units_p8     # List
                 ):

        self.player_count = player_count
        self._player_names = _player_names
        self._player_names_string_table = _player_names_string_table
        self._players_features = _players_features
        self.players_misc_settings = players_misc_settings
        self._ai_files_names = _ai_files_names
        self._ai_files_texts = _ai_files_texts
        self._ai_types = _ai_types
        self._players_resources_color = _players_resources_color
        self.players_resources2_population = players_resources2_population
        self._diplomacies = _diplomacies
        self._allied_victories = _allied_victories
        self._starting_ages = _starting_ages
        self._individual_victories = _individual_victories
        self._disabled_techs_p1 = _disabled_techs_p1
        self._disabled_techs_p2 = _disabled_techs_p2
        self._disabled_techs_p3 = _disabled_techs_p3
        self._disabled_techs_p4 = _disabled_techs_p4
        self._disabled_techs_p5 = _disabled_techs_p5
        self._disabled_techs_p6 = _disabled_techs_p6
        self._disabled_techs_p7 = _disabled_techs_p7
        self._disabled_techs_p8 = _disabled_techs_p8
        self._disabled_buildings_p1 = _disabled_buildings_p1
        self._disabled_buildings_p2 = _disabled_buildings_p2
        self._disabled_buildings_p3 = _disabled_buildings_p3
        self._disabled_buildings_p4 = _disabled_buildings_p4
        self._disabled_buildings_p5 = _disabled_buildings_p5
        self._disabled_buildings_p6 = _disabled_buildings_p6
        self._disabled_buildings_p7 = _disabled_buildings_p7
        self._disabled_buildings_p8 = _disabled_buildings_p8
        self._disabled_units_p1 = _disabled_units_p1
        self._disabled_units_p2 = _disabled_units_p2
        self._disabled_units_p3 = _disabled_units_p3
        self._disabled_units_p4 = _disabled_units_p4
        self._disabled_units_p5 = _disabled_units_p5
        self._disabled_units_p6 = _disabled_units_p6
        self._disabled_units_p7 = _disabled_units_p7
        self._disabled_units_p8 = _disabled_units_p8

        super().__init__()

    # region ===== Properties =====

    @property
    def player_names(self):
        names = [name.replace("\x00", "") for name in self._player_names]    # remove all NUL chars for purer view.
        return names[0:8]

    @property
    def player_names_string_table(self):
        names_stids = []
        for stid in self._player_names_string_table[0:8]:       # u32. 4294967294 => -2, 10020 => 10020
            if stid >= 4294967296/2:
                names_stids.append(stid - 4294967296)
            else:
                names_stids.append(stid)
        return names_stids

    @property
    def players_features(self):
        return self._players_features[0:8]

    # @property
    # def players_misc_settings(self):

    @property
    def players_resources_color(self):
        return self._players_resources_color[0:8]

    # @property
    # def players_resources2_population(self):

    @property
    def ai_files_names(self):
        return self._ai_files_names[0:8]

    @property
    def ai_files_texts(self):
        return self._ai_files_texts[0:8]

    @property
    def ai_types(self):
        return self._ai_types[0:8]

    @property
    def diplomacies(self):
        return self._diplomacies[0:8]
    
    @property
    def allied_victories(self):
        return self._allied_victories[0:8]
    
    @property
    def starting_ages(self):
        return self._starting_ages[0:8]
    
    @property
    def individual_victories(self):
        return self._individual_victories

    @property
    def per_player_disabled_techs(self):
        all_players_list = [
            self._disabled_techs_p1, self._disabled_techs_p2, self._disabled_techs_p3, self._disabled_techs_p4,
            self._disabled_techs_p5, self._disabled_techs_p6, self._disabled_techs_p7, self._disabled_techs_p8
        ]
        return all_players_list

    @property
    def per_player_disabled_buildings(self):
        all_players_list = [
            self._disabled_buildings_p1, self._disabled_buildings_p2, self._disabled_buildings_p3, self._disabled_buildings_p4,
            self._disabled_buildings_p5, self._disabled_buildings_p6, self._disabled_buildings_p7, self._disabled_buildings_p8
        ]
        return all_players_list

    @property
    def per_player_disabled_units(self):
        all_players_list = [
            self._disabled_units_p1, self._disabled_units_p2, self._disabled_units_p3, self._disabled_units_p4,
            self._disabled_units_p5, self._disabled_units_p6, self._disabled_units_p7, self._disabled_units_p8
        ]
        return all_players_list

    # endregion ===== Properties =====

    # region ===== Setters =====
    # endregion ===== Setters =====

    # region ===== Methods =====

    def change_player_name(self, player: PlayerId, new_name='', new_name_stid=-2):
        """
        Args:
            player: Which player you want to change. Could be PlayerId.One ~ EIGHT, PlayerId.GAIA not accepted.
            new_name: 0~256 chars (UTF-8). Each non-ASCII char occupies 3 chars.
            new_name_stid: String Table Id which you want to reference. If set to -2, Game Editor will ingnore it.
        """
        if player == PlayerId.GAIA:
            raise ValueError("Cannot change Gaia's name.")
        else:
            name_bytes = new_name.encode('utf-8') + b"\x00" * 256  # Refill with plenty NUL
            limited_name = name_bytes[0:256].decode('utf-8')  # Limit to 256 bytes (in UTF-8)
            unsigned_name_stid = (new_name_stid + 4294967296) % 4294967296   # u32. -2 => 4294967294, 10020 => 10020
            self._player_names[player.value - 1] = limited_name
            self._player_names_string_table[player.value - 1] = unsigned_name_stid

    # endregion ===== Methods =====

