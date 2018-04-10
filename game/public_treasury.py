from game.field import Field

# класс, отвечающий за поле Общественная казна


class PublicTreasury(Field):

    def __init__(self, name, location):
        super().__init__(name, location)

    def player_interaction(self, players, player_num, queue1, queue2, num_of_players):
        self.print_info(players, player_num)
        num_card = PublicTreasury.get_treasury_card(queue2)
        print("Игрок {} берёт карточку №{}".format(players[player_num].name, num_card))

    @staticmethod
    def get_treasury_card(queue):
        card = queue.get()
        queue.put(card)
        return card