from abc import abstractmethod, ABCMeta


class Player:
    __metaclass__ = ABCMeta

    def __init__(self, player_name, player_num):
        self.__player_name = player_name
        self.__player_num = player_num
        self.__current_balance = 0
        self.__current_location = 0
        self.__owned_fields = {}
        self.__mortgage_fields = {}
        self.__in_jail = False
        self.__in_game = True
        self.__turns_in_jail = 0
        self.start_game()

    def start_game(self):
        self.__current_balance = 1500
        self.__current_location = 0
        self.__owned_fields = {'brown': [], 'blue': [], 'pink': [], 'orange': [], 'red': [], 'yellow': [], 'green': [],
                               'dark_blue': [], 'utility': [], 'railway': []}
        self.__mortgage_fields = {}
        self.__in_jail = False
        self.__turns_in_jail = 0
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

    @balance.setter
    def balance(self, value):
        self.__current_balance = value

    @property
    def net_worth(self):
        value_of_properties = 0
        for fields in self.owned_fields.values():
            for field in fields:
                value_of_properties += field.current_value
        return value_of_properties + self.balance

    @property
    def owned_fields(self):
        return self.__owned_fields

    @property
    def mortgage_fields(self):
        return self.__mortgage_fields

    @property
    def in_jail(self):
        return self.__in_jail

    @property
    def in_game(self):
        return self.__in_game

    @in_game.setter
    def in_game(self, value):
        self.__in_game = value

    @in_jail.setter
    def in_jail(self, value):
        self.__in_jail = value

    @property
    def turns_in_jail(self):
        return self.__turns_in_jail

    @turns_in_jail.setter
    def turns_in_jail(self, value):
        self.__turns_in_jail = value

    @property
    def num_of_houses(self):
        num_of_house = 0
        for fields in self.__owned_fields.values():
            for field in fields:
                if field.kind not in ['utility', 'railway']:
                    num_of_house += field.num_of_house
        return num_of_house

    def own_field(self, field):
            self.__owned_fields[field.kind].append(field)

    def mortgage_field(self, field):
        if field.kind in self.__mortgage_fields:
            self.__mortgage_fields[field.kind].append(field)
        else:
            self.__mortgage_fields[field.kind] = [field]
        if field in self.__owned_fields[field.kind]:
            self.__owned_fields[field.kind].remove(field)

    def redeem_field(self, field):
        if field.kind in self.__owned_fields:
            self.__owned_fields[field.kind].append(field)
        else:
            self.__owned_fields[field.kind] = [field]
        self.__mortgage_fields[field.kind].remove(field)
        if len(self.__mortgage_fields[field.kind]) == 0:
                del self.__mortgage_fields[field.kind]

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.name

    @abstractmethod
    def landed_on_unowned_property(self, game, field):
        pass

    @abstractmethod
    def property_offered_for_auction(self, game, field, price):
        pass

    @abstractmethod
    def build_house(self, game, field):
        pass

    @abstractmethod
    def sell_house(self, game, field):
        pass

    @abstractmethod
    def mortgage_property(self, game, field):
        pass

    @abstractmethod
    def redeem_property(self, game, field):
        pass

    @abstractmethod
    def get_out_of_jail(self, game):
        pass

