from game.player import Player


class SimpleAIPlayer(Player):

    def __init__(self, player_num):
        super().__init__('simple_ai№{}'.format(player_num), player_num)
        self.cash_reserve = 350
        self.min_cash = 150

    def landed_on_unowned_property(self, game, field):
        if self.balance - field.cost > self.cash_reserve:
            return True
        return False

    def property_offered_for_auction(self, game, field, price):
        if self.balance - price > self.cash_reserve:
            return True
        return False

    def build_house(self, game, field):
        if self.balance - field.cost_of_upgrade > self.cash_reserve:
            return True
        return False

    def sell_house(self, game, field):
        if self.balance < self.min_cash:
            return True
        return False

    def mortgage_property(self, game, field):
        if self.balance < self.min_cash and not field.has_house:
            return True
        return False

    def redeem_property(self, game, field):
        if self.balance - field.redeem_cost > self.cash_reserve:
            return True
        return False

    def get_out_of_jail(self, game):
        if self.balance - 50 > self.cash_reserve:
            return True
        return False
