# основная логика игры
from queue import Queue
import random
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
from game.field import Field


class Game:

    def __init__(self):
        self.__board = []
        self.__players = []
        self.__numOfPlayers = 0
        self.set_num_of_players()
        self.init_game_board()
        self.set_players()

    @staticmethod
    def get_num_field_color(color):
        if color in ['brown', 'dark_blue']:
            return 2
        elif color in ['blue', 'pink', 'orange', 'red', 'yellow', 'green']:
            return 3
        else:
            return -1

    @staticmethod
    def available_color_to_upgrade(num_owned_field: dict):
        available_colors = []
        for key in num_owned_field.keys():
            if len(num_owned_field[key]) == Game.get_num_field_color(key):
                available_colors.append(key)
        return available_colors

    def init_game_board(self):
        self.__board.append(Forward("Вперёд", 0))
        self.__board.append(Property("ул.Житная", 1, 60, 2, 50, 10, 30, 90, 160, "brown"))
        self.__board.append(PublicTreasury("Общественная казна", 2))
        self.__board.append(Property("ул. Нагатинская", 3, 60, 4, 50, 20, 60, 180, 320, "brown"))
        self.__board.append(Tax("Налог", 4, 200))
        self.__board.append(Railway("Римская железная дорога", 5, 200, 25))
        self.__board.append(Property("Варшавское шоссе", 6, 100, 6, 50, 30, 90, 270, 400, "blue"))
        self.__board.append(Chance("Шанс", 7))
        self.__board.append(Property("ул. Огарева", 8, 100, 6, 50, 30, 90, 270, 400, "blue"))
        self.__board.append(Property("ул. Первая парковая", 9, 120, 8, 50, 40, 100, 300, 450, "blue"))
        self.__board.append(Jail("Тюрьма", 10))
        self.__board.append(Property("ул. Полянка", 11, 140, 10, 100, 50, 150, 450, 625, "pink"))
        self.__board.append(Utility("Электроэнергия", 12, 150, 4))
        self.__board.append(Property("ул. Сретенка", 13, 140, 10, 100, 50, 150, 450, 625, "pink"))
        self.__board.append(Property("Ростовская набережная", 14, 160, 12, 100, 60, 180, 500, 700, "pink"))
        self.__board.append(Railway("Курская железная дорога", 15, 200, 25))
        self.__board.append(Property("Рязанский проспект", 16, 180, 14, 100, 70, 200, 550, 750, 'orange'))
        self.__board.append(PublicTreasury("Общественная казна", 17))
        self.__board.append(Property("ул. Вавилова", 18, 180, 14, 100, 70, 200, 550, 750, 'orange'))
        self.__board.append(Property("Рублёвское шоссе", 19, 200, 16, 100, 80, 220, 600, 800, 'orange'))
        self.__board.append(FreeParking("Бесплатная стоянка", 20))
        self.__board.append(Property("ул. Тверская", 21, 220, 18, 150, 90, 250, 700, 875, 'red'))
        self.__board.append(Chance("Шанс", 22))
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
        self.__board.append(PublicTreasury("Общественная казна", 33))
        self.__board.append(Property("Кутузовский проспект", 34, 320, 28, 200, 150, 450, 1000, 1200, 'green'))
        self.__board.append(Railway("Ленинградская железная дорога", 35, 200, 25))
        self.__board.append(Chance("Шанс", 36))
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

    def play_round(self):
        for _ in range(100):
            for player in self.__players:
                player.roll_dice()
                self.__board[self.__players[player.num].location].player_interaction(player)
                self.ask_upgrade(player)
            self.print_info()

    def print_info(self):
        f = open('info.txt', 'w')
        for player in self.__players:
            f.write('Player {}\n'.format(player.name))
            f.write(str(player.owned_fields))
        f.close()

    @staticmethod
    def ask_upgrade(player: Player):
        available_colors = Game.available_color_to_upgrade(player.owned_fields)
        if len(player.owned_fields) == 0 or len(available_colors) == 0:
            return
        else:
            available_fields = []
            for fields in player.owned_fields.values():
                for field in fields:
                    if not isinstance(field, Utility) and not isinstance(field, Railway):
                        if field.color in available_colors:
                            available_fields.append(field)
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
                Game.ask_upgrade(player)

