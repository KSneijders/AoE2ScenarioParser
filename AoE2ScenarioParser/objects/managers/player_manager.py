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
        RetrieverObjectLink("_player_name_string_table_ids", "DataHeader", "string_table_player_names"),

        RetrieverObjectLink("players_features", "DataHeader", "player_data_1", process_as_object=PlayerFeatures),
        RetrieverObjectLink("players_misc_settings", "Units", "player_data_3", process_as_object=PlayerMiscSettings),

        RetrieverObjectLink("players_resources_color", "PlayerDataTwo", "resources",
                            process_as_object=PlayerResourcesColor),
        RetrieverObjectLink("players_resources2_population", "Units", "player_data_4",
                            process_as_object=PlayerResources2Population),

        RetrieverObjectLink("ai_files_names", "PlayerDataTwo", "ai_names"),
        RetrieverObjectLink("ai_files_texts", "PlayerDataTwo", "ai_files", process_as_object=PlayerAIFileText),
        RetrieverObjectLink("ai_types", "PlayerDataTwo", "ai_types"),

        RetrieverObjectLink("diplomacies", "Diplomacy", "per_player_diplomacy",
                            process_as_object=PlayerDiplomacy),
        RetrieverObjectLink("allied_victories", "Diplomacy", "per_player_allied_victory"),
        RetrieverObjectLink("starting_ages", "Options", "per_player_starting_age"),
        RetrieverObjectLink("individual_victories", "Diplomacy", "individual_victories"),

        RetrieverObjectLink("per_player_lock_civilization", "DataHeader", "per_player_lock_civilization"),
        RetrieverObjectLink("per_player_base_priority", "Options", "per_player_base_priority"),

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
        RetrieverObjectLink("_disabled_units_p8", "Options", "disabled_unit_ids_player_8"),

        RetrieverObjectLink("_player_1_initial_camera_xy", "Map", "player_1_initial_camera_xy"),  # Since version 1.40?
        RetrieverObjectLink("_player_2_initial_camera_xy", "Map", "player_2_initial_camera_xy"),  # Since version 1.40?
        RetrieverObjectLink("_player_3_initial_camera_xy", "Map", "player_3_initial_camera_xy"),  # Since version 1.40?
        RetrieverObjectLink("_player_4_initial_camera_xy", "Map", "player_4_initial_camera_xy"),  # Since version 1.40?
        RetrieverObjectLink("_player_5_initial_camera_xy", "Map", "player_5_initial_camera_xy"),  # Since version 1.40?
        RetrieverObjectLink("_player_6_initial_camera_xy", "Map", "player_6_initial_camera_xy"),  # Since version 1.40?
        RetrieverObjectLink("_player_7_initial_camera_xy", "Map", "player_7_initial_camera_xy"),  # Since version 1.40?
        RetrieverObjectLink("_player_8_initial_camera_xy", "Map", "player_8_initial_camera_xy"),  # Since version 1.40?
    ]

    def __init__(self,
                 player_count: int,
                 _player_names: List[str],
                 _player_name_string_table_ids: List[int],
                 players_features: List[PlayerFeatures],
                 players_misc_settings: List[PlayerMiscSettings],
                 players_resources_color: List[PlayerResourcesColor],
                 players_resources2_population: List[PlayerResources2Population],
                 ai_files_names: List[str],
                 ai_files_texts: List[PlayerAIFileText],
                 ai_types: List[int],
                 diplomacies: List[PlayerDiplomacy],
                 allied_victories: List[int],
                 starting_ages: List[int],
                 individual_victories: List[bytes],
                 per_player_lock_civilization: List[int],
                 per_player_base_priority: List[int],
                 _disabled_techs_p1, _disabled_techs_p2, _disabled_techs_p3, _disabled_techs_p4,    # List
                 _disabled_techs_p5, _disabled_techs_p6, _disabled_techs_p7, _disabled_techs_p8,    # List
                 _disabled_buildings_p1, _disabled_buildings_p2, _disabled_buildings_p3, _disabled_buildings_p4,  # List
                 _disabled_buildings_p5, _disabled_buildings_p6, _disabled_buildings_p7, _disabled_buildings_p8,  # List
                 _disabled_units_p1, _disabled_units_p2, _disabled_units_p3, _disabled_units_p4,    # List
                 _disabled_units_p5, _disabled_units_p6, _disabled_units_p7, _disabled_units_p8,    # List
                 _player_1_initial_camera_xy, _player_2_initial_camera_xy,
                 _player_3_initial_camera_xy, _player_4_initial_camera_xy,
                 _player_5_initial_camera_xy, _player_6_initial_camera_xy,
                 _player_7_initial_camera_xy, _player_8_initial_camera_xy
                 ):

        self.player_count = player_count
        self._player_names = _player_names
        self._player_name_string_table_ids = _player_name_string_table_ids
        self.players_features = players_features
        self.players_misc_settings = players_misc_settings
        self.ai_files_names = ai_files_names
        self.ai_files_texts = ai_files_texts
        self.ai_types = ai_types
        self.players_resources_color = players_resources_color
        self.players_resources2_population = players_resources2_population
        self.diplomacies = diplomacies
        self.allied_victories = allied_victories
        self.starting_ages = starting_ages   # TODO: 2: DarkAge, 6: PostImp | 1st-8th players, 9th GAIA
        self.individual_victories = individual_victories
        self.per_player_lock_civilization = per_player_lock_civilization
        self.per_player_base_priority = per_player_base_priority
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

        self._player_1_initial_camera_xy = _player_1_initial_camera_xy
        self._player_2_initial_camera_xy = _player_2_initial_camera_xy
        self._player_3_initial_camera_xy = _player_3_initial_camera_xy
        self._player_4_initial_camera_xy = _player_4_initial_camera_xy
        self._player_5_initial_camera_xy = _player_5_initial_camera_xy
        self._player_6_initial_camera_xy = _player_6_initial_camera_xy
        self._player_7_initial_camera_xy = _player_7_initial_camera_xy
        self._player_8_initial_camera_xy = _player_8_initial_camera_xy

        super().__init__()


    # region ===== Properties =====

    @property
    def player_names(self):
        """Read-Only. To change these, please refer to change_player_name()."""
        # Remove all NUL chars for purer view.
        return [self._purify_player_name(name) for name in self._player_names]

    @property
    def player_name_string_table_ids(self):
        """Read-Only. To change these, please refer to change_player_name()."""
        # Convert large numbers to negative numbers for purer view.
        names_stids = []
        for stid in self._player_name_string_table_ids:
            names_stids.append(self._purify_player_name_stid(stid))
        return names_stids

    @property
    def per_player_disabled_techs(self):
        return [
            self._disabled_techs_p1, self._disabled_techs_p2, self._disabled_techs_p3, self._disabled_techs_p4,
            self._disabled_techs_p5, self._disabled_techs_p6, self._disabled_techs_p7, self._disabled_techs_p8
        ]

    @property
    def per_player_disabled_buildings(self):
        return [
            self._disabled_buildings_p1, self._disabled_buildings_p2, self._disabled_buildings_p3,
            self._disabled_buildings_p4, self._disabled_buildings_p5, self._disabled_buildings_p6,
            self._disabled_buildings_p7, self._disabled_buildings_p8
        ]

    @property
    def per_player_disabled_units(self):
        return [
            self._disabled_units_p1, self._disabled_units_p2, self._disabled_units_p3, self._disabled_units_p4,
            self._disabled_units_p5, self._disabled_units_p6, self._disabled_units_p7, self._disabled_units_p8
        ]

    @property
    def per_player_initial_camera_xy(self):
        return [
            self._player_1_initial_camera_xy, self._player_2_initial_camera_xy,
            self._player_3_initial_camera_xy, self._player_4_initial_camera_xy,
            self._player_5_initial_camera_xy, self._player_6_initial_camera_xy,
            self._player_7_initial_camera_xy, self._player_8_initial_camera_xy
        ]

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
            raise ValueError("Can not change Gaia's name.")
        else:
            new_name_standard = self._standardize_player_name(new_name)
            unsigned_name_stid = self._standardize_player_name_stid(new_name_stid)
            self._player_names[player.value - 1] = new_name_standard
            self._player_name_string_table_ids[player.value - 1] = unsigned_name_stid

    # endregion ===== Methods =====


    # region ===== Static Methods =====

    @staticmethod
    def _purify_player_name(name_with_x00: str):
        """Returns a new player names with all NUL chars removed.
         - Such as: 'William\x00...\x00' => 'William'
        """
        return name_with_x00.replace('\x00', '')

    @staticmethod
    def _standardize_player_name(name: str):
        """Returns the player name standardized to 256 bytes/chars in UTF-8.
         - Such as: 'William' => 'William\x00...\x00'.
         - Such as: 'Ａ..Ａ..Ａ..Ａ..ＦＧＨＩ' => 'Ａ..Ａ..Ａ..Ａ..ＦＧ\x00'
        """
        name_bytes = name.encode('utf-8')
        name_bytes += b'\x00' * (256 - len(name_bytes))  # Fill with plenty NUL, or no filling when len>=256
        # Wrong slice will cause decode error.
        # Since each non-ASCII char occupies 3 bytes in UTF-8, there are only 3 cases:
        try:
            limited_name = name_bytes[0:256].decode('utf-8')
        except UnicodeDecodeError:
            try:
                limited_name = (name_bytes[0:255] + b'\x00').decode('utf-8')
            except UnicodeDecodeError:
                limited_name = (name_bytes[0:254] + b'\x00\x00').decode('utf-8')
        return limited_name

    @staticmethod
    def _purify_player_name_stid(name_stid: int):
        """Such as: 4294967294 => -2    Such as: 10020 => 10020"""
        return (name_stid - 4294967296) if (name_stid >= 4294967296/2) else name_stid

    @staticmethod
    def _standardize_player_name_stid(name_stid: int):
        """Such as: -2 => 4294967294    Such as: 10020 => 10020"""
        return (name_stid + 4294967296) % 4294967296

    # endregion ===== Static Methods =====

