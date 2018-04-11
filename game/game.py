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
        self.__cardChance = Queue()
        self.__cardTreasury = Queue()
        self.__numOfPlayers = 0
        self.init_queue()
        self.set_num_of_players()
        self.init_game_board()
        self.set_players()

    @staticmethod
    def fill_queue(q):
        temp = [i + 1 for i in range(16)]
        random.shuffle(temp)
        for el in temp:
            q.put(el)

    @staticmethod
    def get_num_field_color(color):
        if color in ['brown', 'dark_blue']:
            return 2
        else:
            return 3

    def init_game_board(self):
        self.__board.append(Forward("Вперёд", 0))
        self.__board.append(Property("ул.Житная", 1, 60, 2, "brown"))
        self.__board.append(PublicTreasury("Общественная казна", 2))
        self.__board.append(Property("ул. Нагатинская", 3, 60, 4, "brown"))
        self.__board.append(Tax("Налог", 4, 200))
        self.__board.append(Railway("Римская железная дорога", 5, 200, 25))
        self.__board.append(Property("Варшавское шоссе", 6, 100, 6, "blue"))
        self.__board.append(Chance("Шанс", 7))
        self.__board.append(Property("ул. Огарева", 8, 100, 6, "blue"))
        self.__board.append(Property("ул. Первая парковая", 9, 120, 8, "blue"))
        self.__board.append(Jail("Тюрьма", 10))
        self.__board.append(Property("ул. Полянка", 11, 140, 10, "pink"))
        self.__board.append(Utility("Электроэнергия", 12, 150, 4))
        self.__board.append(Property("ул. Сретенка", 13, 140, 10, "pink"))
        self.__board.append(Property("Ростовская набережная", 14, 160, 12, "pink"))
        self.__board.append(Railway("Курская железная дорога", 15, 200, 25))
        self.__board.append(Property("Рязанский проспект", 16, 180, 14, 'orange'))
        self.__board.append(PublicTreasury("Общественная казна", 17))
        self.__board.append(Property("ул. Вавилова", 18, 180, 14, 'orange'))
        self.__board.append(Property("Рублёвское шоссе", 19, 200, 16, 'orange'))
        self.__board.append(FreeParking("Бесплатная стоянка", 20))
        self.__board.append(Property("ул. Тверская", 21, 220, 18, 'red'))
        self.__board.append(Chance("Шанс", 22))
        self.__board.append(Property("ул. Пушкинская", 23, 220, 18, 'red'))
        self.__board.append(Property("Площадь Маяковского", 24, 240, 20, 'red'))
        self.__board.append(Railway("Казанская железная дорога", 25, 200, 25))
        self.__board.append(Property("ул. Грузинский вал", 26, 260, 22, 'yellow'))
        self.__board.append(Property("ул. Чайковского", 27, 260, 22, 'yellow'))
        self.__board.append(Utility("Водопровод", 28, 150, 4))
        self.__board.append(Property('Смоленская площадь', 29, 280, 24, 'yellow'))
        self.__board.append(GoToJail("Отправляйтесь в тюрьму", 30))
        self.__board.append(Property('ул. Щусева', 31, 300, 26, 'green'))
        self.__board.append(Property("Гоголевский бульвар", 32, 300, 26, 'green'))
        self.__board.append(PublicTreasury("Общественная казна", 33))
        self.__board.append(Property("Кутузовский проспект", 34, 320, 28, 'green'))
        self.__board.append(Railway("Ленинградская железная дорога", 35, 200, 25))
        self.__board.append(Chance("Шанс", 36))
        self.__board.append(Property("ул. Малая Бронная", 37, 350, 35, 'dark_blue'))
        self.__board.append(Tax("Сверхналог", 38, 100))
        self.__board.append(Property("ул. Арбат", 39, 400, 50, 'dark_blue'))

    def init_queue(self):
        Game.fill_queue(self.__cardChance)
        Game.fill_queue(self.__cardTreasury)

    def set_num_of_players(self):
        print("Введите количество игроков:")
        self.__numOfPlayers = int(input())

    def set_players(self):
        for i in range(self.__numOfPlayers):
            print("Введите имя игрока №{}".format(i+1))
            name = input()
            self.__players.append(Player(name, i))

    def play_round(self):
        for _ in range(20):
            for player in self.__players:
                player.roll_dice()
                self.__board[self.__players[player.num].location].player_interaction(player)
