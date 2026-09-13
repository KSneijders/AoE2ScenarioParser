import pytest
from bfp_rs.errors import MutabilityError

from AoE2ScenarioParser.managers import TriggerManager
from tests.objects.managers.functions import create_trigger


def test_mutability(tm: TriggerManager):
    with pytest.raises(MutabilityError, match = r'This list is set as immutable'):
        tm.triggers.extend([])

    trigger = create_trigger()
    with pytest.raises(MutabilityError, match = r'This list is set as immutable'):
        trigger.effects.extend([])

    with pytest.raises(MutabilityError, match = r'This list is set as immutable'):
        trigger.conditions.extend([])
