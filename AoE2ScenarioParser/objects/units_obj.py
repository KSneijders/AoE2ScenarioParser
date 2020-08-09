from __future__ import annotations

from typing import List

from AoE2ScenarioParser.datasets.players import Player
from AoE2ScenarioParser.helper.alias import Alias
from AoE2ScenarioParser.helper.helper import Tile
from AoE2ScenarioParser.objects.unit_obj import UnitObject
from AoE2ScenarioParser.pieces.structs.player_units import PlayerUnitsStruct
from AoE2ScenarioParser.pieces.structs.unit import UnitStruct


class UnitsObject:
    """
    The units manager object provides some default handlers for units,
    since performing simple operations such as adding or removing units require to
    modify different places in the file.
    """
    _players_units: List[PlayerUnitsStruct] = Alias('self._units_piece.players_units')

    def __init__(self, parsed_data):
        self._units_piece = parsed_data['UnitsPiece']

        self.units: List[List[UnitObject]] = []
        for i, player_units in enumerate(self._units_piece.players_units):
            current_unit_list = []
            self.units.append(current_unit_list)
            for unit in player_units.units:
                unit_object = UnitObject(unit)
                unit_object._player = Player(i)
                current_unit_list.append(unit_object)

    def add_unit(self, player: Player, unit_const: int, x: float, y: float, z: float = 0, rotation: float = 0,
                 garrisoned_in_id: int = -1, animation_frame: int = 0, status: int = 2,
                 reference_id: int = None, ) -> UnitObject:
        """
        Adds a unit to the scenario.

        Please note, for every unit added a search is done for the next available reference ID. This is done using
        the function `get_next_available_reference_id()`. This is only executed if `reference_id` is left empty. If
        you're intending on adding many units it is recommended to run `get_next_available_reference_id()` once
        yourself. You can use the result to fill the `reference_id` attribute and increment the value by yourself per
        unit. This could improve performance massively. For more information, please read the docstring of said
        function.

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
            The UnitObject created
        """
        if reference_id is None:
            reference_id = self.get_next_available_reference_id()

        unit = UnitObject(UnitStruct(data=[
            x, y, z,
            reference_id,
            unit_const,
            status,
            rotation,
            animation_frame,
            garrisoned_in_id,
        ]))

        unit._player = player

        self.units[player].append(unit)
        self._update_unit_count()
        return unit

    def get_player_units(self, player: Player) -> List[UnitObject]:
        """Returns a list of UnitObjects for the given player."""
        return self.units[player]

    def get_all_units(self) -> List[UnitObject]:
        units = []
        for player_units in self.units:
            units += player_units
        return units

    def remove_eye_candy(self) -> None:
        """
        Remove eye candy objects from the map. List is a WIP.
        """
        eye_candy_ids = [1351, 1352, 1353, 1354, 1355, 1358, 1359, 1360, 1361, 1362, 1363, 1364, 1365, 1366]
        self.units[0] = [gaia_unit for gaia_unit in self.units[0] if gaia_unit.unit_const not in eye_candy_ids]
        self._update_unit_count()

    def get_units_in_area(self,
                          x1: float = None,
                          y1: float = None,
                          x2: float = None,
                          y2: float = None,
                          tile1: Tile = None,
                          tile2: Tile = None,
                          unit_list: List[UnitObject] = None,
                          players: List[Player] = None,
                          ignore_players: List[Player] = None):
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

        if tile1 and tile2:
            x1 = tile1.x1
            y1 = tile1.y1
            x2 = tile2.x2
            y2 = tile2.y2

        if players is not None:
            players = players
        elif ignore_players is not None:
            players = [p for p in Player if p not in ignore_players]
        else:
            players = [p for p in Player]

        if unit_list is None:
            unit_list = self.get_all_units()

        return [unit for unit in unit_list
                if x1 <= unit.x <= x2 and y1 <= unit.y <= y2 and unit.player in players]

    def change_ownership(self, unit: UnitObject, to_player: Player) -> None:
        """
        Changes a unit's ownership to the given player.

        Args:
            unit: The unit object which ownership will be changed
            to_player: The player that'll get ownership over the unit (using Player enum)
        """
        for i, player_unit in enumerate(self.units[unit.player.value]):
            if player_unit == unit:
                del self.units[unit.player][i]
                self.units[to_player].append(unit)
                unit._player = Player(to_player)
                self._update_unit_count()
                return

    def get_next_available_reference_id(self) -> int:
        """
        Finds the highest reference ID currently used (n). Returns n + 1.

        Please note: that this function searches through all units. If this function is used for the creation of
        units (or anything comparable) and also within a controlled order, it is recommended to run this function
        once. Then save the result and increment this value yourself and use the 'reference_id' attribute in the
        add_unit function.
        """
        highest_id: int = 0  # If no units, default to 0
        for player in Player:
            for unit in self.units[player]:
                if highest_id < unit.reference_id:
                    highest_id = unit.reference_id
        return highest_id + 1

    def remove_unit(self, unit: UnitObject = None, reference_id: int = None):
        if reference_id is not None and unit is not None:
            raise ValueError("Cannot use both reference_id and unit arguments. Use one or the other.")
        if reference_id is None and unit is None:
            raise ValueError("Select a unit to be removed using the reference_id or unit arguments.")

        if reference_id is not None:
            for player in Player:
                for i, unit in enumerate(self.units[player]):
                    if unit.reference_id == reference_id:
                        del self.units[player][i]
        elif unit is not None:
            self.units[unit.player].remove(unit)

        self._update_unit_count()

    def _update_unit_count(self):
        """Updates the unit_count numbers in the pieces"""
        for p in Player:
            self._players_units[p].unit_count = len(self.units[p])
