NOTIFY_UNKNOWN_BYTES = True
"""Show a notification of extra bytes being available at the end of the file, so you can notify the maintainer."""

# Reading / Writing settings
PRINT_STATUS_UPDATES = True
"""If status updates of what is being read and written should be printed to console or not."""
DISABLE_ERROR_ON_OVERWRITING_SOURCE = False
"""Disable the error being raised when overwriting source scenario."""

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

# Scenario construction
IGNORE_WRITING_ERRORS = False
"""Ignore possible errors raised while writing, useful for doing scenario debugging"""
