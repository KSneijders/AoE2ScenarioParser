from __future__ import annotations

import copy
from enum import IntEnum
from typing import List, Dict, Union

from AoE2ScenarioParser.datasets.effects import EffectId
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper.list_functions import hash_list, list_changed, update_order_array
from AoE2ScenarioParser.helper.printers import warn
from AoE2ScenarioParser.helper.string_manipulations import add_tabs
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.data_objects.effect import Effect
from AoE2ScenarioParser.objects.data_objects.trigger import Trigger
from AoE2ScenarioParser.objects.support.enums.group_by import GroupBy
from AoE2ScenarioParser.objects.support.trigger_select import TriggerSelect, TS
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink


class TriggerManager(AoE2Object):
    """Manager of the everything trigger related."""

    _link_list = [
        RetrieverObjectLink("triggers", "Triggers", "trigger_data", process_as_object=Trigger),
        RetrieverObjectLink("trigger_display_order", "Triggers", "trigger_display_order_array"),
    ]

    def __init__(self,
                 triggers: List[Trigger],
                 trigger_display_order: List[int],
                 **kwargs
                 ):
        super().__init__(**kwargs)

        self._trigger_hash = hash_list(triggers)
        self.triggers: List[Trigger] = triggers
        self.trigger_display_order: List[int] = trigger_display_order

    @property
    def triggers(self) -> List[Trigger]:
        return self._triggers

    @triggers.setter
    def triggers(self, value):
        self._update_triggers_uuid(value)
        self._trigger_hash = hash_list(value)
        self._triggers = value
        self.trigger_display_order = list(range(len(value)))

    @property
    def trigger_display_order(self) -> List[int]:
        if list_changed(self.triggers, self._trigger_hash):
            update_order_array(self._trigger_display_order, len(self.triggers))
            self._trigger_hash = hash_list(self.triggers)
        return self._trigger_display_order

    @trigger_display_order.setter
    def trigger_display_order(self, val):
        self._trigger_display_order = val

    def copy_trigger_per_player(self,
                                from_player,
                                trigger_select: Union[int, TriggerSelect],
                                change_from_player_only=False,
                                include_player_source=True,
                                include_player_target=False,
                                trigger_ce_lock=None,
                                include_gaia: bool = False,
                                create_copy_for_players: List[IntEnum] = None) -> Dict[PlayerId, Trigger]:
        """
        Copies a trigger for all or a selection of players. Every copy will change desired player attributes with it.

        Args:
            from_player (IntEnum): The central player this trigger is created for. This is the player that will not get
                a copy.
            trigger_select (Union[int, TriggerSelect]): An object used to identify which trigger to select.
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
                {PlayerId.TWO: Trigger, PlayerId.FIVE: Trigger}

        Raises:
            ValueError: if more than one trigger selection is used. Any of (trigger_index, display_index or trigger)
                Or if Both `include_player_source` and `include_player_target` are `False`

        :Authors:
            KSneijders

        """
        trigger_index, display_index, trigger = self._validate_and_retrieve_trigger_info(trigger_select)

        if create_copy_for_players is None:
            create_copy_for_players = [
                PlayerId.ONE, PlayerId.TWO, PlayerId.THREE, PlayerId.FOUR,
                PlayerId.FIVE, PlayerId.SIX, PlayerId.SEVEN, PlayerId.EIGHT
            ]
        if include_gaia and PlayerId.GAIA not in create_copy_for_players:
            create_copy_for_players.append(PlayerId.GAIA)

        alter_conditions, alter_effects = TriggerManager._find_alterable_ce(trigger, trigger_ce_lock)

        return_dict: Dict[PlayerId, Trigger] = {}
        for player in create_copy_for_players:
            if player == from_player:
                continue

            new_trigger = self.copy_trigger(TS.trigger(trigger), append_after_source=False, add_suffix=False)
            new_trigger.name += " (GAIA)" if player == PlayerId.GAIA else f" (p{player})"
            return_dict[player] = new_trigger

            for cond_x in alter_conditions:
                cond = new_trigger.conditions[cond_x]
                if cond.source_player == -1:
                    continue

                if include_player_source:
                    if not change_from_player_only or (change_from_player_only and cond.source_player == from_player):
                        cond.source_player = PlayerId(player)
                if include_player_target:
                    if not change_from_player_only or (change_from_player_only and cond.target_player == from_player):
                        cond.target_player = PlayerId(player)

            for effect_x in alter_effects:
                effect = new_trigger.effects[effect_x]
                if effect.source_player == -1:
                    continue

                if include_player_source:
                    if not change_from_player_only or (change_from_player_only and effect.source_player == from_player):
                        effect.source_player = PlayerId(player)
                if include_player_target:
                    if not change_from_player_only or (change_from_player_only and effect.target_player == from_player):
                        effect.target_player = PlayerId(player)

        # After copies have been made
        trigger.name += f" (p{from_player})"

        return return_dict

    def copy_trigger(
            self,
            trigger_select: Union[int, TriggerSelect],
            append_after_source=True,
            add_suffix=True
    ) -> Trigger:
        """
        Creates an exact copy (deepcopy) of this trigger.

        Args:
            trigger_select (Union[int, TriggerSelect]): An object used to identify which trigger to select.
            append_after_source (bool): If the new trigger should be appended below the source trigger
            add_suffix (bool): If the text ' (copy)' should be added after the trigger

        Returns:
            The newly copied trigger
        """
        trigger_index, display_index, trigger = self._validate_and_retrieve_trigger_info(trigger_select)

        deepcopy_trigger = copy.deepcopy(trigger)
        deepcopy_trigger.trigger_id = len(self.triggers)
        if add_suffix:
            deepcopy_trigger.name += " (copy)"

        self.triggers.append(deepcopy_trigger)

        if append_after_source:
            self.move_triggers([trigger_index, deepcopy_trigger.trigger_id], trigger_index)

        return deepcopy_trigger

    def copy_trigger_tree_per_player(self,
                                     from_player,
                                     trigger_select: Union[int, TriggerSelect],
                                     change_from_player_only=False,
                                     include_player_source=True,
                                     include_player_target=False,
                                     trigger_ce_lock=None,
                                     include_gaia: bool = False,
                                     create_copy_for_players: List[IntEnum] = None,
                                     group_triggers_by=None):
        """
        Copies an entire trigger tree for all or a selection of players. Every copy will change desired player
        attributes with it. Trigger trees are triggers linked together using EffectId.(DE)ACTIVATE_TRIGGER.

        Args:
            from_player (IntEnum): The central player this trigger is created for. This is the player that will not get
                a copy.
            trigger_select (Union[int, TriggerSelect]): An object used to identify which trigger to select.
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
            group_triggers_by (GroupBy): How to group the newly added triggers.

        Returns:
            The newly created triggers in a dict using the Player as key and as value with a list of triggers
        """
        if group_triggers_by is None:
            group_triggers_by = GroupBy.NONE

        trigger_index, display_index, source_trigger = self._validate_and_retrieve_trigger_info(trigger_select)

        known_node_indexes = [trigger_index]
        self._find_trigger_tree_nodes_recursively(source_trigger, known_node_indexes)

        new_triggers = {}
        trigger_index_swap = {}

        # Set values for from_player
        new_triggers[from_player] = [self.triggers[i] for i in known_node_indexes]
        for index in known_node_indexes:
            trigger = self.triggers[index]
            trigger_index_swap.setdefault(index, {})[from_player] = trigger.trigger_id

        # Copy for all other players
        for index in known_node_indexes:
            triggers = self.copy_trigger_per_player(
                from_player,
                index,
                change_from_player_only,
                include_player_source,
                include_player_target,
                trigger_ce_lock,
                include_gaia,
                create_copy_for_players,
            )
            for player, trigger in triggers.items():
                trigger_index_swap.setdefault(index, {})[player] = trigger.trigger_id
                new_triggers.setdefault(player, []).append(trigger)

        # Set trigger_id's in activation effects to the new player copied trigger ID
        for player, triggers in new_triggers.items():
            for trigger in triggers:
                for effect in get_activation_effects(trigger):
                    effect.trigger_id = trigger_index_swap[effect.trigger_id][player]

        # -------------- Group by logic -------------- #
        new_trigger_ids = []
        if group_triggers_by == GroupBy.TRIGGER:
            for i in range(len(known_node_indexes)):
                for player in PlayerId.all():
                    if player == from_player:
                        new_trigger_ids.append(known_node_indexes[i])
                        continue
                    if player not in new_triggers:
                        continue
                    new_trigger_ids.append(new_triggers[player][i].trigger_id)
        elif group_triggers_by == GroupBy.PLAYER:
            for player in PlayerId.all():
                if player == from_player:
                    new_trigger_ids.extend(known_node_indexes)
                    continue
                if player not in new_triggers:
                    continue

                new_trigger_ids.extend([trigger.trigger_id for trigger in new_triggers[player]])

        if group_triggers_by != GroupBy.NONE:
            self.move_triggers(new_trigger_ids, display_index)

        return new_triggers

    def move_triggers(self, trigger_ids: List[int], insert_index: int) -> None:
        """
        Function to move triggers. Moves the given IDs from anywhere to the split index. This function reorders triggers
        BUT keeps ``(de)activate trigger`` effects linked properly!

        As an example:

        >>> [0,1,2,3,4,5,6,7,8]  # Current index order
        >>> # Let's move trigger 1, 4, 5 and 6 to location 2
        >>> self.move_triggers([1, 4, 5, 6], 2)  # << 2 is an INDEX, not the value
        >>> [0,1,4,5,6,2,3,7,8]  # New index order

        Args:
            trigger_ids: The trigger IDs to move
            insert_index: The index that defines where to insert the triggers
        """
        if min(trigger_ids) < 0:
            raise ValueError(f"Trigger IDs cannot be negative")

        if insert_index >= len(self.trigger_display_order):
            # Add to the end of the list
            new_trigger_id_order = [n for n in self.trigger_display_order if n not in trigger_ids]
            new_trigger_id_order += trigger_ids
        else:
            insert_num = self.trigger_display_order[insert_index]
            new_trigger_id_order = [n for n in self.trigger_display_order if n not in trigger_ids or n == insert_num]

            split_index = new_trigger_id_order.index(insert_num)

            if insert_num in trigger_ids:
                new_trigger_id_order.remove(insert_num)

            new_trigger_id_order = new_trigger_id_order[:split_index] + trigger_ids + new_trigger_id_order[split_index:]
        self.reorder_triggers(new_trigger_id_order)

    def reorder_triggers(self, new_id_order: List[int] = None):
        """
        Reorder all triggers to a given order of IDs. This function reorders triggers BUT keeps ``(de)activate trigger``
        effects linked properly!

        As an example:

        >>> [0,1,2,3,4,5,6,7,8]  # Current index order
        >>> self.reorder_triggers([0,1,2,3,5,4,7,8,6])
        >>> [0,1,2,3,5,4,7,8,6]  # New index order

        Keep in mind that all trigger IDs will get remapped with this function. So ``trigger_manager.triggers[4]`` might
        result in a different trigger after this function is called in comparison to before.

        Args:
            new_id_order: The new trigger order. Uses the current display order when left unused
        """
        if new_id_order is not None:
            if min(new_id_order) < 0:
                raise ValueError(f"Trigger IDs cannot be negative")
            self.trigger_display_order = new_id_order

        new_triggers_list = []
        index_changes = {}
        for new_index, index in enumerate(self.trigger_display_order):
            try:
                trigger = self.triggers[index]
            except IndexError:
                raise ValueError(f"The trigger ID {index} doesn't exist") from None
            index_changes[trigger.trigger_id] = new_index

            trigger.trigger_id = new_index
            new_triggers_list.append(trigger)
        self.triggers = new_triggers_list

        # Find and update all (de)activation effect trigger references
        for trigger in self.triggers:
            for effect in get_activation_effects(trigger):
                if effect.trigger_id in index_changes:
                    effect.trigger_id = index_changes[effect.trigger_id]

    def copy_trigger_tree(self, trigger_select: Union[int, TriggerSelect]) -> List[Trigger]:
        """
        Copies an entire trigger tree. Trigger trees are triggers linked together using EffectId.(DE)ACTIVATE_TRIGGER.

        Args:
            trigger_select: An object used to identify which trigger to select

        Returns:
            The newly created triggers in a list
        """
        trigger_index, display_index, trigger = self._validate_and_retrieve_trigger_info(trigger_select)

        known_node_indexes = [trigger_index]
        self._find_trigger_tree_nodes_recursively(trigger, known_node_indexes)

        new_triggers = []
        id_swap = {}
        for index in known_node_indexes:
            trigger = self.copy_trigger(index, append_after_source=False)
            new_triggers.append(trigger)
            id_swap[index] = trigger.trigger_id

        for trigger in new_triggers:
            activation_effects = [
                effect for effect in trigger.effects if
                effect.effect_type in [EffectId.ACTIVATE_TRIGGER, EffectId.DEACTIVATE_TRIGGER]
            ]
            for effect in activation_effects:
                effect.trigger_id = id_swap[effect.trigger_id]

        return new_triggers

    def replace_player(self, trigger_select: Union[int, TriggerSelect], to_player, only_change_from=None,
                       include_player_source=True, include_player_target=False, trigger_ce_lock=None) -> Trigger:
        """
        Replaces player attributes. Specifically useful if multiple players are used in the same trigger.

        Args:
            trigger_select (Union[int, TriggerSelect]): An object used to identify which trigger to select.
            to_player (PlayerId): The player the attributes are changed to.
            only_change_from (PlayerId): Can only change player attributes if the player is equal to the given value
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
        alter_conditions, alter_effects = TriggerManager._find_alterable_ce(trigger, trigger_ce_lock)

        for cond_x in alter_conditions:
            cond = trigger.conditions[cond_x]
            if cond.source_player not in [-1, None] and include_player_source:
                if only_change_from is not None and only_change_from != cond.source_player:
                    continue
                cond.source_player = PlayerId(to_player)
            if cond.target_player not in [-1, None] and include_player_target:
                if only_change_from is not None and only_change_from != cond.target_player:
                    continue
                cond.target_player = PlayerId(to_player)
        for effect_x in alter_effects:
            effect = trigger.effects[effect_x]
            if effect.source_player not in [-1, None] and include_player_source:
                if only_change_from is not None and only_change_from != effect.source_player:
                    continue
                effect.source_player = PlayerId(to_player)
            if effect.target_player not in [-1, None] and include_player_target:
                if only_change_from is not None and only_change_from != effect.target_player:
                    continue
                effect.target_player = PlayerId(to_player)

        return trigger

    def add_trigger(self, name, description=None, description_stid=None, display_as_objective=None,
                    short_description=None, short_description_stid=None, display_on_screen=None, description_order=None,
                    enabled=None, looping=None, header=None, mute_objectives=None, conditions=None,
                    effects=None) -> Trigger:
        """
        Adds a new trigger to the scenario.

        Args:
            name (str): The name for the trigger
            description (str): The trigger description
            description_stid (int): The trigger description string table ID
            display_as_objective (bool): Display the trigger as objective
            short_description (str): The short trigger description
            short_description_stid (int): The short trigger description string table ID
            display_on_screen (bool): Display the trigger objective on screen
            description_order (int): ?
            enabled (bool): If the trigger is enabled from the start.
            looping (bool): If the trigger loops.
            header (bool): Turn objective into header
            mute_objectives (bool): Mute objectives
            conditions (List): A list of condition managers
            effects (List): A list of effect managers

        Returns:
            The newly created trigger
        """
        keys = [
            'description', 'description_stid', 'display_as_objective', 'short_description',
            'short_description_stid', 'display_on_screen', 'description_order', 'enabled', 'looping', 'header',
            'mute_objectives', 'conditions', 'effects'
        ]
        trigger_attr = {}
        for key in keys:
            if locals()[key] is not None:
                trigger_attr[key] = locals()[key]
        new_trigger = Trigger(name=name, trigger_id=len(self.triggers), **trigger_attr, host_uuid=self._host_uuid)
        self.triggers.append(new_trigger)
        return new_trigger

    def import_triggers(self, triggers: List[Trigger], index: int = -1) -> List[Trigger]:
        """
        Adds existing trigger objects (from another scenario) to this scenario. Keeping all ``(de)activate trigger``
        effects linked!

        Args:
            triggers: The list of Trigger objects to be added
            index: The index where to insert the new triggers, will be added at the end when left unused.

        Returns:
            The newly added triggers (with the new IDs and activation links etc.)
        """
        index_changes = {}

        for offset, trigger in enumerate(triggers):
            new_index = len(self.triggers) + offset
            index_changes[trigger.trigger_id] = trigger.trigger_id = new_index

        self._update_triggers_uuid(triggers)
        for trigger in triggers:
            for i, effect in enumerate(get_activation_effects(trigger)):
                try:
                    effect.trigger_id = index_changes[effect.trigger_id]
                except KeyError:
                    warn(f"(De)Activation effect {i} in trigger '{trigger.name}' refers to a trigger that wasn't included "
                         f"in the imported triggers. Effect will be reset")
                    effect.trigger_id = -1

        self.triggers += triggers
        if index != -1:
            self.move_triggers([t.trigger_id for t in triggers], index)
        return triggers

    def _update_triggers_uuid(self, triggers):
        for trigger in triggers:
            trigger._host_uuid = self._host_uuid
            for effect in trigger.effects:
                effect._host_uuid = self._host_uuid
            for condition in trigger.conditions:
                condition._host_uuid = self._host_uuid

    def get_trigger(self, trigger_select: Union[int, TriggerSelect]) -> Trigger:
        trigger_index, display_index, trigger = self._validate_and_retrieve_trigger_info(trigger_select)
        return trigger

    def remove_trigger(self, trigger_select: Union[int, TriggerSelect]) -> None:
        trigger_index, display_index, trigger = self._validate_and_retrieve_trigger_info(trigger_select)

        del self.triggers[trigger_index]

        self.reorder_triggers()

    def _find_trigger_tree_nodes_recursively(self, trigger, known_node_indexes: List[int]) -> None:
        found_node_indexes = TriggerManager._find_trigger_tree_nodes(trigger)
        unknown_node_indexes = [i for i in found_node_indexes if i not in known_node_indexes]

        if len(unknown_node_indexes) == 0:
            return

        known_node_indexes += unknown_node_indexes

        for index in unknown_node_indexes:
            self._find_trigger_tree_nodes_recursively(self.triggers[index], known_node_indexes)

    def _validate_and_retrieve_trigger_info(self, trigger_select) -> (int, int, Trigger):
        if type(trigger_select) is int:
            trigger = display_index = None
            trigger_index = trigger_select
        else:
            trigger = trigger_select.trigger
            trigger_index = trigger_select.trigger_index
            display_index = trigger_select.display_index

        try:
            if trigger is not None:
                trigger_index = trigger.trigger_id
                display_index = self.trigger_display_order.index(trigger_index)
            elif trigger_index is not None:
                trigger = self.triggers[trigger_index]
                display_index = self.trigger_display_order.index(trigger_index)
            elif display_index is not None:
                trigger_index = self.trigger_display_order[display_index]
                trigger = self.triggers[trigger_index]
        except IndexError:
            if trigger_index:
                raise ValueError(f"No trigger with index {trigger_index}") from None
            if display_index:
                raise ValueError(f"No Trigger with display index {display_index}") from None

        return trigger_index, display_index, trigger

    def get_summary_as_string(self) -> str:
        return_string = "\nTrigger Summary:\n"

        triggers = self.triggers
        display_order = self.trigger_display_order

        if len(display_order) == 0:
            return_string += "\t<< No Triggers >>"

        longest_trigger_name = -1
        longest_index_notation = -1
        for display, trigger_index in enumerate(display_order):
            trigger_name = triggers[trigger_index].name
            longest_trigger_name = max(longest_trigger_name, len(trigger_name))

            longest_index_notation = max(
                longest_index_notation,
                helper.get_int_len(display) + helper.get_int_len(trigger_index)
            )

        longest_trigger_name += 3
        for display, trigger_index in enumerate(display_order):
            trigger = triggers[trigger_index]
            trigger_name = trigger.name

            name_buffer = longest_trigger_name - len(trigger_name)
            index_buffer = longest_index_notation - (helper.get_int_len(display) + helper.get_int_len(trigger_index))
            return_string += "\t" + trigger_name + (" " * name_buffer)
            return_string += f" [Index: {trigger_index}, Display: {display}] {' ' * index_buffer}"

            return_string += "\t(conditions: " + str(len(trigger.conditions)) + ", "
            return_string += " effects: " + str(len(trigger.effects)) + ")\n"

        return return_string

    def get_content_as_string(self) -> str:
        return_string = "\nTriggers:\n"

        if len(self.triggers) == 0:
            return_string += "\t<<No triggers>>\n"

        for trigger_index in self.trigger_display_order:
            return_string += self.get_trigger_as_string(trigger_index) + "\n"

        return return_string

    def get_trigger_as_string(self, trigger_select: Union[int, TriggerSelect]) -> str:
        trigger_index, display_index, trigger = self._validate_and_retrieve_trigger_info(trigger_select)

        return_string = "\t'" + trigger.name + "'"
        return_string += " [Index: " + str(trigger_index) + ", Display: " + str(display_index) + "]" + ":\n"

        return_string += add_tabs(trigger.get_content_as_string(include_trigger_definition=False), 2)

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
    def _find_trigger_tree_nodes(trigger: Trigger) -> List[int]:
        return [
            effect.trigger_id for effect in trigger.effects if
            effect.effect_type in [EffectId.ACTIVATE_TRIGGER, EffectId.DEACTIVATE_TRIGGER]
        ]

    def __str__(self) -> str:
        return self.get_content_as_string()


def get_activation_effects(trigger: Trigger) -> List[Effect]:
    """
    Get all activation effects in a Trigger]

    Args:
        trigger (Trigger): The trigger object

    Returns:
        A list with (de)activation effects
    """
    return [eff for eff in trigger.effects if eff.effect_type in [
        EffectId.ACTIVATE_TRIGGER, EffectId.DEACTIVATE_TRIGGER
    ]]
