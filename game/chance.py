from game.field import Field
import random
import logging

# поле "Шанс"


class Chance(Field):

    def __init__(self, location):
        super().__init__("Шанс", location)

    def landed_on(self, game, player):
        logger = logging.getLogger('landed_on')
        self.print_info(player)
        num_card = random.randint(1, 14)
        ("Игрок берёт карточку №{}".format(num_card))
        if num_card == 1:
            logger.info('Отправляйтесь на Арбат')
            player.location = 39
            return True
        elif num_card == 2:
            logger.info('Отправляйтесь на поле Полянка')
            if player.location == 7:
                player.location = 11
            else:
                logger.info("Игрок {} проходит поле Вперёд и получает 200".format(player.name))
                player.location = 11
                game.give_money_to_player(player, 200)
            return True
        elif num_card == 3 or num_card == 8:
            logger.info('Отправляйтесь на ближайщую станцию')
            if player.location == 7:
                player.location = 15
            if player.location == 22:
                player.location = 25
            if player.location == 36:
                logger.info("Игрок {} проходит поле Вперёд и получает 200".format(player.name))
                player.location = 5
                game.give_money_to_player(player, 200)
            return True
        elif num_card == 4:
            logger.info('Банк платит вам 50')
            game.give_money_to_player(player, 200)
            return False
        elif num_card == 5:
            logger.info('Идите на ближайшее поле коммунального предприятия')
            if player.location == 7:
                player.location = 12
            if player.location == 22:
                player.location = 28
            if player.location == 36:
                player.location = 12
                logger.info("Игрок {} проходит поле Вперёд и получает 200".format(player.name))
                game.give_money_to_player(player, 200)
            return True
        elif num_card == 6:
            logger.info('Отправляйтесь в тюрьму')
            game.send_player_to_jail(player)
            return False
        elif num_card == 7:
            logger.info('Отправляйтесь поездом до станции Римская Железная дорога')
            player.location = 5
            logger.info("Игрок {} проходит поле Вперёд и получает 200".format(player.name))
            game.give_money_to_player(player, 200)
            return True
        elif num_card == 9:
            logger.info('Штраф 15')
            game.take_money_from_player(player, 15)
            return False
        elif num_card == 10:
            logger.info('Отправляйтесь на бесплатную стоянку')
            if player.location == 7:
                player.location = 20
            else:
                logger.info("Игрок {} проходит поле Вперёд и получает 200".format(player.name))
                player.location = 20
                game.give_money_to_player(player, 200)
            return True
        elif num_card == 11:
            logger.info('Получите 150')
            game.give_money_to_player(player, 150)
        elif num_card == 12:
            logger.info('Отправляйтесь на площадь Маяковского')
            if player.location == 7 or player.location == 22:
                player.location = 24
            else:
                player.location = 24
                logger.info("Игрок {} проходит поле Вперёд и получает 200".format(player.name))
                game.give_money_to_player(player, 200)
            return True
        elif num_card == 13:
            logger.info('Вернитесь на три поля назад')
            player.location = player.location - 3
            return True
        elif num_card == 14:
            logger.info('Идите на поле Вперёд')
            player.location = 0
            game.give_money_to_player(player, 200)
            logger.info("Игрок {} проходит поле Вперёд и получает 200".format(player.name))
            return True
