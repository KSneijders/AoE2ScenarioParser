from __future__ import annotations

from AoE2ScenarioParser.exceptions.asp_exceptions import EndOfFileError


class IncrementalGenerator:
    """Similar to an actual generator and is used to return the bytes of a file sequentially"""
    def __init__(self, name: str, file_content: bytes, progress: int = 0):
        """
        Args:
            name: The full file path of the file to create the generator for
            file_content: The bytes of the specified file
            progress: Keeps track of how many bytes have been read from the generator.
        """
        self.name = name
        self.file_content: bytes = file_content
        self.progress = progress

    @classmethod
    def from_file(cls, filepath: str) -> IncrementalGenerator:
        """
        Creates and returns an instance of the IncrementalGenerator class from the given file

        Args:
            filepath: The path to the file to create the object from

        Returns:
            An instance of the IncrementalGenerator class
        """
        with open(filepath, 'rb') as f:
            file_content = f.read()
        return cls(filepath, file_content)

    def get_bytes(self, n: int, update_progress: bool = True) -> bytes:
        """
        Get the specified amount of next bytes

        Args:
            n: The number of bytes to get
            update_progress: If set to False, the counter for where to read the next set of bytes from won't be
                increased

        Returns:
            The specified number of bytes

        Raises:
            EndOfFileError: When the number of bytes requested is greater than the number of remaining bytes in the
                generator
        """
        if n <= 0:
            return b''
        result = self.file_content[self.progress:self.progress + n]
        if not result or len(result) != n:
            remaining = self.get_amount_of_remaining_bytes()
            raise EndOfFileError(f"End of file reached. (Requested: {n} bytes, only {remaining} left.")
        if update_progress:
            self.progress += n
        return result

    def get_remaining_bytes(self) -> bytes:
        """
        Get all the remaining bytes in the generator

        Returns:
            The remaining bytes in the generator
        """
        result = self.file_content[self.progress:]
        self.progress = len(self.file_content) - 1
        return result

    def get_amount_of_remaining_bytes(self) -> int:
        """
        Get the amount of remaining bytes in the generator

        Returns:
            The the amount of remaining bytes in the generator
        """
        return len(self.file_content) - self.progress

    def __repr__(self):
        return f"[IncrementalGenerator] Name: {self.name}\n\tProgress: {self.progress}/{len(self.file_content)}"
