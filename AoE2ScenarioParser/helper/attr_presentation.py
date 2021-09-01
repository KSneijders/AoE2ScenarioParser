from typing import Dict

from AoE2ScenarioParser.helper.string_manipulations import q_str

from AoE2ScenarioParser.datasets.conditions import attribute_presentation as condition_attribute_presentation
from AoE2ScenarioParser.datasets.effects import attribute_presentation as effect_attribute_presentation
from AoE2ScenarioParser.datasets.players import PlayerId, PlayerColorId
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.datasets.trigger_lists import DiplomacyState, Operation, AttackStance, UnitAIAction, \
    ButtonLocation, PanelLocation, TimeUnit, VisibilityState, DifficultyLevel, TechnologyState, Comparison, \
    ObjectAttribute, Attribute, ObjectType, ObjectClass, TerrainRestrictions, HeroStatusFlag, BlastLevel, \
    SmartProjectile, DamageClass, Hotkey, ColorMood, ObjectState
from AoE2ScenarioParser.helper.helper import get_enum_from_unit_const
from AoE2ScenarioParser.helper.pretty_format import pretty_format_name

_datasets = {
    "DiplomacyState": DiplomacyState,
    "Operation": Operation,
    "AttackStance": AttackStance,
    "UnitAIAction": UnitAIAction,
    "ButtonLocation": ButtonLocation,
    "PanelLocation": PanelLocation,
    "TimeUnit": TimeUnit,
    "VisibilityState": VisibilityState,
    "DifficultyLevel": DifficultyLevel,
    "TechnologyState": TechnologyState,
    "Comparison": Comparison,
    "ObjectAttribute": ObjectAttribute,
    "Attribute": Attribute,
    "ObjectType": ObjectType,
    "ObjectClass": ObjectClass,
    "TerrainRestrictions": TerrainRestrictions,
    "HeroStatusFlag": HeroStatusFlag,
    "BlastLevel": BlastLevel,
    "SmartProjectile": SmartProjectile,
    "DamageClass": DamageClass,
    "Hotkey": Hotkey,
    "ColorMood": ColorMood,
    "ObjectState": ObjectState,
}

_other = {
    'bool': lambda v: str(bool(v)),
    'PlayerId': lambda p: f"PlayerId.{PlayerId(p).name}",
    'PlayerColorId': lambda p: f"PlayerColorId.{PlayerColorId(p+1).name}",
    'str': q_str
}

_combined_info_datasets = ["UnitInfo", "BuildingInfo", "OtherInfo", "HeroInfo", ]
_other_info_datasets = {"TechInfo": TechInfo}


def transform_effect_attr_value(effect_type, attr, val):
    return transform_attr_value('e', effect_type, attr, val)


def transform_condition_attr_value(condition_type, attr, val):
    return transform_attr_value('c', condition_type, attr, val)


def transform_attr_value(ce, type_, attr, val):
    source: Dict[int, Dict[str, str]]
    source = condition_attribute_presentation if ce == 'c' else effect_attribute_presentation

    representation = get_presentation_value(attr, source, type_)

    if representation == "":
        return val

    new_val, needs_format = transform_value_by_representation(representation, val)

    if new_val is None:
        raise ValueError(f"Unknown representation: '{representation}'")
    if needs_format:
        new_val = f"{pretty_format_name(new_val)}"
    return new_val + (f" ({val})" if representation != "str" else "")


def get_presentation_value(key, source, type_):
    if key in source[type_]:
        return source[type_][key]
    return source[-1][key]


def transform_value_by_representation(representation, value):
    try:
        if representation in _datasets:
            return _datasets[representation](value).name, True
        if representation in _combined_info_datasets:
            return get_enum_from_unit_const(value).from_id(value).name, True
        if representation in _other_info_datasets:
            return _other_info_datasets[representation].from_id(value).name, True
        if representation in _other:
            return _other[representation](value), False
    except KeyError:
        return f"Unknown{value}", False
