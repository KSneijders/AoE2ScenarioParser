import sys

from AoE2ScenarioParser import settings
from AoE2ScenarioParser.helper.exceptions import WarningToError
from AoE2ScenarioParser.helper.string_manipulations import add_tabs

_color = {
    'end': '\033[0m',
    'black': '\033[30m',
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bright_black": "\033[90m",
    "bright_red": "\033[91m",
    "bright_green": "\033[92m",
    "bright_yellow": "\033[93m",
    "bright_blue": "\033[94m",
    "bright_magenta": "\033[95m",
    "bright_cyan": "\033[96m",
    "bright_white": "\033[97m",
}


def rprint(string: str = "", replace: bool = True, final: bool = False) -> None:
    """
    Replaceable print, print lines which can be overwritten by the next

    Args:
        string: The string to print -> print(str)
        replace: If this line should be replaced by the next if the next also has replace=True
        final: If true, the next print is not able to replace this line. Used when this line replaces
            another line but should not be replaced by the next replace=True.

    Returns:
        None
    """
    if replace:
        sys.stdout.write('\r' + string)
        if final:
            print()
    else:
        print(string)


def s_print(string="", replace=True, final=False, color=None) -> None:
    """
    Status print, read rprint docstring for more info.
    Simple rprint wrapper with a check for the PRINT_STATUS_UPDATES setting.
    """
    if settings.PRINT_STATUS_UPDATES:
        if color is not None:
            string = color_string(string, color)
        rprint(string, replace, final)


def color_string(string: str, color: str) -> str:
    return _color[color] + string + _color['end']


def warn(string="") -> None:
    if settings.RAISE_ERROR_ON_WARNING:
        raise WarningToError(
            f"\n\nWarning Occurred with 'settings.THROW_ERROR_ON_WARNING' is True. \nWarning:\n{add_tabs(string, 1)}\n")
    if not settings.DISABLE_WARNINGS:
        print('\n' + color_string(string, 'bright_yellow'))
