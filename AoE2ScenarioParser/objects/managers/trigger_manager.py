from __future__ import annotations

import copy
from enum import IntEnum
from typing import List, Dict

from AoE2ScenarioParser.datasets.effects import EffectId
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.data_objects.trigger import Trigger


class TriggerManager(AoE2Object):
    """Manager of the everything trigger related."""

    def __init__(self,
                 triggers: List[Trigger],
                 trigger_display_order: List[int],
                 ):

        self._trigger_hash = helper.hash_list(triggers)
        self.triggers: List[Trigger] = triggers
        self.trigger_display_order: List[int] = trigger_display_order

        super().__init__()

    @property
    def trigger_display_order(self):
        if helper.list_changed(self.triggers, self._trigger_hash):
            helper.update_order_array(self._trigger_display_order, len(self.triggers))
            self._trigger_hash = helper.hash_list(self.triggers)
        return self._trigger_display_order

    @trigger_display_order.setter
    def trigger_display_order(self, val):
        self._trigger_display_order = val

    def copy_trigger_per_player(self,
                                from_player,
                                trigger_select,
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
                {PlayerId.TWO: Trigger, PlayerId.FIVE: Trigger}

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
                PlayerId.ONE, PlayerId.TWO, PlayerId.THREE, PlayerId.FOUR,
                PlayerId.FIVE, PlayerId.SIX, PlayerId.SEVEN, PlayerId.EIGHT
            ]
        if include_gaia and PlayerId.GAIA not in create_copy_for_players:
            create_copy_for_players.append(PlayerId.GAIA)

        alter_conditions, alter_effects = TriggerManager._find_alterable_ce(trigger, trigger_ce_lock)

        return_dict: Dict[PlayerId, Trigger] = {}
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
                        cond.source_player = PlayerId(player)
                    # Change target player
                    if include_player_target:
                        cond.target_player = PlayerId(player)
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
                        effect.source_player = PlayerId(player)
                    # Change target player
                    if include_player_target:
                        effect.target_player = PlayerId(player)

        return return_dict

    def copy_trigger(self, trigger_select) -> Trigger:
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

        return deepcopy_trigger

    def copy_trigger_tree_per_player(self,
                                     from_player,
                                     trigger_select,
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
        id_swap = {}
        for index in known_node_indexes:
            triggers = self.copy_trigger_per_player(
                from_player,
                TS.index(index),
                change_from_player_only,
                include_player_source,
                include_player_target,
                trigger_ce_lock,
                include_gaia,
                create_copy_for_players,
            )
            for player, trigger in triggers.items():
                id_swap.setdefault(index, {})[player] = trigger.trigger_id
                new_triggers.setdefault(player, []).append(trigger)

        for player, triggers in new_triggers.items():
            for trigger in triggers:
                activation_effects = [
                    effect for effect in trigger.effects if
                    effect.effect_type in [EffectId.ACTIVATE_TRIGGER, EffectId.DEACTIVATE_TRIGGER]
                ]
                for effect in activation_effects:
                    effect.trigger_id = id_swap[effect.trigger_id][player]

        # Group by logic
        if group_triggers_by == GroupBy.TRIGGER:
            for index, source_trigger_id in enumerate(known_node_indexes):
                for player, trigger in [(player, triggers[index]) for player, triggers in new_triggers.items()]:
                    # When going negative (going 'below' the source already happens at insert @ 0
                    display_index_offset = player - from_player if from_player <= player else 0
                    source_trigger_display_index = self.trigger_display_order.index(source_trigger_id)
                    self.trigger_display_order.remove(trigger.trigger_id)
                    new_display_index = max(0, source_trigger_display_index + display_index_offset)
                    self.trigger_display_order.insert(
                        new_display_index,
                        trigger.trigger_id
                    )
        elif group_triggers_by == GroupBy.PLAYER:
            source_trigger_display_index = display_index
            source_trigger_offset = 0
            # Group known tree nodes
            for tree_trigger_id in known_node_indexes:
                self.trigger_display_order.remove(tree_trigger_id)
                self.trigger_display_order.insert(
                    source_trigger_display_index + source_trigger_offset,
                    tree_trigger_id
                )
                source_trigger_offset += 1
            # Group copied triggers
            for player, triggers in new_triggers.items():
                source_trigger_display_index = self.trigger_display_order.index(source_trigger.trigger_id)
                source_trigger_offset = 0
                display_index_offset = (player - from_player if from_player <= player else 0) * len(known_node_indexes)
                for trigger in triggers:
                    final_offset = max(source_trigger_display_index + display_index_offset + source_trigger_offset, 0)
                    self.trigger_display_order.remove(trigger.trigger_id)
                    self.trigger_display_order.insert(
                        final_offset,
                        trigger.trigger_id
                    )
                    source_trigger_offset += 1

        return new_triggers

    def copy_trigger_tree(self, trigger_select: TriggerSelect) -> List[Trigger]:
        trigger_index, display_index, trigger = self._validate_and_retrieve_trigger_info(trigger_select)

        known_node_indexes = [trigger_index]
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
                effect.effect_type in [EffectId.ACTIVATE_TRIGGER, EffectId.DEACTIVATE_TRIGGER]
            ]
            for effect in activation_effects:
                effect.trigger_id = id_swap[effect.trigger_id]

        return new_triggers

    def replace_player(self, trigger_select, to_player, only_change_from=None, include_player_source=True,
                       include_player_target=False, trigger_ce_lock=None) -> Trigger:
        """
        Replaces player attributes. Specifically useful if multiple players are used in the same trigger.

        Args:
            trigger_select (TriggerSelect): An object used to identify which trigger to select.
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
            if not cond.source_player == -1 and include_player_source:
                if only_change_from is not None and only_change_from != cond.source_player:
                    continue
                cond.source_player = PlayerId(to_player)
            if not cond.target_player == -1 and include_player_target:
                if only_change_from is not None and only_change_from != cond.target_player:
                    continue
                cond.target_player = PlayerId(to_player)
        for effect_x in alter_effects:
            effect = trigger.effects[effect_x]
            if not effect.source_player == -1 and include_player_source:
                if only_change_from is not None and only_change_from != effect.source_player:
                    continue
                effect.source_player = PlayerId(to_player)
            if not effect.target_player == -1 and include_player_target:
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
        new_trigger = Trigger(name=name, trigger_id=len(self.triggers), **trigger_attr)
        self.triggers.append(new_trigger)
        # helper.update_order_array(self._trigger_display_order, len(self.triggers))
        return new_trigger

    def get_trigger(self, trigger_select: TriggerSelect) -> Trigger:
        trigger_index, display_index, trigger = self._validate_and_retrieve_trigger_info(trigger_select)
        return trigger

    def remove_trigger(self, trigger_select: TriggerSelect) -> None:
        trigger_index, display_index, trigger = self._validate_and_retrieve_trigger_info(trigger_select)

        for x in self.trigger_display_order:
            if x > trigger_index:
                self.get_trigger(TS.index(x)).trigger_id -= 1

        del self.triggers[trigger_index]
        del self.trigger_display_order[display_index]

        self.trigger_display_order = [x - 1 if x > trigger_index else x for x in self.trigger_display_order]

    def _find_trigger_tree_nodes_recursively(self, trigger, known_node_indexes: List[int]) -> None:
        found_node_indexes = TriggerManager._find_trigger_tree_nodes(trigger)
        # unknown_node_indexes = found_node_indexes.difference(known_node_indexes)
        unknown_node_indexes = [i for i in found_node_indexes if i not in known_node_indexes]

        if len(unknown_node_indexes) == 0:
            return

        known_node_indexes += unknown_node_indexes

        for index in unknown_node_indexes:
            self._find_trigger_tree_nodes_recursively(self.triggers[index], known_node_indexes)

    def _validate_and_retrieve_trigger_info(self, trigger_select) -> (int, int, TriggerManager):
        trigger = trigger_select.trigger
        trigger_index = trigger_select.trigger_index
        display_index = trigger_select.display_index

        if trigger is not None:
            trigger_index = trigger.trigger_id
            display_index = self.trigger_display_order.index(trigger_index)
        elif trigger_index is not None:
            trigger = self.triggers[trigger_index]
            display_index = self.trigger_display_order.index(trigger_index)
        elif display_index is not None:
            trigger_index = self.trigger_display_order[display_index]
            trigger = self.triggers[trigger_index]

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
            return_string += self.get_trigger_as_string(TS.index(trigger_index)) + "\n"

        return_string += "Variables:\n"

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
    def _find_trigger_tree_nodes(trigger: Trigger) -> List[int]:
        return [
            effect.trigger_id for effect in trigger.effects if
            effect.effect_type in [EffectId.ACTIVATE_TRIGGER, EffectId.DEACTIVATE_TRIGGER]
        ]


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
            trigger (Trigger): The trigger object itself.
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
    def trigger(cls, trigger: Trigger):
        return cls(trigger=trigger)


TS = TriggerSelect


class TriggerCELock:
    def __init__(self, lock_conditions=False, lock_effects=False, lock_condition_type=None, lock_effect_type=None,
                 lock_condition_ids=None, lock_effect_ids=None):
        """
        Object used to identify which conditions and effects should be locked from change.

        Args:
            lock_conditions (bool): Lock all conditions
            lock_effects (bool): Lock all effects
            lock_condition_type (List[int]): Lock certain condition types. Example: `ConditionId.OWN_OBJECTS`
            lock_effect_type (List[int]): Lock certain effect types. Example: `EffectId.CREATE_OBJECT`
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


