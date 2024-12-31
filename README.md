# AoE2ScenarioParser

`AoE2ScenarioParser` is a [Python] library that allows you to edit `aoe2scenario` files from **every** version of 
 **Age of Empires 2 Definitive Edition**.

[Python]: https://www.python.org/

# Getting Started

Installing using `pip`:

```sh
pip install AoE2ScenarioParser
```

More documentation about installing etc. can be found below.

## Documentation

Documentation for installation, usage, examples, cheatsheets and API docs can be found on **[GitHub Pages]**.

[GitHub Pages]: https://ksneijders.github.io/AoE2ScenarioParser/

## Quick links

- **[Installing]** → A quick guide on how to install `AoE2ScenarioParser`
- **[Hello World Example]** → Step-by-step guide to get you going
- **[Discord Server]** → For questions about `AoE2ScenarioParser`, [Python] or scenarios in general. 
- **[API Docs]** → Technical documentation for all exposed functions & classes

[Installing]: https://ksneijders.github.io/AoE2ScenarioParser/installation/
[Hello World Example]: https://ksneijders.github.io/AoE2ScenarioParser/hello_world/
[Discord Server]: https://discord.gg/DRUtmugXT3
[API Docs]: https://ksneijders.github.io/AoE2ScenarioParser/api_docs/aoe2_scenario/

# Discord

If you have any questions regarding `AoE2ScenarioParser`? [Join the discord]!

[Join the discord]: https://discord.gg/DRUtmugXT3

# Support

**Every Single Scenario Version from Age of Empires 2 Definitive Edition is SUPPORTED!** 

> Support: `1.36` _Version at Release (November 14th, 2019)_ → `1.54` _Current Version (Since: October 14, 2024)_

Every single version of **Age of Empires 2 Definitive Edition** is supported! 
If a new version of **Age of Empires 2 Definitive Edition** just released it can take a bit for it to be able to be read. 
Check the [Discord Server] for more up-to-date information if this is the case.

If you find a scenario which can be opened by the game itself, but results in an error when using `AoE2ScenarioParser`, 
please report it as an issue or in the **#bug‑reports** channel in the [Discord Server].

> ⚠️ To view the full-blown support table previously shown in this README, visit: [support]. 

[support]: https://github.com/KSneijders/AoE2ScenarioParser/blob/master/resources/md/support.md

# Progress

Every related change to the library is documented and can be found in the [CHANGELOG].

[changelog]: https://github.com/KSneijders/AoE2ScenarioParser/blob/dev/CHANGELOG.md

## Features:

`AoE2ScenarioParser` allows you to edit **anything** inside a scenario. 
For general usability "managers" have been created to make working with the files easier. 
These managers allow you to quickly change aspects of units, triggers, the map, player data and more!

Below is a simplified overview of some of the features:

|            | Inspect           | Add | Edit | Remove |
|------------|-------------------|-----|------|--------|
| Triggers   | ✔️                | ✔️  | ✔️   | ✔️     |
| Conditions | ✔️                | ✔️  | ✔️   | ✔️     |
| Effects    | ✔️                | ✔️  | ✔️   | ✔️     |
| Units      | ✔️                | ✔️  | ✔️   | ✔️     |
| Map        | n/a *<sup>1</sup> | ✔️  | ✔️   | ✔️     |
| Players    | n/a *<sup>1</sup> | ✔️* | ✔️   | ✔️*    |
| Messages   | n/a               | ✔️  | ✔️   | ✔️     |

*: You can disable or enable players like in the in-game editor (min 1, max 8).  
*<sup>1</sup>: There's no specific inspection function. Though, they can still be printed with clean formatting.

# Authors

- [Kerwin Sneijders](https://github.com/KSneijders) (Main Author)
- [Alian713](https://github.com/Divy1211) (Dataset Wizard)

# License

MIT License: Please see the [LICENSE file].

[license file]: https://github.com/KSneijders/AoE2ScenarioParser/blob/dev/LICENSE
