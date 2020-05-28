# AoE2ScenarioParser
This is a project for editing parts of an `aoe2scenario` file from **Age of Empires 2 
Definitive Edition** outside of the in-game editor. 


# Progress
Current up-to-date progress can be found on the [Trello] board. 

[Trello]: https://trello.com/b/7SNm3gXj/aoe2-de-parser

## Features:

|            | View               | Add                | Edit               | Remove             |
|------------|--------------------|--------------------|--------------------|--------------------|
| Triggers   | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Conditions | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | -                  |
| Effects    | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | -                  |
| Units      | -                  | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |

## Bugs:
- None that I know of. Please report any bugs you find to the [github issue board].

[github issue board]: https://github.com/KSneijders/AoE2ScenarioParser/issues

## Support:

| ScenarioFiles | Read               | Write              | Reference                       |
|---------------|--------------------|--------------------|---------------------------------|
| 1.36          | :heavy_check_mark: | :heavy_check_mark: | -
| 1.37          | :heavy_check_mark: | :heavy_check_mark: | Version since game update: [35584] (February 27th) <br> **Unchanged in**: <br> - Update [36202] (March 30th) <br> - Update [36906] (April 29th) <br> - Update [37650] (May 27th)

[35584]: https://www.ageofempires.com/news/aoe2de-update-35584/
[36202]: https://www.ageofempires.com/news/aoe2de-update-36202/
[36906]: https://www.ageofempires.com/news/aoe2de-update-36906/
[37650]: https://www.ageofempires.com/news/aoe2de-update-37650/

# Installation
Run the following pip command for installation:

    pip install AoE2ScenarioParser

## Dependencies:
This project is made in Python but does not support any versions below **Python 3.6**.

The project uses [bidict] for bidirectional  mapping.  
Note: *All these dependencies should install automatically when using the above command.*

[bidict]: https://pypi.org/project/bidict/

# Usage
## Getting Started
To start, import the main `AoE2Scenario` class from the module:

```py
from AoE2ScenarioParser.aoe2_scenario import AoE2Scenario
```

Define the file you will be reading and the path you will be writing to.  
Note: *Creating folders isn't supported at this time. Please use an existing folder.*  

```py
# It is recommended to not overwrite your file. This way you can keep a backup!
input_path = "File/Path/To/Your/Input/File"
output_path = "File/Path/To/Your/Output/File"
```

Now create the `Scenario` object with the filename as parameter. 
```py
scenario = AoE2Scenario(input_path)
```

## Editing a Scenario
You can edit your scenario in many ways. Not every part of the scenario can be edited with this project yet (without diving into the source code). Below you can find cheatsheets of the parts that are supported.

- [Triggers cheatsheet](cheatsheets/TRIGGERS.md)
- [Units cheatsheet](cheatsheets/UNITS.md)

As we all now, `AoE2` has a lot of data involved. From `Terrain types` and `Units` to `Effects` and `Conditions`. All this data is impossible to remember. For that reason there are a number of datasets to help you out. You can find the cheatsheet here:

- [Datasets cheatsheet](cheatsheets/DATASETS.md)

## Saving the Edited Scenario
When you are done, you can write all your progress to a file like so:

```py
scenario.write_to_file(output_path)
```
Please remember to use a different path (filename) than your input file. This way you have a backup file incase you encounter a bug.


---
&nbsp;  

# Authors
-  Kerwin Sneijders (Main Author)

# License
## Code
GNU General Public License v3.0: Please see the [LICENSE file].

[LICENSE file]: https://github.com/KSneijders/AoE2ScenarioParser/blob/dev/LICENSE
