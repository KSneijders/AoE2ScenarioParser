Trigger FAQ (Examples)
======================

This page shows questions I've been asked and my answers to said questions.
These examples might help you get the hang of it a little faster.  

Questions
---------

I will expand this list whenever I get more questions (and have time to add them). 
If you have any questions, and the docs don't answer them, feel free to send them my way! 

Check the support page for up-to-date contact info.

Replace all sound names with a specific name 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

How to replace all sound names in effects with the name: ``OldName`` to ``NewName``?

.. code:: py

    # Import the scenario object
    from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

    # Define Scenario file
    scenario = AoE2DEScenario.from_file(file_path_here)

    trigger_manager = scenario.trigger_manager

    # Loop through all triggers
    for trigger in trigger_manager.triggers:
        # Loop through all effects in a trigger
        for effect in trigger.effects:
            # Check if the sound_name attribute is equal to "OldName" and replace it with "NewName" 
            if effect.sound_name == "OldName":
                effect.sound_name = "NewName"

    scenario.write_to_file(file_output_path_here)

Importing all triggers from another scenario
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get all triggers from one scenario and import them into another scenario.

.. code:: py

    from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

    # Define Scenario files
    source_scenario = AoE2DEScenario.from_file(path_to_the_source_file)
    target_scenario = AoE2DEScenario.from_file(path_to_the_target_file)

    # Define Trigger Managers
    source_trigger_manager = source_scenario.trigger_manager
    target_trigger_manager = target_scenario.trigger_manager

    # Import the triggers
    # In this case all triggers from the source scenario are copied
    # You can optionally set the index to which the imported triggers are set at
    # Leaving this out will add the imported triggers to the end of the target scenario
    # In the example below, the source triggers will be added BEFORE the target triggers due to the 0
    target_trigger_manager.import_triggers(source_trigger_manager.triggers, 0)

    target_scenario.write_to_file(path_to_output_file)
