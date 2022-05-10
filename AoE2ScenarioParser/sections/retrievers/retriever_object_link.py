from typing import Type, List, Callable, Dict, Any, Optional, TYPE_CHECKING
from uuid import UUID

from AoE2ScenarioParser.helper.exceptions import UnsupportedAttributeError
from AoE2ScenarioParser.scenarios.scenario_store import getters
from AoE2ScenarioParser.sections.aoe2_file_section import AoE2FileSection
from AoE2ScenarioParser.sections.aoe2_struct_model import AoE2StructModel
from AoE2ScenarioParser.sections.dependencies.dependency import handle_retriever_dependency
from AoE2ScenarioParser.sections.retrievers.retriever import Retriever
from AoE2ScenarioParser.sections.retrievers.retriever_object_link_parent import RetrieverObjectLinkParent
from AoE2ScenarioParser.sections.retrievers.support import Support

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
    from AoE2ScenarioParser.sections.retrievers.retriever_object_link_group import RetrieverObjectLinkGroup


class RetrieverObjectLink(RetrieverObjectLinkParent):
    def __init__(
            self,
            variable_name: str,
            section_name: str = None,
            link: str = None,
            support: Support = None,
            process_as_object: Type['AoE2Object'] = None,
            retrieve_history_number: int = None,
            commit_callback: Callable = None,
            destination_object: Type['AoE2Object'] = None,
    ):
        if link is not None and retrieve_history_number is not None:
            raise ValueError("You must use 'link' OR 'retrieve_history_number' as parameter, not both.")

        super().__init__(section_name, link or variable_name)

        self.name: str = variable_name
        self.support: Support = support
        self.process_as_object: Type['AoE2Object'] = process_as_object
        self.retrieve_history_number: Optional[int] = retrieve_history_number
        self.commit_callback: Callable = commit_callback
        self.destination_object: Type['AoE2Object'] = destination_object

        self.disabled = False
        """
        Set to True if the given property (referenced by link) is not supported in the current scenario version.
        When True, the properties are overridden to raise an error when used.  
        """
        self.group: Optional['RetrieverObjectLinkGroup'] = None
        """A link to the parent which will be injected by the group if it is in any """

    def get_names(self):
        """
        Returns:
            The name of this object link in a list
        """
        return [self.name]

    def overwrite_unsupported_properties(self, class_reference: Type['AoE2Object'], uuid: UUID) -> bool:
        scenario_version = getters.get_scenario_version(uuid)

        # If support is None, that means that the thing is supported in every scenario version that the parser supports
        if self.support is not None:
            # If already disabled, the property has already been set to raise an error so return True
            if self.disabled:
                return True
            # If the property is supported, return False
            if self.support.supports(scenario_version):
                return False

            error_msg = self.get_unsupported_string(scenario_version)

            def _get(self_):
                raise UnsupportedAttributeError(error_msg)

            def _set(self_, val):
                if val is not None:
                    raise UnsupportedAttributeError(error_msg)

            if self.destination_object is not None:
                class_reference = self.destination_object

            # Todo: Doesn't work properly when reading an older scenario first, and a newer one later
            #  Properties don't get reset!
            #  Just resetting doesnt work either as both scenarios can be used at the same time. get/set functions need
            #  more logic ("or Dynamic classes" -- Alian)
            setattr(class_reference, self.name, property(_get, _set))
            self.disabled = True

            return True
        return False

    def get_value_from_link(
            self,
            uuid: UUID = None,
            number_hist: List[int] = None,
            host_obj: Type['AoE2Object'] = None,
            from_section: Any = None
    ) -> Any:
        """
        Retrieve value based on link.

        Args:
            uuid: The UUID of the current scenario
            host_obj: A reference to the host object class
            from_section: Start retrieving the value from a different starting point than the scenario sections
            number_hist: The history numbers

        Returns:
            The value located at the location found through self.link
        """
        overwritten = self.overwrite_unsupported_properties(host_obj, uuid)
        if overwritten:
            # Unsupported property; So unable to get value as it doesn't exist in current version.
            return None

        value = super().get_value_from_link(uuid, number_hist, host_obj, from_section)

        if self.process_as_object:
            value = self.process_object_list(value, number_hist, uuid)
        return value

    def pull(
            self,
            host_uuid: UUID,
            number_hist: List[int] = None,
            host_obj: Type['AoE2Object'] = None
    ) -> Dict[str, Any]:
        if number_hist is None:
            number_hist = []

        if self.retrieve_history_number is not None:
            value = number_hist[self.retrieve_history_number]
        else:
            value = self.get_value_from_link(host_uuid, number_hist, host_obj)

        return {self.name: value}

    def process_object_list(self, value_list: List[Any], instance_number_history, host_uuid):
        object_list = []
        for index, struct in enumerate(value_list):
            # Todo: Check this out - structs are unused - KSneijders
            object_list.append(
                self.process_as_object._construct(host_uuid, instance_number_history + [index])
            )
        return object_list

    def set_value_from_link(
            self,
            uuid: UUID = None,
            number_hist: List[int] = None,
            host_obj: 'AoE2Object' = None,
            from_section: Any = None
    ):
        if self.retrieve_history_number is not None:
            return
        if self.support and not self.support.supports(getters.get_scenario_version(uuid)):
            return

        retriever = self.get_from_link(True, uuid, from_section, number_hist)

        if retriever is None:
            raise ValueError("RetrieverObjectLink is unable to find retriever")

        value = getattr(host_obj, self.name)
        file_section = self.get_section(uuid, from_section)

        if self.process_as_object:
            struct_model = RetrieverObjectLink.get_struct_model(retriever, file_section)

            RetrieverObjectLink.update_retriever_length(retriever, struct_model, len(value), uuid)
            RetrieverObjectLink.commit_object_list(value, host_obj.instance_number_history)
        else:
            retriever.data = value

        if hasattr(retriever, 'on_commit'):
            handle_retriever_dependency(retriever, "commit", file_section, uuid)

    def push(self, host_uuid: UUID, host_obj: 'AoE2Object') -> None:
        self.set_value_from_link(host_uuid, host_obj.instance_number_history, host_obj)

    @staticmethod
    def get_struct_model(retriever: 'Retriever', section: 'AoE2FileSection'):
        prefix = "struct:"

        struct_datatype = retriever.datatype.var
        if not struct_datatype.startswith(prefix):
            raise ValueError(f"process_as_object isn't defined properly. Expected: '{prefix}...', got: '{struct_datatype}'")

        struct_name = struct_datatype[len(prefix):]
        return section.struct_models[struct_name]

    @staticmethod
    def commit_object_list(object_list: List['AoE2Object'], instance_number_history: List[int]):
        for index, obj in enumerate(object_list):
            obj._instance_number_history = instance_number_history + [index]
            obj.commit()

    # Todo: This could be a retriever function
    @staticmethod
    def update_retriever_length(
            retriever: Retriever,
            model: AoE2StructModel,
            new_len: int,
            host_uuid: UUID
    ) -> None:
        """
        Update the length of a struct retriever. When committing the new data from the managers, certain lists like
        the trigger list might have changed in size. And, because every object (e.g. Trigger) corresponds to a section
        with the same data (e.g. Trigger Section) the 2 lists (in manager and the corresponding one in sections) should
        always be the same size. This function takes care of that.

        If the list is equal, leave it unchanged. If the list is shorter, cut the retriever data short. If the list is
        longer, add new sections to it based on the given model (& the model defaults)

        Args:
            retriever: The retriever containing the list
            model: The model inside the retriever, in case the list grew
            new_len: The new length of the list inside the managers
            host_uuid: The UUID of the current scenario
        """
        try:
            old_len = len(retriever.data)
        except TypeError:  # retriever.data was not set before (list of 0 -> None)
            old_len = 0
            retriever.data = []

        if new_len < old_len:
            retriever.data = retriever.data[:new_len]
        elif new_len > old_len:
            retriever.data += [
                AoE2FileSection.from_model(model, host_uuid, set_defaults=True)
                for _ in range(new_len - old_len)
            ]

            if retriever.log_value:
                retriever.print_value_update(f"[{model.name}] * {old_len}", f"[{model.name}] * {new_len}")

    def get_unsupported_string(self, version: str):
        return f"The property '{self.name}' is {self.support}. Current version: {version}.\n"

    def __repr__(self):
        lines: List[str] = []

        if self.group:
            lines.append(f"[RetrieverObjectLinkGroup] {self.group.section_name}: {self.group.link}")
            lines.append(f"\t[RetrieverObjectLink] {self.name}: {self.link} ({self.group.link}.{self.link})")
        else:
            lines.append(f"[RetrieverObjectLink] {self.name}: {self.section_name}.{self.link}")

        if self.process_as_object is not None:
            lines.append(f"\t- Process as: {self.process_as_object.__name__}")

        if self.retrieve_history_number is not None:
            lines.append(f"\t- Get Hist Number: {self.retrieve_history_number}")

        if self.support is not None:
            lines.append(f"\t- Support: {self.support}")

        return '\n'.join([line for line in lines if line])
