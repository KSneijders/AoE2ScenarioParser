import sys

from AoE2ScenarioParser.exceptions.asp_warnings import PythonVersionWarning
from AoE2ScenarioParser.helper.printers import warn

_block_below = (3, 8)
_notify_below = (3, 8)
_py_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


def python_version_check():
    if sys.version_info < (3, 0):
        raise Exception("AoE2ScenarioParser does not support Python 2")

    if sys.version_info < _block_below:
        raise Exception(f"\n\nAoE2ScenarioParser requires the use of Python {'.'.join(map(str, _block_below))}.\n"
                        f"You are currently using version {_py_version}. You can download a newer version from: \n"
                        f"\thttps://www.python.org/downloads/\n")
    elif sys.version_info < _notify_below:
        v = '.'.join(map(str, _notify_below))
        warn('\n'.join([
            f"AoE2ScenarioParser will update the minimum python requirements to Python {v} in the (near) future.",
            f"You are currently using version {_py_version}. You can download a newer version from:",
            "\thttps://www.python.org/downloads/",
            f"You can disable these warnings using:",
            "\timport warnings",
            "\tfrom AoE2ScenarioParser.helper.exceptions import PythonVersionWarning",
            "\twarnings.filterwarnings(action='ignore', category=PythonVersionWarning)",
        ]), category=PythonVersionWarning)
