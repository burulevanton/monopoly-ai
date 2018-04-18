from game.field import Field
import random

# поле "Шанс"


class Chance(Field):

    def __init__(self, location):
        super().__init__("Шанс", location)

    def player_interaction(self, player):
        self.print_info(player)
        num_card = random.randint(1, 14)
        print("Игрок берёт карточку №{}".format(num_card))
        if num_card == 1:
            print('Отправляйтесь на Арбат')
            player.location = 39
            return True
        elif num_card == 2:
            print('Отправляйтесь на поле Полянка')
            if player.location == 7:
                player.location = 11
            else:
                print("Игрок {} проходит поле Вперёд и получает 200".format(player.name))
                player.location = 11
                player.add_balance(200)
            return True
        elif num_card == 3 or num_card == 8:
            print('Отправляйтесь на ближайщую станцию')
            if player.location == 7:
                player.location = 15
            if player.location == 22:
                player.location = 25
            if player.location == 36:
                print("Игрок {} проходит поле Вперёд и получает 200".format(player.name))
                player.location = 5
                player.add_balance(200)
            return True
        elif num_card == 4:
            print('Банк платит вам 50')
            player.add_balance(50)
            return False
        elif num_card == 5:
            print('Идите на ближайшее поле коммунального предприятия')
            if player.location == 7:
                player.location = 12
            if player.location == 22:
                player.location = 28
            if player.location == 36:
                player.location = 12
                print("Игрок {} проходит поле Вперёд и получает 200".format(player.name))
                player.add_balance(200)
            return False
        elif num_card == 6:
            print('Отправляйтесь в тюрьму')
            player.location = 10
            return True
        elif num_card == 7:
            print('Отправляйтесь поездом до станции Римская Железная дорога')
            player.location = 5
            print("Игрок {} проходит поле Вперёд и получает 200".format(player.name))
            player.add_balance(200)
            return True
        elif num_card == 9:
            print('Штраф 15')
            player.dec_balance(15)
            return False
        elif num_card == 10:
            print('Отправляйтесь на бесплатную стоянку')
            if player.location == 7:
                player.location = 20
            else:
                print("Игрок {} проходит поле Вперёд и получает 200".format(player.name))
                player.location = 20
                player.add_balance(200)
            return True
        elif num_card == 11:
            print('Получите 150')
            player.add_balance(150)
        elif num_card == 12:
            print('Отправляйтесь на площадь Маяковского')
            if player.location == 7 or player.location == 22:
                player.location = 24
            else:
                player.location = 24
                print("Игрок {} проходит поле Вперёд и получает 200".format(player.name))
                player.add_balance(200)
            return True
        elif num_card == 13:
            print('Вернитесь на три поля назад')
            player.location = player.location - 3
            return True
        elif num_card == 14:
            print('Идите на поле Вперёд')
            player.location = 0
            player.add_balance(200)
            print("Игрок {} проходит поле Вперёд и получает 200".format(player.name))
            return True
