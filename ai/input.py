from game.player import Player
from ai.neural_network import NeuralNetworkPLayer
import logging


class RealPlayer(Player):

    def __init__(self, player_num):

        super().__init__('real_player№{}'.format(player_num), player_num)
        self.neural_network = NeuralNetworkPLayer(0, do_train=False)

    def landed_on_unowned_property(self, game, field):
        logging.info('Купить {}?'.format(field))
        print(game.calculate_reward(self))
        state = self.neural_network.env.buy_property_state(game, self, field, field.cost)
        print(self.neural_network.model.predict(state))
        return bool(int(input()))

    def property_offered_for_auction(self, game, field, price):
        logging.info('Купить на аукционе {} за {}Р?'.format(field, price))
        print(game.calculate_reward(self))
        state = self.neural_network.env.buy_property_state(game, self, field, price)
        print(self.neural_network.model.predict(state))
        return bool(int(input()))

    def build_house(self, game, field):
        logging.info('Построить дом {}?'.format(field))
        print(game.calculate_reward(self))
        state = self.neural_network.env.build_house_state(game, self, field)
        print(self.neural_network.model.predict(state))
        return bool(int(input()))

    def sell_house(self, game, field):
        logging.info('Продать дом {}?'.format(field))
        print(game.calculate_reward(self))
        state = self.neural_network.env.sell_house_state(game, self, field)
        print(self.neural_network.model.predict(state))
        return bool(int(input()))

    def mortgage_property(self, game, field):
        logging.info('Заложить {}?'.format(field))
        print(game.calculate_reward(self))
        state = self.neural_network.env.mortgage_property_state(game, self, field)
        print(self.neural_network.model.predict(state))
        return bool(int(input()))

    def redeem_property(self, game, field):
        logging.info('Выкупить {}?'.format(field))
        print(game.calculate_reward(self))
        state = self.neural_network.env.redeem_property_state(game, self, field)
        print(self.neural_network.model.predict(state))
        return bool(int(input()))

    def get_out_of_jail(self, game):
        logging.info('Выйти из тюрьмы?')
        return bool(int(input()))
