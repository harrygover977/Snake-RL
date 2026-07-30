import pygame 
from snake import * 
from game import *
from fruit import *
import random

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

snake_pos = (20 // 2 * SQUARE_SIZE, 15 // 2 * SQUARE_SIZE)
fruit_pos = (random.randrange(0, grid_size[0])*SQUARE_SIZE, random.randrange(0, grid_size[1])*SQUARE_SIZE)

snake = Snake(body=[snake_pos,
               (snake_pos[0]-SQUARE_SIZE, snake_pos[1])
               ],
              current_direction="RIGHT",
              next_direction="RIGHT"
              )
game = Game(screen, WIDTH, HEIGHT, SQUARE_SIZE, grid_size, score, game_font, MOVE_DELAY, running=True)
fruit = Fruit(fruit_pos)

while game.running:
    
    game.handle_events(snake)
            
    game.update(snake, fruit)

    game.draw(snake, fruit)

    clock.tick(FPS)
    pygame.display.flip()