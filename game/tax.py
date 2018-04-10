from game.field import Field

# класс, отвечающий за поле "Налог"


class Tax(Field):

    def __init__(self, name, location, cost):
        super().__init__(name, location)
        self.__cost = cost

    def player_interaction(self, players, player_num, queue1, queue2, num_of_players):
        self.print_info(players, player_num)
        print("Игрок {} платит [}".format(players[player_num].name, self.__cost))
        players[player_num].dec_balance(self.__cost)