class GroupBy(IntEnum):
    """
    Enum used to select what way the triggers should be grouped when using the function 'copy_trigger_tree_per_player'.
    Each mode has it's own explanation explained in the corresponding docstring.
    """
    NONE = -1
    """
    Don't group triggers. Add triggers to the end of the list. This could mean the source triggers aren't near the 
    copies. All copies, however, will be grouped like the TRIGGER grouping mechanism - at the end of the list.
    """
    TRIGGER = 0
    """
    Group triggers by trigger. All copies of a trigger will be put directly below the 'source' trigger. 
    Example: If the 'source' trigger has display_index of 3, and another trigger in it's tree has 5. Assuming the 
    triggers were copied for all players, display indexes of the copies from the first trigger would be 4-10. The second
    trigger in the tree would be bumped up to 12 (from 5) and it's copies would use: 13-19. 
    """
    PLAYER = 1
    """
    Group triggers by player. Warning: This mode could change some of the intended order of the triggers. All copies of
    the trigger will be put together sorted on player first, then trigger order. 
    Example: If the 'source' trigger has display_index of 3, and another trigger in it's tree has 5. Assuming the 
    triggers were copied for all players, display indexes of the copies from the firs trigger would be: 5, 7, 9, 11, 13,
    15 and 17. The second trigger would have moved to 4 (from 5) and it's copies would occupy slots: 6, 8, 10, 12, 14, 
    16 and 18. This way both PlayerId.ONE (assuming that's the source player) triggers will be together, same goes for all
    other player. 
    
    In the example above can be seen how the second trigger was moved from 5 to 4. The unrelated trigger in between was
    moved to the end, 19. This might be an unwanted side effect, be aware.
    """
