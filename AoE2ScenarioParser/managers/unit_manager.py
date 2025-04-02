from __future__ import annotations

from binary_file_parser import Manager, ret, RetrieverRef

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.sections import DataHeader, ScenarioSections, Settings, Unit, UnitData


class UnitManager(Manager):
    _struct: ScenarioSections

    # @formatter:off
    units: list[list[Unit]] = RetrieverRef(ret(ScenarioSections.unit_data), ret(UnitData.units))
    _next_unit_reference_id: int = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.data_header), ret(DataHeader.next_unit_ref))
    # @formatter:on

    @property
    def next_unit_reference_id(self):
        """
        Get a new unit reference ID each time the function is called. Starting from the current highest ID.

        Returns:
            The newly generated ID
        """
        self._next_unit_reference_id += 1

        return self._next_unit_reference_id

    def add_unit(self, player: Player, unit: Unit) -> None:
        """
        Adds a unit for the corresponding player to the scenario

        Args:
            player: The player to add the unit for
            unit: The unit to add
        """
        if not unit.has_reference_id:
            unit.reference_id = self._next_unit_reference_id

        self.units[player].append(unit)

    def apply_global_offset(self, x_offset: int, y_offset: int) -> None:
        """
        Globally applies an X,Y offset to all units in the scenario.

        Args:
            x_offset: The X offset to apply to all units in the scenario.
            y_offset: The Y offset to apply to all units in the scenario.
        """
        for player_units in self.units:
            for unit in player_units:
                unit.x += x_offset
                unit.y += y_offset
