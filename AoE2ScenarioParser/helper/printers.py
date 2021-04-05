import sys

from AoE2ScenarioParser import settings


def rprint(string="", replace=True, final=False) -> None:
    """
    Replaceable print, print lines which can be overwritten by the next

    Args:
        string (str): The string to print -> print(str)
        replace (bool): If this line should be replaced by the next if the next also has replace=True
        final (bool): If true, the next print is not able to replace this line. Used when this line replaces
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


def s_print(string="", replace=True, final=False) -> None:
    """
    Status print, read rprint docstring for more info.
    Simple rprint wrapper with a check for the PRINT_STATUS_UPDATES setting.
    """
    if settings.PRINT_STATUS_UPDATES:
        rprint(string, replace, final)
