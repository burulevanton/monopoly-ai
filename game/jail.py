from game.field import Field

# класс, отвечающий за поле "Тюрьма"


class Jail(Field):

    def __init__(self, name, location):
        super().__init__(name, location)

    def player_interaction(self, player):
        self.print_info(player)
        print("Игрок {} просто посетил".format(player.name))
        return False
