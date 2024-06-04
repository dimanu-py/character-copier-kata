from abc import ABC, abstractmethod


class IDestination(ABC):

    @abstractmethod
    def set_char(self, char):
        """Writes a character to the destination"""


class ListDestination(IDestination):
    """Writes characters to a list"""

    def __init__(self):
        self._chars = []

    def set_char(self, char: str) -> None:
        self._chars.append(char)
