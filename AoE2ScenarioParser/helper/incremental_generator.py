from __future__ import annotations
from AoE2ScenarioParser.helper.exceptions import EndOfFileError


class IncrementalGenerator:
    """
    This class is similar to an actual generator and is used to return the bytes of a file sequentially
    """
    def __init__(self, name: str, file_content: bytes, progress: int = 0):
        """
        Args:
            name (str): The full file path of the file to create the generator for
            file_content (bytes): The bytes of the specified file
            progress (int): Keeps track of how many bytes have been read from the generator
        """
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

    def get_bytes(self, n: int, update_progress: bool=True) -> bytes:
        """
        Get the specified amount of next bytes

        Args:
            n (int): The number of bytes to get
            update_progress (bool): (Default: True) If set to False, the pointer for where to read the next set of bytes
            from won't be moved forward

        Returns:
            The specified number of bytes

        Raises:
            EndOfFileError: if the number of bytes requested is greater than the number of remaining bytes in the
                generator
        """
        if n <= 0:
            return b''
        result = self.file_content[self.progress:self.progress + n]
        if not result:
            raise EndOfFileError("End of file reached")
        if update_progress:
            self.progress += n
        return result

    def get_remaining_bytes(self) -> bytes:
        """
        Get all of the remaining bytes in the generator

        Returns:
            The remaining bytes of the generator
        """
        result = self.file_content[self.progress:]
        self.progress = len(self.file_content) - 1
        return result

    def __repr__(self):
        return f"[IncrementalGenerator] Name: {self.name}\n\tProgress: {self.progress}/{len(self.file_content)}"
