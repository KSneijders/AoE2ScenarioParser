from typing import TypedDict


class AttributeDefinition(TypedDict):
    name: str
    ref: str | None
    type: str
    description: list[str] | str
    default: None | bool | str | int | list[int] | list[str]


class ConditionDefinition(TypedDict):
    id: int
    name: str
    description: list[str] | str
    attributes: list[AttributeDefinition]
