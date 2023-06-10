from typing import overload

from binary_file_parser.retrievers import RetrieverRef

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.datasets.support.info_dataset_base import InfoDatasetBase
from AoE2ScenarioParser.datasets.triggers import EffectType
from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect
from AoE2ScenarioParser.objects.support import TileT, Tile
from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct


class CreateObject(Effect):
    source_player: Player = RetrieverRef(EffectStruct._source_player)  # type:ignore
    """The player to create the object for"""
    object: InfoDatasetBase = RetrieverRef(EffectStruct._object_list_unit_id)  # type:ignore
    """The object (i.e. unit / building / hero) to create"""
    location: Tile = RetrieverRef(EffectStruct._location)  # type: ignore
    """The location where to create the object. If obstructed the creation fails without retrying"""
    facet: int = RetrieverRef(EffectStruct._facet)  # type: ignore
    """The rotation of the created unit"""

    # @overload
    # def __init__(self, source_player: Player, object: InfoDatasetBase, location: TileT): ...

    # @overload
    # def __init__(self, source_player: Player, object: InfoDatasetBase, location: TileT, facet: int): ...

    def __init__(
        self,
        source_player: Player,
        object: InfoDatasetBase,
        location: TileT,
        facet: int = -1,
        **kwargs,
    ):
        """
        Create an object for the source_player

        Args:
            source_player: The player to create the object for
            object: The object (i.e. unit / building / hero) to create
            location: The location where to create the object. If obstructed the creation fails without retrying
            facet: The rotation of the created unit
        """
        super().__init__(local_vars = locals(), **kwargs)

    @property
    def type(self) -> EffectType:
        return EffectType.CREATE_OBJECT
