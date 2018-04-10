from game.field import Field

# класс, отвечающий за поле "Тюрьма"


class Jail(Field):

    def __init__(self, name, location):
        super().__init__(name, location)

    def player_interaction(self, players, player_num, queue1, queue2, num_of_players):
        self.print_info(players, player_num)
        print("Игрок {} просто посетил".format(players[player_num].name))
