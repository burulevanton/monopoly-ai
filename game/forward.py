from game.field import Field

# поле "Вперёд"(начальное поле)


class Forward(Field):

    def __init__(self, name, location):
        super().__init__(name, location)

    def player_interaction(self, player):
        self.print_info(player)
