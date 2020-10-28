Example - Triggers
=========================

You can use the trigger manager to add, remove edit and view triggers and variables.

Adding Triggers
^^^^^^^^^^^^^^^

Here's an example of how to create (add) a trigger and add a condition and effect to it::

    # File & Folder setup
    from AoE2ScenarioParser.aoe2_scenario import AoE2Scenario
    from AoE2ScenarioParser.datasets.conditions import Condition
    from AoE2ScenarioParser.datasets.effects import Effect
    from AoE2ScenarioParser.datasets.players import Player
    from AoE2ScenarioParser.datasets.units import Unit

    # Define paths to scenario, you can find this folder by opening AoE2:DE and going to scenarios and clicking on 'open folder'
    scenario_folder = "YOUR_PATH_TO_THE_SCENARIO_FOLDER"
    read_file = scenario_folder + "MAP_NAME_TO_BE_READ.aoe2scenario"

    # Define Scenario file
    scenario = AoE2Scenario.from_file(read_file)

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

Select existing Triggers
^^^^^^^^^^^^^^^^^^^^^^^^

Selecting a trigger can be done using the ``get_trigger`` function. The function accepts 2 arguments, ``trigger_index`` and ``display_index``.
The ``trigger_index`` expects the trigger ID of a trigger. This is the a number related to the order of creation starting from 0. 
The ``display_index`` expects the display ID of a trigger. This is the a number related to the display order in the in-game editor.
You can use the ``get_summary_as_string`` function to view these values without opening the in-game editor. 
The code below includes the code above::

    print(trigger_manager.get_summary_as_string())

    # Results in:
    """
    Trigger Summary:
        Trigger Name Here    [Index: 0, Display: 0]	(conditions: 1,  effects: 1)

    Variables Summary:
        << No Variables >>
    """

As you can see, the trigger and display index can be seen in the ``[Index: x, Display: x]`` part. 
These are the numbers you can use to select triggers. Which would look like::

    # Define Scenario file
    scenario = AoE2Scenario.from_file(read_file)

    # Get Trigger
    trigger_manager = scenario.trigger_manager
    trigger = trigger_manager.get_trigger(display_index=0)

If you want to see the contents of the trigger you can do so by running the ``get_content_as_string`` function.
This will result in the following (with the ``create trigger`` code)::

    print(trigger_manager.get_content_as_string())
    
    # Results in:
    """
    Triggers:
        'Trigger Name Here' [Index: 0, Display: 0]:
            enabled: True
            looping: False
            conditions:
                timer [Index: 0, Display: 0]:
                    timer: 20
                    inverted: 0
            effects:
                create_object [Index: 0, Display: 0]:
                    object_list_unit_id: Unit.PALADIN
                    source_player: Player.ONE
                    location_x: 5
                    location_y: 4
                    facet: 0

    Variables:
        <<No Variables>>
    """