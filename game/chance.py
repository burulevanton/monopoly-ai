from game.field import Field
import random

# поле "Шанс"


class Chance(Field):

    def __init__(self, name, location):
        super().__init__(name, location)

    def player_interaction(self, player):
        self.print_info(player)
        num_card = random.randint(1, 14)
        print("Игрок берёт карточку №{}".format(num_card))
