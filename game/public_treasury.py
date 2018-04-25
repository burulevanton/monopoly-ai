from game.field import Field
import random
import logging
# класс, отвечающий за поле Общественная казна


class PublicTreasury(Field):

    def __init__(self, location):
        super().__init__("Общественная казна", location)

    def landed_on(self, game, player):
        logger = logging.getLogger('landed_on')
        self.print_info(player)
        num_card = random.randint(1, 14)
        logger.info("Игрок {} берёт карточку №{}".format(player.name, num_card))
        if num_card == 1:
            logger.info('Отправляйтесь в тюрьму')
            game.send_player_to_jail(player)
        elif num_card == 2:
            logger.info('Идите на поле Вперёд')
            player.location = 0
            logger.info("Игрок {} проходит поле Вперёд".format(player.name))
            game.give_money_to_player(player, 200)
        elif num_card == 3:
            logger.info('Заплатите 50')
            game.take_money_from_player(player, 50)
        elif num_card == 4:
            logger.info('Получите 10')
            game.give_money_to_player(player, 10)
        elif num_card == 5:
            logger.info('Вы заработали 50')
            game.give_money_to_player(player, 50)
        elif num_card == 6:
            logger.info('Получите 200')
            game.give_money_to_player(player, 200)
        elif num_card == 7:
            logger.info('Заплатите 100')
            game.take_money_from_player(player, 100)
        elif num_card == 8:
            logger.info('Получите 100')
            game.give_money_to_player(player, 100)
        elif num_card == 9:
            logger.info('Отправляйтесь на бесплатную стоянку')
            if not player.location == 2 or player.location == 17:
                logger.info("Игрок {} проходит поле Вперёд".format(player.name))
                game.give_money_to_player(player, 200)
            player.location = 20
            return True
        elif num_card == 10:
            logger.info('Получите 20')
            game.give_money_to_player(player, 20)
        elif num_card == 11 or num_card == 13:
            logger.info('Вы получаете 100')
            game.give_money_to_player(player, 100)
        elif num_card == 12:
            logger.info('Заплатите 50')
            game.take_money_from_player(player, 50)
        elif num_card == 14:
            logger.info('Получите 25')
            game.give_money_to_player(player, 25)
        return False
