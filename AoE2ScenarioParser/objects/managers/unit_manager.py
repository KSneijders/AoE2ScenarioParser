from __future__ import annotations

from typing import List, Union

from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.data_objects.unit import Unit
from AoE2ScenarioParser.objects.support.tile import Tile
from AoE2ScenarioParser.objects.support.uuid_list import UuidList
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink


class UnitManager(AoE2Object):
    """Manager of the everything trigger related."""

    _link_list = [
        RetrieverObjectLink("units", "Units", "players_units[].units", process_as_object=Unit)
    ]

    def __init__(self, units: List[List[Unit]], **kwargs):
        super().__init__(**kwargs)

        self.units = units
        # `self.find_highest_reference_id()` can be replaced by the value for next_unit_id_to_place in retrievers
        self.reference_id_generator = create_id_generator(self.find_highest_reference_id() + 1)

    @property
    def units(self):
        return self._units

    @units.setter
    def units(self, value: List[List[Unit]]):
        def _raise():
            raise ValueError("Units should be list with a maximum of 9 sub lists, example: [[Unit], [Unit, Unit], ...]")

        if len(value) > 9:
            _raise()
        elif len(value) < 9:
            value.extend([[] for _ in range(9 - len(value))])

        self._units = UuidList(self._host_uuid, value)

    def update_unit_player_values(self):
        """Function to update all player values in all units. Useful when units are moved manually (in mass)."""
        for player in PlayerId.all():
            for unit in self.units[player]:
                unit._player = player

    def add_unit(self,
                 player: Union[int, PlayerId],
                 unit_const: int,
                 x: float,
                 y: float,
                 z: float = 0,
                 rotation: float = 0,
                 garrisoned_in_id: int = -1,
                 animation_frame: int = 0,
                 status: int = 2,
                 reference_id: int = None, ) -> Unit:
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
        Returns:
            The Unit created
        """
        if reference_id is None:
            reference_id = self.get_new_reference_id()

        unit = Unit(
            player=player,
            x=x,
            y=y,
            z=z,
            reference_id=reference_id,
            unit_const=unit_const,
            status=status,
            rotation=rotation,
            initial_animation_frame=animation_frame,
            garrisoned_in_id=garrisoned_in_id,
            host_uuid=self._host_uuid
        )

        self.units[player].append(unit)
        return unit

    def get_player_units(self, player: Union[int, PlayerId]) -> List[Unit]:
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

    def filter_units_by_const(self,
                              unit_consts: List[int],
                              blacklist: bool = False,
                              player_list: List[Union[int, PlayerId]] = None,
                              unit_list: List[Unit] = None) -> List[Unit]:
        """
        Filter unit on their unit_const value.

        Args:
            unit_consts (List[int]): The constants to filter with
            blacklist (bool): Use the given constant list as blacklist instead of whitelist
            player_list (List[int]): A list of players to filter from. If not used, all players are used.
            unit_list (List[Unit]): A set of units to filter from. If not used, all units are used.

        Returns:
            A list of units
        """
        if unit_list is None:
            unit_list = self.get_all_units()
        if player_list is not None:
            unit_list = [unit for unit in unit_list if unit.player in player_list]

        # Both return statements can be combined using: ((unit.unit_const in unit_consts) != blacklist)
        # But splitting them helps performance (not checking against blacklist for each entry)
        if not blacklist:
            return [unit for unit in unit_list if unit.unit_const in unit_consts]
        return [unit for unit in unit_list if unit.unit_const not in unit_consts]

    def get_units_in_area(self,
                          x1: float = None,
                          y1: float = None,
                          x2: float = None,
                          y2: float = None,
                          tile1: Tile = None,
                          tile2: Tile = None,
                          unit_list: List[Unit] = None,
                          players: List[Union[int, PlayerId]] = None,
                          ignore_players: List[PlayerId] = None):
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

        :Authors:
            KSneijders (https://github.com/KSneijders/)
            T-West (https://github.com/twestura/)
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
            x1 = tile1.x1
            y1 = tile1.y1
            x2 = tile2.x2
            y2 = tile2.y2

        if players is not None:
            players = players
        elif ignore_players is not None:
            players = [p for p in PlayerId if p not in ignore_players]
        else:
            players = [p for p in PlayerId]

        if unit_list is None:
            unit_list = self.get_all_units()

        return [unit for unit in unit_list
                if x1 <= unit.x <= x2 and y1 <= unit.y <= y2 and unit.player in players]

    def change_ownership(self, unit: Unit, to_player: Union[int, PlayerId]) -> None:
        """
        Changes a unit's ownership to the given player.

        Args:
            unit: The unit object which ownership will be changed
            to_player: The player that'll get ownership over the unit (using PlayerId enum)
        """
        for i, player_unit in enumerate(self.units[unit.player]):
            if player_unit == unit:
                del self.units[unit.player][i]
                self.units[to_player].append(unit)
                unit._player = PlayerId(to_player)
                return

    def get_new_reference_id(self) -> int:
        """
        Get a new ID each time the function is called. Starting from the current highest ID.

        Returns:
            The newly generator ID
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
            reference_id (int): The id of the unit. Note that this is NOT a unit constant (So NOT: UnitInfo.ARCHER)
            unit (Unit): The Unit object to be removed.
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


def create_id_generator(start_id: int):
    """
    Create generator for increasing value

    Args:
        start_id (int): The id to start returning

    Returns:
        A generator which will return a +1 ID value for each time called with next.
    """
    while True:
        yield start_id
        start_id += 1
