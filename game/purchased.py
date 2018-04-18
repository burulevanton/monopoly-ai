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
    def start_rent(self):
        return self.__rent

    @property
    def rent(self):
        return

    @property
    def is_mortgage(self):
        return self.__is_mortgage

    @is_mortgage.setter
    def is_mortgage(self, value):
        self.__is_mortgage = value

    @property
    def kind(self):
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
        elif self.owner != player and not self.is_mortgage:
            self.__owner.add_balance(self.rent)
            player.dec_balance(self.rent)
            print("Игрок {} платит {} за аренду владельцу(игроку {})".format(player.name, self.rent, self.owner.name))
        return False

    def mortgage(self):
        self.is_mortgage = True
        self.owner.add_balance(self.cost//2)

    def redeem(self):
        self.is_mortgage = False
        self.owner.dec_balance(int(self.cost//2*1.1))

    @abstractmethod
    def ask_player(self, player):
        pass

    @abstractmethod
    def print_info_about_field(self):
        pass
