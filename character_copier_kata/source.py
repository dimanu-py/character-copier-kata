from abc import ABC, abstractmethod


class ISource(ABC):

    @abstractmethod
    def get_char(self):
        """Reads a character from the source"""
