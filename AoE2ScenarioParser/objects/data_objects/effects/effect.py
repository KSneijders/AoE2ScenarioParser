from __future__ import annotations

from typing import Type

from binary_file_parser import BaseStruct, Retriever, Version

from AoE2ScenarioParser.datasets.triggers import EffectType
from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct
from AoE2ScenarioParser.sections.bfp.triggers.trigger_bfp_repr import TriggerBfpRepr


def indentify(repr_str: str, indent = 4) -> str:
    return f"\n{' ' * indent}".join(repr_str.splitlines())


class Effect(TriggerBfpRepr, EffectStruct):
    _type_ = EffectType.NONE
    _type_map: dict[EffectType | int, Type[Effect]] = {}

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

        retriever_inits['_type'] = self._type_

        for ref in self._refs:
            if isinstance(ref.retriever, Retriever):
                name = ref.retriever.p_name
            else:
                name = ref.retriever.get_p_name(struct_ver)

            retriever_inits[name] = local_vars[ref.name]
        super().__init__(struct_ver, parent, **retriever_inits)

    @staticmethod
    def _make_effect(struct: EffectStruct) -> Effect:
        # noinspection PyUnresolvedReferences
        import AoE2ScenarioParser.objects.data_objects.effects.sub_effects

        try:
            effect_cls = Effect._type_map[struct._type]
        except KeyError:
            raise TypeError(f"No Effect type found for: '{struct._type}'")

        return effect_cls(
            **{ref.name: None for ref in effect_cls._refs},
            struct_ver = struct.struct_ver,
            parent = struct.parent,
            **struct.retriever_name_value_map,
        )

    @property
    def type(self) -> EffectType:
        """Returns the EffectType of this effect"""
        return EffectType(self._type)

    def __init_subclass__(cls, **kwargs):
        cls._refs, Effect._refs = cls._refs.copy(), []

        # Map the EffectType to the class
        cls._type_map[cls._type_] = cls
