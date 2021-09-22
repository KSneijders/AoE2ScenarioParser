from typing import Dict, TYPE_CHECKING, Type

from AoE2ScenarioParser.datasets.support.info_dataset_base import InfoDatasetBase
from AoE2ScenarioParser.helper.string_manipulations import q_str, trunc_string

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
from AoE2ScenarioParser.scenarios import scenario_store

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.data_objects.unit import Unit


def _format_trigger_id_representation(id_, uuid) -> str:
    name = trunc_string(scenario_store.get_trigger_name(uuid, id_))
    return f"\"{name}\""


def _format_unit_reference_representation(ref_id, uuid) -> str:
    def format_unit(u: 'Unit') -> str:
        enum_entry = u.unit_const
        if not issubclass(u.unit_const.__class__, InfoDatasetBase):
            enum_entry = get_enum_from_unit_const(u.unit_const)
        name = pretty_format_name(enum_entry.name)
        return f"{name} [P{u.player}, X{u.x}, Y{u.y}]"

    if type(ref_id) is list:
        units = scenario_store.get_units(uuid, ref_id)
        formatted = '\n\t'.join([f"{i}: {format_unit(unit)} ({unit.reference_id})" for i, unit in enumerate(units)])
        return f"{len(units)} unit(s):\n\t{formatted}"
    else:
        unit = scenario_store.get_unit(uuid, ref_id)
        if unit:
            return format_unit(unit)
    return ""


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
    'PlayerId': lambda p: f"Player {PlayerId(p).name.capitalize()}",
    'PlayerColorId': lambda p: f"{PlayerColorId(p + 1).name.capitalize()}",
    'str': q_str,
}

_combined_info_datasets = [
    "UnitInfo",
    "BuildingInfo",
    "OtherInfo",
    "HeroInfo"
]
_other_info_datasets = {
    "TechInfo": TechInfo
}
_store_references = {
    "TriggerId": _format_trigger_id_representation,
    "Unit": _format_unit_reference_representation,
    "Unit[]": _format_unit_reference_representation,
}


def transform_effect_attr_value(effect_type, attr, val, uuid):
    return transform_attr_value('e', effect_type, attr, val, uuid)


def transform_condition_attr_value(condition_type, attr, val, uuid):
    return transform_attr_value('c', condition_type, attr, val, uuid)


def transform_attr_value(ce, type_, attr, val, uuid):
    source: Dict[int, Dict[str, str]]
    source = condition_attribute_presentation if ce == 'c' else effect_attribute_presentation

    representation = get_presentation_value(attr, source, type_)

    if representation == "":
        return val

    value_representation = transform_value_by_representation(representation, val, uuid)
    return value_representation


def get_presentation_value(key, source, type_):
    if key in source[type_]:
        return source[type_][key]
    return source[-1][key]


def transform_value_by_representation(representation, value, uuid):
    unknown = "Unknown", False

    format_value_repr = True
    suffix_original_value = True

    try:
        if representation in _datasets:
            value_representation = _datasets[representation](value).name

        elif representation in _combined_info_datasets:
            enum_entry = get_enum_from_unit_const(value)
            if enum_entry is not None:
                value_representation = enum_entry.name
            else:
                value_representation, format_value_repr = unknown

        elif representation in _other_info_datasets:
            value_representation = _other_info_datasets[representation].from_id(value).name

        elif representation in _store_references:
            value_representation = _store_references[representation](value, uuid)
            format_value_repr = False

            if representation in ["Unit[]"]:
                suffix_original_value = False

        elif representation in _other:
            value_representation = _other[representation](value)
            format_value_repr = False

            if representation == "str":
                suffix_original_value = False
        else:
            raise ValueError(f"Unknown representation: '{representation}'")
    except KeyError:
        value_representation, format_value_repr = unknown

    if format_value_repr:
        value_representation = pretty_format_name(value_representation)
    if suffix_original_value:
        value_representation += f" ({value})"
    return value_representation
