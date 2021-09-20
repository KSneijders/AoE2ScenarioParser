NOTIFY_UNKNOWN_BYTES = True
"""Show a notification of extra bytes being available at the end of the file, so you can notify the maintainer."""

PRINT_STATUS_UPDATES = True
"""If status updates of what is being read and written should be printed to console or not."""

# Warning related settings
DISABLE_WARNINGS = False
"""Disable all warnings thrown by the printers.warn function."""
DISABLE_VERSION_WARNINGS = False
"""Disable warnings about python versions"""
RAISE_ERROR_ON_WARNING = False
"""Raise an error when a warning should be shown. Handy for debugging, shows you the stacktrace."""

# Charset settings
MAIN_CHARSET = "utf-8"
"""The charset used to decode the test in the scenario. If it fails, will try the settings.FALLBACK_CHARSET"""
FALLBACK_CHARSET = "latin-1"
"""The charset used to decode the text in the scenario when the settings.MAIN_CHARSET fails."""

# Ignore UUID
IGNORE_UUID = False
"""
Used to disable saving the host scenario UUID value when creating any object. Recommended to not change this value
If you don't understand what it is used for. Setting mainly used for running tests on objects without scenario host.
"""
