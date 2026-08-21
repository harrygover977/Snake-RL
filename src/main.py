import pygame 
from snake import * 
from game import *
from  fruit import *
import random
from agent import *

pygame.init()
game_font = pygame.font.SysFont('Comic Sans MS', 30)

FPS = 60
MOVE_DELAY = 150
WIDTH = 800
HEIGHT = 600
SQUARE_SIZE = 40
score = 0
grid_size = (20, 15)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

game = Game(screen, WIDTH, HEIGHT, SQUARE_SIZE, grid_size, score, game_font, MOVE_DELAY, running=True)
agent = Agent()
state = game.get_state()

iteration = 0
score = 0

while True:
    game.handle_events()
    
    action = agent.get_action(state)
    next_state, reward, done = game.step(action)
    agent.learn(state, action, reward, next_state, done)
    state = next_state
    
    if game.score > score:
        score = game.score
    
    if done:
        state = game.reset()
        agent.decay_epsilon()
        iteration += 1
        print(f"{iteration} - High score: {score}")

    game.draw()
    clock.tick(FPS)
    pygame.display.flip()
