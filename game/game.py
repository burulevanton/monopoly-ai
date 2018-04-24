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
import logging
import random

logging.basicConfig(format=u'%(filename)s[:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.DEBUG)


class Game:

    def __init__(self):
        self.__board = []
        self.__players = []
        self.__numOfPlayers = 0
        self.__current_roll = 0
        self.__double_in_a_row = 0
        self.set_num_of_players()
        self.init_game_board()
        self.set_players()

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
        for i in range(self.__numOfPlayers):
            print("Введите имя игрока №{}".format(i+1))
            name = input()
            self.__players.append(Player(name, i))

    def play_game(self):
        for _ in range(100):
            for player in self.__players:
                self.ask_upgrade(player)
                self.ask_mortgage(player)
                self.ask_redeem(player)
                self.ask_sell(player)
                self.play_round(player)

    def play_round(self, player):
        is_double = self.roll_dice_and_move(player)
        if self.__board[self.__players[player.num].location].landed_on(self, player):
            self.__board[self.__players[player.num].location].landed_on(self, player)
        self.check_fill_color(player)
        if is_double:
            self.__double_in_a_row += 1
            if self.__double_in_a_row == 3:
                self.__double_in_a_row = 0
                player.location = 10
                player.dec_balance(50)
            else:
                self.play_round(player)
        self.__double_in_a_row = 0

    def roll_dice_and_move(self, player):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        logging.info("Игрок {} выбрасывает {} и {}".format(player, roll1, roll2))
        self.__current_roll = roll1 + roll2
        if player.location + self.__current_roll > 39:
            player.location = player.location + roll1 + roll2 - 40
            logging.info("Игрок {} проходит поле Вперёд".format(player))
            self.give_money_to_player(player, 200)
        else:
            player.location += self.__current_roll
        return roll1 == roll2

    @staticmethod
    def give_money_to_player(player: Player, amount):
        player.balance += amount
        logging.info('Игрок {} получает {}Р'.format(player.name, amount))

    def take_money_from_player(self, player: Player, amount):
        if player.balance - amount < 0:
            logging.info('Игрок {} не может выплатить {}Р'.format(player.name, amount))
            if player.net_worth - amount < 0:
                logging.info('Игрок {} становится банкротом'.format(player))
                return False
            else:
                logging.info('Игроку [} хватит денег если он заложит/продаст что-то из своих активов'.format(player))
                self.ask_sell(player)
                self.ask_mortgage(player)
                if player.balance - amount < 0:
                    logging.info('Игрок {} становится банкротом'.format(player))
                    return False
                self.take_money_from_player(player, amount)
        player.balance -= amount
        logging.info('Игрок {} платит {}Р'.format(player.name, amount))
        return True

    def transfer_money_between_players(self, from_player: Player, to_player: Player, amount):
        if not self.take_money_from_player(from_player, amount):
            
            return False
        self.give_money_to_player(to_player, amount)

    def offer_property_to_buy(self, current_player, field):
        action = self._offer_property_to_current_player(current_player, field)
        if action:
            return
        interested_players = []
        for player in self.__players:
            if not player == current_player:
                interested_players.append(player)
        multiplier = 0.8
        while len(interested_players) > 1:
            multiplier += 0.2
            interested_players = self._offer_property_to_auction(interested_players, field, multiplier)
        if len(interested_players) == 1:
            player = interested_players[0]
            self.take_money_from_player(player, field.cost*multiplier)
            logging.info('Игрок {} покупает поле {}  за {}'.format(player, field.name, field.cost*multiplier))
            field.owner = interested_players[0]
            player.own_field(field)
        else:
            logging.info('Никто не заинтересован в поле {}'.format(field.name))

    def _offer_property_to_current_player(self, current_player, field):
        answer = field.ask_player(current_player)
        if answer == 1:
            if self.take_money_from_player(current_player, field.cost):
                print("Игрок {} покупает поле {} за {}".format(current_player.name, field.name, field.cost))
                field.owner = current_player
                current_player.own_field(field)
                return True
        return False

    @staticmethod
    def _offer_property_to_auction(interested_players, field, multiplier):
        new_interested_players = []
        for player in interested_players:
            logging.info('Игрок {} хотите ли купить поле {} за {}Р?'.format(player, field.name,
                                                                            int(field.cost*multiplier)))
            answer = int(input())
            if answer == 1:
                new_interested_players.append(player)
                logging.info('Игрок {} заинтересован'.format(player))
            else:
                logging.info('Игрок {} не заинтересован'.format(player))
        return new_interested_players

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
                i = 0
                print('0)Ничего не улучшать')
                for field in available_fields:
                    print('{}){}'.format(i+1, field.name))
                    i += 1
                answer = int(input())
                if answer == 0:
                    return
                else:
                    if self.take_money_from_player(player, available_fields[answer-1].cost_of_upgrade):
                        available_fields[answer-1].upgrade()
                        self.check_fill_color(player)
                        self.ask_upgrade(player)

    def ask_mortgage(self, player: Player):
        i = 0
        all_fields = []
        for fields in player.owned_fields.values():
            all_fields.extend(fields)
        for field in all_fields:
            print('{}){}'.format(i+1, field.name))
            i += 1
        if len(all_fields) > 0:
            print('0)Ничего не закладывать')
            answer = int(input())
            if answer == 0:
                return
            else:
                amount = all_fields[answer - 1].mortgage()
                self.give_money_to_player(player, amount)
                player.mortgage_field(all_fields[answer-1])
                Game.check_fill_color(player)
                self.ask_mortgage(player)

    def ask_redeem(self, player: Player):
        i = 0
        all_fields = []
        for fields in player.mortgage_fields.values():
            all_fields.extend(fields)
        for field in all_fields:
            print('{}){}'.format(i + 1, field.name))
            i += 1
        if len(all_fields) > 0:
            print('0)Ничего не выкупать')
            answer = int(input())
            if answer == 0:
                return
            else:
                if self.take_money_from_player(player, all_fields[answer-1].redeem_cost):
                    player.redeem_field(all_fields[answer-1])
                    all_fields[answer-1].redeem()
                    Game.check_fill_color(player)
                    self.ask_redeem(player)

    def ask_sell(self, player: Player):
        i = 0
        fields_with_house = []
        for fields in player.owned_fields.values():
            for field in fields:
                if not isinstance(field, Railway) and not isinstance(field, Utility):
                    if field.has_house:
                        fields_with_house.append(field)
        for field in fields_with_house:
            print('{}) {}'.format(i+1, field.name))
        if len(fields_with_house) > 0:
            print('0)Ничего не продавать')
            answer = int(input())
            if answer == 0:
                return
            else:
                amount = fields_with_house[answer-1].sell_house()
                self.give_money_to_player(player, amount)
                Game.check_fill_color(player)
                self.ask_sell(player)

    @staticmethod
    def check_fill_color(player: Player):
        for key in player.owned_fields.keys():
            if key not in ['railway', 'utility']:
                can_double = Game.check_double_condition(player, key)
                for field in player.owned_fields[key]:
                    field.can_double = can_double

    @staticmethod
    def check_double_condition(player: Player, color):
        if not len(player.owned_fields[color]) == Game.num_field_color(color):
            return False
        for field in player.owned_fields[color]:
            if field.has_house:
                return False
        return True
