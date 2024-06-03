from abc import ABC, abstractmethod


class ISource(ABC):

    @abstractmethod
    def get_char(self):
        """Reads a character from the source"""


class StringReader(ISource):
    """Reads characters one by one from a string"""

    def __init__(self, string_to_read: str) -> None:
        self._string_to_read = iter(string_to_read)

    def get_char(self) -> str:
        return next(self._string_to_read, "\n")
