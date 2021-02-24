from typing import Type, List

from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.sections.dependencies.dependency import handle_retriever_dependency
from AoE2ScenarioParser.sections.retrievers.retriever import get_retriever_by_name


class RetrieverObjectLink:
    def __init__(self,
                 variable_name: str,
                 section_name: str = None,
                 link: str = None,
                 process_as_object: Type[AoE2Object] = None,
                 retrieve_instance_number: bool = False,
                 retrieve_history_number: int = -1
                 ):
        if sum([link is not None, retrieve_instance_number, (retrieve_history_number != -1)]) != 1:
            raise ValueError("You must use one parameter from 'link' and the two 'retrieve...number' parameters.")

        self.name: str = variable_name
        self.section_name = section_name
        self.link = link
        self.is_special_unit_case = self._is_special_unit_case()
        self.process_as_object: Type[AoE2Object] = process_as_object
        self.retrieve_instance_number: bool = retrieve_instance_number
        self.retrieve_history_number: int = retrieve_history_number

        self.splitted_link: List[str] = link.split('.') if link is not None else []

    def construct(self, sections, number_hist=None):
        if number_hist is None:
            number_hist = []
        instance_number = AoE2Object.get_instance_number(number_hist=number_hist)

        if self.retrieve_instance_number:
            return instance_number
        elif self.retrieve_history_number != -1:
            return number_hist[self.retrieve_history_number]
        else:
            # Todo: Look into saving some results here - this code runs 62.556 times
            if self.is_special_unit_case:
                return self._construct_special_unit_case(sections)

            # Retrieve value without using eval() -- Eval is slow
            value = sections[self.section_name]
            for index, item in enumerate(self.splitted_link):
                if "[" in item:
                    value = getattr(value, item[:-11])[number_hist[index]]
                else:
                    value = getattr(value, item)

            if self.process_as_object:
                return self.process_object_list(value, number_hist, sections)
            return value

    def process_object_list(self, value_list, instance_number_history, sections):
        object_list = []
        for index, struct in enumerate(value_list):
            object_list.append(
                self.process_as_object._construct(
                    sections,
                    instance_number_history=instance_number_history + [index]
                )
            )
        return object_list

    def commit(self, sections, host_obj):
        # Object-only retrievers for the ease of access of information.
        # Not actually representing a value in the scenario file.
        if self.retrieve_instance_number or self.retrieve_history_number >= 0:
            return

        instance_number_history = host_obj._instance_number_history
        instance_number = AoE2Object.get_instance_number(obj=host_obj)
        value = host_obj.__getattribute__(self.name)

        # Replace __index__ values
        temp_link = self.link
        if instance_number_history:
            for i in instance_number_history:
                temp_link = temp_link.replace("__index__", str(i), 1)
        temp_link = temp_link.replace("__index__", str(instance_number), 1)

        if self.is_special_unit_case:
            temp_link = temp_link.replace('[]', '[0]', 1)

        split_temp_link: List[str] = temp_link.split(".")
        retriever = None

        section = sections[self.section_name]
        for attribute in split_temp_link:
            if '[' in attribute:
                index_location = attribute.index('[')
                index = int(attribute[index_location + 1:len(attribute) - 1])
                retriever = get_retriever_by_name(section.retrievers, attribute[:index_location]).data[index]
            else:
                retriever = get_retriever_by_name(section.retrievers, attribute)

        if retriever is None:
            raise ValueError("RetrieverObjectLink is unable to connect to retriever")

        retriever_list = section.retrievers

        if self.process_as_object is not None:
            struct_datatype = retriever.datatype.var

            struct_prefix = "struct:"
            if not struct_datatype.startswith(struct_prefix):
                raise ValueError(
                    f"Process as object isn't defined properly. Expected: '{struct_prefix}...' got: '{struct_datatype}'"
                )

            print(section)
            print()

            # Todo: Get struct formation

            if self.is_special_unit_case:
                self._commit_special_unit_case(host_obj, sections, struct_datatype, value)
                return

            try:
                old_length = len(retriever.data)
            except TypeError:
                # retriever.data was not set before (list of 0 -> None)
                retriever.data = []
                old_length = 0
            new_length = len(value)

            if new_length < old_length:
                retriever.data = retriever.data[:new_length]
            elif new_length > old_length:
                retriever.data += [struct_datatype() for _ in range(new_length - old_length)]
                if retriever.log_value:
                    retriever._update_print(
                        f"[{struct_datatype.__name__}] * {old_length}",
                        f"[{struct_datatype.__name__}] * {new_length}"
                    )

            for index, obj in enumerate(value):
                obj._sections = sections
                obj._instance_number_history = host_obj._instance_number_history + [index]
                obj.commit()
        else:
            retriever.data = value

        if hasattr(retriever, 'on_commit'):
            handle_retriever_dependency(retriever, "commit", retriever_list, sections)

    def _is_special_unit_case(self) -> bool:
        return ("[]" in self.link) if self.link else False

    def _construct_special_unit_case(self, sections):
        units = []
        value = sections[self.section_name]
        for index, item in enumerate(self.splitted_link):
            if "[]" in item:
                value = getattr(value, item[:-2])
            else:
                for player, player_units_section in enumerate(value):
                    player_units = getattr(player_units_section, item)
                    units.append(self.process_object_list(player_units, [player], sections))
        return units

    def _commit_special_unit_case(self, host_obj, sections, link_sections, units):
        for player_number in range(len(units)):
            sections['Units'].players_units[player_number].unit_count = len(units[player_number])
            sections['Units'].players_units[player_number].units = \
                [link_sections() for _ in range(len(units[player_number]))]

            for index, obj in enumerate(units[player_number]):
                obj._sections = sections
                obj._instance_number_history = [player_number, index]
                obj.commit()

    def __repr__(self):
        return f"[RetrieverObjectLink] {self.name}: {self.section_name}. {self.link}" + \
               (f"\n\t- Process as: {self.process_as_object.__name__}" if self.process_as_object else "") + \
               (f"\n\t- Get Instance Number: True" if self.retrieve_instance_number else "") + \
               (f"\n\t- Get Hist Number: {self.retrieve_history_number}" if self.retrieve_history_number >= 0 else "")
