from typing import List, Callable, Dict, Any, TYPE_CHECKING, Type
from uuid import UUID

from AoE2ScenarioParser.objects.support.uuid_list import NO_UUID
from AoE2ScenarioParser.sections.retrievers.retriever_object_link_parent import RetrieverObjectLinkParent

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
    from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink


class RetrieverObjectLinkGroup(RetrieverObjectLinkParent):
    def __init__(
            self, section_name: str,
            link: str = "",
            group: List['RetrieverObjectLink'] = None
    ):
        super().__init__(section_name, link)

        if group is not None:
            self.group = group
        else:
            self.group = []

        # Inject reference to the parent into the child for debugging purposes
        for r in self.group:
            r.group = self

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
        section = self.get_value_from_link(host_uuid, number_hist)

        for link in self.group:
            attributes[link.name] = link.get_value_from_link(uuid=host_uuid, number_hist=number_hist,
                                                             host_obj=host_obj, from_section=section)
        return attributes

    def commit(self, host_uuid: UUID, host_obj: 'AoE2Object'):
        if host_uuid == NO_UUID:
            raise ValueError(f"Invalid object commit. No UUID was set. Object class: {host_obj.__class__.__name__}")

        number_hist = host_obj.instance_number_history
        section = self.get_value_from_link(host_uuid, number_hist)

        for link in reversed(self.group):
            link.set_value_from_link(uuid=host_uuid, number_hist=number_hist, host_obj=host_obj, from_section=section)
