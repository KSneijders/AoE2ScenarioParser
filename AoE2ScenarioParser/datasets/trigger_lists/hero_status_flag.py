from __future__ import annotations

from typing import Dict

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntFlags


class HeroStatusFlag(_DataSetIntFlags):
    """
    This enum class provides the integer values for the different hero status flags that can be used in the 'Modify
    Attribute' effect with the 'Hero Status' attribute. This is a combinable bit field

    **Methods**

    - ``HeroStatusFlag.combine()``
    - ``HeroStatusFlag.split_flags()``


    **Examples**

    >>> HeroStatusFlag.HERO_REGENERATION
    <HeroStatusFlag.HERO_REGENERATION: 4>
    >>> HeroStatusFlag.HERO_REGENERATION | HeroStatusFlag.HERO_GLOW
    <HeroStatusFlag.HERO_GLOW|HERO_REGENERATION: 68>
    >>> HeroStatusFlag.combine(hero_regeneration=True, hero_glow=True)
    <HeroStatusFlag.HERO_GLOW|HERO_REGENERATION: 68>
    """

    @staticmethod
    def combine(
            full_hero_status: bool = False,
            cannot_be_converted: bool = False,
            hero_regeneration: bool = False,
            defensive_stance_by_default: bool = False,
            protected_formation: bool = False,
            delete_confirmation: bool = False,
            hero_glow: bool = False,
            invert_all_flags: bool = False
    ) -> HeroStatusFlag:
        """
        This method combines the given hero status flags into an integer value

        Args:
            full_hero_status: Enabling this for a unit grants all the flags mentioned below except invert_all_flags
            cannot_be_converted: Enabling this for a unit makes it un-convertable
            hero_regeneration: Enabling this for a unit grants 0.5 HP/s heal rate to the unit
            defensive_stance_by_default: Enabling this for a unit makes it be on defensive stance by default
            protected_formation: Enabling this for a unit makes it be in protected formation by default
            delete_confirmation: Enabling this for a unit will bring up a delete confirmation for the unit when trying
            to delete it IF the player has them enabled
            hero_glow: Enabling this for a unit grants it the golden hero glow effect
            invert_all_flags: Enabling this for a unit will invert all the above flags except full_hero_status

        Returns:
            An integer combining all the different hero status flags into one value
        """
        total = 1 if full_hero_status else 0
        total += 2 if cannot_be_converted else 0
        total += 4 if hero_regeneration else 0
        total += 8 if defensive_stance_by_default else 0
        total += 16 if protected_formation else 0
        total += 32 if delete_confirmation else 0
        total += 64 if hero_glow else 0
        total += 128 if invert_all_flags else 0
        return HeroStatusFlag(total)

    @staticmethod
    def split_flags(value: int) -> Dict[HeroStatusFlag, bool]:
        """
        Split the Hero Status flags into boolean variables related to their effects

        Args:
            value: An integer value representing all the hero status flags set

        Returns:
            A dict with all the flags values as keys and a bool as their value
        """
        flags = {}
        for flag in HeroStatusFlag:
            flags[flag] = bool(flag & value)

        return flags

    NO_HERO_STATUS = 0
    FULL_HERO_STATUS = 1
    CANNOT_BE_CONVERTED = 2
    HERO_REGENERATION = 4
    DEFENSIVE_STANCE_BY_DEFAULT = 8
    PROTECTED_FORMATION = 16
    DELETE_CONFIRMATION = 32
    HERO_GLOW = 64
    INVERT_FLAGS = 128
