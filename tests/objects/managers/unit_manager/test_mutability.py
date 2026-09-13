import pytest
from bfp_rs.errors import MutabilityError

from AoE2ScenarioParser.managers import UnitManager


def test_mutability(um: UnitManager):
    with pytest.raises(MutabilityError, match = r'This list is set as immutable'):
        um.units.extend([])

    with pytest.raises(MutabilityError, match = r'This list is set as immutable'):
        um.units[0].extend([])

    with pytest.raises(MutabilityError, match = r'This list is set as immutable'):
        um.units[-1].extend([])
