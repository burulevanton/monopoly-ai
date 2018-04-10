from game.purchased import Purchased

# класс "Железная дорога"


class Railway(Purchased):

    def __init__(self, name, location, cost, rent):
        super().__init__(name, location, cost, rent)

    def print_info_about_field(self, players, player_num):
        print("{}(арендная плата:{})".format(self.name, self.rent))

    def ask_player(self, players, player_num):
        print("Купить данную железную дорогу?")
        print("Баланс до покупки:{}".format(players[player_num].balance))
        print("Баланс после покупки:{}".format(players[player_num].balance-self.cost))
        print("1)Да")
        print("2)Нет")
        return int(input())
