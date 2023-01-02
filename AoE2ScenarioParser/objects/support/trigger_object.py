from typing import Any


class TriggerComponent:
    hidden_attribute = ''
    """The attribute that should not be shown in this component. Used to hide the identifier in printing jobs"""

    def get_content_as_string(self) -> str:
        """Generate a string representation of this trigger component"""
        raise NotImplementedError("This method has not been implemented yet.")

    def _should_be_displayed(self, attr: str, val: Any) -> bool:
        """
        Check if a given attribute with a given value should be printed or not

        Args:
            attr: The attribute as string
            val: The value found with the attribute

        Returns:
            A boolean if the attr, val combination should be printed
        """
        if val in [[], [-1], [''], "", " ", -1]:
            return False
        if attr == self.hidden_attribute:
            return False
        return True
