from game.field import Field

# класс, отвечающий за поле "Тюрьма"


class Jail(Field):

    def __init__(self, name, location):
        super().__init__(name, location)

    def landed_on(self, game, player):
        self.print_info(player)
        print("Игрок {} просто посетил".format(player.name))
        return False
