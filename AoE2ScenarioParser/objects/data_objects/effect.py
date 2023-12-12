from __future__ import annotations

from typing import List, Tuple, Any

from AoE2ScenarioParser.datasets import effects
from AoE2ScenarioParser.datasets.effects import EffectId
from AoE2ScenarioParser.datasets.players import PlayerColorId, PlayerId
from AoE2ScenarioParser.datasets.trigger_lists import ObjectAttribute
from AoE2ScenarioParser.exceptions.asp_warnings import IncorrectArmorAttackUsageWarning
from AoE2ScenarioParser.helper.helper import raise_if_not_int_subclass, value_is_valid, validate_coords
from AoE2ScenarioParser.helper.printers import warn
from AoE2ScenarioParser.helper.string_manipulations import add_tabs
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.support.attr_presentation import transform_effect_attr_value
from AoE2ScenarioParser.objects.support.trigger_object import TriggerComponent
from AoE2ScenarioParser.scenarios.scenario_store import getters
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.sections.retrievers.retriever_object_link_group import RetrieverObjectLinkGroup
from AoE2ScenarioParser.sections.retrievers.support import Support


def _add_trail_if_string_attr_is_used_in_effect(obj: Effect, attr_name, val: bytes | str):
    try:
        if attr_name in effects.attributes[obj.effect_type]:
            return val + (b"\x00" if type(val) is bytes else "\x00")
    except KeyError:
        pass
    return val


