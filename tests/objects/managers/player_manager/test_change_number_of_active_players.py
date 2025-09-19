import pytest

from AoE2ScenarioParser.managers import PlayerManager


def test_change_number_of_active_players(pm: PlayerManager):
    nums = [2, 4, 8]
    for num in nums:
        pm.number_of_players = num

        assert pm.number_of_players == num

        for player in pm.players:
            assert player.active is (player.id <= num)

    with pytest.raises(ValueError):
        pm.number_of_players = 0

    with pytest.raises(ValueError):
        pm.number_of_players = 9
