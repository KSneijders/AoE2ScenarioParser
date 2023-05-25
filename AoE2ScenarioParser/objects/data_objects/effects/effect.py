from __future__ import annotations

from typing import Type

from binary_file_parser import BaseStruct, Retriever, Version

from AoE2ScenarioParser.datasets.triggers import EffectType
from AoE2ScenarioParser.objects.data_objects.effects.none_effect import NoneEffect
from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct


class Effect(EffectStruct):
    def __init__(
            self,
            struct_version: Version = None,
            parent: BaseStruct = None,
            local_vars=None,
            **retriever_inits,
    ):
        if len(retriever_inits) > 0:
            struct_version = struct_version or Version((3, 5, 1, 47))

            super().__init__(struct_version, parent, **retriever_inits)
            return

        for ref in self._refs:
            name = (
                ref.retriever.p_name
                if isinstance(ref.retriever, Retriever)
                else ref.retriever.get_p_name(struct_version)
            )
            retriever_inits[name] = local_vars[ref.name]

        super().__init__(struct_version, parent, **retriever_inits)

    @staticmethod
    def _make_effect(struct: Effect, type_: EffectType = EffectType.NONE) -> Effect:
        effect_cls: Type[Effect] = {
            EffectType.NONE: NoneEffect,
        }[type_]

        return effect_cls(
            **{ref.name: None for ref in effect_cls._refs},
            struct_version=struct.struct_version,
            parent=struct.parent,
            **struct.retriever_name_value_map,
        )
