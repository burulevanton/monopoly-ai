from abc import ABCMeta, abstractmethod

# абстрактный класс, обозначающий одну ячейку на поле


class Field:
    __metaclass__ = ABCMeta

    def __init__(self, name, location):
        self.__name = name
        self.__location = location

    def print_info(self, players, player_num):
        print("Игрок {} попал на поле {}".format(players[player_num].name, self.name))

    @abstractmethod
    def player_interaction(self, players, player_num, queue1, queue2, num_of_players):
        pass

    @property
    def name(self):
        return self.__name

    @property
    def location(self):
        return self.__location
