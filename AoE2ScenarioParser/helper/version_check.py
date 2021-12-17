import sys

from AoE2ScenarioParser import settings
from AoE2ScenarioParser.helper.printers import warn


_block_below_minor = 8
_notify_below_minor = 8
_py_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


def python_version_check():
    """
    Raises an error if user's python version is below the configured minimum allowed python version.
    Raises a warning if user's python version is below the configured minimum notify version. Used to notify users when
        the parser's minimum python version requirement will be increased.
    """
    if sys.version_info[0] < 3:
        raise Exception("AoE2ScenarioParser requires the use of Python 3")

    if sys.version_info[1] < _block_below_minor:
        raise Exception(f"\n\nAoE2ScenarioParser requires the use of Python 3.{_block_below_minor}.\n"
                        f"You are currently using version {_py_version}. You can download a newer version from: \n"
                        f"\thttps://www.python.org/downloads/\n")
    elif sys.version_info[1] < _notify_below_minor:
        if not settings.DISABLE_VERSION_WARNINGS:
            warn(f"AoE2ScenarioParser will update it's minimum python requirements to Python 3.{_notify_below_minor} soon.\n"
                 f"You are currently using version {_py_version}. You can download a newer version from: \n"
                 f"\thttps://www.python.org/downloads/\n\n"
                 f"You can disable these warnings using:\n" 
                 "    from AoE2ScenarioParser import settings\n" 
                 "    settings.DISABLE_VERSION_WARNINGS = True")
