from game.field import Field

# класс, отвечающий за поле "Отправляйся в тюрьму"


class GoToJail(Field):

    def __init__(self, name, location):
        super().__init__(name, location)

    def player_interaction(self, player):
        self.print_info(player)
        print("Игрок {} отправляется в тюрьму".format(player.name))
        print("Игрок {} платит 50".format(player.name))
        player.dec_balance(50)
        player.location = 10
