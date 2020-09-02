from __future__ import annotations

import copy
from enum import IntEnum
from typing import List, Dict, Set

from AoE2ScenarioParser.datasets.effects import Effect
from AoE2ScenarioParser.datasets.players import Player
from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper import parser
from AoE2ScenarioParser.helper.retriever import get_retriever_by_name
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.trigger_obj import TriggerObject
from AoE2ScenarioParser.objects.variable_obj import VariableObject


class TriggersObject(AoE2Object):
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
                                from_player: IntEnum,
                                change_from_player_only: bool = False,
                                include_player_source: bool = True,
                                include_player_target: bool = False,

                                trigger_index: int = None,
                                display_index: int = None,
                                trigger: TriggerObject = None,

                                lock_conditions: bool = False,
                                lock_effects: bool = False,
                                lock_condition_type: List[IntEnum] = None,
                                lock_effect_type: List[IntEnum] = None,
                                lock_condition_ids: List[int] = None,
                                lock_effect_ids: List[int] = None,

                                include_gaia: bool = False,
                                create_copy_for_players: List[IntEnum] = None) -> Dict[Player, TriggerObject]:
        """
        Copies a trigger for all or a selection of players. Every copy will change desired player attributes with it.
        Creates copies for all other players if `create_copy_for_players` is left to default.
        By default 'all players' is every player (1-8) excluding the `from_player` value.
        So when `from_player` is set to Player.SEVEN the copies will be: [1, 2, 3, 4, 5, 6, 8].
        When `from_player` is set to Player.GAIA the copies will include all 1-8 players.
        When `change_from_player_only` is set to False (Default) "all player attributes"* will be changed to the copied
        player. When set to true only player attributes that are equal to the `from_player` parameter will be changed.
        The meaning of "All player attributes" is based on the settings of the parameters:
        `include_player_source` (Default: True) and `include_player_target` (Default: False).

        When doing a copy, some conditions or effects might want to stay unchanged. You can do this by 'locking' them.
        You can lock effects and conditions separately in three ways. Locking all effects or conditions, locking a
        specific type (Effect.x) or locking certain specific ones using their IDs.

        When creating the copy you can include a copy for the GAIA 'player'. You can do so by enabling the
        `include_gaia` parameter.

        Args:
            from_player: The player the trigger is copied from. This should be the central player or the player that
                should be changed in all conditions and effects when the `change_from_player_only` is set to `True`
            change_from_player_only: Ensures that only player attributes equal to `from_player` are changed per copy
            include_player_source: Ensures that only source_player attributes are changed
            include_player_target: Ensures that only target_player attributes are changed
            trigger_index: Selects a trigger based on it's index (Mutually exclusive with `display_index` and `trigger`)
            display_index: Selects a trigger based on it's display index (Mutually exclusive with `trigger_index` and
                `trigger`)
            trigger: Selects a trigger (Mutually exclusive with `trigger_index` and `display_index`)
            lock_conditions: Ensures that no player attributes are changed in any condition
            lock_effects: Ensures that no player attributes are changed in any effect
            lock_condition_type: Ensures that no player attributes are changed in the given condition type
            lock_effect_type: Ensures that no player attributes are changed in the given effect type
            lock_condition_ids: Ensures that no player attributes are changed in the given condition IDs
            lock_effect_ids: Ensures that no player attributes are changed in the given effect IDs
            include_gaia: If `True` creates a copy for GAIA
            create_copy_for_players: Copy for certain and overwrite the default (All players)

        Returns:
            Dict: A dict with all the new created triggers. The key is the player for which the trigger is
                created using the IntEnum associated with it. Example: {Player.TWO: TriggerObject, Player.FIVE: TriggerObject}

        Raises:
            ValueError: if more than one trigger selection is used. Any of (trigger_index, display_index or trigger)
                Or if Both `include_player_source` and `include_player_target` are `False`

        :Authors:
            KSneijders
        """

        trigger_index, display_index, trigger = self._compute_trigger_info(trigger_index, display_index, trigger)
        if not include_player_source and not include_player_target:
            raise ValueError("Cannot exclude player source and target.")

        if lock_conditions is None:
            lock_conditions = []
        if lock_effects is None:
            lock_effects = []
        if lock_condition_type is None:
            lock_condition_type = []
        if lock_effect_type is None:
            lock_effect_type = []
        if lock_condition_ids is None:
            lock_condition_ids = []
        if lock_effect_ids is None:
            lock_effect_ids = []

        if create_copy_for_players is None:
            create_copy_for_players = [
                Player.ONE, Player.TWO, Player.THREE, Player.FOUR,
                Player.FIVE, Player.SIX, Player.SEVEN, Player.EIGHT
            ]
        if include_gaia and Player.GAIA not in create_copy_for_players:
            create_copy_for_players.append(Player.GAIA)

        alter_conditions, alter_effects = TriggersObject._find_alterable_ce(
            trigger, lock_conditions, lock_effects,
            lock_condition_type, lock_effect_type,
            lock_condition_ids, lock_effect_ids
        )

        return_dict: Dict[Player, TriggerObject] = {}
        for player in create_copy_for_players:
            if not player == from_player:
                new_trigger = self.copy_trigger(trigger=trigger)
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

    def copy_trigger(self, trigger_index: int = None, display_index: int = None, trigger: TriggerObject = None) \
            -> TriggerObject:
        trigger_index, display_index, trigger = self._compute_trigger_info(trigger_index, display_index, trigger)

        deepcopy_trigger = copy.deepcopy(trigger)
        deepcopy_trigger.name += " (copy)"
        deepcopy_trigger.trigger_id = len(self.triggers)
        self.triggers.append(deepcopy_trigger)
        helper.update_order_array(self.trigger_display_order, len(self.triggers))

        return deepcopy_trigger

    def copy_trigger_tree(self, trigger_index: int = None, display_index: int = None, trigger: TriggerObject = None) \
            -> List[TriggerObject]:
        trigger_index, display_index, trigger = self._compute_trigger_info(trigger_index, display_index, trigger)

        known_node_indexes = {trigger_index}
        # Create new instance of `known_node_indexes` so it doesn't receive updates from the recursion
        for index in set(known_node_indexes):
            self.find_trigger_tree_nodes_recursively(self.triggers[index], known_node_indexes)

        new_triggers = []
        id_swap = {}
        for index in known_node_indexes:
            trigger = self.copy_trigger(trigger_index=index)
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

    def find_trigger_tree_nodes_recursively(self, trigger, known_node_indexes: Set[int]) -> None:
        found_node_indexes = TriggersObject.find_trigger_tree_nodes(trigger)
        unknown_node_indexes = found_node_indexes.difference(known_node_indexes)

        if len(unknown_node_indexes) == 0:
            return

        known_node_indexes.update(unknown_node_indexes)

        for index in unknown_node_indexes:
            self.find_trigger_tree_nodes_recursively(self.triggers[index], known_node_indexes)

    @staticmethod
    def find_trigger_tree_nodes(trigger: TriggerObject) -> Set[int]:
        return {
            effect.trigger_id for effect in trigger.effects if
            effect.effect_type in [Effect.ACTIVATE_TRIGGER, Effect.DEACTIVATE_TRIGGER]
        }

    def replace_player(self,
                       source_player_replacements: Dict[int, int] = None,
                       target_player_replacements: Dict[int, int] = None,

                       trigger_index: int = None,
                       display_index: int = None,
                       trigger: TriggerObject = None,

                       lock_conditions: bool = False,
                       lock_effects: bool = False,
                       lock_condition_type: List[IntEnum] = None,
                       lock_effect_type: List[IntEnum] = None,
                       lock_condition_ids: List[int] = None,
                       lock_effect_ids: List[int] = None) -> TriggerObject:

        trigger_index, display_index, trigger = self._compute_trigger_info(trigger_index, display_index, trigger)

        if lock_conditions is None:
            lock_conditions = []
        if lock_effects is None:
            lock_effects = []
        if lock_condition_type is None:
            lock_condition_type = []
        if lock_effect_type is None:
            lock_effect_type = []
        if lock_condition_ids is None:
            lock_condition_ids = []
        if lock_effect_ids is None:
            lock_effect_ids = []

        alter_conditions, alter_effects = TriggersObject._find_alterable_ce(
            trigger, lock_conditions, lock_effects,
            lock_condition_type, lock_effect_type,
            lock_condition_ids, lock_effect_ids
        )

        for cond_x in alter_conditions:
            cond = trigger.conditions[cond_x]
            if not cond.source_player == -1:
                cond.source_player = Player(source_player_replacements[cond.source_player])
            if not cond.target_player == -1:
                cond.target_player = Player(target_player_replacements[cond.source_player])
        for effect_x in alter_effects:
            effect = trigger.effects[effect_x]
            if not effect.source_player == -1:
                effect.source_player = Player(source_player_replacements[effect.source_player])
            if not effect.target_player == -1:
                effect.target_player = Player(target_player_replacements[effect.target_player])

        return trigger

    def add_trigger(self, name: str) -> TriggerObject:
        new_trigger = TriggerObject(name=name, trigger_id=len(self.triggers))
        self.triggers.append(new_trigger)
        helper.update_order_array(self.trigger_display_order, len(self.triggers))
        return new_trigger

    def add_variable(self, variable_id: int, name: str) -> VariableObject:
        if not (0 <= variable_id <= 255):
            raise ValueError("Variable ID has to fall between 0 and 255 (incl).")

        new_variable = VariableObject(variable_id=variable_id, name=name)
        self.variables.append(new_variable)
        return new_variable

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
            return_string += self.get_trigger_as_string(trigger_index) + "\n"

        return_string += "Variables:\n"

        if len(self.variables) == 0:
            return_string += "\t<<No Variables>>\n"

        for variable in self.variables:
            return_string += f"\t'{variable.name}' [Index: {variable.variable_id}]\n"

        return return_string

    def get_trigger_as_string(self, trigger_index: int = None, display_index: int = None) -> str:
        trigger_index, display_index, trigger = self._compute_trigger_info(trigger_index, display_index)

        return_string = "\t'" + trigger.name + "'"
        return_string += " [Index: " + str(trigger_index) + ", Display: " + str(display_index) + "]" + ":\n"

        return_string += trigger.get_content_as_string()

        return return_string

    def get_trigger(self, trigger_index: int = None, display_index: int = None) -> TriggerObject:
        trigger_index, display_index, trigger = self._compute_trigger_info(trigger_index, display_index)

        return trigger

    def get_variable(self, variable_id: int = None, variable_name: str = None) -> VariableObject:
        if variable_id is None and variable_name is None:
            raise ValueError("Select a variable using the variable_id or variable_name parameters")
        if variable_id is not None and variable_name is not None:
            raise ValueError("Select a variable using either the variable_id or variable_name parameters, not both.")

        for variable in self.variables:
            if variable.variable_id == variable_id or variable.name == variable_name:
                return variable

    def remove_trigger(self,
                       trigger_index: int = None,
                       display_index: int = None,
                       trigger: TriggerObject = None) -> None:
        trigger_index, display_index, trigger = self._compute_trigger_info(trigger_index, display_index, trigger)

        for x in self.trigger_display_order:
            if x > trigger_index:
                self.get_trigger(trigger_index=x).trigger_id -= 1

        del self.triggers[trigger_index]
        del self.trigger_display_order[display_index]

        self.trigger_display_order = [x - 1 if x > trigger_index else x for x in self.trigger_display_order]

    def _compute_trigger_info(self,
                              trigger_index: int = None,
                              display_index: int = None,
                              trigger: TriggerObject = None) -> (int, int, TriggersObject):
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

    @staticmethod
    def _find_alterable_ce(trigger,
                           lock_conditions,
                           lock_effects,
                           lock_condition_type,
                           lock_effect_type,
                           lock_condition_ids,
                           lock_effect_ids) -> (List[int], List[int]):
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
    def _parse_object(parsed_data, **kwargs) -> TriggersObject:  # Expected {}
        display_order = get_retriever_by_name(parsed_data['TriggerPiece'].retrievers, "Trigger display order array").data
        trigger_data = get_retriever_by_name(parsed_data['TriggerPiece'].retrievers, "Trigger data").data
        var_data = get_retriever_by_name(parsed_data['TriggerPiece'].retrievers, "Variables").data

        triggers = []
        for index, trigger in enumerate(trigger_data):
            triggers.append(TriggerObject._parse_object(parsed_data, trigger=trigger, trigger_id=index))

        variables = []
        for var in var_data:
            variables.append(VariableObject._parse_object(parsed_data, variable=var))

        return TriggersObject(
            triggers=triggers,
            trigger_display_order=display_order,
            variables=variables
        )

    @staticmethod
    def _reconstruct_object(parsed_header, parsed_data, objects, **kwargs) -> None:  # Expected {}
        number_of_triggers_retriever = get_retriever_by_name(parsed_data['TriggerPiece'].retrievers, "Number of triggers")
        trigger_data_retriever = get_retriever_by_name(parsed_data['TriggerPiece'].retrievers, "Trigger data")
        display_order_retriever = get_retriever_by_name(parsed_data['TriggerPiece'].retrievers, "Trigger display order array")
        display_order_retriever.data = display_order_retriever.data
        file_header_trigger_count_retriever = get_retriever_by_name(parsed_header['FileHeaderPiece'].retrievers,
                                                             "Trigger count")

        number_of_variable_retriever = get_retriever_by_name(
            parsed_data['TriggerPiece'].retrievers, "Number of variables")
        variable_data_retriever = get_retriever_by_name(parsed_data['TriggerPiece'].retrievers, "Variables")

        trigger_data_retriever.data = []
        for trigger in objects["TriggersObject"].triggers:
            TriggerObject._reconstruct_object(parsed_header, parsed_data, objects, trigger=trigger)

        variable_data_retriever.data = []
        for variable in objects["TriggersObject"].variables:
            VariableObject._reconstruct_object(parsed_header, parsed_data, objects, variable=variable,
                                               variables=variable_data_retriever.data)

        assert len(trigger_data_retriever.data) == len(objects["TriggersObject"].triggers)
        trigger_count = len(trigger_data_retriever.data)
        number_of_triggers_retriever.data = trigger_count
        file_header_trigger_count_retriever.data = trigger_count
        number_of_variable_retriever.data = len(variable_data_retriever.data)
        # Currently not necessary due to the parser changing the 'repeated' value equal to the len(list)
        # trigger_data_retriever.datatype.repeat = trigger_count
        # display_order_retriever.datatype.repeat = trigger_count
        helper.update_order_array(display_order_retriever.data, trigger_count)
