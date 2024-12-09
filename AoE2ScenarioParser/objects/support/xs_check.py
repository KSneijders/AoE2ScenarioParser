import re
import shutil
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Optional, Union, Tuple, Dict

from AoE2ScenarioParser.exceptions.asp_exceptions import XsCheckValidationError
from AoE2ScenarioParser.helper.string_manipulations import add_tabs


class XsCheck:
    # https://github.com/Divy1211/xs-check/releases/download/v0.1.2/xs-check.exe
    supported_versions: Dict[Tuple, str] = {
        (0, 1, 1): '',
        (0, 1, 2): '',
        (0, 1, 3): ''
    }

    def __init__(self):
        self.xs_encoding = 'utf-8'
        self.allow_unsupported_versions: bool = False

        self.path = None
        """The path for the XS check binary"""
        self._path_lookup = False
        """If an automatic path lookup (from PATH) has been done for xs-check"""

        # self.allow_xs_check_download = False
        # """If ASP is allowed to download the xs-check executable from GitHub"""

    @property
    def path(self) -> Optional[Path]:
        if not self._path_lookup and self._path is None:
            self._path_lookup = True
            self.path = shutil.which('xs-check')

        return self._path

    @path.setter
    def path(self, value: Optional[Union[Path, str]]):
        if value is None:
            self._path = value
            return

        path = value if isinstance(value, Path) else Path(value)
        if not path.is_file():
            raise ValueError(f'Unable to find xs-check executable at "{path}"')

        self._path = path

        if not self.is_supported_xs_check_binary():
            version = self.get_version()
            raise ValueError(f'Invalid xs-check binary given with version "{version}" at "{path}"')

    def validate(self, xs_file: Optional[Union[Path, str]]) -> True:
        """
        Validates the XS file and throws an exception if xs-check finds an error

        Args:
            xs_file: The XS file to validate

        Throws:
            XsCheckValidationError: When xs-check encounters an error

        Returns:
            True if no errors are found, an ``XsCheckValidationError`` is thrown otherwise
        """
        xs_path = str(xs_file.absolute()) if isinstance(xs_file, Path) else xs_file

        output = self._xs_check_call(xs_path)

        if output.startswith('No errors found in file'):
            return True

        version = '.'.join(str(v) for v in self.get_version())

        print(f"\nxs-check:{version} output: [ Provided by: https://github.com/Divy1211/xs-check/ ]\n")
        print(add_tabs(output, 1))

        time.sleep(.5)

        raise XsCheckValidationError("Xs-Check failed validation, see errors above", xs_check_errors=output)

    def validate_safe(self, xs_file: Optional[Union[Path, str]]) -> True:
        """
        Validates the XS file and and returns a boolean based on if errors were found

        Args:
            xs_file: The XS file to validate

        Returns:
            True if no errors are found, False otherwise
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
        version_tuple = self.get_version()

        return version_tuple in self.supported_versions or self.allow_unsupported_versions

    def get_version(self) -> Tuple[int, ...]:
        """
        Get the version from the xs-check executable

        Returns:
            A tuple containing the version xs-check number
        """
        stdout = self._xs_check_call('-v')

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

    def _xs_check_call(self, *args: str):
        """
        Call XS Check

        Args:
            *args: The arguments to be added to xs-check

        Returns:
            The STDOUT from the call as a string
        """
        if self.path is None:
            raise ValueError('Unable to locate xs-check, please specify a path using xs_manager.xs_check.path = \'<path>\'')

        # Make temp files to capture xs-check output
        stdout_file, stdout_path = tempfile.mkstemp()
        stderr_file, stderr_path = tempfile.mkstemp()

        command = [self.path, *args]
        try:
            exitcode = subprocess.call(command, timeout=5, stdout=stdout_file, stderr=stderr_file)
        except Exception as e:
            raise ValueError("ad")

        if exitcode != 0:
            error = Path(stderr_path).read_text(encoding=self.xs_encoding)

            raise ValueError(f"A non-zero exit code ({exitcode}) was returned by xs-check: '{error}'")

        return Path(stdout_path).read_text(encoding=self.xs_encoding)
