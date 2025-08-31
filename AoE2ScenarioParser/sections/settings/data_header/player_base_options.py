from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version
from bfp_rs.types.le import bool32, u32

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST
from AoE2ScenarioParser.sections.settings.data_header.resources import Resources


class PlayerBaseOptions(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    active: bool             = Retriever(bool32,                              default = False)
    starting_resources: int  = Retriever(Resources, max_ver = Version(1, 13), default_factory = Resources)
    human: bool              = Retriever(bool32,                              default = False)
    civilization: int        = Retriever(u32,                                 default = 65537)
    architecture: int        = Retriever(u32,       min_ver = Version(1, 40), default = 65537)
    posture: int             = Retriever(u32,                                 default = 4)

    # _civilization_1_36: int = Retriever(u32, default = 36,                           max_ver = Version(1, 40))
    # _civilization_1_41: int = Retriever(u32, default = 38, min_ver = Version(1, 41), max_ver = Version(1, 42))
    # _civilization_1_43: int = Retriever(u32, default = 40, min_ver = Version(1, 43), max_ver = Version(1, 45))
    # _civilization_1_46: int = Retriever(u32, default = 43, min_ver = Version(1, 46))
    #
    # _architecture_1_40: int = Retriever(u32, default = 36, min_ver = Version(1, 40), max_ver = Version(1, 40))
    # _architecture_1_41: int = Retriever(u32, default = 38, min_ver = Version(1, 41), max_ver = Version(1, 42))
    # _architecture_1_43: int = Retriever(u32, default = 40, min_ver = Version(1, 43), max_ver = Version(1, 45))
    # _architecture_1_46: int = Retriever(u32, default = 43, min_ver = Version(1, 46))

    # civilization = RetrieverCombiner(_civilization_1_36, _civilization_1_41, _civilization_1_43, _civilization_1_46)
    # architecture = RetrieverCombiner(_architecture_1_40, _architecture_1_41, _architecture_1_43, _architecture_1_46)

    # @formatter:on
