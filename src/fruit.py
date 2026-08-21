import pygame
import random

class Fruit:
    def __init__(self, fruit_pos):
        self.fruit_pos = fruit_pos
     
    def draw(self, screen, SQUARE_SIZE):
        """Draw the fruit to the screen"""
        pygame.draw.rect(screen, "red", (self.fruit_pos, (SQUARE_SIZE, SQUARE_SIZE)))