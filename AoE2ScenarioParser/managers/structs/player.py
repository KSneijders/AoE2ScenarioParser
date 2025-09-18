from bfp_rs import RefStruct, ret
from bfp_rs.bfp_rs import RetrieverRef
from bfp_rs.combinators import get_attr

from AoE2ScenarioParser.datasets.player_data import Civilization, StartingAge
from AoE2ScenarioParser.managers.support.decorators import dataset_property, no_gaia_property
from AoE2ScenarioParser.objects.support import Point, Tile
from AoE2ScenarioParser.sections import (
    DataHeader, Diplomacy, Options, PlayerBaseOptions, PlayerOptions, Resources,
    ScenarioPlayerData, ScenarioSections, Settings, UnitData, View, ViewF,
)

GAIA_INDEX = 8  # get(ret(ScenarioSections.settings), ret(Settings.data_header), ret(DataHeader.gaia_player_idx)) + 1
INDEX = get_attr('index')
GAIA_LAST_INDEX = get_attr('index') - 1
GAIA_AFTER_PLAYER_INDEX = (GAIA_LAST_INDEX % (GAIA_INDEX + 1))


class Player(RefStruct):
    _struct: ScenarioSections

    # @formatter:off

    # GAIA index 0:              INDEX
    # GAIA index after players:  GAIA_AFTER_PLAYER_INDEX
    # GAIA last:                 GAIA_LAST_INDEX
    # GAIA not present:          GAIA_LAST_INDEX + no_gaia_property
    _active: bool                  = RetrieverRef(ret(ScenarioSections.settings),  ret(Settings.data_header),          ret(DataHeader.player_base_options),   GAIA_LAST_INDEX,         ret(PlayerBaseOptions.active))
    human: bool                    = RetrieverRef(ret(ScenarioSections.settings),  ret(Settings.data_header),          ret(DataHeader.player_base_options),   GAIA_LAST_INDEX,         ret(PlayerBaseOptions.human))
    _civilization: int             = RetrieverRef(ret(ScenarioSections.settings),  ret(Settings.data_header),          ret(DataHeader.player_base_options),   GAIA_LAST_INDEX,         ret(PlayerBaseOptions.civilization))
    _architecture: int             = RetrieverRef(ret(ScenarioSections.settings),  ret(Settings.data_header),          ret(DataHeader.player_base_options),   GAIA_LAST_INDEX,         ret(PlayerBaseOptions.architecture))
    _tribe_name: str               = RetrieverRef(ret(ScenarioSections.settings),  ret(Settings.data_header),          ret(DataHeader.tribe_names),           GAIA_LAST_INDEX)  # NO-GAIA
    _string_table_name_id: int     = RetrieverRef(ret(ScenarioSections.settings),  ret(Settings.data_header),          ret(DataHeader.player_name_str_ids),   GAIA_LAST_INDEX)  # NO-GAIA
    lock_civ: bool                 = RetrieverRef(ret(ScenarioSections.settings),  ret(Settings.data_header),          ret(DataHeader.lock_civilizations),    GAIA_AFTER_PLAYER_INDEX)
    food: int                      = RetrieverRef(ret(ScenarioSections.settings),  ret(Settings.player_options),       ret(PlayerOptions.starting_resources), GAIA_AFTER_PLAYER_INDEX, ret(Resources.food))
    wood: int                      = RetrieverRef(ret(ScenarioSections.settings),  ret(Settings.player_options),       ret(PlayerOptions.starting_resources), GAIA_AFTER_PLAYER_INDEX, ret(Resources.wood))
    gold: int                      = RetrieverRef(ret(ScenarioSections.settings),  ret(Settings.player_options),       ret(PlayerOptions.starting_resources), GAIA_AFTER_PLAYER_INDEX, ret(Resources.gold))
    stone: int                     = RetrieverRef(ret(ScenarioSections.settings),  ret(Settings.player_options),       ret(PlayerOptions.starting_resources), GAIA_AFTER_PLAYER_INDEX, ret(Resources.stone))
    color: int                     = RetrieverRef(ret(ScenarioSections.settings),  ret(Settings.player_options),       ret(PlayerOptions.starting_resources), GAIA_AFTER_PLAYER_INDEX, ret(Resources.player_color))
    population_cap: int            = RetrieverRef(ret(ScenarioSections.settings),  ret(Settings.options),              ret(Options.population_caps),          GAIA_AFTER_PLAYER_INDEX)
    _starting_age: int             = RetrieverRef(ret(ScenarioSections.settings),  ret(Settings.options),              ret(Options.starting_ages),            GAIA_AFTER_PLAYER_INDEX)
    _base_priority: int            = RetrieverRef(ret(ScenarioSections.settings),  ret(Settings.options),              ret(Options.base_priorities),          INDEX)  # NO-GAIA
    _view: View                    = RetrieverRef(ret(ScenarioSections.settings),  ret(Settings.options),              ret(Options.player_views),             GAIA_LAST_INDEX)  # NO-GAIA
    _disabled_techs: list[int]     = RetrieverRef(ret(ScenarioSections.settings),  ret(Settings.options),              ret(Options.disabled_tech_ids),        GAIA_LAST_INDEX)  # NO-GAIA
    _disabled_units: list[int]     = RetrieverRef(ret(ScenarioSections.settings),  ret(Settings.options),              ret(Options.disabled_unit_ids),        GAIA_LAST_INDEX)  # NO-GAIA
    _disabled_buildings: list[int] = RetrieverRef(ret(ScenarioSections.settings),  ret(Settings.options),              ret(Options.disabled_building_ids),    GAIA_LAST_INDEX)  # NO-GAIA
    _diplomacy: list[int]          = RetrieverRef(ret(ScenarioSections.settings),  ret(Settings.diplomacy),            ret(Diplomacy.player_stances),         GAIA_LAST_INDEX)  # NO-GAIA
    _allied_victory: bool          = RetrieverRef(ret(ScenarioSections.settings),  ret(Settings.diplomacy),            ret(Diplomacy.allied_victories),       GAIA_LAST_INDEX)  # NO-GAIA
    _editor_view: ViewF            = RetrieverRef(ret(ScenarioSections.unit_data), ret(UnitData.scenario_player_data), GAIA_LAST_INDEX,                       ret(ScenarioPlayerData.editor_view))  # NO-GAIA
    # @formatter:on

    def __new__(cls, struct, index: int):
        inst = super().__new__(cls, struct)
        inst.index = index
        return inst

    @property
    def id(self):
        return self.index

    @property
    def active(self):
        """Read-only value if this player is active or not, use the player manager to update this value"""
        return self._active

    # ========== Dataset Casting ==========

    @dataset_property(Civilization)
    def civilization(self) -> Civilization:
        return self._civilization  # type: ignore

    @dataset_property(Civilization)
    def architecture(self) -> Civilization:
        return self._architecture  # type: ignore

    @dataset_property(StartingAge)
    def starting_age(self) -> StartingAge:
        return self._starting_age  # type: ignore

    # ========== No GAIA ==========

    @no_gaia_property()
    def diplomacy(self) -> list[int] | None:
        return self._diplomacy

    @no_gaia_property()
    def allied_victory(self) -> bool | None:
        return self._allied_victory

    @no_gaia_property()
    def base_priority(self) -> int | None:
        return self._base_priority

    @no_gaia_property()
    def tribe_name(self) -> str | None:
        return self._tribe_name

    @no_gaia_property()
    def string_table_name_id(self) -> int | None:
        return self._string_table_name_id

    @no_gaia_property()
    def disabled_techs(self) -> list[int] | None:
        return self._disabled_techs

    @no_gaia_property()
    def disabled_units(self) -> list[int] | None:
        return self._disabled_units

    @no_gaia_property()
    def disabled_buildings(self) -> list[int] | None:
        return self._disabled_buildings

    @property
    def view(self) -> Tile | None:
        if self.index == 0:
            return None
        return Tile(self._view.x, self._view.y)

    @view.setter
    def view(self, value: Tile) -> None:
        if self.index == 0:
            raise AttributeError(f"GAIA does not support the view attribute")
        self._view.x = value.x
        self._view.y = value.y

    @property
    def editor_view(self) -> Point | None:
        if self.index == 0:
            return None
        return Point(self._editor_view.x, self._editor_view.y)

    @editor_view.setter
    def editor_view(self, value: Point) -> None:
        if self.index == 0:
            raise AttributeError(f"GAIA does not support the editor_view attribute")
        self._editor_view.x = value.x
        self._editor_view.y = value.y
