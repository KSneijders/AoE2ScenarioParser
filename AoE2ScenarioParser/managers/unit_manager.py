from __future__ import annotations

from typing import Generator, Iterable, Literal

from bfp_rs import Manager, ret, RetrieverRef

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.exceptions.asp_exceptions import InvalidObjectPlacementError
from AoE2ScenarioParser.objects.support import Area
from AoE2ScenarioParser.sections import DataHeader, ScenarioSections, Settings, Unit, UnitData


class UnitManager(Manager):
    _struct: ScenarioSections

    # @formatter:off
    _units: list[list[Unit]]     = RetrieverRef(ret(ScenarioSections.unit_data), ret(UnitData.units))
    _next_unit_reference_id: int = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.data_header), ret(DataHeader.next_unit_ref))
    # @formatter:on

    def _initialize_properties(self):
        self._assign_unit_properties()

    @property
    def units(self) -> list[list[Unit]]:
        return self._units

    @units.setter
    def units(self, units: list[list[Unit]]) -> None:
        if len(units) != 0 and not isinstance(units[0], list):
            raise ValueError("List of units must be nested list")

        self._units = [
            units[i] if i < len(units) else [] for i in range(9)
        ]

        self._assign_unit_properties()

    def _assign_unit_properties(self):
        highest_reference_id = self._next_unit_reference_id

        for player in Player:
            for unit in self._units[player]:
                highest_reference_id = max(highest_reference_id, unit.reference_id + 1)
                unit._player = player
        self._next_unit_reference_id = highest_reference_id

    def get_all_units(self) -> Generator[Unit]:
        return (unit for player_units in self.units for unit in player_units)

    @property
    def next_unit_reference_id(self) -> int:
        """
        Get a new unit reference ID each time the function is called. Starting from the current highest ID.

        Returns:
            The newly generated ID
        """
        unit_reference_id = self._next_unit_reference_id

        self._next_unit_reference_id += 1

        return unit_reference_id

    def change_ownership(self, player: Player, units: Unit | Iterable[Unit]) -> list[Unit]:
        """
        Change the ownership of the given units

        Args:
            player: The player to switch the units to
            units: The units to switch ownership of
        """
        units = units if isinstance(units, Iterable) else [units]

        self.remove_units(units)
        return self.add_units(player, units)

    def add_unit(self, player: Player, unit: Unit) -> Unit:
        """
        Adds a unit for the corresponding player to the scenario

        Args:
            player: The player to add the unit for
            unit: The unit to add

        Returns:
            The added unit
        """
        if not unit.has_reference_id:
            unit.reference_id = self.next_unit_reference_id

        # Set read-only player attribute for unit
        unit._player = player

        self.units[player].append(unit)

        return unit

    def add_units(self, player: Player, units: Iterable[Unit]) -> list[Unit]:
        """
        Adds units for the corresponding player to the scenario

        Args:
            player: The player to add the units for
            units: The units to add

        Returns:
            The added units
        """
        return [self.add_unit(player, unit) for unit in units]

    def clone_unit(self, unit: Unit, player: Player = None) -> Unit:
        """
        Creates and adds a clone of the given unit to the game world. The cloned unit will
        inherit the properties of the original unit, including its position, type, state,
        rotation, frame, and other relevant attributes. If no player is specified, the
        clone will belong to the same player as the original unit.

        Args:
            unit: The unit to clone.
            player: The player to which the cloned unit should belong. Defaults to the player of the original unit.

        Returns:
            Unit: The newly added cloned unit.
        """
        if unit.player is None and player is None:
            raise ValueError("Either unit.player or player must be specified")

        return self.add_unit(player or unit.player, Unit(
            reference_id=-1,
            x=unit.x,
            y=unit.y,
            z=unit.z,
            type=unit.type,
            state=unit.state,
            rotation=unit.rotation,
            frame=unit.frame,
            garrisoned_in_ref=unit.garrisoned_in_ref,
            caption_string_id=unit.caption_string_id,
            caption_string=unit.caption_string,
        ))

    def remove_unit(self, unit: Unit) -> None:
        """
        Removes a unit from the scenario.

        Args:
            unit: The unit to remove
        """
        if unit.player is None:
            for units in self.units:
                if unit in units:
                    units.remove(unit)

            return

        if unit in self.units[unit.player]:
            self.units[unit.player].remove(unit)

    def remove_units(self, units: Iterable[Unit]) -> None:
        """
        Removes units from the scenario.

        Args:
            units: The units to remove
        """
        for unit in units:
            self.remove_unit(unit)

    # Todo: Add tests
    def import_units(self, player: Player, units: Iterable[Unit]) -> list[Unit]:
        """
        Imports units (resetting the reference_id) for the corresponding player to the scenario.

        Args:
            player: The player to add the unit for
            units: The units to add
        """
        result = []
        for unit in units:
            unit.reference_id = -1
            result.append(self.add_unit(player, unit))

        return result

    def filter_units_by(
        self,
        attr: str,
        attr_values: list[int],
        is_allowlist: bool = True,
        players: Iterable[Player] = None,
        *,
        units: Iterable[Unit] = None,
    ) -> Generator[Unit]:
        """
        Filter units based on a given attribute of units

        Args:
            attr: The attribute to filter by
            attr_values: The values for the attributes to filter with
            is_allowlist: Use the given attrs list as allowlist instead of blocklist
            players: A list of players to filter from. If not used, all players are used.
            units: A set of units to filter from. If not used, all units are used.

        Returns:
            A generator of units matching the given attribute requirements

        Raises:
            AttributeError: If the provided attr does not exist on objects of the Unit class
        """
        if units is None:
            units = self.get_all_units()
        if players is not None:
            units = [unit for unit in units if unit.player in players]

        # Both return statements can be combined using: ``(getattr(unit, attr) in attr_values) == is_allowlist``
        # But splitting them helps performance (not checking against ``is_allowlist`` for each unit)
        if is_allowlist:
            return (unit for unit in units if getattr(unit, attr) in attr_values)
        return (unit for unit in units if getattr(unit, attr) not in attr_values)

    def filter_units_by_type(
        self,
        unit_types: list[int],
        is_allowlist: bool = True,
        players: Iterable[Player] = None,
        *,
        units: Iterable[Unit] = None,
    ) -> Generator[Unit]:
        """
        Filter unit on their type value.

        Args:
            unit_types: The types to filter with
            is_allowlist: Use the given attrs list as allowlist instead of blocklist
            players: A list of players to filter from. If not used, all players are used.
            units: A set of units to filter from. If not used, all units are used.

        Returns:
            A list of units
        """
        return self.filter_units_by("type", unit_types, is_allowlist, players, units = units)

    def filter_units_by_id(
        self,
        unit_ids: list[int],
        is_allowlist: bool = True,
        players: Iterable[Player] = None,
        *,
        units: Iterable[Unit] = None,
    ) -> Generator[Unit]:
        """
        Filter unit on their id value.

        Args:
            unit_ids: The unit ids to filter with
            is_allowlist: Use the given attrs list as allowlist instead of blocklist
            players: A list of players to filter from. If not used, all players are used.
            units: A set of units to filter from. If not used, all units are used.

        Returns:
            A list of units
        """
        return self.filter_units_by("reference_id", unit_ids, is_allowlist, players, units = units)

    def get_units_in_area(
        self,
        area: Area,
        players: Iterable[Player] = None,
        *,
        units: Iterable[Unit] = None,
    ) -> Generator[Unit]:
        """
        Get all units in a given area. Optionally filter by given players.

        Args:
            area: The area to use when filtering units based on location
            players: An optional iterable of players to filter the units by
            units: An optional iterable of units to filter, if not used, all units on the map are used. Mainly useful
                for narrowing down a selection of units from other filters

        Returns:
            A generator of units in the given area
        """
        if units is None:
            units = list(self.get_all_units())

        if players is None:
            return (unit for unit in units if area.contains(unit.tile))

        return (unit for unit in units if area.contains(unit.tile) and unit.player in players)

    def apply_global_offset(
        self,
        x_offset: int,
        y_offset: int,
        map_size: int = -1,
        unit_overflow_action: Literal['remove', 'error'] = 'error',
    ) -> None:
        """
        Globally applies an (x, y) offset to all units in the scenario.

        Args:
            x_offset: The X offset to apply to all units in the scenario.
            y_offset: The Y offset to apply to all units in the scenario.
            map_size: The value to use for checking
            unit_overflow_action: The action to perform when units become outside the map. Can be either 'remove'
                to remove the units in question or 'error' to throw an error when it happens (so no units are removed
                accidentally). Only checked when map_size is given
        """
        for player_units in self.units:
            units_to_be_removed = []

            for unit in player_units:
                unit.x += x_offset
                unit.y += y_offset

                if map_size == -1:
                    continue

                if not (0 <= unit.x < map_size and 0 <= unit.y < map_size):
                    if unit_overflow_action == 'error':
                        raise InvalidObjectPlacementError(
                            f"Unit [ref: {unit.reference_id}] placed outside"
                            f" of the map {unit.x, unit.y} after applying offset"
                        )
                    elif unit_overflow_action == 'remove':
                        units_to_be_removed.append(unit)

            self.remove_units(units_to_be_removed)
