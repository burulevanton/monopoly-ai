from game.field import Field

# поле "Шанс"

class Chance(Field):

    def __init__(self, name, location):
        super().__init__(name, location)

    def player_interaction(self, players, player_num, queue1, queue2, num_of_players):
        self.print_info(players, player_num)
        num_card = Chance.get_chance_card(queue1)
        print("Игрок берёт карточку №{}".format(num_card))

    @staticmethod
    def get_chance_card(queue):
        card = queue.get()
        queue.put(card)
        return card
