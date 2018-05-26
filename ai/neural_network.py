from game.player import Player
import random
import copy
from collections import deque
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from ai.neural_network_env import NeuralNetworkEnv
from keras.utils import plot_model
import time


class NeuralNetworkPLayer(Player):

    def __init__(self, player_num, do_train= True):
        super().__init__('neural_network_player№{}'.format(player_num), player_num)

        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.1
        self.batch_size = 32
        self.alpha = 0.2

        self.action_size = 3

        self.memory = deque(maxlen=100)

        self.do_train = do_train

        self.model = Sequential()
        self.model.add(Dense(200, activation='relu', input_dim=25))
        self.model.add(Dense(75, activation='relu'))
        self.model.add(Dense(3, activation='tanh'))
        self.model.compile(Adam(lr=0.01), 'mean_squared_error')
        self.model.load_weights('weights.h5')

        self.env = NeuralNetworkEnv()

    def select_action(self, state):
        if self.do_train and np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        return np.argmax(self.model.predict(state)[0])

    def record(self, state, action, reward, next_state, done):
        if len(self.memory) == 100:
            self.memory.clear()
        self.memory.append((state, action, reward, next_state, done))

    def replay(self):
        if len(self.memory) < self.batch_size:
            return
        batch = random.sample(self.memory, self.batch_size)
        for state, action, reward, next_state, done in batch:
            target = reward
            if not done:
                target = reward + self.gamma * np.amax(self.model.predict(next_state)[0])
            target_f = self.model.predict(state)
            # target_f[0][action] = target
            target_f[0][action] = (1-self.alpha)*target_f[0][action] + self.alpha*target
            self.model.fit(state, target_f, epochs=1, verbose=2)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def landed_on_unowned_property(self, game, field):
        state = self.env.create_state(game, self, field)
        action = self.select_action(state)
        if action == 0:
            self.env.record_action(game, self)
            self.env.current_action = action
        else:
            self.env.record_action(game, self)
            self.env.current_action = 2
        return self.env.current_action == 0
        #return bool(self.env.current_action)

    def property_offered_for_auction(self, game, field, price):
        state = self.env.create_state(game, self, field)
        action = self.select_action(state)
        if action == 0:
            self.env.record_action(game, self)
            self.env.current_action = action
        else:
            self.env.record_action(game, self)
            self.env.current_action = 2
        return self.env.current_action == 0
        #return bool(self.env.current_action)

    def build_house(self, game, field):
        state = self.env.create_state(game, self, field)
        action = self.select_action(state)
        if action == 0:
            self.env.record_action(game, self)
            self.env.current_action = action
        else:
            self.env.record_action(game, self)
            self.env.current_action = 2
        return self.env.current_action == 0
        # return bool(self.env.current_action)

    def sell_house(self, game, field):
        state = self.env.create_state(game, self, field)
        action = self.select_action(state)
        if action == 1:
            self.env.record_action(game, self)
            self.env.current_action = action
        else:
            self.env.record_action(game, self)
            self.env.current_action = 2
        return self.env.current_action == 1
        #return bool(self.env.current_action)

    def mortgage_property(self, game, field):
        state = self.env.create_state(game, self, field)
        action = self.select_action(state)
        if action == 1:
            self.env.record_action(game, self)
            self.env.current_action = action
        else:
            self.env.record_action(game, self)
            self.env.current_action = 2
        return self.env.current_action == 1
        # state = self.env.mortgage_property_state(game, self, field)
        # self.env.current_action = self.select_action(state)
        # return self.env.current_action == 1
        #return bool(self.env.current_action)

    def redeem_property(self, game, field):
        state = self.env.create_state(game, self, field)
        action = self.select_action(state)
        if action == 0:
            self.env.record_action(game, self)
            self.env.current_action = action
        else:
            self.env.record_action(game, self)
            self.env.current_action = 2
        return self.env.current_action == 0
        #return bool(self.env.current_action)

    def get_out_of_jail(self, game):
        if self.balance > 50:
            return True
        else:
            return False
