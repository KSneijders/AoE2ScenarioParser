from __future__ import annotations

from typing import Type

from binary_file_parser import BaseStruct, Retriever, Version

from AoE2ScenarioParser.datasets.triggers import EffectType
from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct
from AoE2ScenarioParser.sections.bfp.triggers.trigger_bfp_repr import TriggerBfpRepr


def indentify(repr_str: str, indent = 4) -> str:
    return f"\n{' ' * indent}".join(repr_str.splitlines())


class Effect(TriggerBfpRepr, EffectStruct):
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
        from AoE2ScenarioParser.objects.data_objects.effects.sub_effects import (
            NoneEffect,
            ChangeDiplomacy,
            ResearchTechnology,
            SendChat,
            PlaySound,
            Tribute,
            UnlockGate,
            LockGate,
            ActivateTrigger,
            DeactivateTrigger,
            AiScriptGoal,
            CreateObject,
            TaskObject,
            DeclareVictory,
        )

        try:
            effect_cls: Type[Effect] = {
                EffectType.NONE:                NoneEffect,
                EffectType.CHANGE_DIPLOMACY:    ChangeDiplomacy,
                EffectType.RESEARCH_TECHNOLOGY: ResearchTechnology,
                EffectType.SEND_CHAT:           SendChat,
                EffectType.PLAY_SOUND:          PlaySound,
                EffectType.TRIBUTE:             Tribute,
                EffectType.UNLOCK_GATE:         UnlockGate,
                EffectType.LOCK_GATE:           LockGate,
                EffectType.ACTIVATE_TRIGGER:    ActivateTrigger,
                EffectType.DEACTIVATE_TRIGGER:  DeactivateTrigger,
                EffectType.AI_SCRIPT_GOAL:      AiScriptGoal,
                EffectType.CREATE_OBJECT:       CreateObject,
                EffectType.TASK_OBJECT:         TaskObject,
                EffectType.DECLARE_VICTORY:     DeclareVictory,
            }[EffectType(struct._type)]
        except ValueError:
            raise ValueError(f"No Effect found for ID: '{struct._type}'")

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