class Effect(AoE2Object, TriggerComponent):
    """Object for handling an effect."""
    hidden_attribute = 'effect_type'

    _link_list = [
        RetrieverObjectLinkGroup("Triggers", "trigger_data[__index__].effect_data[__index__]", group=[
            RetrieverObjectLink("effect_type"),
            RetrieverObjectLink("ai_script_goal"),
            RetrieverObjectLink("quantity"),
            RetrieverObjectLink("tribute_list"),
            RetrieverObjectLink("diplomacy"),
            RetrieverObjectLink("legacy_location_object_reference"),
            RetrieverObjectLink("object_list_unit_id"),
            RetrieverObjectLink("source_player"),
            RetrieverObjectLink("target_player"),
            RetrieverObjectLink("technology"),
            RetrieverObjectLink("string_id"),
            RetrieverObjectLink("display_time"),
            RetrieverObjectLink("trigger_id"),
            RetrieverObjectLink("location_x"),
            RetrieverObjectLink("location_y"),
            RetrieverObjectLink("location_object_reference"),
            RetrieverObjectLink("area_x1"),
            RetrieverObjectLink("area_y1"),
            RetrieverObjectLink("area_x2"),
            RetrieverObjectLink("area_y2"),
            RetrieverObjectLink("object_group"),
            RetrieverObjectLink("object_type"),
            RetrieverObjectLink("instruction_panel_position"),
            RetrieverObjectLink("attack_stance"),
            RetrieverObjectLink("time_unit"),
            RetrieverObjectLink("enabled"),
            RetrieverObjectLink("food"),
            RetrieverObjectLink("wood"),
            RetrieverObjectLink("stone"),
            RetrieverObjectLink("gold"),
            RetrieverObjectLink("item_id"),
            RetrieverObjectLink("flash_object"),
            RetrieverObjectLink("force_research_technology"),
            RetrieverObjectLink("visibility_state"),
            RetrieverObjectLink("scroll"),
            RetrieverObjectLink("operation"),
            RetrieverObjectLink("object_list_unit_id_2"),
            RetrieverObjectLink("button_location"),
            RetrieverObjectLink("ai_signal_value"),
            RetrieverObjectLink("object_attributes"),
            RetrieverObjectLink("variable"),
            RetrieverObjectLink("timer"),
            RetrieverObjectLink("facet"),
            RetrieverObjectLink("play_sound"),
            RetrieverObjectLink("player_color", support=Support(since=1.40)),
            RetrieverObjectLink("color_mood", support=Support(since=1.42)),
            RetrieverObjectLink("reset_timer", support=Support(since=1.44)),
            RetrieverObjectLink("object_state", support=Support(since=1.44)),
            RetrieverObjectLink("action_type", support=Support(since=1.44)),
            RetrieverObjectLink("message", commit_callback=_add_trail_if_string_attr_is_used_in_effect),
            RetrieverObjectLink("sound_name", commit_callback=_add_trail_if_string_attr_is_used_in_effect),
            RetrieverObjectLink("selected_object_ids"),
        ])
    ]

    def __init__(
            self,
            effect_type: int = None,
            ai_script_goal: int = None,
            armour_attack_quantity: int = None,
            armour_attack_class: int = None,
            quantity: int = None,
            tribute_list: int = None,
            diplomacy: int = None,
            legacy_location_object_reference: int = None,
            object_list_unit_id: int = None,
            source_player: int = None,
            target_player: int = None,
            technology: int = None,
            string_id: int = None,
            display_time: int = None,
            trigger_id: int = None,
            location_x: int = None,
            location_y: int = None,
            location_object_reference: int = None,
            area_x1: int = None,
            area_y1: int = None,
            area_x2: int = None,
            area_y2: int = None,
            object_group: int = None,
            object_type: int = None,
            instruction_panel_position: int = None,
            attack_stance: int = None,
            time_unit: int = None,
            enabled: int = None,
            food: int = None,
            wood: int = None,
            stone: int = None,
            gold: int = None,
            item_id: int = None,  # Unused (?)
            flash_object: int = None,
            force_research_technology: int = None,
            visibility_state: int = None,
            scroll: int = None,
            operation: int = None,
            object_list_unit_id_2: int = None,
            button_location: int = None,
            ai_signal_value: int = None,
            object_attributes: int = None,
            variable: int = None,
            timer: int = None,
            facet: int = None,
            play_sound: int = None,
            player_color: int = None,
            color_mood: int = None,
            reset_timer: int = None,
            object_state: int = None,
            action_type: int = None,
            message: str = None,
            sound_name: str = None,
            selected_object_ids: List[int] = None,
            **kwargs
    ):
        super().__init__(**kwargs)

        raise_if_not_int_subclass([object_list_unit_id, technology, object_list_unit_id_2])

        if selected_object_ids is None:
            selected_object_ids = []

        # Set flags
        self._armour_attack_flag = _set_armour_attack_flag(effect_type, object_attributes)

        # Handle armour effect attributes:
        #   When effect is created through trigger.new_effect, aa values will be -1.
        #   If created while reading a scenario, they both default to None.
        if self._armour_attack_flag:
            # If effect created through reading scenario file
            if quantity is not None and armour_attack_class is None and armour_attack_quantity is None:
                armour_attack_class, armour_attack_quantity = self._quantity_to_aa(quantity)
                quantity = None
            # If effect created through new_effect with aa values defined
            elif value_is_valid(armour_attack_class) or value_is_valid(armour_attack_quantity):
                quantity = None
            # If created through new_effect with quantity defined instead of the aa values. Handled by quantity property
            else:
                pass
        else:
            armour_attack_class = armour_attack_quantity = None

        area_x1, area_y1, area_x2, area_y2 = validate_coords(area_x1, area_y1, area_x2, area_y2)

        if value_is_valid(legacy_location_object_reference):
            location_object_reference = legacy_location_object_reference

        # Bypass the @property which causes: self._update_armour_attack_flag()
        self._effect_type: int = effect_type
        self.ai_script_goal: int = ai_script_goal
        self.armour_attack_quantity: int = armour_attack_quantity
        self.armour_attack_class: int = armour_attack_class
        self.quantity: int = quantity
        self.tribute_list: int = tribute_list
        self.diplomacy: int = diplomacy
        self.object_list_unit_id: int = object_list_unit_id
        self.source_player: int = source_player
        self.target_player: int = target_player
        self.technology: int = technology
        self.string_id: int = string_id
        self.display_time: int = display_time
        self.trigger_id: int = trigger_id
        self.location_x: int = location_x
        self.location_y: int = location_y
        self.location_object_reference: int = location_object_reference
        self.area_x1: int = area_x1
        self.area_y1: int = area_y1
        self.area_x2: int = area_x2
        self.area_y2: int = area_y2
        self.object_group: int = object_group
        self.object_type: int = object_type
        self.instruction_panel_position: int = instruction_panel_position
        self.attack_stance: int = attack_stance
        self.time_unit: int = time_unit
        self.enabled: int = enabled
        self.food: int = food
        self.wood: int = wood
        self.stone: int = stone
        self.gold: int = gold
        # self.item_id: int = item_id  # Unused (?)
        self.flash_object: int = flash_object
        self.force_research_technology: int = force_research_technology
        self.visibility_state: int = visibility_state
        self.scroll: int = scroll
        self.operation: int = operation
        self.object_list_unit_id_2: int = object_list_unit_id_2
        self.button_location: int = button_location
        self.ai_signal_value: int = ai_signal_value
        self.object_attributes: int = object_attributes
        self.variable: int = variable
        self.timer: int = timer
        self.facet: int = facet
        self.play_sound: int = play_sound
        self.player_color: int = player_color
        self.color_mood: int = color_mood
        self.reset_timer = reset_timer
        self.object_state = object_state
        self.action_type = action_type
        self.message: str = message
        self.sound_name: str = sound_name
        self.selected_object_ids: List[int] = selected_object_ids

    @property
    def legacy_location_object_reference(self) -> int:
        """Getter for legacy object_reference location. Always returns `-1`."""
        return -1

    @property
    def player_color(self):
        """Get the player color attribute"""
        return self._player_color

    @player_color.setter
    def player_color(self, value):
        if type(value) in [PlayerColorId, PlayerId]:
            value -= 1
        self._player_color = value

    @property
    def item_id(self):
        """Get the currently selected item_id based on other attributes"""
        if value_is_valid(self.object_list_unit_id):
            return self.object_list_unit_id
        if value_is_valid(self.technology):
            return self.technology
        if value_is_valid(self.tribute_list):
            return self.tribute_list
        return -1

    @item_id.setter
    def item_id(self, value):
        raise ValueError("The `item_id` attribute is always equal to its corresponding attribute."
                         "Please use that attribute (i.e. 'object_list_unit_id' or 'technology' or 'tribute_list').")

    @property
    def effect_type(self):
        """The type of the effect (EffectId dataset)"""
        return self._effect_type

    @effect_type.setter
    def effect_type(self, value):
        self._effect_type = value
        self._update_armour_attack_flag()

    @property
    def object_attributes(self):
        return self._object_attributes

    @object_attributes.setter
    def object_attributes(self, value):
        self._object_attributes = value
        self._update_armour_attack_flag()

    @property
    def armour_attack_quantity(self):
        """Helper property for handling the armour_attack related values"""
        return self._armour_attack_quantity

    @armour_attack_quantity.setter
    def armour_attack_quantity(self, value):
        if value is not None and value != [] and not self._armour_attack_flag:
            warn("Setting 'effect.armour_attack_quantity' when the effect doesn't use armour/attack attributes "
                 "might result in unintended behaviour.", category=IncorrectArmorAttackUsageWarning)
        self._armour_attack_quantity = value

    @property
    def armour_attack_class(self):
        """Helper property for handling the armour_attack related values"""
        return self._armour_attack_class

    @armour_attack_class.setter
    def armour_attack_class(self, value):
        if value is not None and value != [] and not self._armour_attack_flag:
            warn("Setting 'effect.armour_attack_class' when the effect doesn't use armour/attack attributes "
                 "might result in unintended behaviour.", category=IncorrectArmorAttackUsageWarning)
        self._armour_attack_class = value

    @property
    def quantity(self):
        """Getter for quantity, even if it is combined with `armour_attack_quantity` and `armour_attack_class`"""
        if self._armour_attack_flag:
            return self._aa_to_quantity(self.armour_attack_quantity, self.armour_attack_class)
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        # Quantity by default, when unused is []
        if value is not None and value != [] and self._armour_attack_flag:
            warn(
                message="Setting 'effect.quantity' directly in an effect that uses armour/attack attributes "
                        "might result in unintended behaviour.\nPlease use the 'effect.armour_attack_quantity' "
                        "and 'effect.armour_attack_class' attributes instead.",
                category=IncorrectArmorAttackUsageWarning
            )
            self.armour_attack_class, self.armour_attack_quantity = self._quantity_to_aa(value)
        self._quantity = value

    @property
    def selected_object_ids(self) -> List[int]:
        """Get the current selected objects"""
        return self._selected_object_ids

    @selected_object_ids.setter
    def selected_object_ids(self, val: List[int]):
        if type(val) is int:
            val = [val]
        self._selected_object_ids = val

    def _should_be_displayed(self, attr: str, val: Any) -> bool:
        # Ignore the quantity value in the print statement when flag is True.
        if self._armour_attack_flag and attr == "quantity":
            return False
        if not self._armour_attack_flag and (attr == "armour_attack_quantity" or attr == "armour_attack_class"):
            return False

        return super()._should_be_displayed(attr, val)

    def get_content_as_string(self, include_effect_definition: bool = False) -> str:
        """
        Create a human-readable string showcasing all content of this effect.

        This is also the function that is called when doing: `print(effect)`

        Args:
            include_effect_definition: If the effect meta-data should be added by this function

        Returns:
            The created string
        """
        if self.effect_type not in effects.attributes:  # Unknown effect
            attributes_list = effects.empty_attributes
        else:
            attributes_list = effects.attributes[self.effect_type]

        return_string = ""
        for attribute in attributes_list:
            val = getattr(self, attribute)
            if not self._should_be_displayed(attribute, val):
                continue

            value_string = transform_effect_attr_value(self.effect_type, attribute, val, self._uuid)
            return_string += f"{attribute}: {value_string}\n"

        if return_string == "":
            return "<< No Attributes >>\n"

        if include_effect_definition:
            try:
                effect_name = effects.effect_names[self.effect_type]
            except KeyError:
                effect_name = "Unknown"

            return f"{effect_name}:\n{add_tabs(return_string, 1)}"
        return return_string

    def _update_armour_attack_flag(self):
        self._armour_attack_flag = _set_armour_attack_flag(self.effect_type, self.object_attributes)

    def _quantity_to_aa(self, quantity: int) -> Tuple[int, int]:
        """
        A function to convert the initial quantity value to the quantity and armor/attack values.
        Unfortunately this problem has to be solved in the object due to how specific this was implemented in DE.

        Args:
            quantity: the initial quantity value

        Returns:
            The one byte armor/attack class as int and one byte armor/attack quantity as int

        ----

        **Trigger Version 2.4**::

            Quantity value: (3, 5)
            00000000 00000000 00000011 000000101
                                aaq      aac

        Final 2/4 bytes are aaq (1 byte), and aac (1 byte). First 2 are unused. Max value of both is 255.

        **Trigger Version 2.5**::

            Quantity value: (3, 5)
            00000000 00000011 00000000 000000101
              aaq      aaq      aac      aac

        The 4/4 bytes are aaq (2 bytes), and aac (2 bytes). All are used. Max value of both is 65535.

        ----
        """
        trigger_version = getters.get_trigger_version(self._uuid)
        if trigger_version >= 2.5:
            return quantity >> 16, quantity & 65535
        return quantity >> 8, quantity & 255

    def _aa_to_quantity(self, aa_quantity: int, aa_class: int) -> int:
        """
        A function to convert the quantity and armor/attack field to a quantity value.
        Unfortunately this problem has to be solved in the object due to how specific this was implemented in DE.

        Args:
            aa_quantity: the armor quantity value
            aa_class: the armor/attack value

        Returns:
            The one byte quantity and one byte armor/attack value
        """
        trigger_version = getters.get_trigger_version(self._uuid)
        if trigger_version >= 2.5:
            return aa_class * 65536 + aa_quantity

        # Would use `aa_class << 8` - but apparently multiplication is faster
        return aa_class * 256 + aa_quantity

    def __str__(self):
        return f"[Effect] {self.get_content_as_string(include_effect_definition=True)}"


def _set_armour_attack_flag(effect_type, object_attributes) -> bool:
    aa_effects = [
        EffectId.CHANGE_OBJECT_ATTACK,
        EffectId.CHANGE_OBJECT_ARMOR,
        EffectId.CREATE_OBJECT_ATTACK,
        EffectId.CREATE_OBJECT_ARMOR,
    ]
    return (effect_type in aa_effects) or \
           (effect_type == EffectId.MODIFY_ATTRIBUTE and object_attributes in [
               ObjectAttribute.ATTACK, ObjectAttribute.ARMOR
           ])
