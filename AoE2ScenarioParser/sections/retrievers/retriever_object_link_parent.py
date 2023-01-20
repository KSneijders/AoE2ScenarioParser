from __future__ import annotations

from typing import Any, List, Type, Dict, TYPE_CHECKING, Optional
from uuid import UUID

from AoE2ScenarioParser.scenarios.scenario_store import getters
from AoE2ScenarioParser.sections.retrievers.construct_progress import ConstructProgress

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
    from AoE2ScenarioParser.sections.retrievers.retriever import Retriever
    from AoE2ScenarioParser.sections.aoe2_file_section import AoE2FileSection
    from AoE2ScenarioParser.sections.retrievers.retriever_object_link_group import RetrieverObjectLinkGroup


class RetrieverObjectLinkParent:
    def __init__(
            self,
            section_name: str = None,
            link: str = None,
    ):
        self.section_name: str = section_name
        self.link: str = link
        self.splitted_link: List[str] = link.split('.') if link else []

        self.parent: Optional['RetrieverObjectLinkGroup'] = None
        """A link to the parent which will be injected by the group if it is in any """

    def pull_from_link(
            self,
            uuid: UUID,
            number_hist: List[int],
            host_obj: Type['AoE2Object'] = None,
            progress: ConstructProgress = None
    ) -> Any:
        """
        Retrieve value based on link

        Args:
            uuid: The UUID of the current scenario
            number_hist: The history numbers
            host_obj: A reference to the host object class
            progress: Start retrieving the value from a different starting point than the scenario sections

        Returns:
            The value located at the location found through self.link
        """
        return self.get_from_link(False, uuid, progress, number_hist)

    def get_section(self, uuid: UUID = None, progress: ConstructProgress = None) -> 'AoE2FileSection':
        """
        Wrapper function to return the ``from_section`` if it is defined. If not, get a section based on the current
        ``self.section_name`` from the scenario sections dict.

        Args:
            uuid: The UUID of the current scenario
            progress: The section to get another section from

        Returns:
            The section given or one from the scenario
        """
        if progress is None:
            sections = getters.get_sections(uuid)
            return sections[self.section_name]
        return progress.section

    def get_from_link(
            self,
            return_retriever=True,
            uuid: UUID = None,
            progress: ConstructProgress = None,
            number_hist: List[int] = None,
    ) -> 'Retriever' | Any:
        """
        Retrieve a retriever or the value inside it from a given link. Starting point (where the link should start
        looking from) can be from the scenario sections (if ``from_section`` is left empty). If ``from_section`` is not
        empty, it'll start looking from there. ``from_section`` is only used when this function is called from
        a RetrieverObjectLinkGroup.

        Args:
            return_retriever: If this function should return the retriever or the data inside of it
            uuid: The UUID of the scenario
            progress: If defined, use the link to start from this section instead of the main scenario sections
            number_hist: The number history of this object

        Returns:
            The found retriever or the value inside it depending on `return_retriever` parameter
        """
        section = self.get_section(uuid, progress)

        starting_index = 0
        if progress is not None:
            starting_index = progress.done

        # for index, item in enumerate(self.splitted_link, starting_index):
        for index in range(starting_index, len(self.splitted_link)):
            item = self.splitted_link[index]

            # If looking for a retriever and the end of the loop is found, return it
            if return_retriever and index == len(self.splitted_link) - 1:
                return section.retriever_map[item]

            if item.endswith("]"):
                # item[:-11] removes "[__index__]" from the key
                section = getattr(section, item[:-11])[number_hist[index]]
            else:
                section = getattr(section, item)

        # Can only be reached if `return_retriever=False`
        return section

    def overwrite_unsupported_properties(self, class_reference: Type['AoE2Object'], uuid: UUID) -> bool:
        """
        Overwrites the properties of class_reference if they are not supported in the version of the scenario with the
        given uuid

        Args:
            class_reference: A reference to the class containing the retriever object link ('self') in its link list
                (Mostly the host object where this link_list belongs to)
            uuid: The UUID of the current scenario

        Returns:
            `True` if values are (or already have been) overwritten
        """
        return False

    def get_names(self) -> List[str]:
        """
        Returns:
            All names from this link (singular/group) inside of a list
        """
        raise NotImplementedError("This function has not been implemented in the subclass yet.")

    def pull(
            self,
            uuid: UUID,
            number_hist: List[int] = None,
            host_obj: Type['AoE2Object'] = None,
            progress: ConstructProgress = None
    ) -> Dict[str, Any]:
        """
        Should result in the values being pulled from AoE2FileSection and Retrievers into the corresponding descendants
        of AoE2Object.

        Args:
            uuid: The UUID of the current scenario
            number_hist: The history number list
            host_obj: The host object that belongs to the retriever links
            progress: If defined, use the link to start from this section instead of the main scenario sections

        Returns:
            A Dict with keys as object constructor params and values corresponding to said keys
        """
        raise NotImplementedError("This function has not been implemented in the subclass yet.")

    def push(self, uuid: UUID, host_obj: 'AoE2Object') -> None:
        """
        Should result in the values going from the descendants of AoE2Object and being pushed back into the
        corresponding Retrievers and AoE2FileSection

        Args:
            uuid: The UUID of the current scenario
            host_obj: The host object that belongs to the retriever links
        """
        raise NotImplementedError("This function has not been implemented in the subclass yet.")

    @staticmethod
    def format_link_string(link: str, history: List[int]) -> str:
        """
        Format a link string to include the index values from the history

        Args:
            link: The link string (i.e. `"trigger_data[__index__].effect_data[__index__]"`)
            history: The number history i.e. `[4, 1]`

        Returns:
            The formatted string. Taking the examples from params, this would become `"trigger_data[4].effect_data[1]"`.
        """
        for i in range(len(history)):
            link = link.replace('__index__', str(history[i]), 1)
        return link
