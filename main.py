from game.game import Game

winners = [0, 0]

for i in range(1000):
    g = Game()
    winner = g.play_game()

print(winners)