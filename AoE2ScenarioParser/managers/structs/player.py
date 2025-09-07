from bfp_rs import RefStruct, ret
from bfp_rs.bfp_rs import RetrieverRef
from bfp_rs.combinators import get_attr

from sections import DataHeader, PlayerBaseOptions, ScenarioSections, Settings


class Player(RefStruct):
    _struct: ScenarioSections

    _active = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.data_header), ret(DataHeader.player_base_options), get_attr('index'), ret(PlayerBaseOptions.active))

    @property
    def active(self):
        return self._active

    def __new__(cls, struct: ScenarioSections, index: int):
        self = super().__new__(cls, struct)
        self.index = index
        return self
