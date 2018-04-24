from game.field import Field
import random
# класс, отвечающий за поле Общественная казна


class PublicTreasury(Field):

    def __init__(self, location):
        super().__init__("Общественная казна", location)

    def landed_on(self, game, player):
        self.print_info(player)
        num_card = random.randint(1, 14)
        print("Игрок {} берёт карточку №{}".format(player.name, num_card))
        if num_card == 1:
            print('Отправляйтесь в тюрьму')
            player.location = 10
            return True
        elif num_card == 2:
            print('Идите на поле Вперёд')
            player.location = 0
            print("Игрок {} проходит поле Вперёд и получает 200".format(player.name))
            game.give_money_to_player(player, 200)
        elif num_card == 3:
            print('Заплатите 50')
            game.take_money_from_player(player, 50)
        elif num_card == 4:
            print('Получите 10')
            game.give_money_to_player(player, 10)
        elif num_card == 5:
            print('Вы заработали 50')
            game.give_money_to_player(player, 50)
        elif num_card == 6:
            print('Получите 200')
            game.give_money_to_player(player, 200)
        elif num_card == 7:
            print('Заплатите 100')
            game.take_money_from_player(player, 100)
        elif num_card == 8:
            print('Получите 100')
            game.give_money_to_player(player, 100)
        elif num_card == 9:
            print('Отправляйтесь на бесплатную стоянку')
            if not player.location == 2 or player.location == 17:
                print("Игрок {} проходит поле Вперёд и получает 200".format(player.name))
                game.give_money_to_player(player, 200)
            player.location = 20
            return True
        elif num_card == 10:
            print('Получите 20')
            game.give_money_to_player(player, 20)
        elif num_card == 11 or num_card == 13:
            print('Вы получаете 100')
            game.give_money_to_player(player, 100)
        elif num_card == 12:
            print('Заплатите 50')
            game.take_money_from_player(player, 50)
        elif num_card == 14:
            print('Получите 25')
            game.give_money_to_player(player, 25)
        return False
