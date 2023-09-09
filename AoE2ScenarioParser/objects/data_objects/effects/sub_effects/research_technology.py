from binary_file_parser.retrievers import RetrieverRef

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.datasets.triggers import EffectType
from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect
from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct


class ResearchTechnology(Effect):
    _type_ = EffectType.RESEARCH_TECHNOLOGY

    source_player: Player = RetrieverRef(EffectStruct._source_player)  # type: ignore
    """The player to research the technology for"""
    technology: TechInfo = RetrieverRef(EffectStruct._technology)  # type: ignore
    """The technology to research"""
    force: bool = RetrieverRef(EffectStruct._force_research_technology)  # type: ignore
    """If enabled, research the technology even if it has already been researched or not available in the tech tree"""

    # @overload
    # def __init__(self, source_player: Player, technology: TechInfo): ...

    # @overload
    # def __init__(self, source_player: Player, technology: TechInfo, force: bool): ...

    def __init__(
        self,
        source_player: Player,
        technology: TechInfo,
        force: bool = False,
        **kwargs,
    ):
        """
        Research a technology for the source_player

        Args:
            source_player: The player to research the technology for
            technology: The technology to research
            force: If enabled, research the technology even if it has already been researched or not available in the
                tech tree
        """
        super().__init__(local_vars = locals(), **kwargs)
