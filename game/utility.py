from game.property import Property
import logging

# класс Коммунальное предпреятие


class Utility(Property):

    def __init__(self, name, location, cost):
        super().__init__(name, location, cost)

    @property
    def kind(self):
        return 'utility'

    def get_rent(self, player):
        if len(self.owner.owned_fields['utility']) == 2:
            return 10 * player.current_roll
        else:
            return 4 * player.current_roll

    def ask_player(self, player):
        logger = logging.getLogger('ask_player')
        logger.info("Купить данное коммунальное предприятие?")
        # print("Баланс до покупки:{}".format(player.balance))
        # print("Баланс после покупки:{}".format(player.balance - self.cost))
        # print("1)Да")
        # print("2)Нет")
        return int(input())

    def print_info_about_field(self):
        logger = logging.getLogger('print_info_about_field')
        logger.info("{}(арендная плата:{}*количество очков)".format(self.name, 4))

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        multiplier = 10 if len(self.owner.owned_fields['utility']) == 2 else 4
        return 'Поле {} (арендная плата: {}*количество кубиков Р, стоимость: {}Р'.format(self.name, multiplier,
                                                                                         self.cost)
