from AoE2ScenarioParser.exceptions.asp_exceptions import EndOfFileError


class IncrementalGenerator:
    def __init__(self, name, file_content, progress=0):
        self.name = name
        self.file_content: bytes = file_content
        self.progress = progress

    @classmethod
    def from_file(cls, filepath: str):
        with open(filepath, 'rb') as f:
            file_content = f.read()
        return cls(filepath, file_content)

    def get_bytes(self, n: int, update_progress=True):
        if n <= 0:
            return b''
        result = self.file_content[self.progress:self.progress + n]
        if not result:
            raise EndOfFileError("End of file reached")
        if update_progress:
            self.progress += n
        return result

    def get_remaining_bytes(self):
        result = self.file_content[self.progress:]
        self.progress = len(self.file_content) - 1
        return result

    def __repr__(self):
        return f"[IncrementalGenerator] Name: {self.name}\n\tProgress: {self.progress}/{len(self.file_content)}"
