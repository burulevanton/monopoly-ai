from abc import ABCMeta, abstractmethod
from game.player import Player

# абстрактный класс, обозначающий одну ячейку на поле


class Field:
    __metaclass__ = ABCMeta

    def __init__(self, name, location):
        self.__name = name
        self.__location = location

    def print_info(self, player: Player):
        print("Игрок {} попал на поле {}".format(player.name, self.name))

    @abstractmethod
    def player_interaction(self, player):
        pass

    @property
    def name(self):
        return self.__name

    @property
    def location(self):
        return self.__location
