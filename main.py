from game.game import Game

winners = [0, 0]

for _ in range(100):
    g = Game()
    winner = g.play_game()
    winners[winner] += 1

print(winners)