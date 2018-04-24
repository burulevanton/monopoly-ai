from game.field import Field

# класс, отвечающий за поле "Отправляйся в тюрьму"


class GoToJail(Field):

    def __init__(self, name, location):
        super().__init__(name, location)

    def landed_on(self, game, player):
        self.print_info(player)
        print("Игрок {} отправляется в тюрьму".format(player.name))
        print("Игрок {} платит 50".format(player.name))
        game.take_money_from_player(player, 50)
        player.location = 10
        return True
