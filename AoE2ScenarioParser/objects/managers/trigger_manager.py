from __future__ import annotations

import copy
from enum import IntEnum
from typing import List, Dict

from AoE2ScenarioParser.datasets.effects import EffectId
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper.helper import value_is_valid
from AoE2ScenarioParser.helper.list_functions import hash_list, list_changed, update_order_array
from AoE2ScenarioParser.helper.printers import warn
from AoE2ScenarioParser.helper.string_manipulations import add_tabs
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.data_objects.effect import Effect
from AoE2ScenarioParser.objects.data_objects.trigger import Trigger
from AoE2ScenarioParser.objects.support.enums.group_by import GroupBy
from AoE2ScenarioParser.objects.support.trigger_ce_lock import TriggerCELock
from AoE2ScenarioParser.objects.support.trigger_select import TriggerSelect
from AoE2ScenarioParser.objects.support.uuid_list import UuidList
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink


class TriggerManager(AoE2Object):
    """
    Manager of everything trigger related.
    This class does not include the logic for DE specific features (e.g. `Variable` objects).
    For those see: `TriggerManagerDE`
    """

    _link_list = [
        RetrieverObjectLink("triggers", "Triggers", "trigger_data", process_as_object=Trigger),
        RetrieverObjectLink("trigger_display_order", "Triggers", "trigger_display_order_array"),
    ]

    def __init__(
            self,
            triggers: List[Trigger],
            trigger_display_order: List[int],
            **kwargs
    ):
        super().__init__(**kwargs)

        self.triggers = triggers
        self.trigger_display_order: List[int] = trigger_display_order
        self._trigger_hash = hash_list(triggers)

    @property
    def triggers(self) -> UuidList[Trigger]:
        """All triggers"""
        return self._triggers

    @triggers.setter
    def triggers(self, triggers: List[Trigger]) -> None:
        triggers = UuidList(self._uuid, triggers, on_update_execute_entry=self._update_triggers_uuid)

        self._trigger_hash = hash_list(triggers)
        self._triggers: UuidList[Trigger] = triggers
        self.trigger_display_order = list(range(len(triggers)))

    def _update_triggers_uuid(self, trigger):
        """Function to update inner UUIDs """
        for effect in trigger.effects:
            effect._uuid = self._uuid
        for condition in trigger.conditions:
            condition._uuid = self._uuid

    @property
    def trigger_display_order(self) -> List[int]:
        """The display order. This is a list of trigger IDs in the display order. NOT execution order!"""
        if list_changed(self.triggers, self._trigger_hash):
            update_order_array(self._trigger_display_order, len(self.triggers))
            self._trigger_hash = hash_list(self.triggers)
        return self._trigger_display_order

    @trigger_display_order.setter
    def trigger_display_order(self, val):
        self._trigger_display_order = val

    def copy_trigger_per_player(
            self,
            from_player: IntEnum,
            trigger_select: int | TriggerSelect,
            change_from_player_only: bool = False,
            include_player_source: bool = True,
            include_player_target: bool = False,
            trigger_ce_lock: TriggerCELock | None = None,
            include_gaia: bool = False,
            create_copy_for_players: List[IntEnum] = None
    ) -> Dict[PlayerId, Trigger]:
        """
        Copies a trigger for all or a selection of players. Every copy will change desired player attributes with it.

        Args:
            from_player: The central player this trigger is created for. This is the player that will not get
                a copy.
            trigger_select: The ID of the trigger or an object used to identify which trigger to select.
            change_from_player_only: If set to `True`,  only change player attributes in effects and conditions that
                are equal to the player defined using the `from_player` parameter.
            include_player_source: If set to `True`,  allow player source attributes to be changed while copying.
                Player source attributes are attributes where a player is defined to perform an action such as create an
                object. If set to `False` these attributes will remain unchanged.
            include_player_target: If set to `True`,  allow player target attributes to be changed while copying.
                Player target attributes are attributes where a player is defined as the target such as change ownership
                or sending resources. If set to `False` these attributes will remain unchanged.
            trigger_ce_lock: The TriggerCELock object. Used to lock certain (types) of conditions or
                effects from being changed while copying.
            include_gaia: If `True`,  GAIA is included in the copied list. (Also when `create_copy_for_players` is
                defined)
            create_copy_for_players: A list of Players to create a copy for. The `from_player` will be
                excluded from this list.

        Returns:
            A dict with all the new created triggers. The key is the player for which the trigger is
                created using the IntEnum associated with it. Example:
                `{PlayerId.TWO: Trigger, PlayerId.FIVE: Trigger}`

        Raises:
            ValueError: if more than one trigger selection is used. Any of (trigger_index, display_index or trigger)
                Or if Both `include_player_source` and `include_player_target` are `False`
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

            new_trigger = self.copy_trigger(TriggerSelect.trigger(trigger), append_after_source=False, add_suffix=False)
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
            trigger_select: int | TriggerSelect,
            append_after_source: bool = True,
            add_suffix: bool = True
    ) -> Trigger:
        """
        Creates an exact copy (deepcopy) of this trigger.

        Args:
            trigger_select: The ID of the trigger or an object used to identify which trigger to select.
            append_after_source: If the new trigger should be appended below the source trigger
            add_suffix: If the text ' (copy)' should be added after the trigger

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

    def copy_trigger_tree_per_player(
            self,
            from_player: IntEnum,
            trigger_select: int | TriggerSelect,
            change_from_player_only: bool = False,
            include_player_source: bool = True,
            include_player_target: bool = False,
            trigger_ce_lock: TriggerCELock | None = None,
            include_gaia: bool = False,
            create_copy_for_players: List[IntEnum] | None = None,
            group_triggers_by: GroupBy | None = None
    ) -> Dict[IntEnum, List[Trigger]]:
        """
        Copies an entire trigger tree for all or a selection of players. Every copy will change desired player
        attributes with it. Trigger trees are triggers linked together using `(de)activate_trigger` effects.

        Args:
            from_player: The central player this trigger is created for. This is the player that will not get
                a copy.
            trigger_select: The ID of the trigger or an object used to identify which trigger to select.
            change_from_player_only: If set to `True`,  only change player attributes in effects and conditions that
                are equal to the player defined using the `from_player` parameter.
            include_player_source: If set to `True`,  allow player source attributes to be changed while copying.
                Player source attributes are attributes where a player is defined to perform an action such as create an
                object. If set to `False` these attributes will remain unchanged.
            include_player_target: If set to `True`,  allow player target attributes to be changed while copying.
                Player target attributes are attributes where a player is defined as the target such as change ownership
                or sending resources. If set to `False` these attributes will remain unchanged.
            trigger_ce_lock: The TriggerCELock object. Used to lock certain (types) of conditions or
                effects from being changed while copying.
            include_gaia: If `True`,  GAIA is included in the copied list. (Also when `create_copy_for_players` is
                defined)
            create_copy_for_players: A list of Players to create a copy for. The `from_player` will be
                excluded from this list.
            group_triggers_by: How to group the newly added triggers.

        Returns:
            The newly created triggers in a dict using the Player as key and as value with a list of triggers
        """
        if group_triggers_by is None:
            group_triggers_by = GroupBy.NONE

        trigger_index, display_index, source_trigger = self._validate_and_retrieve_trigger_info(trigger_select)

        known_node_indexes = [trigger_index]
        self._find_trigger_tree_nodes_recursively(source_trigger, known_node_indexes)

        new_triggers: Dict[IntEnum, List[Trigger]] = {}
        trigger_index_swap = {}

        # Set values for from_player
        new_triggers[from_player] = [self.triggers[i] for i in known_node_indexes]
        for index in known_node_indexes:
            trigger: Trigger = self.triggers[index]
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
        Moves the given IDs from anywhere to the split index. This function reorders triggers BUT keeps
        ``(de)activate trigger`` effects linked properly!

        As an example:

        ```
        [0,1,2,3,4,5,6,7,8]  # Current index order
        # Let's move trigger 1, 4, 5 and 6 to location 2
        self.move_triggers([1, 4, 5, 6], 2)  # << 2 is an INDEX, not the value
        [0,1,4,5,6,2,3,7,8]  # New index order
        ```

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

    def reorder_triggers(self, new_id_order: List[int] = None, ) -> None:
        """
        Reorder all triggers to a given order of IDs. This function reorders triggers BUT keeps ``(de)activate trigger``
        effects linked properly!

        Examples:

            Moving the 6th trigger to the end of the trigger list::

                [0,1,2,3,4,5,6,7,8]  # Trigger IDs before
                self.reorder_triggers([0,1,2,3,5,4,7,8,6])
                [0,1,2,3,5,4,7,8,6]  # Trigger IDs after

            Setting the trigger (execution) order to the current display order::

                self.reorder_triggers(self.trigger_display_order)

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

    def copy_trigger_tree(self, trigger_select: int | TriggerSelect) -> List[Trigger]:
        """
        Copies an entire trigger tree. Trigger trees are triggers linked together using `(de)activate_trigger` effects.

        Args:
            trigger_select: The ID of the trigger or an object used to identify which trigger to select

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
            for effect in get_activation_effects(trigger):
                effect.trigger_id = id_swap[effect.trigger_id]

        return new_triggers

    def replace_player(
            self,
            trigger_select: int | TriggerSelect,
            to_player: PlayerId,
            only_change_from: PlayerId = None,
            include_player_source: bool = True,
            include_player_target: bool = False,
            trigger_ce_lock: TriggerCELock = None
    ) -> Trigger:
        """
        Replaces player attributes. Specifically useful if multiple players are used in the same trigger.

        Args:
            trigger_select: The ID of the trigger or an object used to identify which trigger to select.
            to_player: The player the attributes are changed to.
            only_change_from: Can only change player attributes if the player is equal to the given value
            include_player_source: If set to `True`,  allow player source attributes to be changed while replacing.
                Player source attributes are attributes where a player is defined to perform an action such as create an
                object. If set to `False` these attributes will remain unchanged.
            include_player_target: If set to `True`,  allow player target attributes to be changed while replacing.
                Player target attributes are attributes where a player is defined as the target such as change ownership
                or sending resources. If set to `False` these attributes will remain unchanged.
            trigger_ce_lock: The TriggerCELock object. Used to lock certain (types) of conditions or
                effects from being changed.

        Returns:
            The given trigger with the proper player attributes changed
        """
        trigger_index, display_index, trigger = self._validate_and_retrieve_trigger_info(trigger_select)
        alter_conditions, alter_effects = TriggerManager._find_alterable_ce(trigger, trigger_ce_lock)

        for cond_x in alter_conditions:
            cond = trigger.conditions[cond_x]
            if value_is_valid(cond.source_player) and include_player_source:
                if only_change_from is not None and only_change_from != cond.source_player:
                    continue
                cond.source_player = PlayerId(to_player)
            if value_is_valid(cond.target_player) and include_player_target:
                if only_change_from is not None and only_change_from != cond.target_player:
                    continue
                cond.target_player = PlayerId(to_player)
        for effect_x in alter_effects:
            effect = trigger.effects[effect_x]
            if value_is_valid(effect.source_player) and include_player_source:
                if only_change_from is not None and only_change_from != effect.source_player:
                    continue
                effect.source_player = PlayerId(to_player)
            if value_is_valid(effect.target_player) and include_player_target:
                if only_change_from is not None and only_change_from != effect.target_player:
                    continue
                effect.target_player = PlayerId(to_player)

        return trigger

    def add_trigger(
            self,
            name: str,
            description: str | None = None,
            description_stid: int | None = None,
            display_as_objective: bool | None = None,
            short_description: str | None = None,
            short_description_stid: int | None = None,
            display_on_screen: bool | None = None,
            description_order: int | None = None,
            enabled: bool | None = None,
            looping: bool | None = None,
            header: bool | None = None,
            mute_objectives: bool | None = None,
            conditions: List | None = None,
            effects: List | None = None
    ) -> Trigger:
        """
        Adds a new trigger to the scenario. Everything that is left empty will be set to in-game editor defaults.

        Args:
            name: The name for the trigger
            description: The trigger description
            description_stid: The trigger description string table ID
            display_as_objective: Display the trigger as objective
            short_description: The short trigger description
            short_description_stid: The short trigger description string table ID
            display_on_screen: Display the trigger objective on screen
            description_order: ?
            enabled: If the trigger is enabled from the start.
            looping: If the trigger loops.
            header: Turn objective into header
            mute_objectives: Mute objectives
            conditions: A list of condition managers
            effects: A list of effect managers

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
        new_trigger = Trigger(name=name, trigger_id=len(self.triggers), **trigger_attr, uuid=self._uuid)
        self.triggers.append(new_trigger)
        return new_trigger

    def import_triggers(self, triggers: List[Trigger], index: int = -1, deepcopy: bool = True) -> List[Trigger]:
        """
        Adds existing trigger objects (from another scenario) to this scenario. Keeping all ``(de)activate trigger``
        effects linked!

        Args:
            triggers: The list of Trigger objects to be added
            index: The index where to insert the new triggers, will be added at the end when left unused.
            deepcopy: If the given triggers need to be deep copied or not when importing. Can be useful to keep the
                reference alive between the source and target trigger the same when setting this to `False`.

        Returns:
            The newly added triggers (with the new IDs and activation links etc.)
        """
        if deepcopy:
            triggers = copy.deepcopy(triggers)
        index_changes = {}

        for offset, trigger in enumerate(triggers):
            new_index = len(self.triggers) + offset
            index_changes[trigger.trigger_id] = trigger.trigger_id = new_index

        for trigger in triggers:
            for i, effect in enumerate(get_activation_effects(trigger)):
                try:
                    effect.trigger_id = index_changes[effect.trigger_id]
                except KeyError:
                    warn(f"(De)Activation effect {i} in trigger '{trigger.name}' refers to a trigger that wasn't "
                         f"included in the imported triggers. Effect will be reset")
                    effect.trigger_id = -1

        self.triggers += triggers
        if index != -1:
            self.move_triggers([t.trigger_id for t in triggers], index)
        return triggers

    def get_trigger(self, trigger_select: int | TriggerSelect) -> Trigger:
        """
        Get a single trigger

        Args:
            trigger_select: The ID of the trigger or an object used to identify which trigger to select.

        Returns:
            The selected trigger
        """
        trigger_index, display_index, trigger = self._validate_and_retrieve_trigger_info(trigger_select)
        return trigger

    def remove_trigger(self, trigger_select: int | TriggerSelect) -> None:
        """
        Removes a trigger BUT keeps ``(de)activate trigger`` effects linked properly!

        Args:
            trigger_select: The ID of the trigger or an object used to identify which trigger to select.
        """
        self.remove_triggers([trigger_select])

    def remove_triggers(self, trigger_selects: List[int | TriggerSelect]) -> None:
        """
        Removes a list of triggers BUT keeps ``(de)activate trigger`` effects linked properly!

        Args:
            trigger_selects: The list with trigger IDs
        """
        removing_trigger_ids = [
            self._validate_and_retrieve_trigger_info(trigger_select)[0] for trigger_select in trigger_selects
        ]
        removing_trigger_ids.sort(reverse=True)

        new_display_order = self.compute_updated_display_order(removing_trigger_ids)

        for trigger_id in removing_trigger_ids:
            del self.triggers[trigger_id]

        index_changes = {}
        for new_index, trigger in enumerate(self.triggers):
            if new_index != trigger.trigger_id:
                index_changes[trigger.trigger_id] = new_index
                trigger.trigger_id = new_index

        # Find and update all (de)activation effect trigger references
        for trigger in self.triggers:
            for effect in get_activation_effects(trigger):
                if effect.trigger_id in index_changes:
                    effect.trigger_id = index_changes[effect.trigger_id]

        self.trigger_display_order = new_display_order

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
        """
        Create a human-readable string showcasing a summary of the content of the manager.
        This includes all triggers and the amount of conditions and effects they hold.

        Returns:
            The created string
        """
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
        """
        Create a human-readable string showcasing all content of the manager.
        This includes all triggers and their conditions and effects.

        This is also the function that is called when doing: `print(trigger_manager)`

        Returns:
            The created string
        """
        return_string = "\nTriggers:\n"

        if len(self.triggers) == 0:
            return_string += "\t<<No triggers>>\n"

        for trigger_index in self.trigger_display_order:
            return_string += self.get_trigger_as_string(trigger_index) + "\n"

        return return_string

    def get_trigger_as_string(self, trigger_select: int | TriggerSelect) -> str:
        """
        Create a human-readable string showcasing trigger meta-data and content.

        Args:
            trigger_select: The ID of the trigger or an object used to identify which trigger to select.

        Returns:
            The created string
        """
        trigger_index, display_index, trigger = self._validate_and_retrieve_trigger_info(trigger_select)

        return_string = "\t'" + trigger.name + "'"
        return_string += " [Index: " + str(trigger_index) + ", Display: " + str(display_index) + "]" + ":\n"

        return_string += add_tabs(trigger.get_content_as_string(include_trigger_definition=False), 2)

        return return_string

    @staticmethod
    def _find_alterable_ce(trigger: Trigger, trigger_ce_lock: TriggerCELock) -> (List[int], List[int]):
        """Logic for selecting the proper conditions and effects based on a TriggerCELock"""
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
        """Get all linked trigger ids from all (de)activation effects in a trigger"""
        return [
            effect.trigger_id for effect in trigger.effects if
            effect.effect_type in [EffectId.ACTIVATE_TRIGGER, EffectId.DEACTIVATE_TRIGGER]
        ]

    def __str__(self) -> str:
        return self.get_content_as_string()

    def compute_updated_display_order(self, removing_trigger_ids: List[int]):
        new_display_order = []
        for index in self.trigger_display_order:
            subtract = 0
            skip = False

            for removing_index in removing_trigger_ids:
                if removing_index == index:
                    skip = True
                    break

                if index > removing_index:
                    subtract += 1

            if skip:
                continue

            new_display_order.append(index - subtract)

        return new_display_order


def get_activation_effects(trigger: Trigger) -> List[Effect]:
    """
    Get all activation effects in a Trigger

    Args:
        trigger: The trigger object

    Returns:
        A list with (de)activation effects
    """
    return [eff for eff in trigger.effects if eff.effect_type in [
        EffectId.ACTIVATE_TRIGGER, EffectId.DEACTIVATE_TRIGGER
    ]]
