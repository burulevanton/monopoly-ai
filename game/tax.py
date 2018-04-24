from game.field import Field

# класс, отвечающий за поле "Налог"


class Tax(Field):

    def __init__(self, name, location, cost):
        super().__init__(name, location)
        self.__cost = cost

    def landed_on(self, game, player):
        self.print_info(player)
        game.take_money_from_player(self.__cost)
        return False
