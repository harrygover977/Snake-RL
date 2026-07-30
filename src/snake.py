import pygame

class Snake:
    def __init__(self, body, current_direction, next_direction):
        self.body = body
        self.current_direction = current_direction
        self.next_direction = next_direction 
        
    def move(self, SQUARE_SIZE):
        """Updates the position of the body depending on the key pressed"""
        body_copy = self.body[:]
        if self.next_direction == "UP":
            body_copy.insert(0, (body_copy[0][0], body_copy[0][1] - 40))
            body_copy.pop()
        elif self.next_direction == "DOWN":
            body_copy.insert(0, (body_copy[0][0], body_copy[0][1] + 40))
            body_copy.pop()
        elif self.next_direction == "LEFT":
            body_copy.insert(0, (body_copy[0][0] - 40, body_copy[0][1]))
            body_copy.pop()
        else:
            body_copy.insert(0, (body_copy[0][0] + 40, body_copy[0][1]))
            body_copy.pop()
        
        self.body = body_copy
        self.current_direction = self.next_direction
        
    def grow(self):
        """Updates the size of the snake by one square"""
        body_copy = self.body[:]
        if self.current_direction == "UP":
            body_copy.insert(0, (body_copy[0][0], body_copy[0][1] - 40))
        elif self.current_direction == "DOWN":
            body_copy.insert(0, (body_copy[0][0], body_copy[0][1] + 40))
        elif self.current_direction == "LEFT":
            body_copy.insert(0, (body_copy[0][0] - 40, body_copy[0][1]))
        else:
            body_copy.insert(0, (body_copy[0][0] + 40, body_copy[0][1]))
        
        self.body = body_copy
        
    def draw(self, screen, SQUARE_SIZE):
        """Draws the snake to the screen"""
        for pos in self.body:
            pygame.draw.rect(screen, "blue",
                         pygame.Rect(pos[0], pos[1], SQUARE_SIZE, SQUARE_SIZE))

    
    