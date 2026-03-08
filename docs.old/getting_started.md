# Getting started

Once you have installed the library the fun can begin! 
To get started import the library in your python project like so:

```py
from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
```

Define the file you will be reading from and where you will be writing your new file to.  

!!! Note "Where to find your scenario files"
    The scenarios can usually be found here:  
    `C:\Users\<USERNAME>\Games\Age of Empires 2 DE\<STEAMID>\resources\_common\scenario`  
    The `STEAMID` folder is your steam ID and looks something like: `12345678901234567`

```py
input_path = "File/Path/To/Your/Input/kFile.aoe2scenario"
output_path = "File/Path/To/Your/Output/File.aoe2scenario"
```

!!! warning "Do not overwrite your source scenario"
    It is recommended to not overwrite the file you will be reading for backup reasons.

Now create the `Scenario` object with the filename as parameter.

```py
scenario = AoE2DEScenario.from_file(input_path)
```

## Managers

You can now edit to your heart's content. Every aspect of the scenario is seperated in managers. 
Not all parts are currently supported. The following list shows the current support and use of 
all available managers:

| Manager         | Description                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------|
| trigger_manager | The trigger manager is used for creating, editing and removing Triggers, Conditions, Effects and Variables. |
| unit_manager    | The unit manager is used for creating, editing and removing Units. This includes buildings and heroes etc.  |
| map_manager     | The map manager is used for changing terrain, elevation or simply getting coordinates for certain types.    |
| player_manager  | The player manager is used to edit player attributes such as civs, starting age, diplomacy, disables etc.   |
| xs_manager      | The XS manager is used to store XS in a script_call effect to make it easily transferable in Multiplayer    |
| message_manager | The Message manager is used to edit the fields in the Messages tab in the in-game editor.                   |

You can access all managers like so:

```py
scenario = AoE2DEScenario.from_file(input_path)

trigger_manager = scenario.trigger_manager
unit_manager = scenario.unit_manager
# etc...
```

After you're done editing, you can save your work and write it to an `aoe2scenario` file:

```py
scenario.write_to_file(output_path)
```
