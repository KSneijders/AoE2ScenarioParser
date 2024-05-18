# AoE2ScenarioParser

This is a project for editing parts of an `aoe2scenario` file from **Age of Empires 2 Definitive Edition** outside
the in-game editor.

# Getting started

[GitHub Pages]: https://ksneijders.github.io/AoE2ScenarioParser/
## Quick links

- [Installing AoE2ScenarioParser](https://ksneijders.github.io/AoE2ScenarioParser/installation/)
- [Getting Started](https://ksneijders.github.io/AoE2ScenarioParser/getting_started/)
- [Hello World Example](https://ksneijders.github.io/AoE2ScenarioParser/hello_world/)
- [Discord Server](https://discord.gg/DRUtmugXT3)
- [API Docs](https://ksneijders.github.io/AoE2ScenarioParser/api_docs/aoe2_scenario/)

## Documentation

Documentation can be found on **[GitHub Pages]**.

# Discord

If you have any questions regarding the parser, [join the discord]!

[join the discord]: https://discord.gg/DRUtmugXT3
# Progress

Current up-to-date progress can be found on the [changelog.md] page. (Check the `dev` branch for non-released progress).

[changelog.md]: https://github.com/KSneijders/AoE2ScenarioParser/blob/dev/CHANGELOG.md
## Features:


|            | View              | Add | Edit | Remove |
|------------|-------------------|-----|------|--------|
| Triggers   | ✔️                | ✔️  | ✔️   | ✔️     |
| Conditions | ✔️                | ✔️  | ✔️   | ✔️     |
| Effects    | ✔️                | ✔️  | ✔️   | ✔️     |
| Units      | n/a *<sup>1</sup> | ✔️  | ✔️   | ✔️     |
| Map        | n/a *<sup>1</sup> | ✔️  | ✔️   | ✔️     |
| Players    | n/a *<sup>1</sup> | ✔️* | ✔️   | ✔️*    |
| Messages   | n/a               | ✔️  | ✔️   | ✔️     |

*: You can disable or enable players like in the in-game editor (min 1, max 8).  
*<sup>1</sup>: There's no overall formatting function to display these. Though, they can still be printed.

&nbsp;

## Support:


| Scenario file version | Read | Write | Reference                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-----------------------|------|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.36                  | ✔️   | ✔️    | Version since the**release of the Definitive Edition**                                                                                                                                                                                                                                                                                                                                                                                                            |
| 1.37                  | ✔️   | ✔️    | Version since game update: [35584] (February 27th, 2020) <br> **Unchanged in**: <br> - Update [36202] (March 30th, 2020) <br> - Update [36906] (April 29th, 2020) <br> - Update [37650] (May 27th, 2020) <br> - Hotfix [37906] (June 2nd, 2020) <br> - Update [39284] (July 20th, 2020) <br> - Hotfix [39515] (July 27th, 2020) <br> - Update [40220] (August 24th, 2020) <br> - Update [40874] (September 22nd, 2020) <br> - Update [41855] (October 20th, 2020) |
| 1.40                  | ✔️   | ✔️    | Version since game update: [42848] (November 17th, 2020) <br> **Unchanged in**: <br> - Hotfix [43210] (November 24th, 2020)                                                                                                                                                                                                                                                                                                                                       |
| 1.41                  | ✔️   | ✔️    | Version since game update: [44725] (January 25th, 2021) <br> **Unchanged in**: <br> - Hotfix [44834] (January 28th, 2021)<br> - Hotfix [45185] (February 11th, 2021)<br> - Update [46265] (March 24th, 2021)<br> - Update [47820] (May 3rd, 2021)                                                                                                                                                                                                                 |
| 1.42                  | ✔️   | ✔️    | Version since game update: [50292] (July 6th, 2021) <br> **Unchanged in**: <br> - Hotfix [50700] (July 13th, 2021)                                                                                                                                                                                                                                                                                                                                                |
| 1.43                  | ✔️   | ✔️    | Version since game update: [51737] (August 10th, 2021)                                                                                                                                                                                                                                                                                                                                                                                                            |
| 1.44                  | ✔️   | ✔️    | Version since game update: [54480] (October 5th, 2021) <br> **Unchanged in**: <br> - Hotfix [54684] (October 6th, 2021)                                                                                                                                                                                                                                                                                                                                           |
| 1.45                  | ✔️   | ✔️    | Version since game update: [56005] (November 17th, 2021) <br> **Unchanged in**: <br> - Update [58259] (January 31st, 2022)                                                                                                                                                                                                                                                                                                                                        |
| 1.46                  | ✔️   | ✔️    | Version since game update: [61321] (April 27th, 2022) <br> **Unchanged in**: <br> - Update [63482] (June 28th, 2021) <br> - Hotfix [63581] (July 6th, 2021)                                                                                                                                                                                                                                                                                                       |
| 1.47                  | ✔️   | ✔️    | Version since game update: [66692] (August 29th, 2022) <br> **Unchanged in**: <br> - Update [73855] (December 7th, 2022) <br> - Update 75350 (Console update) (January 31st, 2023) <br> - Update [78174] (March 8th, 2023) <br> - Hotfix [78757] (March 8th, 2023)                                                                                                                                                                                                |
| 1.48                  | ✔️   | ✔️    | Version since game update: [81058] (April 11th, 2023) <br> **Unchanged in**: <br> - Hotfix [82587] (April 28th, 2023)                                                                                                                                                                                                                                                                                                                                             |
| 1.49                  | ✔️   | ✔️    | Version since game update: [83607] (May 16th, 2023) <br> **Unchanged in**: <br> - Hotfix [85208] (June 1st, 2023) <br> - Hotfix [85614] (June 6th, 2023) <br> - Update [87863] (June 27th, 2023) <br> - Update [90260] (July 26th, 2023) <br> - Update [93001] (September 6th, 2023)                                                                                                                                                                              |
| 1.51                  | ✔️   | ✔️    | Version since game update: [95810] (October 31th, 2023) <br> **Unchanged in**: <br> - Update [99311] (December 11th, 2023) <br> - Update [104954] (February 23th, 2024)                                                                                                                                                                                                                                                                                           |
| 1.53                  | ✔️   | ✔️    | Version since game update: [107882] (March 13th, 2024) <br> **Unchanged in**: <br> - Update [108769] (March 26th, 2024)                                                                                                                                                                                                                                                                                                                                           |

[35584]: https://www.ageofempires.com/news/aoe2de-update-35584/
[36202]: https://www.ageofempires.com/news/aoe2de-update-36202/
[36906]: https://www.ageofempires.com/news/aoe2de-update-36906/
[37650]: https://www.ageofempires.com/news/aoe2de-update-37650/
[37906]: https://www.ageofempires.com/news/aoe2de-hotfix-37906/
[39284]: https://www.ageofempires.com/news/aoe2de-update-39284/
[39515]: https://www.ageofempires.com/news/aoe2de-hotfix-39515/
[40220]: https://www.ageofempires.com/news/aoe2de-update-40220/
[40874]: https://www.ageofempires.com/news/aoe2de-update-40874/
[41855]: https://www.ageofempires.com/news/aoe2de-update-41855/
[42848]: https://www.ageofempires.com/news/aoe2de-update-42848/
[43210]: https://www.ageofempires.com/news/aoe2de-hotfix-43210/
[44725]: https://www.ageofempires.com/news/aoeiide-update-44725/
[44834]: https://www.ageofempires.com/news/aoeiide-update-44725/#hotfix-44834
[45185]: https://www.ageofempires.com/news/aoe2de-hotfix-45185/
[46265]: https://www.ageofempires.com/news/aoe2de-update-46295/
[47820]: https://www.ageofempires.com/news/aoe2de-update-47820/
[50292]: https://www.ageofempires.com/news/aoe2de-update-50292/
[50700]: https://www.ageofempires.com/news/aoe2de-update-50292/#hotfix-50700
[51737]: https://www.ageofempires.com/news/aoeiide-update-51737/
[54480]: https://www.ageofempires.com/news/aoeii-de-update-54480/
[54684]: https://www.ageofempires.com/news/aoeii-de-update-54480/#hotfix-54684
[56005]: https://www.ageofempires.com/news/aoeii_de_update_56005/
[58259]: https://www.ageofempires.com/news/aoe-ii-de-update-58259/
[61321]: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-61321/
[63482]: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-63482/
[63581]: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-63482#Hotfix-63581
[66692]: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-66692/
[73855]: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-73855/
[78174]: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-78174/
[78757]: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-78174#641ecbac39a80
[81058]: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-81058/
[82587]: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-hotfix-82587/
[83607]: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-83607/
[85208]: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-hotfix-85208/
[85614]: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-hotfix-85614/
[87863]: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-87863/
[90260]: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-90260/
[93001]: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-93001/
[95810]: https://www.ageofempires.com/news/preview-age-of-empires-ii-definitive-edition-update-95810/
[99311]: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-99311/
[104954]: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-104954/
[107882]: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-107882/
[108769]: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-108769/


# Authors

- Kerwin Sneijders (Main Author)
- [Alian713](https://github.com/Divy1211) (Dataset Wizard)

# License

MIT License: Please see the [LICENSE file].

[license file]: https://github.com/KSneijders/AoE2ScenarioParser/blob/dev/LICENSE
