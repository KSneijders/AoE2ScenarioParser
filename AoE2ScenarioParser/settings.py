"""

Warning: IMPORT THE MODULE, NOT THE VALUES!
    To change these settings, import the module: `from AoE2ScenarioParser import settings`.
    Then you can change the settings like: `settings.RAISE_ERROR_ON_WARNING = True`

If you import the values directly like: `from ... import RAISE_ERROR_ON_WARNING`
_(not written out because it wouldn't work)_, change the value would overwrite the reference and not the value which
means the change wouldn't transfer to the `settings` module.

"""

NOTIFY_UNKNOWN_BYTES = True
"""Show a notification of extra bytes being available at the end of the file, so you can notify the maintainer"""

# Reading / Writing settings
PRINT_STATUS_UPDATES = True
"""If status updates of what is being read and written should be printed to console"""
ALLOW_OVERWRITING_SOURCE = False
"""Disable the error being raised when overwriting source scenario"""
ALLOW_DIRTY_RETRIEVER_OVERWRITE = False
"""If it is allowed to overwrite a retriever that is dirty (it has been changed manually)"""
SHOW_VARIANT_WARNINGS = True
"""If warnings about incorrect variants should be shown or not"""

# Charset settings
MAIN_CHARSET = "utf-8"
"""The charset used to decode the text in the scenario. If it fails, will try the settings.FALLBACK_CHARSET"""
FALLBACK_CHARSET = "latin-1"
"""The charset used to decode the text in the scenario when the settings.MAIN_CHARSET fails"""

ENABLE_XS_CHECK_INTEGRATION = True
"""If the xs-check integration should be active. If set to False, xs-check will not be used anywhere"""
