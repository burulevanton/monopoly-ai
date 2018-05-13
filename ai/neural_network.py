from game.player import Player
import random
import copy


class NeuralNetworkPLayer(Player):

    def __init__(self, player_num):

        super().__init__('neural_network_player№{}'.format(player_num), player_num)

    def landed_on_unowned_property(self, game, field):
        game1 = copy.deepcopy(game)
        player = copy.deepcopy(self)
        field1 = copy.deepcopy(field)
        game1.give_property_to_player(player, field1)
        return 0
        #return bool(random.randint(0, 1))

    def property_offered_for_auction(self, game, field):
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
