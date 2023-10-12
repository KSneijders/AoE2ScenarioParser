class AoE2ScenarioParserWarning(Warning):
    """
    The super class of all warnings in the AoE2ScenarioParser.
    Can be used to act on all AoE2ScenarioParser Warnings at the same time
    """


class PythonVersionWarning(AoE2ScenarioParserWarning):
    """Shown when the user's python version might be incompatible with the libraries version in the (near) future"""
    pass


class ByteDecodeWarning(AoE2ScenarioParserWarning):
    """Shown when a non-fatal decoding issue occurs"""
    pass


class UpdateDirtyWarning(AoE2ScenarioParserWarning):
    """Shown when a manually edited object (aka dirty) is being updated/overwritten by a library process"""
    pass


class UuidForcedUnlinkWarning(AoE2ScenarioParserWarning):
    """Shown when a UUID object is updated in a way that forces the object to not be synced anymore"""
    pass


class XsScriptNameUsageWarning(AoE2ScenarioParserWarning):
    """Shown when someone uses the script_name value """
    pass


class IncorrectArmorAttackUsageWarning(AoE2ScenarioParserWarning):
    """
    Shown when a user uses calls that modify an effect's quantity/armor/attack class values.
    This can be intentional if you know what you're doing, so it deserves its own class so it can be disabled.
    """
    pass


class IncorrectVariantWarning(AoE2ScenarioParserWarning):
    """Shown when a user writes a file with a variant that is not AoE2 or RoR"""
    pass
