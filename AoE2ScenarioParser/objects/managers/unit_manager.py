from __future__ import annotations

from typing import List, Tuple, Generator, Union

from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.data_objects.unit import Unit
from AoE2ScenarioParser.objects.data_objects.units.player_units import PlayerUnits
from AoE2ScenarioParser.objects.support.tile import Tile
from AoE2ScenarioParser.objects.support.uuid_list import UuidList
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink


class UnitManager(AoE2Object):
    """Manager of everything unit related."""

    _link_list = [
        RetrieverObjectLink("_player_units", "Units", "players_units", process_as_object=PlayerUnits),
        RetrieverObjectLink("next_unit_id", "DataHeader", "next_unit_id_to_place")
    ]

    def __init__(
            self,
            _player_units: List[PlayerUnits],
            next_unit_id: int,
            **kwargs
    ):
        super().__init__(**kwargs)

        self.units: List[List[Unit]] = [pu.units for pu in _player_units]
        self.reference_id_generator: Generator[int] = create_id_generator(next_unit_id)

    @property
    def next_unit_id(self):
        return self.get_new_reference_id()

    @property
    def units(self) -> List[List[Unit]]:
        return self._units

    @units.setter
    def units(self, value: List[List[Unit]]):
        def _raise():
            raise ValueError("Units should be list with a maximum of 9 sub lists, example: [[Unit], [Unit, Unit], ...]")

        if len(value) > 9:
            _raise()
        elif len(value) < 9:
            value.extend([[] for _ in range(9 - len(value))])

        self._units = UuidList(self._uuid, value)

    def update_unit_player_values(self):
        """Function to update all player values in all units. Useful when units are moved manually (in mass)."""
        for player in PlayerId.all():
            for unit in self.units[player]:
                unit._player = player

    def clone_unit(
            self,
            unit: Unit,
            player: int | PlayerId = None,
            unit_const: int = None,
            x: float = None,
            y: float = None,
            z: float = None,
            rotation: float = None,
            garrisoned_in_id: int = None,
            animation_frame: int = None,
            status: int = None,
            reference_id: int = None,
            tile: Tile | Tuple[int, int] = None,
    ) -> Unit:
        """
        Clones an existing unit with the adjusted variables. Everything except the initial unit is optional.
        When arguments are provided, they will override the corresponding values in the cloned unit.

        Args:
            unit: The unit to clone
            player: The player to set the cloned unit to (If not provided, the original player will be used)
            unit_const: The unit you're placing (If not provided, the original unit constant will be used)
            x: The X coordinate of the cloned unit (If not provided, the original x coordinate will be used)
            y: The Y coordinate of the cloned unit (If not provided, the original y coordinate will be used)
            z: The Z coordinate of the cloned unit (If not provided, the original z coordinate will be used)
            rotation: The rotation of the cloned unit (If not provided, the original rotation will be used)
            garrisoned_in_id: The id of the garrisoned unit (If not provided, the original garrisoned id will be used)
            animation_frame: The animation frame of the cloned unit (If not provided, the original animation frame will be used)
            status: The status of the cloned unit (If not provided, the original status will be used)
            reference_id: Reference id of the cloned unit (If not provided, a new reference id will be generated)
            tile: The tile of the cloned unit (If not provided, the original x,y coordinates will be used)

        Returns:
            The cloned unit
        """

        if (x is not None or y is not None) and tile is not None:
            raise ValueError("Cannot use both x,y notation and tile notation at the same time")

        return self.add_unit(
            player=player or unit.player,
            unit_const=unit_const or unit.unit_const,
            x=x or unit.x,
            y=y or unit.y,
            z=z or unit.z,
            rotation=rotation or unit.rotation,
            garrisoned_in_id=garrisoned_in_id or unit.garrisoned_in_id,
            animation_frame=animation_frame or unit.initial_animation_frame,
            status=status or unit.status,
            reference_id=reference_id,
            tile=tile,
        )

    def add_unit(
            self,
            player: int | PlayerId,
            unit_const: int,
            x: float = 0,
            y: float = 0,
            z: float = 0,
            rotation: float = 0,
            garrisoned_in_id: int = -1,
            animation_frame: int = 0,
            status: int = 2,
            reference_id: int = None,
            caption_string_id: int = -1,
            tile: Tile | Tuple[int, int] = None,
    ) -> Unit:
        """
        Adds a unit to the scenario.

        Args:
            player: The player the unit belongs to.
            unit_const: Defines what unit you're placing. The IDs used in the unit/buildings dataset.
            x: The x location in the scenario.
            y: The y location in the scenario.
            z: The z (height) location in the scenario.
            rotation: The rotation of the unit.
            garrisoned_in_id: The reference_id of another unit this unit is garrisoned in.
            animation_frame: The animation frame of the unit.
            status: Unknown - Always 2. 0-6 no difference (?) | 7-255 makes it disappear. (Except from the mini-map)
            reference_id: The reference ID of this unit. Normally added automatically. Used for garrisoning or reference
                in triggers
            caption_string_id: A string ID for the caption of a unit
            tile: An object that represents a tile on the map. Replaces parameters x and y. Also, automatically adds
                .5 to both ints to place the unit centered on the tile.

        Returns:
            The Unit created
        """
        if reference_id is None:
            reference_id = self.get_new_reference_id()

        caption_string_id_retriever = Unit._link_list[1].group[9]
        if not caption_string_id_retriever.support.supports(self.get_scenario().scenario_version):
            caption_string_id = None

        unit = Unit(
            player=player,
            x=x if tile is None else (tile[0] + .5),
            y=y if tile is None else (tile[1] + .5),
            z=z,
            reference_id=reference_id,
            unit_const=unit_const,
            status=status,
            rotation=rotation,
            initial_animation_frame=animation_frame,
            garrisoned_in_id=garrisoned_in_id,
            caption_string_id=caption_string_id,
            uuid=self._uuid
        )

        self.units[player].append(unit)
        return unit

    def get_player_units(self, player: int | PlayerId) -> List[Unit]:
        """
        Returns a list of UnitObjects for the given player.

        Raises:
            ValueError: If player is not between 0 (GAIA) and 8 (EIGHT)
        """
        if not 0 <= player <= 8:
            raise ValueError("Player must have a value between 0 and 8")
        return self.units[player]

    def get_all_units(self) -> List[Unit]:
        units = []
        for player_units in self.units:
            units += player_units
        return units

    def filter_units_by(
            self,
            attr: str,
            unit_attrs: List[int],
            blacklist: bool = False,
            player_list: List[Union[int, PlayerId]] = None,
            unit_list: List[Unit] = None
    ) -> List[Unit]:
        """
        Filter units based on a given attribute of units

        Args:
            attr: The attribute to filter by
            unit_attrs: The values for the attributes to filter with
            blacklist: Use the given constant list as blacklist instead of whitelist
            player_list: A list of players to filter from. If not used, all players are used.
            unit_list: A set of units to filter from. If not used, all units are used.

        Returns:
            A list of units

        Raises:
            AttributeError: If the provided attr does not exist on objects of the Unit class
        """

        if unit_list is None:
            unit_list = self.get_all_units()
        if player_list is not None:
            unit_list = [unit for unit in unit_list if unit.player in player_list]

        if len(unit_list) == 0:
            return []

        unit = unit_list[0]
        if not hasattr(unit, attr):
            raise AttributeError(f"Cannot filter Unit objects by {attr}")

        # Both return statements can be combined using: ((unit.unit_const in unit_consts) != blacklist)
        # But splitting them helps performance (not checking against blacklist for each entry)
        if not blacklist:
            return [unit for unit_attr in unit_attrs for unit in unit_list if getattr(unit, attr) == unit_attr]
        return [unit for unit_attr in unit_attrs for unit in unit_list if getattr(unit, attr) != unit_attr]

    def filter_units_by_const(
            self,
            unit_consts: List[int],
            blacklist: bool = False,
            player_list: List[Union[int, PlayerId]] = None,
            unit_list: List[Unit] = None
    ) -> List[Unit]:
        """
        Filter unit on their unit_const value.

        Args:
            unit_consts: The constants to filter with
            blacklist: Use the given constant list as blacklist instead of whitelist
            player_list: A list of players to filter from. If not used, all players are used.
            unit_list: A set of units to filter from. If not used, all units are used.

        Returns:
            A list of units
        """
        return self.filter_units_by("unit_const", unit_consts, blacklist, player_list, unit_list)

    def filter_units_by_reference_id(
            self,
            unit_reference_ids: List[int],
            blacklist: bool = False,
            player_list: List[Union[int, PlayerId]] = None,
            unit_list: List[Unit] = None
    ) -> List[Unit]:
        """
        Filter unit on their unit_const value.

        Args:
            unit_reference_ids (List[int]): The reference_ids to filter with
            blacklist (bool): Use the given constant list as blacklist instead of whitelist
            player_list (List[int]): A list of players to filter from. If not used, all players are used.
            unit_list (List[Unit]): A set of units to filter from. If not used, all units are used.

        Returns:
            A list of units
        """
        return self.filter_units_by("reference_id", unit_reference_ids, blacklist, player_list, unit_list)

    def get_units_in_area(
            self,
            x1: float = None,
            y1: float = None,
            x2: float = None,
            y2: float = None,
            tile1: Tile = None,
            tile2: Tile = None,
            unit_list: List[Unit] = None,
            players: List[Union[int, PlayerId]] = None,
            ignore_players: List[PlayerId] = None
    ) -> List[Unit]:
        """
        Returns all units in the square with left corner (x1, y1) and right corner (x2, y2). Both corners inclusive.

        Args:
            x1: The X location of the left corner
            y1: The Y location of the left corner
            x2: The X location of the right corner
            y2: The Y location of the right corner
            tile1: The x,y location of the 1st corner as Tile Object
            tile2: The x,y location of the 2nd corner as Tile Object
            unit_list: (Optional) A list of units (Defaults to all units in the map, including GAIA (Trees etc.)
            players: (Optional) A list of Players which units need to be selected from the selected area
            ignore_players: (Optional) A list of Players which units need to be ignored from the selected area

        Raises:
            ValueError: if not all 4 (x1, y1, x2 and y2) are used simultaneously.
                Or if both (tile1 and tile2) are not used simultaneously.
                Or if any of the 4 (x1, y1, x2, y2) is used together with any of (tile1, tile2). Use one or the other.
                Or if players and ignore_players are used simultaneously.
        """
        if (x1 is not None or y1 is not None or x2 is not None or y2 is not None) and any([tile1, tile2]):
            raise ValueError("Cannot use both x1,y1,x2,y2 notation and tile1,tile2 notation at the same time")
        if (x1 is not None or y1 is not None or x2 is not None or y2 is not None) and \
                (x1 is None or y1 is None or x2 is None or y2 is None):
            raise ValueError("Cannot use some but not all from x1,y1,x2,y2.")
        if (not all([tile1, tile2])) and any([tile1, tile2]):
            raise ValueError("Cannot use one from tile1, tile2. Use both.")
        if players is not None and ignore_players is not None:
            raise ValueError("Cannot use both whitelist (players) and blacklist (ignore_players) at the same time")

        if tile1:
            x1 = tile1.x
            y1 = tile1.y
            x2 = tile2.x
            y2 = tile2.y
        else:
            # Inclusive selection
            x2 += 1
            y2 += 1

        if players is not None:
            players = players
        elif ignore_players is not None:
            players = [p for p in PlayerId if p not in ignore_players]
        else:
            players = [p for p in PlayerId]

        if unit_list is None:
            unit_list = self.get_all_units()

        return [unit for unit in unit_list if x1 <= unit.x <= x2 and y1 <= unit.y <= y2 and unit.player in players]

    @staticmethod
    def change_ownership(unit: Unit | List[Unit], to_player: int | PlayerId) -> None:
        """
        Changes a unit's ownership to the given player.

        Args:
            unit: The unit object which ownership will be changed
            to_player: The player that'll get ownership over the unit (using PlayerId enum)
        """
        if isinstance(unit, list):
            for u in unit:
                u.player = to_player
        else:
            unit.player = to_player

    def get_new_reference_id(self) -> int:
        """
        Get a new ID each time the function is called. Starting from the current highest ID.

        Returns:
            The newly generated ID
        """
        return next(self.reference_id_generator)

    def find_highest_reference_id(self) -> int:
        """
        Find the highest ID in the map. Searches through all units for the highest ID.

        Returns:
            The highest ID in the map
        """
        highest_id = 0  # If no units, default to 0
        for player in PlayerId.all():
            for unit in self.units[player]:
                highest_id = max(highest_id, unit.reference_id)
        return highest_id

    def remove_unit(self, reference_id: int = None, unit: Unit = None) -> None:
        """
        Removes a unit. Please note that `unit=...` is a lot faster than `reference_id=...` due to reference_id having
        to search through all units on the map. And unit has an ownership (player) attribute which is used for knowing
        which list to remove the unit from.

        Args:
            reference_id: The id of the unit. Note that this is NOT a unit constant (So NOT: UnitInfo.ARCHER)
            unit: The Unit object to be removed.
        """
        if reference_id is not None and unit is not None:
            raise ValueError("Cannot use both unit_ref_id and unit arguments. Use one or the other.")
        if reference_id is None and unit is None:
            raise ValueError("Both unit_ref_id and unit arguments were unused. Use one.")

        if reference_id is not None:
            for player in range(0, 9):
                for i, unit in enumerate(self.units[player]):
                    if unit.reference_id == reference_id:
                        del self.units[player][i]
                        return
        elif unit is not None:
            self.units[unit.player].remove(unit)

    def remove_eye_candy(self) -> None:
        eye_candy_ids = [1351, 1352, 1353, 1354, 1355, 1358, 1359, 1360, 1361, 1362, 1363, 1364, 1365, 1366]
        self.units[0] = [gaia_unit for gaia_unit in self.units[0] if gaia_unit.unit_const not in eye_candy_ids]

    # ###############################################################################################
    # ################################# Functions for reconstruction ################################
    # ###############################################################################################

    @property
    def _player_units(self):
        player_units = []
        for i in range(9):
            units = self.get_player_units(i)
            player_units.append(PlayerUnits(unit_count=len(units), units=units))

        return UuidList(self._uuid, player_units)


def create_id_generator(start_id: int) -> Generator[int]:
    """
    Create generator for increasing value

    Args:
        start_id: The id to start returning

    Returns:
        A generator which will return a +1 ID value for each time called with next.
    """
    while True:
        yield start_id
        start_id += 1
