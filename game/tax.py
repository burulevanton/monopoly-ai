from game.field import Field

# класс, отвечающий за поле "Налог"


class Tax(Field):

    def __init__(self, name, location, cost):
        super().__init__(name, location)
        self.__cost = cost

    def player_interaction(self, player):
        self.print_info(player)
        print("Игрок {} платит {}".format(player.name, self.__cost))
        player.dec_balance(self.__cost)
