from binary_file_parser.retrievers import RetrieverRef

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.datasets.triggers import EffectType
from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect
from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct


class ResearchTechnology(Effect):
    source_player = RetrieverRef(EffectStruct._source_player)
    technology = RetrieverRef(EffectStruct._technology)
    force = RetrieverRef(EffectStruct._force_research_technology)

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
            force: If the technology should be researched even if it's not available to the civilization of the
                source_player
        """
        super().__init__(type=EffectType.RESEARCH_TECHNOLOGY, local_vars=locals(), **kwargs)
