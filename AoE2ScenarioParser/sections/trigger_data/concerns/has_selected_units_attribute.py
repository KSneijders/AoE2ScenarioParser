from __future__ import annotations

from typing import Iterable, TYPE_CHECKING

if TYPE_CHECKING:
    from AoE2ScenarioParser.sections import Unit


# These are all solved for a class getting this as a super class
# noinspection PyUnresolvedReferences,PyTypeChecker,PyAttributeOutsideInit
class HasSelectedUnitsAttribute:

    @property
    def selected_units(self) -> tuple[Unit, ...]:
        return self._selected_units

    # noinspection PyProtectedMember
    @selected_units.setter
    def selected_units(self, value: Iterable[Unit]):
        missing_units = tuple(unit for unit in self._selected_units if unit not in value)
        new_units = tuple(unit for unit in value if unit not in self._selected_units)

        for unit in missing_units:
            unit._remove_trigger_artifact_reference(self)

        self._selected_units: tuple[Unit, ...] = tuple(value)

        for unit in new_units:
            unit._add_trigger_artifact_reference(self)

        self._selected_unit_ref_ids.clear()
        for unit in self._selected_units:
            self._selected_unit_ref_ids.append(unit.reference_id)

    def add_selected_unit(self, value: Unit):
        self.selected_units = (*self.selected_units, value)

    #  -------------------------- Unit Reference functions -------------------------- #

    def _get_unit_references(self, key: str = '') -> tuple['Unit', ...]:
        return self.selected_units

    # noinspection PyProtectedMember
    def _remove_unit_reference(self, unit: 'Unit', _: str = '') -> None:
        unit._remove_trigger_artifact_reference(self)

        self._selected_units = tuple(existing for existing in self.selected_units if existing is not unit)

    # noinspection PyProtectedMember
    def _add_unit_reference(self, unit: 'Unit', _: str = '') -> None:
        if any(unit is existing for existing in self.selected_units):
            return

        unit._add_trigger_artifact_reference(self)

        self._selected_units = (
            *self.selected_units,
            unit,
        )
