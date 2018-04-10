import random


class Player:

    def __init__(self, player_name, player_num):
        self.__player_name = player_name
        self.__player_num = player_num
        self.__current_balance = 1500
        self.__current_location = 0
        self.__in_game = True

    @property
    def name(self):
        return self.__player_name

    @property
    def num(self):
        return self.__player_num

    @property
    def location(self):
        return self.__current_location

    @location.setter
    def location(self, value):
        self.__current_location = value

    @property
    def balance(self):
        return self.__current_balance

    def add_balance(self, value):
        self.__current_balance += value

    def dec_balance(self, value):
        self.__current_balance -= value

    def quit_game(self):
        print("Игрок {} покидает игру".format(self.name))

    @property
    def in_game(self):
        return self.__in_game

    def roll_dice(self):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        print("Игрок {} выбрасывает {} и {}".format(self.name, roll1, roll2))
        if self.location + roll1 + roll2 > 40:
            self.location = self.location + roll1 + roll2 - 40
            self.add_balance(200)
            print("Игрок {} проходит поле Вперёд и получает 200".format(self.name))
        else:
            self.location += roll1+roll2

