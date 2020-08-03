from __future__ import annotations

from typing import List

from AoE2ScenarioParser.datasets.players import Player
from AoE2ScenarioParser.datasets.units import Unit
from AoE2ScenarioParser.helper.alias import Alias
from AoE2ScenarioParser.helper.helper import Tile
from AoE2ScenarioParser.pieces.structs.player_units import PlayerUnitsStruct
from AoE2ScenarioParser.pieces.structs.unit import UnitStruct

class UnitsObject():
    _players_units = Alias('_units_piece', 'players_units')

    def __init__(self, pieces):
        self._units_piece = pieces['UnitsPiece']

        # Set the player value for all the units
        for i, units_of_player in enumerate(self.units):
            for unit in units_of_player:
                unit._player = Player(i)

    @property
    def units(self):
        return [player_units.units for player_units in self._players_units]

    def add_unit(self, player: Player, unit_const: int, x: float, y: float, z: float = 0, rotation: float = 0,
                 garrisoned_in_id: int = -1, animation_frame: int = 0, status: int = 2,
                 reference_id: int = None, ) -> UnitStruct:
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
            The UnitStruct created
        """
        if reference_id is None:
            reference_id = self.get_next_available_reference_id()

        unit = UnitStruct(data = [
            x,
            y,
            z,
            reference_id,
            unit_const,
            status,
            rotation,
            animation_frame,
            garrisoned_in_id,
        ])

        unit._player = player

        self.units[player.value].append(unit)
        self._update_unit_count()
        return unit

    def get_player_units(self, player: Player) -> List[UnitStruct]:
        """
        Returns a list of UnitObjects for the given player.

        Raises:
            ValueError: If player is not between 0 (GAIA) and 8 (EIGHT)
        """
        if not 0 <= player.value <= 8:
            raise ValueError("Player must have a value between 0 and 8")
        return self.units[player.value]

    def get_all_units(self) -> List[UnitStruct]:
        units = []
        for player_units in self.units:
            units += player_units
        return units

    def remove_eye_candy(self) -> None:
        eye_candy_ids = [1351, 1352, 1353, 1354, 1355, 1358, 1359, 1360, 1361, 1362, 1363, 1364, 1365, 1366]
        self.units[0] = [gaia_unit for gaia_unit in self.units[0] if gaia_unit.unit_const not in eye_candy_ids]

    def get_units_in_area(self,
                          x1: float = None,
                          y1: float = None,
                          x2: float = None,
                          y2: float = None,
                          tile1: Tile = None,
                          tile2: Tile = None,
                          unit_list: List[UnitStruct] = None,
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

        if tile1:
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

    def change_ownership(self, unit: UnitStruct, to_player: Player) -> None:
        """
        Changes a unit's ownership to the given player.

        Args:
            unit: The unit object which ownership will be changed
            to_player: The player that'll get ownership over the unit (using Player enum)
        """
        for i, player_unit in enumerate(self.units[unit.player.value]):
            if player_unit == unit:
                del self.units[unit.player.value][i]
                self.units[to_player.value].append(unit)
                unit._player = Player(to_player)
                self._update_unit_count()
                return

    def get_next_available_reference_id(self) -> int:
        highest_id = 0  # If no units, default to 0
        for player in range(0, 9):
            for unit in self.units[player]:
                if highest_id < unit.reference_id:
                    highest_id = unit.reference_id
        return highest_id + 1

    def remove_unit(self, unit: UnitStruct = None, reference_id: int = None):
        if reference_id is not None and unit is not None:
            raise ValueError("Cannot use both unit_ref_id and unit arguments. Use one or the other.")
        if reference_id is None and unit is None:
            raise ValueError("Both unit_ref_id and unit arguments were unused. Use one.")

        if reference_id is not None:
            for player in range(0, 9):
                for i, unit in enumerate(self.units[player]):
                    if unit.reference_id == reference_id:
                        del self.units[player][i]
        elif unit is not None:
            self.units[unit.player.value].remove(unit)
        
        self._update_unit_count()

    def _update_unit_count(self):
        for i in range(0, 9):
            self._players_units[i].unit_count = len(self.units[i])