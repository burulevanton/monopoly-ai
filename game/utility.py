from game.purchased import Purchased

# класс Коммунальное предпреятие


class Utility(Purchased):

    def __init__(self, name, location, cost):
        super().__init__(name, location, cost)

    @property
    def kind(self):
        return 'utility'

    def player_interaction(self, player):
        self.print_info(player)
        if self.owner == player:
            print("Игрок {} отдыхает".format(player.name))
        if not self.owner:
            answer = self.ask_player(player)
            if answer == 1:
                player.dec_balance(self.cost)
                print("Игрок {} покупает поле {} за {}".format(player.name, self.name, self.cost))
                self.owner = player
                player.own_field(self)
            else:
                return
        elif self.owner != player:
            rent = self.get_rent(player)
            self.owner.add_balance(rent)
            player.dec_balance(rent)
            print("Игрок {} платит {} за аренду владельцу(игроку {})".format(player.name, rent, self.owner.name))
        return False

    def get_rent(self, player):
        if len(self.owner.owned_fields['utility']) == 2:
            return 10 * player.current_roll
        else:
            return 4 * player.current_roll

    def ask_player(self, player):
        print("Купить данное коммунальное предприятие?")
        print("Баланс до покупки:{}".format(player.balance))
        print("Баланс после покупки:{}".format(player.balance - self.cost))
        print("1)Да")
        print("2)Нет")
        return int(input())

    def print_info_about_field(self):
        print("{}(арендная плата:{}*количество очков)".format(self.name, 4))
