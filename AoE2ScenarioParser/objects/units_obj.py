from __future__ import annotations

from typing import List

from AoE2ScenarioParser.datasets.players import Player
from AoE2ScenarioParser.helper import parser
from AoE2ScenarioParser.helper.helper import Tile
from AoE2ScenarioParser.helper.retriever import find_retriever
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.unit_obj import UnitObject
from AoE2ScenarioParser.pieces.structs.player_units import PlayerUnitsStruct


class UnitsObject(AoE2Object):
    def __init__(self,
                 units: List[List[UnitObject]]
                 ):

        self.units = units

        super().__init__()

    def add_unit(self, player: Player, unit_id: int, x: int, y: int, z: int = 0, rotation: int = 0,
                 garrisoned_in_id: int = -1, animation_frame: int = 0, status: int = 2,
                 reference_id: int = None, ) -> UnitObject:
        """
        Adds a unit to the scenario.

        Args:
            player: The player the unit belongs to.
            unit_id: Defines what unit you're placing. The IDs used in the unit/buildings dataset.
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
            reference_id = self.get_new_reference_id()

        unit = UnitObject(
            player=player,
            x=x,
            y=y,
            z=z,
            reference_id=reference_id,
            unit_id=unit_id,
            status=status,
            rotation=rotation,
            animation_frame=animation_frame,
            garrisoned_in_id=garrisoned_in_id,
        )

        self.units[player.value].append(unit)
        return unit

    def get_player_units(self, player: Player) -> List[UnitObject]:
        """
        Returns a list of UnitObjects for the given player.

        Raises:
            ValueError: If player is not between 0 (GAIA) and 8 (EIGHT)
        """
        if not 0 <= player.value <= 8:
            raise ValueError("Player must have a value between 0 and 8")
        return self.units[player.value]

    def get_all_units(self) -> List[UnitObject]:
        units = []
        for player_units in self.units:
            units += player_units
        return units

    def get_units_in_area(self, x1: float = None, y1: float = None, x2: float = None, y2: float = None,
                          tile1: Tile = None, tile2: Tile = None, unit_list: List[UnitObject] = None,
                          players: List[Player] = None, ignore_players: List[Player] = None):
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
            raise ValueError("Cannot use both whitelist and blacklist at the same time")

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

    def remove_eye_candy(self) -> None:
        eye_candy_ids = [1351, 1352, 1353, 1354, 1355, 1358, 1359, 1360, 1361, 1362, 1363, 1364, 1365, 1366]
        self.units[0] = [gaia_unit for gaia_unit in self.units[0] if gaia_unit.unit_id not in eye_candy_ids]

    def change_ownership(self, unit: UnitObject, to_player: Player) -> None:
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
                return

    def get_new_reference_id(self) -> int:
        highest_id = 0  # If no units, default to 0
        for player in range(0, 9):
            for unit in self.units[player]:
                if highest_id < unit.reference_id:
                    highest_id = unit.reference_id
        return highest_id

    @staticmethod
    def _parse_object(parsed_data, **kwargs) -> UnitsObject:
        object_piece = parsed_data['UnitsPiece']
        units_per_player = find_retriever(object_piece.retrievers, "Player Units").data

        player_units = []
        for player_id in range(0, 9):  # 0 Gaia & 1-8 Players:
            player_units.append([])
            units = parser.listify(find_retriever(units_per_player[player_id].retrievers, "Units").data)

            for unit in units:
                player_units[player_id].append(
                    UnitObject._parse_object(parsed_data, unit=unit, player=Player(player_id))
                )

        return UnitsObject(
            units=player_units
        )

    @staticmethod
    def _reconstruct_object(parsed_data, objects, **kwargs) -> None:  # Expected {}
        player_units_retriever = find_retriever(parsed_data['UnitsPiece'].retrievers, "Player Units")

        player_units_retriever.data = []
        for player_units in objects['UnitsObject'].units:

            units_list = []
            for unit in player_units:
                UnitObject._reconstruct_object(parsed_data, objects, unit=unit, units=units_list)

            player_units_retriever.data.append(
                PlayerUnitsStruct(data=[len(units_list), units_list])
            )
