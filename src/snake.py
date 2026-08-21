import pygame

class Snake:
    def __init__(self, body, direction):
        self.body = body
        self.direction = direction
        
        self.DIRECTIONS = [
            (0, -1),   # UP
            (1, 0),    # RIGHT
            (0, 1),    # DOWN
            (-1, 0)    # LEFT
        ]
        self.moves = 0
        
    def change_direction(self, action):
        """Change direction based on a relative action."""

        current_index = self.DIRECTIONS.index(self.direction)

        if action == 1:        # left
            new_index = (current_index - 1) % 4

        elif action == 2:      # right
            new_index = (current_index + 1) % 4
        else:                  # straight
            new_index = current_index

        self.direction = self.DIRECTIONS[new_index]
        
        
        
    def move(self, SQUARE_SIZE):
        """Updates the position of the body depending on the action selected"""
        body_copy = self.body[:]
        if self.direction == (0, 1):
            body_copy.insert(0, (body_copy[0][0], body_copy[0][1] + 40))
            body_copy.pop()
        elif self.direction == (0, -1):
            body_copy.insert(0, (body_copy[0][0], body_copy[0][1] - 40))
            body_copy.pop()
        elif self.direction == (-1, 0):
            body_copy.insert(0, (body_copy[0][0] - 40, body_copy[0][1]))
            body_copy.pop()
        elif self.direction == (1, 0):
            body_copy.insert(0, (body_copy[0][0] + 40, body_copy[0][1]))
            body_copy.pop()
        
        self.body = body_copy
        self.moves += 1
    
        
    def grow(self):
        """Updates the size of the snake by one square"""
        body_copy = self.body[:]
        if self.direction == (0, -1):
            body_copy.insert(0, (body_copy[0][0], body_copy[0][1] - 40))
        elif self.direction == (0, 1):
            body_copy.insert(0, (body_copy[0][0], body_copy[0][1] + 40))
        elif self.direction == (-1, 0):
            body_copy.insert(0, (body_copy[0][0] - 40, body_copy[0][1]))
        else:
            body_copy.insert(0, (body_copy[0][0] + 40, body_copy[0][1]))
        
        self.body = body_copy
        
    def draw(self, screen, SQUARE_SIZE):
        """Draws the snake to the screen"""
        for pos in self.body:
            pygame.draw.rect(screen, "blue",
                         pygame.Rect(pos[0], pos[1], SQUARE_SIZE, SQUARE_SIZE))

    
    