from pathlib import Path
from typing import Union

from AoE2ScenarioParser.helper.printers import warn
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.data_objects.trigger import Trigger
from AoE2ScenarioParser.scenarios import scenario_store
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.sections.retrievers.support import Support


class XsManagerDE(AoE2Object):
    """Manager of the everything XS related."""

    _link_list = [
        RetrieverObjectLink("script_name", "Map", "script_name", Support(since=1.40)),
    ]

    def __init__(self, script_name: str, **kwargs):
        self._script_name = script_name
        self.xs_trigger: Union[Trigger, None] = None

        super().__init__(**kwargs)

    @property
    def script_name(self):
        return self._script_name

    @script_name.setter
    def script_name(self, value):
        if value:
            warn("Using script files added through `xs_manager.script_name` will not work in multiplayer.\n"
                 "You can work around this issue by using: `xs_manager.add_script(xs_file_path='path/to/script.xs')`.\n"
                 "For more information check out: https://ksneijders.github.io/AoE2ScenarioParser/cheatsheets/xs/")
        self._script_name = value

    @property
    def xs_trigger(self):
        if self._xs_trigger is None:
            self.initialise_xs_trigger()
        return self._xs_trigger

    @xs_trigger.setter
    def xs_trigger(self, value):
        self._xs_trigger = value

    def initialise_xs_trigger(self, insert_index: int = -1) -> None:
        """
        Creates the XS trigger on a desired location. If you don't care about the location, the `add_script()` function
        adds the trigger when calling it the first time too.

        If you want the trigger to be (almost) at the top of the list and you're reading a scenario with barely any to
        no triggers, it is recommended to call this somewhere at the start of the script.

        Insert index is used to move this trigger to a desired index.
        Keep in mind that moving triggers like this might take some time when you have a lot of triggers (thousands).

        Args:
            insert_index: The index where the xs trigger is added. Will be added at the end of the list if left as -1
        """
        self.xs_trigger = Trigger(
            name="XS SCRIPT", enabled=False,
            description="Due to the lack of support for transferring XS files between systems in Age of Empires II:DE, "
                        "this trigger adds the entire script to an effect script call. This will add the script to"
                        "each system once the game starts in the default0.xs file. -- Created using AoE2ScenarioParser",
            host_uuid=self._host_uuid
        )
        self.xs_trigger.new_effect.script_call(message="")

        trigger_manager = scenario_store.get_trigger_manager(self._host_uuid)
        trigger_manager.import_triggers([self.xs_trigger], insert_index)

    def _append_to_xs(self, title, string) -> None:
        self.xs_trigger.effects[0].message += f"// {'-' * 25} {title} {'-' * 25}\n{string}\n\n"

    def add_script(self, xs_file_path="", xs_string=""):
        """
        Add a script to the script call effect in the XS trigger

        Args:
            xs_file_path: Path to an XS file
            xs_string: Raw XS
        """
        if xs_file_path:
            path = Path(xs_file_path)
            with path.open() as xs_file:
                self._append_to_xs(path.name, xs_file.read())
        if xs_string:
            self._append_to_xs(f"XS string", xs_string)

    def _debug_write_script_to_file(self, filename="xs.txt"):
        with open(filename, 'w') as file:
            file.write(self.xs_trigger.effects[0].message)
