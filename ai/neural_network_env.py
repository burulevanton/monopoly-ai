import numpy as np


class NeuralNetworkEnv:

    def __init__(self):
        self.index_of_properties = ['brown', 'blue', 'pink', 'orange', 'red', 'yellow', 'green', 'dark_blue',
                                    'utility', 'railway']
        self.current_state = []
        self.current_action = None

    @staticmethod
    def create_numpy_state(state):
        temp_state = []
        temp_state.extend(state.area_player)
        temp_state.extend(state.area_other_player)
        temp_state.extend(state.finance)
        temp_state.extend(state.action_state)
        state = np.array(temp_state)
        return state.reshape(1, 25)

    def buy_property_state(self, game, player, field, price):
        state = game.create_game_state_for_player(player)
        state.action_state.append(0.2)
        state.action_state.append((self.index_of_properties.index(field.kind) + 1) / 10)
        state.action_state.append(-price / (player.balance+price))
        state = self.create_numpy_state(state)
        if len(self.current_state) > 0:
            reward = game.calculate_reward(player)
            done = not game.game_in_progress
            player.record(self.current_state, self.current_action, reward, state, int(done))
        self.current_state = state
        return state

    def build_house_state(self, game, player, field):
        state = game.create_game_state_for_player(player)
        state.action_state.append(0.4)
        state.action_state.append((self.index_of_properties.index(field.kind) + 1) / 10)
        state.action_state.append(-field.cost_of_upgrade / (player.balance+field.cost_of_upgrade))
        state = self.create_numpy_state(state)
        reward = game.calculate_reward(player)
        done = not game.game_in_progress
        player.record(self.current_state, self.current_action, reward, state, int(done))
        self.current_state = state
        return state

    def sell_house_state(self, game, player, field):
        state = game.create_game_state_for_player(player)
        state.action_state.append(0.6)
        state.action_state.append((self.index_of_properties.index(field.kind) + 1) / 10)
        state.action_state.append((field.cost_of_upgrade//2) / (player.balance+field.cost_of_upgrade//2))
        state = self.create_numpy_state(state)
        reward = game.calculate_reward(player)
        done = not game.game_in_progress
        player.record(self.current_state, self.current_action, reward, state, int(done))
        self.current_state = state
        return state

    def mortgage_property_state(self, game, player, field):
        state = game.create_game_state_for_player(player)
        state.action_state.append(0.8)
        state.action_state.append((self.index_of_properties.index(field.kind) + 1) / 10)
        state.action_state.append( (field.cost//2) / (player.balance+field.cost//2))
        state = self.create_numpy_state(state)
        reward = game.calculate_reward(player)
        done = not game.game_in_progress
        player.record(self.current_state, self.current_action, reward, state, int(done))
        self.current_state = state
        return state

    def redeem_property_state(self, game, player, field):
        state = game.create_game_state_for_player(player)
        state.action_state.append(1.0)
        state.action_state.append((self.index_of_properties.index(field.kind) + 1) / 10)
        state.action_state.append(-field.redeem_cost / (player.balance+field.redeem_cost))
        state = self.create_numpy_state(state)
        reward = game.calculate_reward(player)
        done = not game.game_in_progress
        player.record(self.current_state, self.current_action, reward, state, int(done))
        self.current_state = state
        return state
