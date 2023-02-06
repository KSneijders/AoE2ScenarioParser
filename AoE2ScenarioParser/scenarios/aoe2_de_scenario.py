# @formatter:off
__READ_THE_STATEMENT_BELOW__ = '\n'.join([
    "",
    "",
    "###################################",
    "# PLEASE READ THE STATEMENT BELOW #",
    "###################################",
    "",
    "You're code is likely not updated for AoE2ScenarioParser v1.0.0!",
    "",
    "AoE2ScenarioParser has updated to the first major version, version 1.0.0!",
    "This update brings a lot of changes which should help the development experience by A LOT.",
    "To read about the many great changes made to the parser in the v1.0.0 release, please see the changelog:",
    ">>> https://github.com/KSneijders/AoE2ScenarioParser/blob/master/CHANGELOG.md",  # TODO: <-- VERIFY URL BEFORE RELEASE
    "",
    "Here are a couple examples of the updated/new features of the v1.0.0 release:",
    "- Speed improvements due to a completely new library: BinaryFileParser (Credits: Alian713)",   # TODO: VERIFY BEFORE RELEASE!!
    "- Removed A LOT of clutter from the library",                                                  # TODO: VERIFY BEFORE RELEASE!!
    "- Better distinct Effect and Condition classes for ease of use",                               # TODO: VERIFY BEFORE RELEASE!!
    "- More consistent naming schemes across the library",                                          # TODO: VERIFY BEFORE RELEASE!!
    "- Many improvements to the Area & Tile objects and their functionality",                       # TODO: VERIFY BEFORE RELEASE!!
    "",
    "To use this version, changes will have to be made to your code.",
    "Depending on the scale of your project, this might take up some time. But, rest assured, it is worth it!",
    "A document that lists the changes that you (might) need to make, can be found here:",
    ">>> https://ksneijders.github.io/.../UPDATE_GUIDE_URL/",  # TODO: <-- ADD URL TO UPDATE GUIDE
    "",
    "For questions regarding the linked document above, or questions about anything upgrade related,",
    "Please refer to the discord server:",
    ">>> https://discord.gg/DRUtmugXT3",
    "",
    "In case you do NOT want to use v1.0.0+ you can downgrade your version using:",
    ">>> `pip install 'AoE2ScenarioParser==<VERSION>' --force-reinstall`",  # TODO: <-- ADD LAST VERSION BEFORE v1.0.0
    "",
    "Please note:",
    "If you decide to downgrade, newer versions of AoE2:DE will not be supported by older versions of the parser.",
    "",
])
# @formatter:on

PLEASE = Exception
raise PLEASE(__READ_THE_STATEMENT_BELOW__)
