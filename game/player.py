import random


class Player:

    def __init__(self, player_name, player_num):
        self.__player_name = player_name
        self.__player_num = player_num
        self.__current_balance = 1500
        self.__current_location = 0
        self.__in_game = True
        self.__owned_fields = {}
        self.__mortgage_fields = {}
        self.__current_roll = 0

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

    @property
    def owned_fields(self):
        return self.__owned_fields

    @property
    def current_roll(self):
        return self.__current_roll

    @property
    def mortgage_fields(self):
        return self.__mortgage_fields

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
        self.__current_roll = roll1 + roll2
        if self.location + self.__current_roll > 39:
            self.location = self.location + roll1 + roll2 - 40
            self.add_balance(200)
            print("Игрок {} проходит поле Вперёд и получает 200".format(self.name))
        else:
            self.location += self.__current_roll
        return roll1 == roll2

    def own_field(self, field):
        if field.kind in self.__owned_fields:
            self.__owned_fields[field.kind].append(field)
        else:
            self.__owned_fields[field.kind] = [field]

    def mortgage_field(self, field):
        if field.kind in self.__mortgage_fields:
            self.__mortgage_fields[field.kind].append(field)
        else:
            self.__mortgage_fields[field.kind] = [field]
        self.__owned_fields[field.kind].remove(field)
        if len(self.__owned_fields[field.kind]) == 0:
            del self.__owned_fields[field.kind]

    def redeem_field(self, field):
        if field.kind in self.__owned_fields:
            self.__owned_fields[field.kind].append(field)
        else:
            self.__owned_fields[field.kind] = [field]
        self.__mortgage_fields[field.kind].remove(field)
        if len(self.__mortgage_fields[field.kind]) == 0:
            del self.__mortgage_fields[field.kind]
