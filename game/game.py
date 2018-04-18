# основная логика игры
from game.chance import Chance
from game.forward import Forward
from game.free_parking import FreeParking
from game.go_to_jail import GoToJail
from game.jail import Jail
from game.player import Player
from game.property import Property
from game.public_treasury import PublicTreasury
from game.railway import Railway
from game.tax import Tax
from game.utility import Utility


class Game:

    def __init__(self):
        self.__board = []
        self.__players = []
        self.__numOfPlayers = 0
        self.__double_in_a_row = 0
        self.set_num_of_players()
        self.init_game_board()
        self.set_players()

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
        self.__board.append(Forward("Вперёд", 0))
        self.__board.append(Property("ул.Житная", 1, 60, 2, 50, 10, 30, 90, 160, "brown"))
        self.__board.append(PublicTreasury(2))
        self.__board.append(Property("ул. Нагатинская", 3, 60, 4, 50, 20, 60, 180, 320, "brown"))
        self.__board.append(Tax("Налог", 4, 200))
        self.__board.append(Railway("Римская железная дорога", 5, 200, 25))
        self.__board.append(Property("Варшавское шоссе", 6, 100, 6, 50, 30, 90, 270, 400, "blue"))
        self.__board.append(Chance(7))
        self.__board.append(Property("ул. Огарева", 8, 100, 6, 50, 30, 90, 270, 400, "blue"))
        self.__board.append(Property("ул. Первая парковая", 9, 120, 8, 50, 40, 100, 300, 450, "blue"))
        self.__board.append(Jail("Тюрьма", 10))
        self.__board.append(Property("ул. Полянка", 11, 140, 10, 100, 50, 150, 450, 625, "pink"))
        self.__board.append(Utility("Электроэнергия", 12, 150, 4))
        self.__board.append(Property("ул. Сретенка", 13, 140, 10, 100, 50, 150, 450, 625, "pink"))
        self.__board.append(Property("Ростовская набережная", 14, 160, 12, 100, 60, 180, 500, 700, "pink"))
        self.__board.append(Railway("Курская железная дорога", 15, 200, 25))
        self.__board.append(Property("Рязанский проспект", 16, 180, 14, 100, 70, 200, 550, 750, 'orange'))
        self.__board.append(PublicTreasury(17))
        self.__board.append(Property("ул. Вавилова", 18, 180, 14, 100, 70, 200, 550, 750, 'orange'))
        self.__board.append(Property("Рублёвское шоссе", 19, 200, 16, 100, 80, 220, 600, 800, 'orange'))
        self.__board.append(FreeParking("Бесплатная стоянка", 20))
        self.__board.append(Property("ул. Тверская", 21, 220, 18, 150, 90, 250, 700, 875, 'red'))
        self.__board.append(Chance(22))
        self.__board.append(Property("ул. Пушкинская", 23, 220, 18, 150, 90, 250, 700, 875, 'red'))
        self.__board.append(Property("Площадь Маяковского", 24, 240, 20, 150, 100, 300, 750, 925, 'red'))
        self.__board.append(Railway("Казанская железная дорога", 25, 200, 25))
        self.__board.append(Property("ул. Грузинский вал", 26, 260, 22, 150, 110, 330, 800, 975, 'yellow'))
        self.__board.append(Property("ул. Чайковского", 27, 260, 22, 150, 110, 330, 800, 975, 'yellow'))
        self.__board.append(Utility("Водопровод", 28, 150, 4))
        self.__board.append(Property('Смоленская площадь', 29, 280, 24, 150, 120, 360, 850, 1025, 'yellow'))
        self.__board.append(GoToJail("Отправляйтесь в тюрьму", 30))
        self.__board.append(Property('ул. Щусева', 31, 300, 26, 200, 130, 390, 900, 1100, 'green'))
        self.__board.append(Property("Гоголевский бульвар", 32, 300, 26, 200, 130, 390, 900, 1100, 'green'))
        self.__board.append(PublicTreasury(33))
        self.__board.append(Property("Кутузовский проспект", 34, 320, 28, 200, 150, 450, 1000, 1200, 'green'))
        self.__board.append(Railway("Ленинградская железная дорога", 35, 200, 25))
        self.__board.append(Chance(36))
        self.__board.append(Property("ул. Малая Бронная", 37, 350, 35, 200, 175, 500, 1100, 1300, 'dark_blue'))
        self.__board.append(Tax("Сверхналог", 38, 100))
        self.__board.append(Property("ул. Арбат", 39, 400, 50, 200, 200, 600, 1400, 1700, 'dark_blue'))

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
                self.play_round(player)
                self.ask_upgrade(player)
                self.ask_mortgage(player)
                self.ask_redeem(player)
                self.ask_sell(player)
                self.check_fill_color(player)
            self.print_info()

    def play_round(self, player):
        is_double = player.roll_dice()
        if self.__board[self.__players[player.num].location].player_interaction(player):
            self.__board[self.__players[player.num].location].player_interaction(player)
        if is_double:
            self.__double_in_a_row += 1
            if self.__double_in_a_row == 3:
                self.__double_in_a_row = 0
                player.location = 10
                player.dec_balance(50)
            else:
                self.play_round(player)
        self.__double_in_a_row = 0

    def print_info(self):
        f = open('info.txt', 'w')
        for player in self.__players:
            f.write('Player {}\n'.format(player.name))
            f.write(str(player.owned_fields))
        f.close()

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
                    available_fields[answer-1].upgrade()
                    self.ask_upgrade(player)

    @staticmethod
    def ask_mortgage(player: Player):
        print('Mortgage')
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
                player.mortgage_field(all_fields[answer-1])
                all_fields[answer-1].mortgage()
                Game.ask_mortgage(player)

    @staticmethod
    def ask_redeem(player: Player):
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
                player.redeem_field(all_fields[i-1])
                all_fields[answer-1].redeem()
                Game.ask_redeem(player)

    @staticmethod
    def ask_sell(player: Player):
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
                fields_with_house[answer-1].sell_house()
                Game.ask_sell(player)

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
