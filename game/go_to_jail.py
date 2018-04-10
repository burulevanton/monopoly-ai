from game.field import Field

# класс, отвечающий за поле "Отправляйся в тюрьму"


class GoToJail(Field):

    def __init__(self, name, location):
        super().__init__(name, location)

    def player_interaction(self, players, player_num, queue1, queue2, num_of_players):
        self.print_info(players, player_num)
        print("Игрок {} отправляется в тюрьму".format(players[player_num].name))
        print("Игрок {} платит 50".format(players[player_num].name))
        players[player_num].dec_balance(50)
        # переместить в тюрьму
