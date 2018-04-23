from game.purchased import Purchased

# класс "Железная дорога"


class Railway(Purchased):

    def __init__(self, name, location, cost):
        super().__init__(name, location, cost)
        self.__rent = 25

    def get_rent(self):
        return self.__rent*(2**(len(self.owner.owned_fields['railway'])-1))

    @property
    def kind(self):
        return 'railway'

    def print_info_about_field(self):
        print("{}(арендная плата:{})".format(self.name, self.get_rent()))

    def ask_player(self, player):
        print("Купить данную железную дорогу?")
        print("Баланс до покупки:{}".format(player.balance))
        print("Баланс после покупки:{}".format(player.balance-self.cost))
        print("1)Да")
        print("2)Нет")
        return int(input())
