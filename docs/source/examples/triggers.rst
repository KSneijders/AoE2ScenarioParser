Example - Triggers
=========================

You can use the trigger manager to add, remove edit and view triggers and variables.

Adding Triggers
^^^^^^^^^^^^^^^

a::

    # File & Folder setup
    from AoE2ScenarioParser.aoe2_scenario import AoE2Scenario
    from AoE2ScenarioParser.datasets.conditions import Condition
    from AoE2ScenarioParser.datasets.effects import Effect
    from AoE2ScenarioParser.datasets.players import Player
    from AoE2ScenarioParser.datasets.units import Unit

    # Define paths to scenario
    scenario_folder = "C:/Users/Kerwin Sneijders/Games/Age of Empires 2 DE/76561198140740017/resources/_common/scenario/"
    read_file = scenario_folder + "testout.aoe2scenario"
    write_to_file = scenario_folder + "test10.aoe2scenario"

    # Define Scenario file
    scenario = AoE2Scenario(read_file)

    # Add Trigger
    trigger_manager = scenario.trigger_manager
    trigger = trigger_manager.add_trigger("Trigger Name Here")

    # Add Timer Condition
    timer_condition = trigger.add_condition(Condition.TIMER)
    timer_condition.timer = 20

    # Add Create Object Effect 
    create_paladin_effect = trigger.add_effect(Effect.CREATE_OBJECT)
    create_paladin_effect.object_list_unit_id = Unit.PALADIN
    create_paladin_effect.source_player = Player.ONE
    create_paladin_effect.location_x = 5
    create_paladin_effect.location_y = 4

