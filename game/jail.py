from game.field import Field
import logging

# класс, отвечающий за поле "Тюрьма"


class Jail(Field):

    def __init__(self, name, location):
        super().__init__(name, location)

    def landed_on(self, game, player):
        logger = logging.getLogger('landed_on')
        if player.in_jail:
            logger.info('Игрок {} находится в тюрьме'.format(player))
        else:
            self.print_info(player)
            logger.info("Игрок {} просто посетил".format(player))
        return False
