from __future__ import annotations

import copy
from enum import IntEnum
from typing import List, Dict, Set

from AoE2ScenarioParser.datasets.effects import Effect
from AoE2ScenarioParser.datasets.players import Player
from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.trigger_obj import TriggerObject
from AoE2ScenarioParser.objects.variable_obj import VariableObject


class TriggersObject(AoE2Object):
    """Manager of the everything trigger related."""

    _link_list = [
        RetrieverObjectLink("triggers", "TriggerPiece.trigger_data", process_as_object=TriggerObject),
        RetrieverObjectLink("trigger_display_order", "TriggerPiece.trigger_display_order_array"),
        RetrieverObjectLink("variables", "TriggerPiece.variable_data", process_as_object=VariableObject),
    ]

    def __init__(self,
                 triggers: List[TriggerObject],
                 trigger_display_order: List[int],
                 variables: List[VariableObject]
                 ):

        self.triggers: List[TriggerObject] = triggers
        self.trigger_display_order: List[int] = trigger_display_order
        self.variables: List[VariableObject] = variables

        super().__init__()

    def copy_trigger_per_player(self,
                                from_player,
                                trigger_select,
                                change_from_player_only=False,
                                include_player_source=True,
                                include_player_target=False,
                                trigger_ce_lock=None,
                                include_gaia: bool = False,
                                create_copy_for_players: List[IntEnum] = None) -> Dict[Player, TriggerObject]:
        """
        Copies a trigger for all or a selection of players. Every copy will change desired player attributes with it.

        Args:
            from_player (IntEnum): The central player this trigger is created for. This is the player that will not get
                a copy.
            trigger_select (TriggerSelect): An object used to identify which trigger to select.
            change_from_player_only (bool): If set to True, only change player attributes in effects and conditions that
                are equal to the player defined using the `from_player` parameter.
            include_player_source (bool): If set to True, allow player source attributes to be changed while copying.
                Player source attributes are attributes where a player is defined to perform an action such as create an
                object. If set to False these attributes will remain unchanged.
            include_player_target (bool): If set to True, allow player target attributes to be changed while copying.
                Player target attributes are attributes where a player is defined as the target such as change ownership
                or sending resources. If set to False these attributes will remain unchanged.
            trigger_ce_lock (TriggerCELock): The TriggerCELock object. Used to lock certain (types) of conditions or
                effects from being changed while copying.
            include_gaia (bool): If True, GAIA is included in the copied list. (Also when `create_copy_for_players` is
                defined)
            create_copy_for_players (List[IntEnum]): A list of Players to create a copy for. The `from_player` will be
                excluded from this list.

        Returns:
            A dict with all the new created triggers. The key is the player for which the trigger is
                created using the IntEnum associated with it. Example:
                {Player.TWO: TriggerObject, Player.FIVE: TriggerObject}

        Raises:
            ValueError: if more than one trigger selection is used. Any of (trigger_index, display_index or trigger)
                Or if Both `include_player_source` and `include_player_target` are `False`

        :Authors:
            KSneijders

        """
        trigger_index, display_index, trigger = self._validate_and_retrieve_trigger_info(trigger_select)
        if not include_player_source and not include_player_target:
            raise ValueError("Cannot exclude player source and target.")

        if create_copy_for_players is None:
            create_copy_for_players = [
                Player.ONE, Player.TWO, Player.THREE, Player.FOUR,
                Player.FIVE, Player.SIX, Player.SEVEN, Player.EIGHT
            ]
        if include_gaia and Player.GAIA not in create_copy_for_players:
            create_copy_for_players.append(Player.GAIA)

        alter_conditions, alter_effects = TriggersObject._find_alterable_ce(trigger, trigger_ce_lock)

        return_dict: Dict[Player, TriggerObject] = {}
        for player in create_copy_for_players:
            if not player == from_player:
                new_trigger = self.copy_trigger(TS.trigger(trigger))
                new_trigger.name += f" (p{player})"
                return_dict[player] = new_trigger

                for cond_x in alter_conditions:
                    cond = new_trigger.conditions[cond_x]
                    # Player not set
                    if cond.source_player == -1:
                        continue
                    # Player not equal to 'from_player'
                    if change_from_player_only:
                        if not cond.source_player == from_player:
                            continue
                    # Change source player
                    if include_player_source:
                        cond.source_player = Player(player)
                    # Change target player
                    if include_player_target:
                        cond.target_player = Player(player)
                for effect_x in alter_effects:
                    effect = new_trigger.effects[effect_x]
                    # Player not set
                    if effect.source_player == -1:
                        continue
                    # Player not equal to 'from_player'
                    if change_from_player_only:
                        if not effect.source_player == from_player:
                            continue
                    # Change source player
                    if include_player_source:
                        effect.source_player = Player(player)
                    # Change target player
                    if include_player_target:
                        effect.target_player = Player(player)

        return return_dict

    def copy_trigger(self, trigger_select) -> TriggerObject:
        """
        Creates an exact copy (deepcopy) of this trigger.

        Args:
            trigger_select (TriggerSelect): An object used to identify which trigger to select.

        Returns:
            The newly copied trigger
        """
        trigger_index, display_index, trigger = self._validate_and_retrieve_trigger_info(trigger_select)

        deepcopy_trigger = copy.deepcopy(trigger)
        deepcopy_trigger.name += " (copy)"
        deepcopy_trigger.trigger_id = len(self.triggers)
        self.triggers.append(deepcopy_trigger)
        helper.update_order_array(self.trigger_display_order, len(self.triggers))

        return deepcopy_trigger

    def copy_trigger_tree(self, trigger_select: TriggerSelect) -> List[TriggerObject]:
        trigger_index, display_index, trigger = self._validate_and_retrieve_trigger_info(trigger_select)

        known_node_indexes = {trigger_index}
        self._find_trigger_tree_nodes_recursively(trigger, known_node_indexes)

        new_triggers = []
        id_swap = {}
        for index in known_node_indexes:
            trigger = self.copy_trigger(TS.index(index))
            new_triggers.append(trigger)
            id_swap[index] = trigger.trigger_id

        for trigger in new_triggers:
            activation_effects = [
                effect for effect in trigger.effects if
                effect.effect_type in [Effect.ACTIVATE_TRIGGER, Effect.DEACTIVATE_TRIGGER]
            ]
            for effect in activation_effects:
                effect.trigger_id = id_swap[effect.trigger_id]

        return new_triggers

    def replace_player(self, trigger_select, to_player, only_change_from=None, include_player_source=True,
                       include_player_target=False, trigger_ce_lock=None) -> TriggerObject:
        """
        Replaces player attributes. Specifically useful if multiple players are used in the same trigger.

        Args:
            trigger_select (TriggerSelect): An object used to identify which trigger to select.
            to_player (Player): The player the attributes are changed to.
            only_change_from (Player): Can only change player attributes if the player is equal to the given value
            include_player_source (bool): If set to True, allow player source attributes to be changed while replacing.
                Player source attributes are attributes where a player is defined to perform an action such as create an
                object. If set to False these attributes will remain unchanged.
            include_player_target (bool): If set to True, allow player target attributes to be changed while replacing.
                Player target attributes are attributes where a player is defined as the target such as change ownership
                or sending resources. If set to False these attributes will remain unchanged.
            trigger_ce_lock (TriggerCELock): The TriggerCELock object. Used to lock certain (types) of conditions or
                effects from being changed.

        Returns:
            The given trigger with the proper player attributes changed
        """

        trigger_index, display_index, trigger = self._validate_and_retrieve_trigger_info(trigger_select)
        alter_conditions, alter_effects = TriggersObject._find_alterable_ce(trigger, trigger_ce_lock)

        for cond_x in alter_conditions:
            cond = trigger.conditions[cond_x]
            if not cond.source_player == -1 and include_player_source:
                if only_change_from is not None and only_change_from != cond.source_player:
                    continue
                cond.source_player = Player(to_player)
            if not cond.target_player == -1 and include_player_target:
                if only_change_from is not None and only_change_from != cond.target_player:
                    continue
                cond.target_player = Player(to_player)
        for effect_x in alter_effects:
            effect = trigger.effects[effect_x]
            if not effect.source_player == -1 and include_player_source:
                if only_change_from is not None and only_change_from != effect.source_player:
                    continue
                effect.source_player = Player(to_player)
            if not effect.target_player == -1 and include_player_target:
                if only_change_from is not None and only_change_from != effect.target_player:
                    continue
                effect.target_player = Player(to_player)

        return trigger

    def add_trigger(self, name: str) -> TriggerObject:
        """
        Adds a trigger.

        Args:
            name (str): The name for the trigger

        Returns:
            The newly added TriggerObject
        """
        new_trigger = TriggerObject(name=name, trigger_id=len(self.triggers))
        self.triggers.append(new_trigger)
        helper.update_order_array(self.trigger_display_order, len(self.triggers))
        return new_trigger

    def add_variable(self, name: str, variable_id: int = -1) -> VariableObject:
        """
        Adds a variable.

        Args:
            name (str): The name for the variable
            variable_id (int): The ID of the variable. If left empty (default: -1), lowest available value will be used

        Returns:
            The newly added VariableObject
        """
        list_of_var_ids = [var.variable_id for var in self.variables]
        if variable_id == -1:
            for i in range(256):
                if i not in list_of_var_ids:
                    variable_id = i
                    break
            if variable_id == -1:
                raise IndexError(f"No variable ID available. All in use? In use: ({list_of_var_ids}/256)")
        if not (0 <= variable_id <= 255):
            raise ValueError("Variable ID has to fall between 0 and 255 (incl).")
        if variable_id in list_of_var_ids:
            raise ValueError("Variable ID already in use.")

        new_variable = VariableObject(variable_id=variable_id, name=name)
        self.variables.append(new_variable)
        return new_variable

    def get_trigger(self, trigger_select: TriggerSelect) -> TriggerObject:
        trigger_index, display_index, trigger = self._validate_and_retrieve_trigger_info(trigger_select)
        return trigger

    def get_variable(self, variable_id: int = None, variable_name: str = None) -> VariableObject:
        if variable_id is None and variable_name is None:
            raise ValueError("Select a variable using the variable_id or variable_name parameters")
        if variable_id is not None and variable_name is not None:
            raise ValueError("Select a variable using either the variable_id or variable_name parameters, not both.")

        for variable in self.variables:
            if variable.variable_id == variable_id or variable.name == variable_name:
                return variable

    def remove_trigger(self, trigger_select: TriggerSelect) -> None:
        trigger_index, display_index, trigger = self._validate_and_retrieve_trigger_info(trigger_select)

        for x in self.trigger_display_order:
            if x > trigger_index:
                self.get_trigger(TS.index(x)).trigger_id -= 1

        del self.triggers[trigger_index]
        del self.trigger_display_order[display_index]

        self.trigger_display_order = [x - 1 if x > trigger_index else x for x in self.trigger_display_order]

    def _find_trigger_tree_nodes_recursively(self, trigger, known_node_indexes: Set[int]) -> None:
        found_node_indexes = TriggersObject._find_trigger_tree_nodes(trigger)
        unknown_node_indexes = found_node_indexes.difference(known_node_indexes)

        if len(unknown_node_indexes) == 0:
            return

        known_node_indexes.update(unknown_node_indexes)

        for index in unknown_node_indexes:
            self._find_trigger_tree_nodes_recursively(self.triggers[index], known_node_indexes)

    def _validate_and_retrieve_trigger_info(self, trigger_select) -> (int, int, TriggersObject):
        trigger = trigger_select.trigger
        trigger_index = trigger_select.trigger_index
        display_index = trigger_select.display_index

        if trigger is None:
            helper.evaluate_index_params(trigger_index, display_index, "trigger")
        else:
            trigger_index = trigger.trigger_id

        if trigger_index is None:
            trigger_index = self.trigger_display_order[display_index]
        else:
            display_index = self.trigger_display_order.index(trigger_index)

        if not trigger:
            trigger = self.triggers[trigger_index]

        return trigger_index, display_index, trigger

    def get_summary_as_string(self) -> str:
        return_string = "\nTrigger Summary:\n"

        triggers = self.triggers
        display_order = self.trigger_display_order

        if len(display_order) == 0:
            return_string += "\t<< No Triggers >>"

        longest_trigger_name = -1
        for trigger_index in display_order:
            trigger_name = triggers[trigger_index].name
            longest_trigger_name = max(longest_trigger_name, len(trigger_name))

        longest_trigger_name += 3
        for display, trigger_index in enumerate(display_order):
            trigger = triggers[trigger_index]
            trigger_name = trigger.name

            buffer = longest_trigger_name - len(trigger_name)
            return_string += "\t" + trigger_name + (" " * buffer)
            return_string += " [Index: " + str(trigger_index) + ", Display: " + str(display) + "]"

            return_string += "\t(conditions: " + str(len(trigger.conditions)) + ", "
            return_string += " effects: " + str(len(trigger.effects)) + ")\n"

        variables = self.variables

        return_string += "\nVariables Summary:\n"
        if len(variables) == 0:
            return_string += "\t<< No Variables >>"

        longest_variable_name = -1
        for variable in variables:
            longest_variable_name = max(longest_variable_name, len(variable.name))

        longest_variable_name += 3
        for index, variable in enumerate(variables):
            var_name = variable.name
            buffer = " " * (longest_variable_name - len(var_name))
            return_string += f"\t{var_name}{buffer}[Index: {variable.variable_id}]\n"

        return return_string

    def get_content_as_string(self) -> str:
        return_string = "\nTriggers:\n"

        if len(self.triggers) == 0:
            return_string += "\t<<No triggers>>\n"

        for trigger_index in self.trigger_display_order:
            return_string += self.get_trigger_as_string(TS.index(trigger_index)) + "\n"

        return_string += "Variables:\n"

        if len(self.variables) == 0:
            return_string += "\t<<No Variables>>\n"

        for variable in self.variables:
            return_string += f"\t'{variable.name}' [Index: {variable.variable_id}]\n"

        return return_string

    def get_trigger_as_string(self, trigger_select: TriggerSelect) -> str:
        trigger_index, display_index, trigger = self._validate_and_retrieve_trigger_info(trigger_select)

        return_string = "\t'" + trigger.name + "'"
        return_string += " [Index: " + str(trigger_index) + ", Display: " + str(display_index) + "]" + ":\n"

        return_string += trigger.get_content_as_string()

        return return_string

    @staticmethod
    def _find_alterable_ce(trigger, trigger_ce_lock) -> (List[int], List[int]):
        lock_conditions = trigger_ce_lock.lock_conditions if trigger_ce_lock is not None else False
        lock_effects = trigger_ce_lock.lock_effects if trigger_ce_lock is not None else False
        lock_condition_type = trigger_ce_lock.lock_condition_type if trigger_ce_lock is not None else []
        lock_effect_type = trigger_ce_lock.lock_effect_type if trigger_ce_lock is not None else []
        lock_condition_ids = trigger_ce_lock.lock_condition_ids if trigger_ce_lock is not None else []
        lock_effect_ids = trigger_ce_lock.lock_effect_ids if trigger_ce_lock is not None else []

        alter_conditions: List[int] = []
        alter_effects: List[int] = []
        if not lock_conditions:
            for i, cond in enumerate(trigger.conditions):
                if i not in lock_condition_ids and cond.condition_type not in lock_condition_type:
                    alter_conditions.append(i)
        if not lock_effects:
            for i, effect in enumerate(trigger.effects):
                if i not in lock_effect_ids and effect.effect_type not in lock_effect_type:
                    alter_effects.append(i)

        return alter_conditions, alter_effects

    @staticmethod
    def _find_trigger_tree_nodes(trigger: TriggerObject) -> Set[int]:
        return {
            effect.trigger_id for effect in trigger.effects if
            effect.effect_type in [Effect.ACTIVATE_TRIGGER, Effect.DEACTIVATE_TRIGGER]
        }


