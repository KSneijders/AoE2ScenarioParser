from typing import List, Dict, Any, TYPE_CHECKING, Type
from uuid import UUID

from AoE2ScenarioParser.objects.support.uuid_list import NO_UUID
from AoE2ScenarioParser.sections.retrievers.construct_progress import ConstructProgress
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

        self.group = group or []

        # Inject reference to the parent into the child for debugging purposes
        for rol in self.group:
            rol.parent = self

    def get_names(self):
        return [e.name for e in self.group]

    def pull(
            self,
            uuid: UUID,
            number_hist: List[int] = None,
            host_obj: Type['AoE2Object'] = None,
            progress: ConstructProgress = None
    ) -> Dict[str, Any]:
        if number_hist is None:
            number_hist = []

        attributes = {}

        section = self.pull_from_link(uuid, number_hist, progress=progress)

        # 'done' is set to 0 as entries within a group do not have a prefix that has already been cleared
        progress = ConstructProgress(section=section, done=0)

        for link in self.group:
            attributes[link.name] = link.pull_from_link(uuid=uuid, number_hist=number_hist,
                                                        host_obj=host_obj, progress=progress)
        return attributes

    def push(self, uuid: UUID, host_obj: 'AoE2Object'):
        if uuid == NO_UUID:
            raise ValueError(f"Invalid object push. No UUID was set. Object class: {host_obj.__class__.__name__}")

        number_hist = host_obj.instance_number_history
        section = self.pull_from_link(uuid, number_hist)

        for link in reversed(self.group):
            link.push_to_link(
                uuid=uuid, number_hist=number_hist, host_obj=host_obj,
                # 'done' is set to 0 as entries within a group do not have a prefix that has already been cleared
                progress=ConstructProgress(section=section, done=0)
            )
