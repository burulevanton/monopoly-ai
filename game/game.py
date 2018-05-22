# основная логика игры
from game.chance import Chance
from game.forward import Forward
from game.free_parking import FreeParking
from game.go_to_jail import GoToJail
from game.jail import Jail
from game.player import Player
from game.street import Street
from game.public_treasury import PublicTreasury
from game.railway import Railway
from game.tax import Tax
from game.utility import Utility
from ai.random_ai import RandomAIPlayer
from ai.input import RealPlayer
from ai.neural_network import NeuralNetworkPLayer
from ai.simple_ai import SimpleAIPlayer
import logging
import random
import math

# logging.basicConfig(format=u'%(filename)s[%(lineno)d]# [%(name)s] [%(asctime)s]  %(message)s',
#                     level=logging.DEBUG)
logging.basicConfig(format=u'%(message)s',
                    level=logging.INFO)

class Game:

    class GameState:

        streets_index = ['brown', 'blue', 'pink', 'orange', 'red', 'yellow', 'green', 'dark_blue']
        other_property_index = ['utility', 'railway']
        num_of_other_properties = {
            'utility': 2,
            'railway': 4
        }

        def __init__(self):
            self.area_player = []
            self.area_other_player = []
            self.finance = []
            self.action_state = []

    def __init__(self):
        self.__board = []
        self.__players = []
        self.__bankrupt_players = []
        self.__numOfPlayers = 0
        self.__current_roll = 0
        self.__double_in_a_row = 0
        self.__rounds_played = 0
        #self.set_num_of_players()
        self.init_game_board()
        self.set_players()

    def restart_game(self):
        self.__board.clear()
        self.init_game_board()
        for player in self.__bankrupt_players:
            self.__players.append(player)
        self.__bankrupt_players.clear()
        self.__current_roll = 0
        self.__double_in_a_row = 0
        self.__rounds_played = 0
        for player in self.__players:
            player.start_game()

    @property
    def current_roll(self):
        return self.__current_roll

    @staticmethod
    def num_field_color(color):
        if color in ['brown', 'dark_blue']:
            return 2
        elif color in ['blue', 'pink', 'orange', 'red', 'yellow', 'green']:
            return 3
        else:
            return -1

    def available_color_to_upgrade(self, num_owned_field: dict, mortgage_fields: dict):
        available_colors = []
        for key in num_owned_field.keys():
            if len(num_owned_field[key]) == self.num_field_color(key) and key not in mortgage_fields:
                available_colors.append(key)
        return available_colors

    def init_game_board(self):
        self.__board.append(Forward(name="Вперёд",
                                    location=0))
        self.__board.append(Street(name="ул.Житная",
                                        location=1,
                                        cost=60,
                                        rents=[2, 10, 30, 90, 160],
                                        cost_of_upgrade=50,
                                        color="brown"))
        self.__board.append(PublicTreasury(location=2))
        self.__board.append(Street(name="ул. Нагатинская",
                                        location=3,
                                        cost=60,
                                        rents=[4, 20, 60, 180, 320],
                                        cost_of_upgrade=50,
                                        color="brown"))
        self.__board.append(Tax(name="Налог",
                                location=4,
                                cost=200))
        self.__board.append(Railway(name="Римская железная дорога",
                                    location=5,
                                    cost=200))
        self.__board.append(Street(name="Варшавское шоссе",
                                        location=6,
                                        cost=100,
                                        rents=[6, 30, 90, 270, 400],
                                        cost_of_upgrade=50,
                                        color="blue"))
        self.__board.append(Chance(location=7))
        self.__board.append(Street(name="ул. Огарева",
                                        location=8,
                                        cost=100,
                                        rents=[6, 30, 90, 270, 400],
                                        cost_of_upgrade=50,
                                        color="blue"))
        self.__board.append(Street(name="ул. Первая парковая",
                                        location=9,
                                        cost=120,
                                        rents=[8, 40, 100, 300, 450],
                                        cost_of_upgrade=50,
                                        color="blue"))
        self.__board.append(Jail(name="Тюрьма",
                                 location=10))
        self.__board.append(Street(name="ул. Полянка",
                                        location=11,
                                        cost=140,
                                        rents=[10, 50, 150, 450, 625],
                                        cost_of_upgrade=100,
                                        color="pink"))
        self.__board.append(Utility(name="Электроэнергия",
                                    location=12,
                                    cost=150))
        self.__board.append(Street(name="ул. Сретенка",
                                        location=13,
                                        cost=140,
                                        rents=[10, 50, 150, 450, 625],
                                        cost_of_upgrade=100,
                                        color="pink"))
        self.__board.append(Street(name="Ростовская набережная",
                                        location=14,
                                        cost=160,
                                        rents=[12, 60, 180, 500, 700],
                                        cost_of_upgrade=100,
                                        color="pink"))
        self.__board.append(Railway(name="Курская железная дорога",
                                    location=15,
                                    cost=200))
        self.__board.append(Street(name="Рязанский проспект",
                                        location=16,
                                        cost=180,
                                        rents=[14, 70, 200, 550, 750],
                                        cost_of_upgrade=100,
                                        color='orange'))
        self.__board.append(PublicTreasury(location=17))
        self.__board.append(Street(name="ул. Вавилова",
                                        location=18,
                                        cost=180,
                                        rents=[14, 70, 200, 550, 750],
                                        cost_of_upgrade=100,
                                        color='orange'))
        self.__board.append(Street(name="Рублёвское шоссе",
                                        location=19,
                                        cost=200,
                                        rents=[16, 80, 220, 600, 800],
                                        cost_of_upgrade=100,
                                        color='orange'))
        self.__board.append(FreeParking(name="Бесплатная стоянка",
                                        location=20))
        self.__board.append(Street(name="ул. Тверская",
                                        location=21,
                                        cost=220,
                                        rents=[18, 90, 250, 700, 875],
                                        cost_of_upgrade=150,
                                        color='red'))
        self.__board.append(Chance(location=22))
        self.__board.append(Street(name="ул. Пушкинская",
                                        location=23,
                                        cost=220,
                                        rents=[18, 90, 250, 700, 875],
                                        cost_of_upgrade=150,
                                        color='red'))
        self.__board.append(Street(name="Площадь Маяковского",
                                        location=24,
                                        cost=240,
                                        rents=[20, 100, 300, 750, 925],
                                        cost_of_upgrade=150,
                                        color='red'))
        self.__board.append(Railway(name="Казанская железная дорога",
                                    location=25,
                                    cost=200))
        self.__board.append(Street(name="ул. Грузинский вал",
                                        location=26,
                                        cost=260,
                                        rents=[22, 110, 330, 800, 975],
                                        cost_of_upgrade=150,
                                        color='yellow'))
        self.__board.append(Street(name="ул. Чайковского",
                                        location=27,
                                        cost=260,
                                        rents=[22, 110, 330, 800, 975],
                                        cost_of_upgrade=150,
                                        color='yellow'))
        self.__board.append(Utility(name="Водопровод",
                                    location=28,
                                    cost=150))
        self.__board.append(Street(name='Смоленская площадь',
                                        location=29,
                                        cost=280,
                                        rents=[24, 120, 360, 850, 1025],
                                        cost_of_upgrade=150,
                                        color='yellow'))
        self.__board.append(GoToJail(name="Отправляйтесь в тюрьму",
                                     location=30))
        self.__board.append(Street(name='ул. Щусева',
                                        location=31,
                                        cost=300,
                                        rents=[26, 130, 390, 900, 1100],
                                        cost_of_upgrade=200,
                                        color='green'))
        self.__board.append(Street(name="Гоголевский бульвар",
                                        location=32,
                                        cost=300,
                                        rents=[26, 130, 390, 900, 1100],
                                        cost_of_upgrade=200,
                                        color='green'))
        self.__board.append(PublicTreasury(location=33))
        self.__board.append(Street(name="Кутузовский проспект",
                                        location=34,
                                        cost=320,
                                        rents=[28, 150, 450, 1000, 1200],
                                        cost_of_upgrade=200,
                                        color='green'))
        self.__board.append(Railway(name="Ленинградская железная дорога",
                                    location=35,
                                    cost=200))
        self.__board.append(Chance(location=36))
        self.__board.append(Street(name="ул. Малая Бронная",
                                        location=37,
                                        cost=350,
                                        rents=[35, 175, 500, 1100, 1300],
                                        cost_of_upgrade=200,
                                        color='dark_blue'))
        self.__board.append(Tax(name="Сверхналог",
                                location=38,
                                cost=100))
        self.__board.append(Street(name="ул. Арбат",
                                        location=39,
                                        cost=400,
                                        rents=[50, 200, 600, 1400, 1700],
                                        cost_of_upgrade=200,
                                        color='dark_blue'))

    def set_num_of_players(self):
        print("Введите количество игроков:")
        self.__numOfPlayers = int(input())

    def set_players(self):
        self.__players.append(NeuralNetworkPLayer(0))
        self.__players.append(SimpleAIPlayer(1))
        #self.__players.append(RandomAIPlayer(2))
        # self.give_property_to_player(self.__players[0], self.__board[5])
        # self.__players[0].balance -= 1250
        # self.give_property_to_player(self.__players[1], self.__board[37])
        # self.give_property_to_player(self.__players[1], self.__board[39])
        # self.__players[0].location = 39
        # self.__board[39].landed_on(self, self.__players[0])
        # self.__players[1].balance += 1312312312
        # self.__players[2].balance += 13231231231
        # for i in range(self.__numOfPlayers):
        #     print("Введите имя игрока №{}".format(i+1))
        #     name = input()
        #     self.__players.append(Player(name, i))

    def play_game(self):
        logger = logging.getLogger('play_game')
        winners = [0, 0, 0]
        mean_winners = []
        full_rounds = 0
        k = -1
        for i in range(1000):
            while self.game_in_progress:
                for player in self.__players:
                    if self.game_in_progress:
                        logger.info('Ход игрока {}'.format(player))
                        self.log_info_about_player(player)
                        self.ask_upgrade(player)
                        self.ask_redeem(player)
                        self.ask_mortgage(player)
                        self.ask_sell(player)
                        self.play_round(player)
                self.info_about_players()
                self.__rounds_played += 1
            logger.info('Игра окончена')
            winner = self.announce_winner()
            full_rounds += self.__rounds_played
            for player in self.__players:
                if not player == winner:
                    self.delete_player(player)
            if i % 100 == 0:
                print(mean_winners)
                mean_winners.append([0, 0, 0])
                k += 1
            winners[winner.num] += 1
            mean_winners[k][winner.num] += 1
            print(winners)
            self.restart_game()
            for player in self.__players:
                if isinstance(player, NeuralNetworkPLayer):
                    player.replay()
                    player.model.save_weights("weights.h5", overwrite=True)
        print(full_rounds/1000)
        print(mean_winners)

    def play_round(self, player):
        if player in self.__players and self.game_in_progress:
            is_double = self.roll_dice_and_move(player)
            if self.__board[player.location].landed_on(self, player):
                self.__board[player.location].landed_on(self, player)
            self.check_fill_color(player)
            if is_double:
                self.__double_in_a_row += 1
                if self.__double_in_a_row == 3:
                    self.send_player_to_jail(player)
                else:
                    self.play_round(player)
            self.__double_in_a_row = 0

    def roll_dice_and_move(self, player: Player):
        logger = logging.getLogger('roll_dice_and_move')
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        logger.info("Игрок {} выбрасывает {} и {}".format(player, roll1, roll2))
        self.__current_roll = roll1 + roll2
        is_double = (roll1 == roll2)
        if player.in_jail:
            if not is_double and player.turns_in_jail == 3:
                self.take_money_from_player(player, 50)
                self.get_out_of_jail(player)
            elif not is_double and player.turns_in_jail < 3:
                if self.ask_get_out_of_jail(player):
                    self.take_money_from_player(player, 50)
                    self.get_out_of_jail(player)
                else:
                    player.turns_in_jail += 1
                    return False
            else:
                is_double = False
                self.get_out_of_jail(player)
        if not player.in_game:
            return False
        if player.location + self.__current_roll > 39:
            player.location = player.location + roll1 + roll2 - 40
            logger.info("Игрок {} проходит поле Вперёд".format(player))
            self.give_money_to_player(player, 200)
        else:
            player.location += self.__current_roll
        return is_double

    @staticmethod
    def give_money_to_player(player: Player, amount):
        logger = logging.getLogger('give_money_to_player')
        player.balance += amount
        logger.info('Игрок {} получает {}Р Баланс:{}Р'.format(player.name, amount, player.balance))

    def get_money(self, player: Player, amount):
        attempts = 0
        while player.balance - amount < 0 and attempts < 5:
            self.ask_sell(player)
            self.ask_mortgage(player)
            attempts += 1

    def take_money_from_player(self, player: Player, amount, *args):
        logger = logging.getLogger('take_money_from_player')
        if player.balance - amount < 0:
            logger.info('Игрок {} не может выплатить {}Р'.format(player.name, amount))
            if player.net_worth - amount < 0:
                if len(args) == 0:
                    self.bankrupt_bank(player)
                return False
            else:
                logger.info('Игроку {} хватит денег если он заложит/продаст что-то из своих активов'.format(player))
                self.get_money(player, amount)
                if player.balance - amount < 0:
                    if len(args) == 0:
                        self.bankrupt_bank(player)
                    return False
        player.balance -= amount
        logger.info('Игрок {} платит {}Р Баланс:{}Р'.format(player.name, amount, player.balance))
        return True

    def transfer_money_between_players(self, from_player: Player, to_player: Player, amount):
        if not self.take_money_from_player(from_player, amount, to_player):
            self.bankrupt_player(from_player, to_player)
            return False
        self.give_money_to_player(to_player, amount)

    def offer_property_to_buy(self, current_player: Player, field):
        action = False
        answer = current_player.landed_on_unowned_property(self, field)
        if answer:
            action = self.give_property_to_player(current_player, field)
        if action or not current_player.in_game:
            return
        interested_players = []
        for player in self.__players:
            if not player == current_player:
                interested_players.append(player)
        self.auction(interested_players, field)

    def auction(self, interested_players: list, field):
        logger = logging.getLogger('auction')
        multiplier = 1
        interested_players = self._offer_property_to_auction(interested_players, field, multiplier)
        while len(interested_players) > 1:
            multiplier += 0.2
            interested_players = self._offer_property_to_auction(interested_players, field, multiplier)
        if len(interested_players) == 1:
            player = interested_players[0]
            self.give_property_to_player(player, field)
        else:
            logger.info('Никто не заинтересован в поле {}'.format(field.name))

    # def _offer_property_to_current_player(self, current_player: Player, field):
    #     answer = current_player.landed_on_unowned_property(self, field)
    #     if answer:
    #         return self.give_property_to_player(current_player, field)
    #     return False

    def _offer_property_to_auction(self, interested_players, field, multiplier):
        logger = logging.getLogger('_offer_property_to_auction')
        new_interested_players = []
        for player in interested_players:
            logger.info('Игрок {} хотите ли купить поле {} за {}Р?'.format(player, field.name,
                                                                           int(field.cost*multiplier)))
            answer = player.property_offered_for_auction(self, field, int(field.cost*multiplier))
            # answer = int(input())
            if answer:
                new_interested_players.append(player)
                logger.info('Игрок {} заинтересован'.format(player))
            else:
                logger.info('Игрок {} не заинтересован'.format(player))
        return new_interested_players

    def give_property_to_player(self, player: Player, field):
        logger = logging.getLogger('give_property_to_player')
        if player.balance > field.cost:
            logger.info("Игрок {} покупает поле {} за {}".format(player, field.name, field.cost))
            self.take_money_from_player(player, field.cost)
            field.owner = player
            player.own_field(field)
            self.check_fill_color(player)
            return True
        else:
            logger.info("Игроку {} не хватает денег".format(player))
        return False

    @staticmethod
    def transfer_property_between_players(from_player: Player, to_player: Player, field):
        # from_player.owned_fields[field.kind].remove(field)
        field.owner = to_player
        to_player.own_field(field)

    def upgrade_property(self, player: Player, field: Street):
        logger = logging.getLogger('upgrade_property')
        logger.info('Игрок {} хочет купить дом на поле {}'.format(player, field))
        self.take_money_from_player(player, field.cost_of_upgrade)
        field.upgrade()
        self.check_fill_color(player)

    def ask_upgrade(self, player: Player):
        available_colors = self.available_color_to_upgrade(player.owned_fields, player.mortgage_fields)
        if len(player.owned_fields) == 0 or len(available_colors) == 0:
            return
        else:
            available_fields = []
            for fields in player.owned_fields.values():
                for field in fields:
                    if not isinstance(field, Utility) and not isinstance(field, Railway):
                        if field.color in available_colors and field.can_upgrade:
                            available_fields.append(field)
            if len(available_fields) > 0:
                for field in available_fields:
                    if player.in_game:
                        while field.num_of_house < 4:
                            if not player.in_game:
                                return
                            if player.balance > field.cost_of_upgrade:
                                answer = player.build_house(self, field)
                                if answer:
                                    self.upgrade_property(player, field)
                                else:
                                    break
                            else:
                                break

    def mortgage_property(self, player: Player, field):
        logger = logging.getLogger('mortgage_property')
        logger.info('Игрок {} закладывает поле {}'.format(player, field))
        amount = field.mortgage()
        self.give_money_to_player(player, amount)
        player.mortgage_field(field)
        self.check_fill_color(player)

    def ask_mortgage(self, player: Player):
        all_fields = []
        for fields in player.owned_fields.values():
            all_fields.extend(fields)
        if len(all_fields) > 0:
            for field in all_fields:
                if player.in_game and player.mortgage_property(self, field):
                    self.mortgage_property(player, field)

    @staticmethod
    def transfer_mortgage_property(from_player: Player, to_player: Player, field):
        field.owner = to_player
        from_player.mortgage_fields[field.kind].remove(field)
        to_player.mortgage_field(field)

    def redeem_property(self, player: Player, field):
        logger = logging.getLogger('redeem_property')
        logger.info('Игрок {} выкупает поле {}'.format(player, field))
        self.take_money_from_player(player, field.redeem_cost)
        player.redeem_field(field)
        field.redeem()
        self.check_fill_color(player)

    def ask_redeem(self, player: Player):
        all_fields = []
        for fields in player.mortgage_fields.values():
            all_fields.extend(fields)
        if len(all_fields) > 0:
            for field in all_fields:
                if player.in_game and player.balance > field.redeem_cost and player.redeem_property(self, field):
                    self.redeem_property(player, field)

    def sell_house(self, player: Player, field):
        logger = logging.getLogger('sell_house')
        logger.info('Игрок {} продаёт дом на поле {}'.format(player, field))
        amount = field.sell_house()
        self.give_money_to_player(player, amount)
        self.check_fill_color(player)

    def ask_sell(self, player: Player):
        fields_with_house = []
        for fields in player.owned_fields.values():
            for field in fields:
                if not isinstance(field, Railway) and not isinstance(field, Utility):
                    if field.has_house:
                        fields_with_house.append(field)
        if len(fields_with_house) > 0:
            for field in fields_with_house:
                if player.in_game:
                    while field.num_of_house > 0:
                        answer = player.sell_house(self, field)
                        if answer:
                            self.sell_house(player, field)
                        else:
                            break

    @staticmethod
    def send_player_to_jail(player):
        logger = logging.getLogger('send_player_to_jail')
        logger.info('Игрок {} попадает в тюрьму'.format(player))
        player.in_jail = True
        player.turns_in_jail = 0
        player.location = 10

    @staticmethod
    def get_out_of_jail(player):
        logger = logging.getLogger('get_out_of_jail')
        logger.info('Игрок {} выходит из тюрьмы'.format(player))
        player.in_jail = False

    def ask_get_out_of_jail(self, player):
        logger = logging.getLogger('ask_get_out_of_jail')
        logger.info('Игрок {} хотите ли вы заплатить 50 за выход из тюрьмы?'.format(player))
        return player.get_out_of_jail(self)

    @staticmethod
    def check_fill_color(player: Player):
        for key in player.owned_fields.keys():
            if key not in ['railway', 'utility']:
                can_double = len(player.owned_fields[key]) == Game.num_field_color(key)
                for field in player.owned_fields[key]:
                    field.can_double = can_double if not field.has_house else False

    # @staticmethod
    # def check_double_condition(player: Player, color):
    #     if not len(player.owned_fields[color]) == Game.num_field_color(color):
    #         return False
    #     for field in player.owned_fields[color]:
    #         if field.has_house:
    #             return False
    #     return True

    def bankrupt_player(self, bankrupt_player: Player, win_player: Player):
        logger = logging.getLogger('bankrupt_player')
        logger.info('Игрок {} обанкротил игрока {}'.format(win_player, bankrupt_player))
        amount = 0
        for key, fields in bankrupt_player.owned_fields.items():
            if key not in ['utility', 'railway']:
                for field in fields:
                    amount += field.sell_all_house()
        self.give_money_to_player(win_player, bankrupt_player.balance + amount)
        bankrupt_player.balance = 0
        for fields in bankrupt_player.owned_fields.values():
            for field in fields:
                self.transfer_property_between_players(bankrupt_player, win_player, field)
        for fields in bankrupt_player.mortgage_fields.values():
            for field in fields:
                self.transfer_mortgage_property(bankrupt_player, win_player, field)
        self.delete_player(bankrupt_player)
        self.check_fill_color(win_player)

    def bankrupt_bank(self, bankrupt_player: Player):
        logger = logging.getLogger('bankrupt_bank')
        logger.info('Банк обанкротил игрока {}'.format(bankrupt_player))
        bankrupt_player.balance = 0
        for fields in bankrupt_player.mortgage_fields.values():
            for field in fields:
                field.owner = None
                field.redeem()
        fields_for_auction = []
        for fields in bankrupt_player.owned_fields.values():
            for field in fields:
                if field.kind not in ['utility', 'railway']:
                    field.sell_all_house()
                field.owner = None
                fields_for_auction.append(field)
        self.delete_player(bankrupt_player)
        if self.game_in_progress:
            for field in fields_for_auction:
                self.auction(self.__players, field)

    def delete_player(self, player: Player):
        self.__players.remove(player)
        player.owned_fields.clear()
        player.mortgage_fields.clear()
        self.__bankrupt_players.append(player)
        player.in_game = False

    @property
    def game_in_progress(self):
        return len(self.__players) > 1 and self.__rounds_played < 200

    def announce_winner(self):
        logger = logging.getLogger('announce_winner')
        winner = None
        max_net_worth = 0
        for player in self.__players:
            if max_net_worth < player.net_worth:
                winner = player
                max_net_worth = player.net_worth
        logger.info('Победитель: игрок {}'.format(winner))
        logger.info('Количество ходов: {}'.format(self.__rounds_played))
        return winner

    def info_about_players(self):
        for player in self.__players:
            self.log_info_about_player(player)

    @staticmethod
    def log_info_about_player(player: Player):
        logger = logging.getLogger('log_info_about_player')
        logger.info('Игрок {}'.format(player))
        logger.info('Баланс:{}Р'.format(player.balance))
        if len(player.owned_fields):
            logger.info('Приобретено:')
            for fields in player.owned_fields.values():
                for field in fields:
                    logger.info(field)
        if len(player.mortgage_fields):
            logger.info('Заложено:')
            for fields in player.mortgage_fields.values():
                for field in fields:
                    logger.info(field)

    def create_game_state_for_player(self, current_player: Player):
        # подсчёт значений для улиц для игрока
        game_state = Game.GameState()
        for street in game_state.streets_index:
            num_mortgage = 0
            sum_num_of_houses = 0
            for field in current_player.owned_fields[street]:
                sum_num_of_houses += field.num_of_house
            if street in current_player.mortgage_fields:
                num_mortgage = len(current_player.mortgage_fields[street])
            info = 6 / self.num_field_color(street) * len(current_player.owned_fields[street])
            if num_mortgage == 0 and sum_num_of_houses > 0:
                info = info + sum_num_of_houses / len(current_player.owned_fields[street])
            info /= 10
            game_state.area_player.append(info)

        # подсчёт значений для улиц для других игроков
        for street in game_state.streets_index:
            num_mortgage = 0
            sum_num_of_houses = 0
            num_owned = 0
            for player in self.__players:
                if not player == current_player and street in player.owned_fields:
                    for field in player.owned_fields[street]:
                        num_owned += 1
                        sum_num_of_houses += field.num_of_house
                    if street in player.mortgage_fields:
                        num_mortgage += len(player.mortgage_fields[street])
            info = 6 / self.num_field_color(street) * num_owned
            if num_mortgage == 0 and sum_num_of_houses > 0:
                info = info + sum_num_of_houses / num_owned
            info /= 10
            game_state.area_other_player.append(info)

        # подсчёт значений для других полей для текущего игрока
        for other_property in game_state.other_property_index:
            info = 0
            if other_property in current_player.owned_fields:
                info = len(current_player.owned_fields[other_property])/game_state.num_of_other_properties[other_property]
            game_state.area_player.append(info)

        # подсчёт значений для других полей для другого игрока
        for other_property in game_state.other_property_index:
            num_owned = 0
            for player in self.__players:
                if not player == current_player and other_property in player.owned_fields:
                    num_owned += len(player.owned_fields[other_property])
            info = num_owned / game_state.num_of_other_properties[other_property]
            game_state.area_other_player.append(info)

        # подсчёт финансовой составляющей
        total_amount = 0
        for player in self.__players:
            total_amount += player.net_worth
        game_state.finance.append(current_player.net_worth/total_amount)
        x = (current_player.balance / 1500) / (1 + current_player.balance / 1500)
        game_state.finance.append(x)

        return game_state

    def calculate_reward(self, current_player: Player):
        num_of_owned_fields = 0
        num_of_mortgage_fields = 0
        for fields in current_player.owned_fields.values():
            num_of_owned_fields += len(fields)
        for fields in current_player.mortgage_fields.values():
            num_of_mortgage_fields += len(fields)
        num_of_owned_fields_enemy = 0
        houses_enemy = 0
        num_of_mortgage_fields_enemy = 0
        for player in self.__players:
            if not player == current_player:
                houses_enemy += player.num_of_houses
                for fields in player.owned_fields.values():
                    num_of_owned_fields_enemy += len(fields)
                for fields in player.mortgage_fields.values():
                    num_of_mortgage_fields_enemy += len(fields)

        v = num_of_owned_fields + current_player.num_of_houses + num_of_mortgage_fields_enemy
        l = num_of_mortgage_fields - num_of_mortgage_fields_enemy

        total = 0
        for player in self.__players:
            total += player.balance

        m = current_player.balance/total

        num_of_players = len(self.__players)

        # return ((v/num_of_players/3.5) / (1 + math.fabs(v/num_of_players/3.5)))/2 + m/num_of_players/3.5
        return (v/num_of_players/5) / (1 + math.fabs(v/num_of_players/5)) + m/num_of_players
