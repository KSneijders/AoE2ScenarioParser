from AoE2ScenarioParser.helper.alias import Alias


class PlayerObject:
    """
    The player object is providing handlers that match the features of the player
    tab in the in-game editor

    Since player data is scattered around the scenario file, it provides a
    centralized way to access meaningful data about one player
    """
    active: bool = Alias('self._player_data_one[self._internal_player_id].active')
    human = Alias('self._player_data_one[self._internal_player_id].human')
    civilization = Alias('self._player_data_one[self._internal_player_id].civilization')
    gold = Alias('self._resources[self._internal_player_id].gold')
    wood = Alias('self._resources[self._internal_player_id].wood')
    food = Alias('self._resources[self._internal_player_id].food')
    stone = Alias('self._resources[self._internal_player_id].stone')
    color = Alias('self._resources[self._internal_player_id].player_color')
    starting_age = Alias('self._per_player_starting_age[self._internal_player_id]')

    def __init__(self, player_id, parsed_data):
        self._player_data_one = parsed_data['DataHeaderPiece'].player_data_1
        self._resources = parsed_data['PlayerDataTwoPiece'].resources
        self._player_data_four = parsed_data['UnitsPiece'].player_data_4
        self._per_player_starting_age = parsed_data['OptionsPiece'].per_player_starting_age

        self.player_id = player_id  # 0 = Gaia, 1-8 players, to be consistent with units

    @property
    def pop_limit(self):
        if self.player_id == 0:  # Gaia has no pop limit
            return -1
        return self._player_data_four[self._internal_player_id].population_limit

    @pop_limit.setter
    def pop_limit(self, val):
        if self.player_id != 0:
            self._player_data_four[self._internal_player_id].population_limit = val

    @staticmethod
    def create_player_list(parsed_data):
        return [PlayerObject(i, parsed_data) for i in range(0, 9)]

    @property
    def _internal_player_id(self):
        """
        Player data is sometimes stored internally as 0-7 players and 8 Gaia
        We should be consistent and only expose data in the same format,
        so the chosen one is 0 Gaia and 1-8 players
        @param id: the player index in the format 0 = Gaia, 1-8 players
        @return: the corresponding index in the format 0-7 players, 8 = Gaia
        """
        if self.player_id == 0:
            return 8
        return self.player_id - 1

    def __repr__(self):
        result = ""
        result += "active " + str(self.active) + "\n"
        result += "human " + str(self.human) + "\n"
        result += "civilization " + str(self.civilization) + "\n"
        result += "gold " + str(self.gold) + "\n"
        result += "wood " + str(self.wood) + "\n"
        result += "food " + str(self.food) + "\n"
        result += "stone " + str(self.stone) + "\n"
        result += "color " + str(self.color) + "\n"
        result += "pop_limit " + str(self.pop_limit) + "\n"
        result += "starting_age " + str(self.starting_age) + "\n"
        return result
