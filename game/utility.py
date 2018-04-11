from game.purchased import Purchased

# класс Коммунальное предпреятие


class Utility(Purchased):

    def __init__(self, name, location, cost, rent):
        super().__init__(name, location, cost, rent)

    def ask_player(self, player):
        print("Купить данное коммунальное предприятие?")
        print("Баланс до покупки:{}".format(player.balance))
        print("Баланс после покупки:{}".format(player.balance - self.cost))
        print("1)Да")
        print("2)Нет")
        return int(input())

    def print_info_about_field(self):
        print("{}(арендная плата:{})".format(self.name, self.rent))
