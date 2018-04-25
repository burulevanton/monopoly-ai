from game.field import Field
import logging

# класс, отвечающий за поле "Бесплатная стоянка"


class FreeParking(Field):

    def __init__(self, name, location):
        super().__init__(name, location)

    def landed_on(self, game, player):
        logger = logging.getLogger('landed_on')
        self.print_info(player)
        logger.info("Игрок {} отдыхает".format(player.name))
        return False
