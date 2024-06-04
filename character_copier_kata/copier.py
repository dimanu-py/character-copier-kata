from character_copier_kata.destination import IDestination
from character_copier_kata.source import ISource


class Copier:

    def __init__(self, source: ISource, destination: IDestination) -> None:
        self.source = source
        self.destination = destination

    def copy_character(self) -> None:
        next_char = self.source.get_char()
        while next_char != "\n":
            self.destination.set_char(next_char)
            next_char = self.source.get_char()
