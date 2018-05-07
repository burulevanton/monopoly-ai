from game.property import Property
import logging

# класс "Железная дорога"


class Railway(Property):

    def __init__(self, name, location, cost):
        super().__init__(name, location, cost)
        self.__rent = 25

    def get_rent(self):
        return self.__rent*(2**(len(self.owner.owned_fields['railway'])-1))

    @property
    def kind(self):
        return 'railway'

    def print_info_about_field(self):
        logger = logging.getLogger('print_info_about_field')
        logger.info("{}(арендная плата:{})".format(self.name, self.get_rent()))

    def ask_player(self, player):
        logger = logging.getLogger('ask_player')
        logger.info("Купить данную железную дорогу?")
        # print("Баланс до покупки:{}".format(player.balance))
        # print("Баланс после покупки:{}".format(player.balance-self.cost))
        # print("1)Да")
        # print("2)Нет")
        return int(input())

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if self.is_mortgage or not self.owner:
            return 'Поле {} (арендная плата:25Р, стоимость: {}Р)'.format(self.name, self.cost)
        else:
            return 'Поле {} (арендная плата:{}Р, стоимость: {}Р)'.format(self.name, self.get_rent(), self.cost)
