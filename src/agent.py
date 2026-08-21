import numpy as np
import random

class Agent:
    
    def __init__(self):
        self.alpha = 0.5 # learning rate
        self.gamma = 0.9 # discount factor
        self.epsilon = 0.8
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.01
        
        self.q_table = np.zeros((2048, 3))
        
    def get_state_index(self, state):
        """Returns a value between 0 and 2047 depeding on the current state"""
        index = 0
        
        for value in state:
            index = (index << 1) | value
            
        return index
    
    def get_action(self, state):
        """Returns the next action to perform"""
        state_index = self.get_state_index(state)
        q_values = self.q_table[state_index]
        
        if random.random() < self.epsilon:
            action = random.randint(0, 2)
        else:
            action = np.argmax(q_values)           
        return action 

    def decay_epsilon(self):
        """Reduces the epsilon value"""
        self.epsilon = max(
        self.epsilon_min,
        self.epsilon * self.epsilon_decay
    )
    
    def learn(self, state, action, reward, next_state, done):
        """Updates the q_table from the knowledge of the previous state"""
        state_index = self.get_state_index(state)
        next_state_index = self.get_state_index(next_state)
        
        current_q_value = self.q_table[state_index][action]
        
        if done:
            target = reward
        else:
            target = reward + self.gamma * max(self.q_table[next_state_index])
        
        new_q_value = current_q_value + (self.alpha * (target - current_q_value))
            
        self.q_table[state_index][action] = new_q_value
        