from binary_file_parser.retrievers import RetrieverRef

from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect
from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct


class ResearchTechnology(Effect):
    """
    Research a technology for the source player
    """
    force = RetrieverRef(EffectStruct.force_research_technology)
    source_player = RetrieverRef(EffectStruct._source_player)
    technology = RetrieverRef(EffectStruct._technology)
