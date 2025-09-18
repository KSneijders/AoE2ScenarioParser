from __future__ import annotations

from bfp_rs import RefStruct, ret, RetrieverRef

from AoE2ScenarioParser.managers.structs import Player
from AoE2ScenarioParser.sections import FileHeader, ScenarioSections


class PlayerManager(RefStruct):
    NUM_PLAYERS = 9

    _struct: ScenarioSections

    _number_of_players: int = RetrieverRef(ret(ScenarioSections.file_header), ret(FileHeader.num_players))
    _players: tuple[Player]

    def _initialize_properties(self):
        self._setup_player_objects()

    def _setup_player_objects(self):
        self.players = tuple(Player(self._struct, index = i) for i in range(9))

    @property
    def number_of_players(self) -> int:
        return self._number_of_players

    @number_of_players.setter
    def number_of_players(self, value: int) -> None:
        for index, player in enumerate(self.players[1:]):
            player._active = index < value

        self._number_of_players = value

    @property
    def players(self) -> tuple[Player]:
        return self._players

    @players.setter
    def players(self, value: tuple[Player]):
        if len(value) != PlayerManager.NUM_PLAYERS:
            raise ValueError("List of players must contain 9 Player objects")
        
        self._players = value
