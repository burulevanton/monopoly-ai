from game.field import Field
from abc import ABCMeta, abstractmethod

# абстрактный класс, отвечающий за приобретаемые ячейки поля


class Purchased(Field):
    __metaclass__ = ABCMeta

    def __init__(self, name, location, cost, rent):
        super().__init__(name, location)
        self.__cost = cost
        self.__rent = rent
        self.__owner = None

    @property
    def cost(self):
        return self.__cost

    @property
    def owner(self):
        return self.__owner

    @property
    def start_rent(self):
        return self.__rent

    @property
    def rent(self):
        return

    def player_interaction(self, player):
        self.print_info(player)
        if self.owner == player:
            print("Игрок {} отдыхает".format(player.name))
        if not self.owner:
            answer = self.ask_player(player)
            if answer == 1:
                player.dec_balance(self.cost)
                print("Игрок {} покупает поле {} за {}".format(player.name, self.name, self.cost))
                self.__owner = player
                player.own_field(self)
            else:
                return
        elif self.owner != player:
            self.__owner.add_balance(self.rent)
            player.dec_balance(self.rent)
            print("Игрок {} платит {} за аренду".format(player.name, self.rent))

    @abstractmethod
    def ask_player(self, player):
        pass

    @abstractmethod
    def print_info_about_field(self):
        pass
