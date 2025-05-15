import os
import re
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Optional, Union, Tuple, Set, List
from uuid import UUID

from AoE2ScenarioParser import settings
from AoE2ScenarioParser.datasets.conditions import ConditionId
from AoE2ScenarioParser.datasets.effects import EffectId
from AoE2ScenarioParser.exceptions.asp_exceptions import XsCheckValidationError
from AoE2ScenarioParser.helper.pretty_format import pretty_format_name
from AoE2ScenarioParser.helper.printers import s_print
from AoE2ScenarioParser.helper.string_manipulations import add_tabs
from AoE2ScenarioParser.scenarios.scenario_store import getters


class XsCheck:
    version: Tuple[int, int, int] = (0, 2, 4)

    def __init__(self, uuid: UUID):
        self._uuid: UUID = uuid

        self.enabled = True
        """If XS-Check is enabled or not"""
        self.xs_encoding = 'utf-8'
        """The encoding that should be used for reading and writing the file with the XS script"""
        self.allow_unsupported_versions: bool = False
        """If XS-Check should be checked for compatibility"""
        self.raise_on_error: bool = False
        """If a Python error should be raised if XS-Check encounters an error"""
        self.ignores: Set[str] = set()
        """A set of warnings to ignore"""
        self.additional_args: List[str] = []
        """A list of additional arguments to append to the validation calls"""

        self.path = None
        """The path for a custom XS check binary (One that is not shipped with AoE2ScenarioParser"""

        self.timeout_seconds = 60
        """The timeout for the XS-Check call in seconds"""

        self._default_folder = Path(__file__).parent.parent.parent / 'dependencies' / 'xs-check'
        """The folder path to look for the XS check binaries (shipped with AoE2ScenarioParser)"""

    @property
    def is_enabled(self):
        return self.enabled and settings.ENABLE_XS_CHECK_INTEGRATION

    @property
    def is_disabled(self):
        return not self.is_enabled

    @property
    def path(self) -> Optional[Path]:
        """The path for a custom XS check binary (One that is not shipped with AoE2ScenarioParser"""
        if self._path is None:
            if os.name == 'nt':
                extension = '.exe'
            elif os.name == 'posix':
                extension = ''
            else:
                raise Exception('Unsupported platform')

            return self._default_folder / ('xs-check' + extension)

        return self._path

    @path.setter
    def path(self, value: Optional[Union[Path, str]]):
        if value is None:
            self._path = None
            return

        path = value if isinstance(value, Path) else Path(value)
        if not path.is_file():
            raise ValueError(f'Unable to find xs-check binary at "{path}"')

        self._path = path

        if not self.is_supported_xs_check_binary():
            self._raise_unsupported()

    def validate(self, xs_file: Optional[Union[Path, str]], show_tmpfile: bool = True) -> True:
        """
        Validates the XS file and throws an exception if xs-check finds an error

        Args:
            xs_file: The XS file to validate
            show_tmpfile: If a reference to the tmp file should be displayed

        Throws:
            XsCheckValidationError: When xs-check encounters an error

        Returns:
            True if no errors are found or xs-check has been disabled, an ``XsCheckValidationError`` is thrown otherwise
        """
        if self.is_disabled:
            return True

        if not self.is_supported_xs_check_binary():
            self._raise_unsupported()

        xs_file_path = str(xs_file.absolute()) if isinstance(xs_file, Path) else xs_file

        args = [xs_file_path, *self.additional_args]
        if len(self.ignores) > 0:
            args.extend(['--ignores', ','.join(self.ignores)])

        output = self._call(*args)

        if output.startswith('No errors found in file'):
            return True

        # Do not show temp file name as it might be confusing
        output = output.replace(xs_file_path, 'AoE2ScenarioParser.xs')

        version = '.'.join(str(v) for v in self.get_version())

        s_print('\n' + ('-' * 25) + '<[ XS-CHECK VALIDATION RESULT ]>' + ('-' * 25), final=True)

        s_print(f"\nxs-check:{version} output: [ Provided by: https://github.com/Divy1211/xs-check/ ]\n", final=True)
        s_print(add_tabs(output, 1), final=True)

        self._print_parsed_xs_check_errors(output)

        if show_tmpfile:
            display_path = xs_file_path.replace('\\', '/')
            s_print(f"\nOpen the file below to view the entire XS file:\n\tfile:///{display_path}", final=True)

        time.sleep(.5)

        if self.raise_on_error:
            raise XsCheckValidationError("Xs-Check failed validation, see errors above", xs_check_errors=output)

        s_print('\n' + ('-' * 25) + '<[ END XS-CHECK VALIDATION RESULT ]>' + ('-' * 25), final=True)

    def validate_safe(self, xs_file: Optional[Union[Path, str]]) -> bool:
        """
        Validates the XS file and and returns a boolean based on if errors were found

        Args:
            xs_file: The XS file to validate

        Returns:
            True if no errors are found or xs-check has been disabled, False otherwise
        """
        try:
            return self.validate(xs_file)
        except XsCheckValidationError:
            return False

    def is_supported_xs_check_binary(self) -> bool:
        """
        Check if the xs-check binary is supported by this version of AoE2ScenarioParser.
        Allows an override to easily allow users to use newer versions which might be supported too.

        Returns:
            True if it is supported, False otherwise
        """
        if self.allow_unsupported_versions:
            return True

        version_tuple = self.get_version()

        if (0, 1, 2) <= version_tuple <= (0, 2, 4):
            return True

        return False

    def get_version(self) -> Tuple[int, ...]:
        """
        Get the version from the xs-check binary

        Returns:
            A tuple containing the version xs-check number
        """
        stdout = self._call('-v')

        version_string = self._get_version_from_xs_check_v_string(stdout)

        # Make it a proper version tuple
        return tuple(map(int, version_string.split('.')))

    def _get_version_from_xs_check_v_string(self, stdout: str) -> str:
        """
        Use a regex match to find the xs-check version from the string

        Args:
            stdout: The STDOUT from a ``xs-check -v`` call

        Returns:
            The xs-check version
        """

        def is_match(result: re.Match) -> bool:
            return result is not None and len(result.groups()) == 1

        if is_match(result := re.match(r'xs-check v(\d+\.\d+\.\d+):', stdout)):
            return result.groups()[0]

        raise ValueError(f'Unable to locate version from xs-check string: "{stdout}"')

    def _call(self, *args: str):
        """
        Call XS Check

        Args:
            *args: The arguments to be added to xs-check

        Returns:
            The STDOUT from the call as a string
        """
        # Make temp files to capture xs-check output
        stdout_file, stdout_path = tempfile.mkstemp()
        stderr_file, stderr_path = tempfile.mkstemp()

        command = [self.path, *args]
        exitcode = subprocess.call(command, timeout=self.timeout_seconds, stdout=stdout_file, stderr=stderr_file)

        if exitcode != 0:
            error = Path(stderr_path).read_text(encoding=self.xs_encoding)

            raise ValueError(f"A non-zero exit code ({exitcode}) was returned by xs-check: '{error}'")

        return Path(stdout_path).read_text(encoding=self.xs_encoding)

    def _print_parsed_xs_check_errors(self, output: str) -> None:
        # Remove unwanted characters from output (Color highlighting etc.)
        plain_output = re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', output)

        prev_trigger_index = None
        matches = re.findall(r'/\*T(\d+)([CE])(\d+)\*/', plain_output)

        if len(matches) == 0:
            return

        s_print(f"\nXS-Check errors origins:\n", final=True)
        for match in matches:
            trigger_index, ce_type, ce_index = match

            trigger = getters.get_trigger(self._uuid, int(trigger_index))
            if ce_type == 'C':
                obj = 'Condition'
                type_ = trigger.conditions[int(ce_index)].condition_type
                obj_name = pretty_format_name(ConditionId(type_).name)
            elif ce_type == 'E':
                obj = 'Effect'
                type_ = trigger.effects[int(ce_index)].effect_type
                obj_name = pretty_format_name(EffectId(type_).name)
            else:
                continue

            if prev_trigger_index != trigger_index:
                s_print(f"  ⇒ [Trigger #{trigger_index}] '{trigger.name}'", final=True)

            s_print(f"     ↳ [{obj} #{ce_index}] {obj_name} {obj}", final=True)
        s_print(f"", final=True)

    def _raise_unsupported(self):
        version = '.'.join(str(v) for v in self.get_version())
        raise ValueError(
            f'Unsupported xs-check binary given with version "{version}" at "{self._path}". \n'
            f'You can try `xs_manager.xs_check.allow_unsupported_versions = True` to override this check'
        )
