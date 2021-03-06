from abc import ABCMeta, abstractmethod
import logging

# абстрактный класс, обозначающий одну ячейку на поле


class Field:
    __metaclass__ = ABCMeta

    def __init__(self, name, location):
        self.__name = name
        self.__location = location

    def print_info(self, player):
        logger = logging.getLogger('print_info')
        logger.info("Игрок {} попал на поле {}".format(player.name, self.name))

    @abstractmethod
    def landed_on(self, game, player):
        pass

    @property
    def name(self):
        return self.__name

    @property
    def location(self):
        return self.__location

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return 'Поле {}'.format(self.name)
