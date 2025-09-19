import pytest

from AoE2ScenarioParser.managers import PlayerManager
from AoE2ScenarioParser.objects.support import Tile
from datasets.player_data import Civilization
from datasets.trigger_data import DiplomacyStance
from objects.support import Point


def test_no_gaia_attributes(pm: PlayerManager):
    gaia = pm.players[0]
    p1 = pm.players[1]

    assert gaia.diplomacy is None
    assert p1.diplomacy is not None

    with pytest.raises(AttributeError):
        gaia.diplomacy = [DiplomacyStance.ALLY] * 16


def test_dataset_attributes(pm: PlayerManager):
    p1 = pm.players[1]

    p1.civilization = Civilization.WEI
    assert p1.civilization == Civilization.WEI

    p1.civilization = 50
    assert p1.civilization == Civilization.WU


def test_view_attributes(pm: PlayerManager):
    p1 = pm.players[1]

    p1.view = (1, 4)
    assert p1.view == Tile(1, 4)
    p1.view = Tile(4, 5)
    assert p1.view == Tile(4, 5)

    p1.editor_view = (1.5, 1.2)
    assert p1.editor_view == Point(1.5, 1.2)
    p1.editor_view = Point(4.5, 5.1)
    assert p1.editor_view == Point(4.5, 5.1)
