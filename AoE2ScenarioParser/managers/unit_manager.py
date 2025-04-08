from __future__ import annotations

from typing import Generator, Iterable, Literal

from binary_file_parser import Manager, ret, RetrieverRef

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.exceptions.asp_exceptions import InvalidObjectPlacementError
from AoE2ScenarioParser.sections import DataHeader, ScenarioSections, Settings, Unit, UnitData


class UnitManager(Manager):
    _struct: ScenarioSections

    # Todo: Unit.player (Somehow)

    # @formatter:off
    units: list[list[Unit]] = RetrieverRef(ret(ScenarioSections.unit_data), ret(UnitData.units))
    _next_unit_reference_id: int = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.data_header), ret(DataHeader.next_unit_ref))
    # @formatter:on

    # Todo: Add tests
    @property
    def next_unit_reference_id(self):
        """
        Get a new unit reference ID each time the function is called. Starting from the current highest ID.

        Returns:
            The newly generated ID
        """
        unit_reference_id = self._next_unit_reference_id

        self._next_unit_reference_id += 1

        return unit_reference_id

    # Todo: Add tests
    def change_ownership(self, player: Player, units: Unit | Iterable[Unit]) -> None:
        """
        Change the ownership of the given units

        Args:
            player: The player to switch the units to
            units: The units to switch ownership of
        """
        units = units if isinstance(units, Iterable) else [units]

        self.remove_units(units)
        self.add_units(player, units)

    # Todo: Add tests
    def add_unit(self, player: Player, unit: Unit) -> None:
        """
        Adds a unit for the corresponding player to the scenario

        Args:
            player: The player to add the unit for
            unit: The unit to add
        """
        if not unit.has_reference_id:
            unit.reference_id = self.next_unit_reference_id

        self.units[player].append(unit)

    # Todo: Add tests
    def add_units(self, player: Player, units: Iterable[Unit]) -> None:
        """
        Adds units for the corresponding player to the scenario

        Args:
            player: The player to add the units for
            units: The units to add
        """
        for unit in units:
            self.add_unit(player, unit)

    # Todo: Add tests
    def remove_unit(self, unit: Unit) -> None:
        """
        Removes a unit from the scenario.

        Args:
            unit: The unit to remove
        """
        for player_units in self.units:
            if unit in player_units:
                player_units.remove(unit)
                break

    # Todo: Add tests
    def remove_units(self, units: Iterable[Unit]) -> None:
        """
        Removes units from the scenario.

        Args:
            units: The units to remove
        """
        for unit in units:
            self.remove_unit(unit)

    def apply_global_offset(
        self,
        x_offset: int,
        y_offset: int,
        unit_overflow_action: Literal['remove', 'error']
    ) -> None:
        """
        Globally applies an X,Y offset to all units in the scenario.

        Args:
            x_offset: The X offset to apply to all units in the scenario.
            y_offset: The Y offset to apply to all units in the scenario.
            unit_overflow_action: The action to perform when units become outside the map. Can be either 'remove'
                to remove the units in question or 'error' to throw an error when it happens (so no units are removed
                accidentally).
        """
        map_size = self._struct.map_manager.map_size

        for player_units in self.units:
            to_be_removed_units = []

            for unit in player_units:
                unit.x += x_offset
                unit.y += y_offset

                if not (0 <= unit.x < map_size and 0 <= unit.y < map_size):
                    if unit_overflow_action == 'error':
                        raise InvalidObjectPlacementError(
                            f"Unit [ref: {unit.reference_id}] placed outside"
                            f" of the map {unit.x, unit.y} after applying offset"
                        )
                    elif unit_overflow_action == 'remove':
                        to_be_removed_units.append(unit)

            self.remove_units(to_be_removed_units)
