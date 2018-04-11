from game.purchased import Purchased

# класс, отвечающий за поля недвижимости


class Property(Purchased):

    def __init__(self, name, location, cost, rent, color):
        super().__init__(name, location, cost, rent)
        self.__color = color

    @property
    def color(self):
        return self.__color

    def print_info_about_field(self):
        print("{} (арендная плата:{}, цвет:{})".format(self.name, self.rent, self.color))

    def ask_player(self, player):
        print("Купить данную улицу?(арендная плата:{}, цвет:{})".format(self.rent, self.color))
        print("Баланс до покупки:{}".format(player.balance))
        print("Баланс после покупки:{}".format(player.balance-self.cost))
        print("1) Да")
        print("2) Нет")
        return int(input())
