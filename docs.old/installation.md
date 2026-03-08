# Installation

You can install the project using **pip**:

    pip install AoE2ScenarioParser 

Or install it manually by cloning the **git** repo.

!!! note
    This method requires you to install the dependencies and all updates manually too.

```
git clone https://github.com/KSneijders/AoE2ScenarioParser.git
```

## Dependencies

This project is made in Python 3. You'll need **Python 3.8** or newer to be able to run it properly.

To see the project dependencies, please check the [requirements.txt] file in the project.

[requirements.txt]: https://github.com/KSneijders/AoE2ScenarioParser/blob/master/requirements.txt

!!! note
    All these dependencies should install automatically when using the above **pip** command.

## Updating

To update the library using pip when you have an older version, use the following command:

    pip install --no-cache-dir --upgrade AoE2ScenarioParser

To view the changes between versions, visit the GitHub page and check the [changelog.md] file.

[changelog.md]: https://github.com/KSneijders/AoE2ScenarioParser/blob/master/changelog.md

### Rollback or update to specific versions

To change your installation to a specific version (i.e. when you have issues with the current build), use the following command:

    pip install "AoE2ScenarioParser==<VERSION>" --force-reinstall

Where `<VERSION>` is the version you want (e.g. `0.1.47`)
