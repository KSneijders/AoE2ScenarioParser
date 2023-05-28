from __future__ import annotations

from io import StringIO
from typing import Type

from binary_file_parser import BaseStruct, Retriever, Version

from AoE2ScenarioParser.datasets.triggers import EffectType

from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct

from AoE2ScenarioParser.objects.data_objects.effects.change_diplomacy import ChangeDiplomacy
from AoE2ScenarioParser.objects.data_objects.effects.none_effect import NoneEffect
from AoE2ScenarioParser.objects.data_objects.effects.research_technology import ResearchTechnology


def indentify(repr_str: str, indent = 4) -> str:
    return f"\n{' '*indent}".join(repr_str.splitlines())


class Effect(EffectStruct):
    def __init__(
        self,
        struct_ver: Version = Version((3, 5, 1, 47)),
        parent: BaseStruct = None,
        local_vars = None,
        **retriever_inits,
    ):
        if len(retriever_inits) > 1:
            super().__init__(struct_ver, parent, **retriever_inits)
            return

        for ref in self._refs:
            name = (
                ref.retriever.p_name
                if isinstance(ref.retriever, Retriever)
                else ref.retriever.get_p_name(struct_ver)
            )
            retriever_inits[name] = local_vars[ref.name]
        super().__init__(struct_ver, parent, **retriever_inits)

    @staticmethod
    def _make_effect(struct: EffectStruct) -> Effect:
        effect_cls: Type[Effect] = {
            EffectType.NONE: NoneEffect,
            EffectType.CHANGE_DIPLOMACY: ChangeDiplomacy,
            EffectType.RESEARCH_TECHNOLOGY: ResearchTechnology,
        }[EffectType(struct.type)]

        return effect_cls(
            **{ref.name: None for ref in effect_cls._refs},
            struct_ver = struct.struct_ver,
            parent = struct.parent,
            **struct.retriever_name_value_map,
        )

    def __init_subclass__(cls, **kwargs):
        cls._refs, Effect._refs = cls._refs.copy(), []

    def __repr__(self):
        repr_builder = StringIO()
        repr_builder.write(f"{self.__class__.__name__}(")
        for retriever in self._refs:
            if not retriever.supported(self.struct_ver):
                continue

            obj = getattr(self, retriever.p_name)
            if isinstance(obj, list):
                sub_obj_repr_str = (
                        "[\n    "
                        + ",\n    ".join(map(lambda x: indentify(repr(x)), obj))
                        + ",\n]"
                )
            else:
                sub_obj_repr_str = f"{obj!r}"

            repr_builder.write(f"\n    {retriever.p_name} = {indentify(sub_obj_repr_str)},")
        repr_builder.write("\n)")
        return repr_builder.getvalue()
