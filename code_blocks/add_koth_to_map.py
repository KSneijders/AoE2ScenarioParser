from AoE2ScenarioParser.aoe2_scenario import AoE2Scenario
from AoE2ScenarioParser.datasets import effects, conditions, buildings
from AoE2ScenarioParser.datasets.players import Player, PlayerColor

# File & Folder setup
scenario_folder = "C:/Users/<USER>/Games/Age of Empires 2 DE/<STEAM_ID>/resources/_common/scenario/"
read_file = scenario_folder + "mapName.aoe2scenario"
write_to_file = "mapName_KOTH.aoe2scenario"

# Reading the scenario & Getting trigger manager
scenario = AoE2Scenario(read_file, log_parsing=True)
trigger_manager = scenario.object_manager.trigger_manager

# Create new trigger named "StartYearCountdown", add effects & conditions to it
StartYearCountdown = trigger_manager.add_trigger("StartYearCountdown")

condition = StartYearCountdown.add_condition(conditions.owh_fewer_objects)
condition.amount_or_quantity = 0
condition.object_list = buildings.monument
condition.player = Player.GAIA.value

effect = StartYearCountdown.add_effect(effects.change_variable)
effect.quantity = 550
effect.operation = 1
effect.from_variable = 1
effect.message = "Years"

effect = StartYearCountdown.add_effect(effects.change_variable)
effect.quantity = 0
effect.operation = 1
effect.from_variable = 2
effect.message = "PlayerControl"

# Create trigger named "LowerYears"
LowerYears = trigger_manager.add_trigger("LowerYears")
LowerYears.looping = 1

condition = LowerYears.add_condition(conditions.timer)
condition.timer = 5

condition = LowerYears.add_condition(conditions.variable_value)
condition.amount_or_quantity = 0
condition.inverted = 0
condition.variable = 1
condition.comparison = 2

effect = LowerYears.add_effect(effects.change_variable)
effect.quantity = 1
effect.operation = 3
effect.from_variable = 1
effect.message = "Years"

# For every year, add a trigger showing the timer
for year in range(550, -1, -1):
    trigger = trigger_manager.add_trigger("CountdownTimer_" + str(year))
    trigger.looping = 1

    condition = trigger.add_condition(conditions.variable_value)
    condition.amount_or_quantity = year
    condition.inverted = 0
    condition.variable = 1
    condition.comparison = 0

    effect = trigger.add_effect(effects.clear_timer)
    effect.variable_or_timer = 0

    effect = trigger.add_effect(effects.display_timer)
    effect.display_time = 1
    effect.time_unit = 2
    effect.variable_or_timer = 0
    effect.message = f"Years Remaining: {year}"

# For every player add multiple triggers for who controls the monument and victory conditions
for player in range(1, 9):
    """Trigger per player for capturing the monument and update the variables etc."""
    trigger = trigger_manager.add_trigger("Player" + str(player) + "CapturesMonument")
    trigger.looping = 1

    condition = trigger.add_condition(conditions.timer)
    condition.timer = 5

    condition = trigger.add_condition(conditions.own_objects)
    condition.object_list = buildings.monument
    condition.amount_or_quantity = 1
    condition.player = player

    effect = trigger.add_effect(effects.clear_timer)
    effect.variable_or_timer = 1

    effect = trigger.add_effect(effects.display_timer)
    effect.display_time = 1
    effect.time_unit = 0
    effect.variable_or_timer = 1
    effect.message = f"<{PlayerColor(player).name}>Monument owned by {PlayerColor(player).name}"

    """
    Trigger per player for capturing the monument and update the variables etc. after the 100 year mark for resetting
    the timer
    """
    trigger = trigger_manager.add_trigger("Player" + str(player) + "CapturesMonumentBelow100Years")
    trigger.looping = 1

    condition = trigger.add_condition(conditions.own_objects)
    condition.object_list = buildings.monument
    condition.amount_or_quantity = 1
    condition.player = player

    condition = trigger.add_condition(conditions.variable_value)
    condition.amount_or_quantity = 100
    condition.comparison = 1
    condition.variable = 1
    condition.inverted = 0

    condition = trigger.add_condition(conditions.variable_value)
    condition.amount_or_quantity = player
    condition.comparison = 0
    condition.variable = 2
    condition.inverted = 1

    effect = trigger.add_effect(effects.change_variable)
    effect.quantity = 100
    effect.operation = 1
    effect.from_variable = 1
    effect.message = "Years"

    effect = trigger.add_effect(effects.change_variable)
    effect.quantity = player
    effect.operation = 1
    effect.from_variable = 2
    effect.message = "PlayerCaptured"

    """Trigger per player for capturing the monument for the first time. (Fix for Year<100 first time bug)"""
    trigger = trigger_manager.add_trigger("PlayerCapturedFirstTime" + str(player))

    condition = trigger.add_condition(conditions.own_objects)
    condition.object_list = buildings.monument
    condition.amount_or_quantity = 1
    condition.player = player

    effect = trigger.add_effect(effects.change_variable)
    effect.quantity = player
    effect.operation = 1
    effect.from_variable = 2
    effect.message = "PlayerCaptured"

    """Trigger per player for Victory Condition"""
    trigger = trigger_manager.add_trigger("VictoryPlayer" + str(player))

    condition = trigger.add_condition(conditions.variable_value)
    condition.amount_or_quantity = 0
    condition.inverted = 0
    condition.variable = 1
    condition.comparison = 0

    condition = trigger.add_condition(conditions.variable_value)
    condition.amount_or_quantity = player
    condition.comparison = 0
    condition.variable = 2
    condition.inverted = 0

    effect = trigger.add_effect(effects.declare_victory)
    effect.player_source = player

# Write scenario
scenario.write_to_file(scenario_folder + write_to_file, log_reconstructing=True)
