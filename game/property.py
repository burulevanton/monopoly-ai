from game.purchased import Purchased

# класс, отвечающий за поля недвижимости


class Property(Purchased):

    def __init__(self, name, location, cost, rents, cost_of_upgrade, color):
        super().__init__(name, location, cost)
        self.__cost_of_upgrade = cost_of_upgrade
        self.__rents = rents
        self.__num_of_upgrades = 0
        self.__color = color
        self.__can_upgrade = True
        self.__can_double_rent = False

    @property
    def color(self):
        return self.__color

    def get_rent(self):
        if self.__num_of_upgrades == 0:
            return self.__rents[0]*2 if self.__can_double_rent else self.__rents[0]
        else:
            return self.__rents[self.__num_of_upgrades]

    @property
    def can_upgrade(self):
        return self.__can_upgrade

    @property
    def can_double(self):
        return self.__can_double_rent

    @can_double.setter
    def can_double(self, value):
        self.__can_double_rent = value

    @property
    def kind(self):
        return self.__color

    @property
    def has_house(self):
        return self.__num_of_upgrades > 0

    def print_info_about_field(self):
        print("{} (арендная плата:{}, цвет:{})".format(self.name, self.get_rent(), self.color))

    def ask_player(self, player):
        print("Купить данную улицу?(арендная плата:{}, цвет:{})".format(self.get_rent(), self.color))
        print("Баланс до покупки:{}".format(player.balance))
        print("Баланс после покупки:{}".format(player.balance-self.cost))
        print("1) Да")
        print("2) Нет")
        return int(input())

    def upgrade(self):
        self.__num_of_upgrades += 1
        if self.__num_of_upgrades == 4:
            self.__can_upgrade = False

    def mortgage(self):
        self.is_mortgage = True
        if self.__num_of_upgrades > 0:
            self.owner.add_balance(self.__num_of_upgrades*self.__cost_of_upgrade//2)
        self.__num_of_upgrades = 0
        self.owner.add_balance(self.cost//2)

    def sell_house(self):
        if self.__num_of_upgrades == 4:
            self.__can_upgrade = True
        self.__num_of_upgrades -= 1
        self.owner.add_balance(self.__cost_of_upgrade//2)
