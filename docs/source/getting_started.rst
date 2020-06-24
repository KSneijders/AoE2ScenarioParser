Getting started
===============

Once you have installed the library the fun can begin! 
To get started import the library in your python project like so::

    from AoE2ScenarioParser.aoe2_scenario import AoE2Scenario

| Define the file you will be reading from and where you will be writing your new file to. 
| Please note: *It is recommended to not overwrite the file you will be reading for backup reasons.* 

::

    input_path = "File/Path/To/Your/Input/File.aoe2scenario"
    output_path = "File/Path/To/Your/Output/File.aoe2scenario"

Now create the ``Scenario`` object with the filename as parameter.::

    scenario = AoE2Scenario(input_path)

You can now edit to your heart's content. Every aspect of the scenario is seperated in managers. 
Not all parts are currently supported. The following list shows the current support and use of 
all available managers:

- **trigger_manager**: The trigger manager is used for creating, editing and removing Triggers, Conditions, Effects and Variables.
- **unit_manager**: The unit manager is used for creating, editing and removing Units. This includes buildings and heroes etc.

You can access all managers like so::

    trigger_manager = scenario.object_manager.trigger_manager