import pygame
import random

class Fruit:
    def __init__(self, fruit_pos):
        self.fruit_pos = fruit_pos
       
    def respawn(self, grid_size, SQUARE_SIZE):
        """Create a new position for the fruit"""
        self.fruit_pos = (random.randrange(0, grid_size[0])*SQUARE_SIZE, random.randrange(0, grid_size[1])*SQUARE_SIZE)
     
    def draw(self, screen, SQUARE_SIZE):
        """Draw the fruit to the screen"""
        pygame.draw.rect(screen, "red", (self.fruit_pos, (SQUARE_SIZE, SQUARE_SIZE)))