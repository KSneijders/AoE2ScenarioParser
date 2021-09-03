# Hello World Example

## Intro

With the information from the getting started page, we can make a "**Hello World**" example. We'll read a scenario, add
a trigger, some units and edit some terrain and write it back to a new scenario.

This "hello world" example assumes you've installed an editor.  
A great editor (IDE) is PyCharm ([Download Community Edition]))

## Step by step

1. Create an empty scenario in the editor and save it as "hello world"
2. Create a new project and file in PyCharm. Name the file `hello_world.py`
3. Copy the code below into `hello_world.py`

    ```py
    from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

    # The path to your scenario folder
    input_folder = "C:/path/to/your/scenario/folder/"

    # The scenario object. 
    scenario = AoE2DEScenario.from_file(input_folder + "hello world.aoe2scenario")
    ```

4. Go to the "Load Scenario" menu in-game (Single Player :arrow_right: Editors)
5. Copy the path that is opened when clicking the "Open Scenario Folder" button (Bottom right)
6. Paste the folder path in the input_folder string

    !!! note "Folder separators"
        If you use `\` to separate folders, use 2 per folder (`c:\\folder\\folder\\`)  
        If you use `/` to separate folders, 1 is enough (`c:/folder/folder/`) 

7. Remember to add a `/` or `\\` at the end of the string too
8. Run the python code by pressing ++ctrl+shift+f10++

    !!! note "Executing python code in PyCharm"
        ++ctrl+shift+f10++ executes the current file in PyCharm. [More info here](https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html#run).
    
    You should get a console output that looks like this:

    ```md
    Reading file: 'YOUR FILE PATH' 
    Reading scenario file finished successfully.
    ############### Attributes ###############
    >>> Game version: 'DE'
    >>> Scenario version: 1.43
    ##########################################
    Loading scenario structure finished successfully.
    Parsing scenario file...
        ✔ FileHeader
        ✔ DataHeader
    ...
    ```

9. Now let's add a trigger with a `Display Instructions` effect that reads "Hello World"
10. Add the following code to `hello_world.py`

    ```py
    # Save reference to the manager, so you don't have to do "scenario.trigger_manager..." each time
    trigger_manager = scenario.trigger_manager

    # Save the created trigger
    hello_world_trigger = trigger_manager.add_trigger("Hello World Trigger")
    # Add display_instructions effect to the new trigger
    hello_world_trigger.new_effect.display_instructions(
        display_time=11,
        message="Hello World"
    )
    ```

11. Now let's check it out in game. Add the following code:

    ```py
    scenario.write_to_file(input_folder + "hello world output.aoe2scenario")
    ```

12. Run the python code by pressing ++shift+f10++ (rerun the last file)
13. You should see something like this at the end of your console:

    ```
    ...
        ✔ Triggers
        ✔ Files
    File writing finished successfully.
    File successfully written to: 'YOUR OUTPUT FILE PATH'
    Process finished with exit code 0
    ```

14. Check out the "hello world output" scenario in-game and test it!
15. Now remove the `scenario.write_to_file(...)` line, we'll add it back later
16. Let's add the `unit_manager` to the script where we added the trigger manager:

    ```py
    unit_manager = scenario.unit_manager
    ```

17. Now let's add the code to add some units to the end of the script:

    ```py
    unit_manager.add_unit(player=PlayerId.ONE, unit_const=UnitInfo.MILITIA.ID,              x=15, y=12)
    unit_manager.add_unit(player=PlayerId.ONE, unit_const=UnitInfo.MAN_AT_ARMS.ID,          x=15, y=13)
    unit_manager.add_unit(player=PlayerId.ONE, unit_const=UnitInfo.LONG_SWORDSMAN.ID,       x=15, y=14)
    unit_manager.add_unit(player=PlayerId.ONE, unit_const=UnitInfo.TWO_HANDED_SWORDSMAN.ID, x=15, y=15)
    unit_manager.add_unit(player=PlayerId.ONE, unit_const=UnitInfo.CHAMPION.ID,             x=15, y=16)
    ```

    Take a look at the code, maybe you can see what it does?

18. We add one unit per unit from the militia line to the editor, one per tile.

    !!! note
        These units are placed using whole numbers (called: integers, `x=15, y=12`), if you want units to spawn in the middle of a tile, use
        `.5` after the integer, like so: `x=15.5, y=12.5`

19. You can also see the above code uses `PlayerId` and `UnitInfo` objects.

    ```
    PlayerId.ONE         # The number representing player one (1)
    UnitInfo.MILITIA.ID  # The number representing a militia unit (74)
    ```

    !!! note "Datasets"
        These are datasets, [read more about datasets here](https://ksneijders.github.io/AoE2ScenarioParser/cheatsheets/datasets/).

20. Let's import those objects using the code below. Add these lines to the top of your file.

    ```py
    from AoE2ScenarioParser.datasets.players import PlayerId
    from AoE2ScenarioParser.datasets.units import UnitInfo
    ```

21. And now as final change let's add a hill and change the size of the map  
    Add the `map_manager`:

    ```py
    map_manager = scenario.map_manager
    ```
    Place it with the `unit_manager` and the `trigger_manager`

22. Now let's add the code for the hill:

    ```py
    map_manager.create_hill(x1=10, y1=10, x2=20, y2=20, elevation=3)
    ```

    The in-game max elevation is 7, that's equivelant to `elevation=6` in the parser.
    This is because `elevation=0` is elevation 1 in the editor.
    Using the parser you can go as large as you want, although above ~20 
    without UHD and ~15 with UHD the camera starts clipping into the hill. 

23. And finally let's shrink the map size to `40x40` tiles

    ```py
    map_manager.map_size = 40
    ```

    !!! warning "Max map size limit"
        The limit of a scenario is set to the size of a ludikrous map (`480x480`).
        Going over this limit will cause the game to crash.

24. Now let's add the writing to file back:

    ```py
    scenario.write_to_file(input_folder + "hello world output.aoe2scenario")
    ```

25. Run the python code by pressing ++shift+f10++ again and check out the scenario!


## Complete code block

Your code should look something like the below block. You can find more examples & explanation on the
[cheatsheets](https://ksneijders.github.io/AoE2ScenarioParser/cheatsheets/triggers/) and the
[examples](https://ksneijders.github.io/AoE2ScenarioParser/examples/triggers/) page.

```py
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

