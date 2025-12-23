from typing import TypedDict


class LegacyEffectDefinition(TypedDict):
    name: str
    attributes: list[str]
    default_attributes: dict[str, str | int]


class AttributeDefinition(TypedDict):
    name: str
    ref: str | None
    type: str
    description: list[str] | str
    default: None | bool | str | int | list[int] | list[str]


class EffectDefinition(TypedDict):
    id: int
    name: str
    description: list[str] | str
    attributes: list[AttributeDefinition]
