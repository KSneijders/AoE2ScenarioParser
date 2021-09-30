from __future__ import annotations
from AoE2ScenarioParser.helper.exceptions import EndOfFileError


class IncrementalGenerator:
    """
    This class is similar to a generator and is used to return the bytes of a file sequentially
    """
    def __init__(self, name, file_content, progress=0):
        self.name = name
        self.file_content = file_content
        self.progress = progress

    @classmethod
    def from_file(cls, filepath: str) -> IncrementalGenerator:
        """
        This function creates and returns an instance of the IncrementalGenerator class from the given file

        Args:
            filepath (str): The path to the file to create the object from

        Returns:
            An instance of the IncrementalGenerator class
        """

        with open(filepath, 'rb') as f:
            file_content = f.read()
        return cls(filepath, file_content)

    def get_bytes(self, n: int, update_progress=True):
        """
        Get the specified amount of next bytes

        Args:
            n (int): The number of bytes to get
            update_progress (bool): (Default: True) If set to False, the pointer for where to read the next set of bytes
            from won't be moved forward

        Returns:
            The specified number of bytes
        """
        if n <= 0:
            return b''
        result = self.file_content[self.progress:self.progress + n]
        if not result:
            raise EndOfFileError("End of file reached")
        if update_progress:
            self.progress += n
        return result

    def get_remaining_bytes(self):
        """
        Get all of the remaining bytes left

        Returns: bytes
        """
        result = self.file_content[self.progress:]
        self.progress = len(self.file_content) - 1
        return result

    def __repr__(self):
        return f"[IncrementalGenerator] Name: {self.name}\n\tProgress: {self.progress}/{len(self.file_content)}"