# The path to your scenario folder
input_folder = "C:\\Users\\Kerwin Sneijders\\Games\\Age of Empires 2 DE\\76561198140740017\\resources\\_common\\scenario\\"

# The scenario object.
scenario = AoE2DEScenario.from_file(input_folder + "hello world.aoe2scenario")

# Save reference to the manager, so you don't have to do "scenario.trigger_manager..." each time
trigger_manager = scenario.trigger_manager
unit_manager = scenario.unit_manager
map_manager = scenario.map_manager

# Save the created trigger
hello_world_trigger = trigger_manager.add_trigger("Hello World Trigger")
# Add display_instructions effect to the new trigger
hello_world_trigger.new_effect.display_instructions(
    display_time=11,
    message="Hello World"
)

unit_manager.add_unit(player=PlayerId.ONE, unit_const=UnitInfo.MILITIA.ID,              x=15, y=12)
unit_manager.add_unit(player=PlayerId.ONE, unit_const=UnitInfo.MAN_AT_ARMS.ID,          x=15, y=13)
unit_manager.add_unit(player=PlayerId.ONE, unit_const=UnitInfo.LONG_SWORDSMAN.ID,       x=15, y=14)
unit_manager.add_unit(player=PlayerId.ONE, unit_const=UnitInfo.TWO_HANDED_SWORDSMAN.ID, x=15, y=15)
unit_manager.add_unit(player=PlayerId.ONE, unit_const=UnitInfo.CHAMPION.ID,             x=15, y=16)

map_manager.create_hill(x1=10, y1=10, x2=20, y2=20, elevation=3)
map_manager.map_size = 40

scenario.write_to_file(input_folder + "hello world output.aoe2scenario")

```

[Download Community Edition]: https://www.jetbrains.com/pycharm/download/#section=windows