from game.field import Field
from game.player import Player

# класс, отвечающий за поле "Бесплатная стоянка"


class FreeParking(Field):

    def __init__(self, name, location):
        super().__init__(name, location)

    def player_interaction(self, player: Player):
        self.print_info(player)
        print("Игрок {} отдыхает".format(player.name))
