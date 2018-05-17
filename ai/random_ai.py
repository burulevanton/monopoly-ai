from game.player import Player
import random


class RandomAIPlayer(Player):

    def __init__(self, player_num):

        super().__init__('random_ai№{}'.format(player_num), player_num)

    def landed_on_unowned_property(self, game, field):
        return bool(random.randint(0, 1))

    def property_offered_for_auction(self, game, field, price):
        return bool(random.randint(0, 1))

    def build_house(self, game, field):
        return bool(random.randint(0, 1))

    def sell_house(self, game, field):
        return bool(random.randint(0, 1))

    def mortgage_property(self, game, field):
        return bool(random.randint(0, 1))

    def redeem_property(self, game, field):
        return bool(random.randint(0, 1))

    def get_out_of_jail(self, game):
        return bool(random.randint(0, 1))
