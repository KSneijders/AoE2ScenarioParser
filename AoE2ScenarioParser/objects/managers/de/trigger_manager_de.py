from typing import List

from AoE2ScenarioParser.helper.helper import exclusive_if
from AoE2ScenarioParser.objects.data_objects.trigger import Trigger
from AoE2ScenarioParser.objects.data_objects.variable import Variable
from AoE2ScenarioParser.objects.managers.trigger_manager import TriggerManager
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink


class TriggerManagerDE(TriggerManager):
    _link_list = [
        RetrieverObjectLink("triggers", "Triggers", "trigger_data", process_as_object=Trigger),
        RetrieverObjectLink("trigger_display_order", "Triggers", "trigger_display_order_array"),
        RetrieverObjectLink("variables", "Triggers", "variable_data", process_as_object=Variable),
    ]

    def __init__(self, triggers: List[Trigger], trigger_display_order: List[int], variables: List[Variable], **kwargs):
        self.variables: List[Variable] = variables

        super().__init__(triggers, trigger_display_order, **kwargs)

    def add_variable(self, name: str, variable_id: int = -1) -> Variable:
        """
        Adds a variable.

        Args:
            name (str): The name for the variable
            variable_id (int): The ID of the variable. If left empty (default: -1), lowest available value will be used

        Returns:
            The newly added Variable
        """
        list_of_var_ids = [var.variable_id for var in self.variables]
        if variable_id == -1:
            for i in range(256):
                if i not in list_of_var_ids:
                    variable_id = i
                    break
            if variable_id == -1:
                raise IndexError(f"No variable ID available. All in use? In use: ({list_of_var_ids}/256)")
        if not (0 <= variable_id <= 255):
            raise ValueError("Variable ID has to fall between 0 and 255 (incl).")
        if variable_id in list_of_var_ids:
            raise ValueError("Variable ID already in use.")

        new_variable = Variable(variable_id=variable_id, name=name, host_uuid=self._host_uuid)
        self.variables.append(new_variable)
        return new_variable

    def get_variable(self, variable_id: int = None, variable_name: str = None) -> Variable:
        if not exclusive_if(variable_id is not None, variable_name is not None):
            raise ValueError("Select a variable using either the variable_id or variable_name parameters.")
        for variable in self.variables:
            if variable.variable_id == variable_id or variable.name == variable_name:
                return variable

    def get_summary_as_string(self) -> str:
        return_string = super().get_summary_as_string()

        return_string += "\nVariables Summary:\n"
        if len(self.variables) == 0:
            return_string += "\t<< No Variables >>"

        longest_variable_name = -1
        for variable in self.variables:
            longest_variable_name = max(longest_variable_name, len(variable.name))

        longest_variable_name += 3
        for index, variable in enumerate(self.variables):
            var_name = variable.name
            name_buffer = " " * (longest_variable_name - len(var_name))
            return_string += f"\t{var_name}{name_buffer}[Index: {variable.variable_id}]\n"

        return return_string

    def get_content_as_string(self) -> str:
        return_string = super().get_content_as_string()

        return_string += "Variables:\n"

        if len(self.variables) == 0:
            return_string += "\t<<No Variables>>\n"

        for variable in self.variables:
            return_string += f"\t'{variable.name}' [Index: {variable.variable_id}]\n"

        return return_string
