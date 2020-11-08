# AoE2ScenarioParser
This is a project for editing parts of an `aoe2scenario` file from **Age of Empires 2 
Definitive Edition** outside of the in-game editor.  

Documentation can be found on the [readthedocs] page (**Work in Progress**).  
Examples can be found in the cheatsheets.

- [Triggers Cheatsheet]
- [Units Cheatsheet]
- [Datasets Cheatsheet]


[readthedocs]: https://aoe2scenarioparser.readthedocs.io/en/master/
[Triggers Cheatsheet]: ./cheatsheets/TRIGGERS.md
[Units Cheatsheet]: ./cheatsheets/UNITS.md
[Datasets Cheatsheet]: ./cheatsheets/DATASETS.md

# Progress
Current up-to-date progress can be found on the [changelog.md] page. (Dev branch for non-released progress).

[changelog.md]: ./changelog.md

## Features:

|            | View               | Add                | Edit               | Remove             |
| ---------- | ------------------ | ------------------ | ------------------ | ------------------ |
| Triggers   | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Conditions | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Effects    | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Units      | -                  | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |

## Bugs:

- copy trigger functions take a long time to copy

If you find a bug, please check if it's already been reported or maybe even fixed ([changelog.md]). Please report any bugs you find to the [github issue board].

[github issue board]: https://github.com/KSneijders/AoE2ScenarioParser/issues

## Support:

| ScenarioFiles | Read               | Write              | Reference                                                                 |
| ------------- | ------------------ | ------------------ | ------------- |
| 1.36          | :heavy_check_mark: | :heavy_check_mark: | -                                                                         |
| 1.37          | :heavy_check_mark: | :heavy_check_mark: | Version since game update: [35584] (February 27th) <br> **Unchanged in**: <br> - Update [36202] (March 30th) <br> - Update [36906] (April 29th) <br> - Update [37650] (May 27th) <br> - Hotfix [37906] (June 2nd) <br> - Update [39284] (July 20th) <br> - Hotfix [39515] (July 27th) <br> - Update [40220] (August 24th) <br> - Update [40874] (September 22nd) <br> - Update [41855] (October 20th) 



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

# Authors
-  Kerwin Sneijders (Main Author)

# License 
GNU General Public License v3.0: Please see the [LICENSE file].

[LICENSE file]: https://github.com/KSneijders/AoE2ScenarioParser/blob/dev/LICENSE
