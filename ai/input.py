from game.player import Player
import logging


class RealPlayer(Player):

    def __init__(self, player_num):

        super().__init__('real_player№{}'.format(player_num), player_num)

    def landed_on_unowned_property(self, game, field):
        logging.info('Купить {}'.format(field))
        return bool(int(input()))

    def property_offered_for_auction(self, game, field):
        logging.info('Купить на аукционе{}'.format(field))
        return bool(int(input()))

    def build_house(self, game, field):
        logging.info('Построить дом {}'.format(field))
        return bool(int(input()))

    def sell_house(self, game, field):
        logging.info('Продать дом {}'.format(field))
        return bool(int(input()))

    def mortgage_property(self, game, field):
        logging.info('Заложить {}'.format(field))
        return bool(int(input()))

    def redeem_property(self, game, field):
        logging.info('Выкупить {}'.format(field))
        return bool(int(input()))

    def get_out_of_jail(self, game):
        logging.info('Выйти из тюрьмы')
        return bool(int(input()))
