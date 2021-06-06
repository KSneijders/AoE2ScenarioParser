from __future__ import annotations

# from typing import List

from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.data_objects.player_data import PlayerFeature, PlayerResourcesColor, PlayerAiFileText,\
    PlayerMiscSettings, PlayerResourcesPopulation, PlayerDiplomacy
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink


class PlayerManager(AoE2Object):
    """Manager of the everything player related."""

    _link_list = [
        RetrieverObjectLink("player_count", "FileHeader", "player_count"),

        RetrieverObjectLink("_player_names", "DataHeader", "player_names"),
        RetrieverObjectLink("_player_names_stid", "DataHeader", "string_table_player_names"),

        RetrieverObjectLink("_player_features", "DataHeader", "player_data_1", process_as_object=PlayerFeature),
        RetrieverObjectLink("player_misc_settings", "Units", "player_data_3", process_as_object=PlayerMiscSettings),

        RetrieverObjectLink("_player_resources_color", "PlayerDataTwo", "resources",
                            process_as_object=PlayerResourcesColor),
        RetrieverObjectLink("player_resources_population", "Units", "player_data_4",
                            process_as_object=PlayerResourcesPopulation),

        RetrieverObjectLink("_ai_files_names", "PlayerDataTwo", "ai_names"),
        RetrieverObjectLink("_ai_files_text", "PlayerDataTwo", "ai_files", process_as_object=PlayerAiFileText),
        RetrieverObjectLink("_ai_type", "PlayerDataTwo", "ai_type"),

        RetrieverObjectLink("_per_player_diplomacy", "Diplomacy", "per_player_diplomacy",
                            process_as_object=PlayerDiplomacy),
        RetrieverObjectLink("_per_player_allied_victory", "Diplomacy", "per_player_allied_victory"),
        RetrieverObjectLink("_per_player_starting_age", "Options", "per_player_starting_age"),
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
                 player_count,
                 _player_names,
                 _player_names_stid,
                 _player_features,
                 player_misc_settings,
                 _player_resources_color,
                 player_resources_population,
                 _ai_files_names,
                 _ai_files_text,
                 _ai_type,
                 _per_player_diplomacy,
                 _per_player_allied_victory,
                 _per_player_starting_age,
                 _individual_victories,
                 _disabled_techs_p1, _disabled_techs_p2, _disabled_techs_p3, _disabled_techs_p4,
                 _disabled_techs_p5, _disabled_techs_p6, _disabled_techs_p7, _disabled_techs_p8,
                 _disabled_buildings_p1, _disabled_buildings_p2, _disabled_buildings_p3, _disabled_buildings_p4,
                 _disabled_buildings_p5, _disabled_buildings_p6, _disabled_buildings_p7, _disabled_buildings_p8,
                 _disabled_units_p1, _disabled_units_p2, _disabled_units_p3, _disabled_units_p4,
                 _disabled_units_p5, _disabled_units_p6, _disabled_units_p7, _disabled_units_p8
                 ):

        self.player_count = player_count
        self._player_names = _player_names
        self._player_names_stid = _player_names_stid
        self._player_features = _player_features
        self.player_misc_settings = player_misc_settings
        self._ai_files_names = _ai_files_names
        self._ai_files_text = _ai_files_text
        self._ai_type = _ai_type
        self._player_resources_color = _player_resources_color
        self.player_resources_population = player_resources_population
        self._per_player_diplomacy = _per_player_diplomacy
        self._per_player_allied_victory = _per_player_allied_victory
        self._per_player_starting_age = _per_player_starting_age
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
        return [name.replace("\x00", "") for name in self._player_names]    # remove all NUL chars for purer view.

    @property
    def player_names_stid(self):
        names_stids = []
        for stid in self._player_names_stid[0:8]:       # u32. 4294967294 => -2, 10020 => 10020
            if stid >= 4294967296/2:
                names_stids.append(stid - 4294967296)
            else:
                names_stids.append(stid)
        return names_stids

    @property
    def player_features(self):
        return self._player_features[0:8]

    # @property
    # def player_misc_settings(self):
    #     return self.player_misc_settings

    @property
    def player_resources_color(self):
        return self._player_resources_color[0:8]

    # @property
    # def player_resources_population(self):
    #     return self.player_resources_population

    @property
    def ai_files_names(self):
        return self._ai_files_names[0:8]

    @property
    def ai_files_text(self):
        return self._ai_files_text[0:8]

    @property
    def ai_type(self):
        return self._ai_type[0:8]

    @property
    def per_player_diplomacy(self):
        return self._per_player_diplomacy[0:8]
    
    @property
    def per_player_allied_victory(self):
        return self._per_player_allied_victory[0:8]
    
    @property
    def per_player_starting_age(self):
        return self._per_player_starting_age[0:8]
    
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
            new_name_stid: String Table Id which you want to reference. Set to -2 for ingnore.
        """
        if player == PlayerId.GAIA:
            raise ValueError("Cannot change Gaia's name.")
        else:
            name_bytes = new_name.encode('utf-8') + b"\x00" * 256  # Refill with plenty NUL
            limited_name = name_bytes[0:256].decode('utf-8')  # Limit to 256 bytes (in UTF-8)
            unsigned_name_stid = (new_name_stid + 4294967296) % 4294967296   # u32. -2 => 4294967294, 10020 => 10020
            self._player_names[player.value - 1] = limited_name
            self._player_names_stid[player.value - 1] = unsigned_name_stid

    # endregion ===== Methods =====

