from game.property import Property
import logging

# класс, отвечающий за поля недвижимости


class Street(Property):

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

    @property
    def cost_of_upgrade(self):
        return self.__cost_of_upgrade

    @property
    def current_value(self):
        return self.cost//2 + self.__num_of_upgrades*self.cost_of_upgrade//2

    def print_info_about_field(self):
        logger = logging.getLogger('print_info_about_field')
        logger.info("{} (арендная плата:{}, цвет:{})".format(self.name, self.get_rent(), self.color))

    def ask_player(self, player):
        logger = logging.getLogger('ask_player')
        logger.info("Купить данную улицу?(арендная плата:{}, цвет:{})".format(self.get_rent(), self.color))
        # print("Баланс до покупки:{}".format(player.balance))
        # print("Баланс после покупки:{}".format(player.balance-self.cost))
        # print("1) Да")
        # print("2) Нет")
        return int(input())

    def upgrade(self):
        self.__num_of_upgrades += 1
        if self.__num_of_upgrades == 4:
            self.__can_upgrade = False

    def mortgage(self):
        self.is_mortgage = True
        amount = self.cost//2
        if self.__num_of_upgrades > 0:
            amount += self.__num_of_upgrades*self.__cost_of_upgrade//2
        self.__num_of_upgrades = 0
        return amount

    def sell_house(self):
        if self.__num_of_upgrades == 4:
            self.__can_upgrade = True
        self.__num_of_upgrades -= 1
        return self.__cost_of_upgrade//2

    def sell_all_house(self):
        self.__can_upgrade = True
        amount = self.cost_of_upgrade//2*self.__num_of_upgrades
        self.__num_of_upgrades = 0
        return amount

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return 'Поле {} (текущая арендная плата - {}Р, количество домов - {}, цвет - {}, стоимость дома - {}Р, ' \
               'стоимость - {}Р)'.\
            format(self.name, self.get_rent(), self.__num_of_upgrades, self.color, self.cost_of_upgrade, self.cost)
