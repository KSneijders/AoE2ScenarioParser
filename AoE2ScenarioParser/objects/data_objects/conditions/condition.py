from __future__ import annotations

from typing import Type

from binary_file_parser import BaseStruct, Retriever, Version

from AoE2ScenarioParser.datasets.triggers.condition_type import ConditionType
from AoE2ScenarioParser.sections.bfp.triggers import ConditionStruct
from AoE2ScenarioParser.sections.bfp.triggers.trigger_bfp_repr import TriggerBfpRepr


def indentify(repr_str: str, indent = 4) -> str:
    return f"\n{' ' * indent}".join(repr_str.splitlines())


class Condition(TriggerBfpRepr, ConditionStruct):
    _type_ = ConditionType.NONE
    _type_map: dict[ConditionType | int, Type[Condition]] = {}

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
    def _make_condition(struct: ConditionStruct) -> Condition:
        # noinspection PyUnresolvedReferences
        import AoE2ScenarioParser.objects.data_objects.conditions.sub_conditions

        try:
            condition_cls = Condition._type_map[struct._type]
        except ValueError:
            raise ValueError(f"No Condition found for ID: '{struct._type}'")

        return condition_cls(
            **{ref.name: None for ref in condition_cls._refs},
            struct_ver = struct.struct_ver,
            parent = struct.parent,
            **struct.retriever_name_value_map,
        )

    @property
    def type(self) -> ConditionType:
        """Returns the EffectType of this effect"""
        return ConditionType(self._type)

    def __init_subclass__(cls, **kwargs):
        cls._refs, Condition._refs = cls._refs.copy(), []

        # Map the ConditionType to the class
        cls._type_map[cls._type_] = cls
