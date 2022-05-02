from typing import Any, List, Callable, Type, Dict, TYPE_CHECKING
from uuid import UUID

from AoE2ScenarioParser.scenarios.scenario_store import getters

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


class RetrieverObjectLinkParent:
    def __init__(
            self,
            section_name: str = None,
            link: str = None,
            commit_callback: Callable = None,
    ):
        self.section_name: str = section_name
        self.link: str = link
        self.commit_callback: Callable = commit_callback
        self.splitted_link: List[str] = link.split('.') if link else []

    def retrieve_value_from_link(
            self,
            uuid: UUID = None,
            host_obj: Type['AoE2Object'] = None,
            from_section: Any = None,
            number_hist: List[int] = None
    ) -> Any:
        """
        Retrieve value based on link

        Args:
            uuid: The UUID of the current scenario
            host_obj: A reference to the host object class
            from_section: Start retrieving the value from a different starting point than the scenario sections
            number_hist: The history numbers

        Returns:
            The value located at the location found through self.link
        """
        starting_index = 0

        if from_section is None:
            sections = getters.get_sections(uuid)
            value = sections[self.section_name]
        else:
            value = from_section
            # Get the index up to date if this link is within a group.
            starting_index = len(number_hist)

        for index, item in enumerate(self.splitted_link, starting_index):
            if item.endswith("]"):
                # item[:-11] removes "[__index__]" from the key
                value = getattr(value, item[:-11])[number_hist[index]]
            else:
                value = getattr(value, item)
        return value

    def overwrite_unsupported_properties(self, class_reference: Type['AoE2Object'], uuid: UUID) -> bool:
        """
        Overwrites the properties of class_reference if they are not supported in the version of the scenario with the
        given uuid

        Args:
            class_reference: A reference to the class containing the retriever object link ('self') in its link list
                (Mostly the host object where this link_list belongs to)
            uuid: The UUID of the current scenario

        Returns:
            True if values are (or already have been) overwritten
        """
        return False

    def get_names(self) -> List[str]:
        raise NotImplementedError("This function has not been implemented in the subclass yet.")

    def construct(
            self,
            host_uuid: UUID,
            number_hist: List[int] = None,
            host_obj: Type['AoE2Object'] = None
    ) -> Dict[str, Any]:
        """
        Construct all retrievers in the group

        Args:
            host_uuid: The UUID of the current scenario
            number_hist: The history number list
            host_obj: The host object that belongs to the retriever links

        Returns:
            A Dict with keys as object constructor params and values corresponding to said keys
        """
        raise NotImplementedError("This function has not been implemented in the subclass yet.")

    def commit(self, host_uuid: UUID, host_obj: 'AoE2Object') -> None:
        raise NotImplementedError("This function has not been implemented in the subclass yet.")
