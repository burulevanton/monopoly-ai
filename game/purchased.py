from game.field import Field
from abc import ABCMeta, abstractmethod

# абстрактный класс, отвечающий за приобретаемые ячейки поля


class Purchased(Field):
    __metaclass__ = ABCMeta

    def __init__(self, name, location, cost, rent):
        super().__init__(name, location)
        self.__cost = cost
        self.__rent = rent
        self.__owner = -1

    @property
    def cost(self):
        return self.__cost

    @property
    def owner(self):
        return self.__owner

    @property
    def rent(self):
        return self.__rent

    def player_interaction(self, players, player_num, queue1, queue2, num_of_players):
        self.print_info(players, player_num)
        if self.owner == player_num:
            print("Игрок {} отдыхает".format(players[player_num].name))
        if self.owner < 0:
            answer = self.ask_player(players, player_num)
            if answer == 1:
                players[player_num].dec_balance(self.cost)
                print("Игрок {} покупает поле {} за {}".format(players[player_num].name, self.name, self.cost))
                self.__owner = player_num
            else:
                return
        elif self.owner != player_num:
            players[self.owner].add_balance(self.rent)
            players[player_num].dec_balance(self.rent)
            print("Игрок {} платит {} за аренду".format(players[player_num].name, self.rent))

    @abstractmethod
    def ask_player(self, players, player_num):
        pass

    @abstractmethod
    def print_info_about_field(self, players, player_num):
        pass



