from game.field import Field

# поле "Вперёд"(начальное поле)


class Forward(Field):

    def __init__(self, name, location):
        super().__init__(name, location)

    def landed_on(self, game, player):
        self.print_info(player)
        return False
