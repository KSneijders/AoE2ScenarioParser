import tempfile
from pathlib import Path
from typing import Optional, Union, TYPE_CHECKING

from AoE2ScenarioParser.datasets.effects import EffectId
from AoE2ScenarioParser.exceptions.asp_exceptions import UnsupportedAttributeError, UnsupportedVersionError
from AoE2ScenarioParser.helper.pretty_format import pretty_format_list
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.data_objects.trigger import Trigger
from AoE2ScenarioParser.objects.support.xs_check import XsCheck
from AoE2ScenarioParser.scenarios.scenario_store import actions
from AoE2ScenarioParser.scenarios.scenario_store.getters import get_scenario_version
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.sections.retrievers.support import Support


if TYPE_CHECKING:
    from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario


class XsManagerDE(AoE2Object):
    """Manager of everything XS related."""

    _link_list = [
        RetrieverObjectLink("script_name", "Map", "script_name", Support(since=1.40)),
    ]

    def __init__(self, script_name: str, **kwargs):
        super().__init__(**kwargs)

        self._script_name = script_name
        """
        Using script files (added through this attribute) will NOT work for spectators.
        You can work around this issue by using: ```xs_manager.add_script(xs_file_path='path/to/script.xs')```
        For more information check out: https://ksneijders.github.io/AoE2ScenarioParser/cheatsheets/xs/
        """

        # Instantiate the xs-check helper
        self.xs_check = XsCheck()

        # --- XS Script Call Trigger ---
        self._initialized = False
        self._xs_trigger: Optional[Trigger] = Trigger(
            name="XS SCRIPT",
            enabled=False,
            description="Due to the lack of support for transferring XS files between systems in Age of Empires II:DE, "
                        "this trigger adds the entire script to an effect script call. This will add the script to"
                        "each system once the game starts in the default0.xs file. -- Created using AoE2ScenarioParser",
        )

        # Register this function to run on write
        self.get_scenario().on_write(self.on_write_register_xs_validation)

    @property
    def script_name(self):
        """The XS script name to include in the scenario"""
        return self._script_name

    @script_name.setter
    def script_name(self, value):
        self._script_name = value

    @property
    def xs_trigger(self):
        """The trigger holding the script call effect holding all the XS"""
        if not self._initialized:
            self.initialise_xs_trigger()
        return self._xs_trigger

    @xs_trigger.setter
    def xs_trigger(self, value):
        self._xs_trigger = value

    def initialise_xs_trigger(self, insert_index: int = -1) -> None:
        """
        Creates the XS trigger on a desired location. If you don't care about the location, the `add_script()` function
        adds the trigger when calling it the first time too.

        If you want the trigger to be (almost) at the top of the list, and you're reading a scenario with barely any to
        no triggers, it is recommended to call this somewhere at the start of the script.

        Insert index is used to move this trigger to a desired index.
        Keep in mind that moving triggers like this might take some time when you have a lot of triggers (thousands).

        Args:
            insert_index: The index where the xs trigger is added. Will be added at the end of the list if left empty
        """
        if self._initialized:
            return

        try:
            self._xs_trigger.new_effect.script_call(message="")
        except UnsupportedAttributeError:
            raise UnsupportedVersionError(
                f"The scenario version ({get_scenario_version(self._uuid)}) does not support XS. "
                f"Save the scenario in the editor to update the scenario to allow for XS."
            ) from None
        self._initialized = True
        actions.import_triggers(self._uuid, [self.xs_trigger], insert_index, deepcopy=False)

    def _append_to_xs(self, title, xs) -> None:
        self.xs_trigger.effects[0].message += f"// {'-' * 25} {title} {'-' * 25}\n{xs}\n\n"

    def add_script(self, xs_file_path: str = "", xs_string: str = "", validate: bool = False):
        """
        Add a script to the script call effect in the XS trigger

        Args:
            xs_file_path: Path to an XS file
            xs_string: Raw XS
            validate: If the given XS code should be validated using ``Alian713/xs-check`` → https://github.com/Divy1211/xs-check
        """
        strings = {}

        if xs_file_path:
            path = Path(xs_file_path)
            with path.open() as xs_file:
                strings[path.name] = xs_file.read()

        if xs_string:
            strings['XS string'] = xs_string

        for key, xs in strings.items():
            if validate:
                self.validate(xs=xs)

            self._append_to_xs(key, xs)

    def validate(self, xs: str = "", xs_path: Union[Path, str] = "") -> True:
        """
        Validate a given string

        Args:
            xs: The XS string (not file path) to validate
            xs_path: A path to an XS file

        Throws:
            XsCheckValidationError: When xs-check encounters an error

        Returns:
            True when the validation succeeds without errors. Throws an XsCheckValidationError otherwise
        """
        if not xs and not xs_path:
            raise ValueError("Unable to validate XS without XS string or Path")

        file = None

        if xs_path:
            file = xs_path if isinstance(xs_path, Path) else Path(xs_path)

            if not file.is_file():
                raise ValueError(f"File '{xs_path}' does not exist")
        if xs:
            _, path = tempfile.mkstemp()
            file = Path(path)
            file.write_text(xs)

        return self.xs_check.validate(str(file.absolute()))

    def on_write_register_xs_validation(self, scenario: 'AoE2DEScenario'):
        if self.xs_check.is_disabled:
            return

        def on_write_run_xs_validation(scenario: 'AoE2DEScenario'):
            xs_snippets = []
            for trigger in scenario.trigger_manager.triggers:
                for condition in trigger.conditions:
                    if condition.xs_function:
                        xs_snippets.append(condition.xs_function)
                for effect in trigger.effects:
                    if effect.effect_type == EffectId.SCRIPT_CALL and effect.message != '':
                        xs_snippets.append(effect.message)

            xs_code = '\n'.join(xs_snippets)
            if not xs_code:
                return

            self.validate(xs=xs_code)

        scenario.on_write(on_write_run_xs_validation)

    def _debug_write_script_to_file(self, filename: str = "xs.txt"):
        with open(filename, 'w') as file:
            file.write(self.xs_trigger.effects[0].message)
