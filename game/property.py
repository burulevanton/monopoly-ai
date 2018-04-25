from game.field import Field
from abc import ABCMeta, abstractmethod
import logging

# абстрактный класс, отвечающий за приобретаемые ячейки поля


class Property(Field):
    __metaclass__ = ABCMeta

    def __init__(self, name, location, cost):
        super().__init__(name, location)
        self.__cost = cost
        self.__owner = None
        self.__is_mortgage = False

    @property
    def cost(self):
        return self.__cost

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        self.__owner = value

    @property
    def is_mortgage(self):
        return self.__is_mortgage

    @is_mortgage.setter
    def is_mortgage(self, value):
        self.__is_mortgage = value

    @property
    def kind(self):
        return

    @property
    def redeem_cost(self):
        return int(self.cost//2*1.1)

    @property
    def current_value(self):
        return self.cost//2

    def landed_on(self, game, player):
        logger = logging.getLogger('landed_on')
        self.print_info(player)
        if self.owner == player:
            logger.info("Игрок {} отдыхает".format(player.name))
        if not self.owner:
            game.offer_property_to_buy(player, self)
        elif self.owner != player and not self.is_mortgage:
            rent = self.get_rent(player) if self.kind == 'utility' else self.get_rent()
            if game.transfer_money_between_players(from_player=player, to_player=self.owner, amount=rent):
                logger.info("Игрок {} платит {} за аренду владельцу(игроку {})".format(player.name, rent,
                                                                                       self.owner.name))
        return False

    def mortgage(self):
        self.is_mortgage = True
        return self.cost//2

    def redeem(self):
        self.is_mortgage = False

    @abstractmethod
    def get_rent(self, *args):
        pass

    @abstractmethod
    def ask_player(self, player):
        pass

    @abstractmethod
    def print_info_about_field(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass
