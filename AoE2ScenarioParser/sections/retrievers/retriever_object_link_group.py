from typing import List, Callable, Dict, Any, TYPE_CHECKING, Type
from uuid import UUID

from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.sections.retrievers.retriever_object_link_parent import RetrieverObjectLinkParent

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


class RetrieverObjectLinkGroup(RetrieverObjectLinkParent):
    def __init__(
            self, section_name: str,
            link: str = "",
            commit_callback: Callable = None,
            group: List[RetrieverObjectLink] = None
    ):
        super().__init__(section_name, link, commit_callback)

        self.group = group if group is not None else []

    def get_names(self):
        """
        Returns:
            The names of all retriever object links in this group
        """
        return [e.name for e in self.group]

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
        if number_hist is None:
            number_hist = []
        attributes = {}
        section = self.retrieve_value_from_link(uuid=host_uuid, number_hist=number_hist)

        for link in self.group:
            attributes[link.name] = link.retrieve_value_from_link(
                uuid=host_uuid,
                host_obj=host_obj,
                from_section=section,
                number_hist=number_hist
            )

        return attributes

    def commit(self, host_uuid: UUID, host_obj: 'AoE2Object'):
        ...