class TriggerSelect:
    def __init__(self, trigger_index=None, display_index=None, trigger=None):
        """
        Object used to select a trigger in many trigger related functions. For ease of use, the alias `TS` can be
        called. You can also use those in combination with the class methods (factory methods). Like so:

        TS.index(4)    # To select the trigger with index 4

        TS.display(4)  # Trigger with display index 4

        TS.trigger(trigger)  # Well... The trigger object given...

        Args:
            trigger_index (int): The index of the trigger. Starting from 0, based on creation time
            display_index (int): The display index of a trigger. Starting from 0, based on display order in the editor
            trigger (TriggerObject): The trigger object itself.
        """
        self.trigger = trigger
        self.display_index = display_index
        self.trigger_index = trigger_index

    @classmethod
    def index(cls, index: int):
        return cls(trigger_index=index)

    @classmethod
    def display(cls, display_index: int):
        return cls(display_index=display_index)

    @classmethod
    def trigger(cls, trigger: TriggerObject):
        return cls(trigger=trigger)


TS = TriggerSelect


class TriggerCELock:
    def __init__(self,
                 lock_conditions=False,
                 lock_effects=False,
                 lock_condition_type=None,
                 lock_effect_type=None,
                 lock_condition_ids=None,
                 lock_effect_ids=None,
                 ):
        """
        Object used to identify which conditions and effects should be locked from change.

        Args:
            lock_conditions (bool): Lock all conditions
            lock_effects (bool): Lock all effects
            lock_condition_type (List[int]): Lock certain condition types. Example: `Condition.OWN_OBJECTS`
            lock_effect_type (List[int]): Lock certain effect types. Example: `Effect.CREATE_OBJECT`
            lock_condition_ids (List[int]): Lock certain conditions by their id
            lock_effect_ids (List[int]): Lock certain effects by their id
        """
        if lock_condition_type is None:
            lock_condition_type = []
        if lock_effect_type is None:
            lock_effect_type = []
        if lock_condition_ids is None:
            lock_condition_ids = []
        if lock_effect_ids is None:
            lock_effect_ids = []

        self.lock_conditions = lock_conditions
        self.lock_effects = lock_effects
        self.lock_condition_type = lock_condition_type
        self.lock_effect_type = lock_effect_type
        self.lock_condition_ids = lock_condition_ids
        self.lock_effect_ids = lock_effect_ids
