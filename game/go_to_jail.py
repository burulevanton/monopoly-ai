from game.field import Field
import logging

# класс, отвечающий за поле "Отправляйся в тюрьму"


class GoToJail(Field):

    def __init__(self, name, location):
        super().__init__(name, location)

    def landed_on(self, game, player):
        logger = logging.getLogger('landed_on')
        self.print_info(player)
        logger.info("Игрок {} отправляется в тюрьму".format(player.name))
        game.send_player_to_jail(player)
        return False
