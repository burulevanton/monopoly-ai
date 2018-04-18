from game.purchased import Purchased

# класс, отвечающий за поля недвижимости


class Property(Purchased):

    def __init__(self, name, location, cost, rent, cost_of_upgrade, rent_lvl_1, rent_lvl_2, rent_lvl_3, rent_lvl_4,
                 color):
        super().__init__(name, location, cost, rent)
        self.__cost_of_upgrade = cost_of_upgrade
        self.__rent_lvl_1 = rent_lvl_1
        self.__rent_lvl_2 = rent_lvl_2
        self.__rent_lvl_3 = rent_lvl_3
        self.__rent_lvl_4 = rent_lvl_4
        self.__num_of_upgrades = 0
        self.__color = color
        self.__can_upgrade = True
        self.__can_double_rent = False

    @property
    def color(self):
        return self.__color

    @property
    def rent(self):
        if self.__num_of_upgrades == 0:
            return self.start_rent*2 if self.__can_double_rent else self.start_rent
        elif self.__num_of_upgrades == 1:
            return self.__rent_lvl_1
        elif self.__num_of_upgrades == 2:
            return self.__rent_lvl_2
        elif self.__num_of_upgrades == 3:
            return self.__rent_lvl_3
        elif self.__num_of_upgrades == 4:
            return self.__rent_lvl_4

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
        print("{} (арендная плата:{}, цвет:{})".format(self.name, self.rent, self.color))

    def ask_player(self, player):
        print("Купить данную улицу?(арендная плата:{}, цвет:{})".format(self.rent, self.color))
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
