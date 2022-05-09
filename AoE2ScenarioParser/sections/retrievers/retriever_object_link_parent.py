from typing import Any, List, Callable, Type, Dict, TYPE_CHECKING
from uuid import UUID

from AoE2ScenarioParser.scenarios.scenario_store import getters

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
    from AoE2ScenarioParser.sections.retrievers.retriever import Retriever


class RetrieverObjectLinkParent:
    def __init__(
            self,
            section_name: str = None,
            link: str = None,
    ):
        self.section_name: str = section_name
        self.link: str = link
        self.splitted_link: List[str] = link.split('.') if link else []

    def get_value_from_link(
            self,
            uuid: UUID,
            number_hist: List[int],
            host_obj: Type['AoE2Object'] = None,
            from_section: Any = None
    ) -> Any:
        """
        Retrieve value based on link

        Args:
            uuid: The UUID of the current scenario
            number_hist: The history numbers
            host_obj: A reference to the host object class
            from_section: Start retrieving the value from a different starting point than the scenario sections

        Returns:
            The value located at the location found through self.link
        """
        return self.get_from_link(
            return_retriever=False,
            uuid=uuid,
            number_hist=number_hist,
            from_section=from_section,
        )

    def get_section(self, uuid: UUID = None, from_section: Any = None):
        if from_section is None:
            sections = getters.get_sections(uuid)
            try:
                return sections[self.section_name]
            except KeyError as e:
                print(self)
                print("\n\n\n")

                import time
                time.sleep(.1)

                raise e

        return from_section

    def get_from_link(
            self,
            return_retriever=True,
            uuid: UUID = None,
            from_section: Any = None,
            number_hist: List[int] = None,
    ) -> 'Retriever':
        # print(f"return_retriever={return_retriever} uuid={uuid} host_obj={host_obj} from_section={from_section} number_hist={number_hist}")
        old = value = self.get_section(uuid, from_section)

        starting_index = 0
        if from_section is not None:
            # Get the index up to date if this link is within a group.
            starting_index = len(number_hist)

        # if self.splitted_link == ['garrisoned_in_id']:
        #     print("\n+++++++++++++++")
        #     print(starting_index)
        #     print(self.splitted_link)
        #     print(self.section_name)

        # If we want the retriever and there's only one link, we can directly extract it from the retriever map
        if return_retriever and len(self.splitted_link) == 1:
            return value.retriever_map[self.splitted_link[0]]

        for index, item in enumerate(self.splitted_link, starting_index):
            # If the end of the loop is found, return the retriever
            if return_retriever and index == len(self.splitted_link) - 1:
                try:
                    return value.retriever_map[item]
                except KeyError as e:
                    import time
                    print(self)
                    print(type(value))
                    print(value.retriever_map.keys())
                    # print(value)
                    time.sleep(.2)
                    raise e

            if value.name == "PlayerDataThreeStruct":
                print(index)
                print(return_retriever)
                print(index == len(self.splitted_link) - 1)
                print("----\n")

            if item.endswith("]"):
                # item[:-11] removes "[__index__]" from the key
                value = getattr(value, item[:-11])[number_hist[index]]
            else:
                value = getattr(value, item)

        # if type(value) is int and return_retriever:
        #     print(f"old: {old}")
        #     print(self.splitted_link)
        #     # print(self)
        #     # print(type(value))
        #     # print(value)
        #     # print(f"return_retriever={return_retriever} uuid={uuid} from_section={from_section} number_hist={number_hist}")
        #     exit(889211)
        # Can only be reached if `return_retriever=False`
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
