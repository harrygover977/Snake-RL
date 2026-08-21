import pygame
import random
from snake import Snake
from fruit import Fruit

class Game:
    def __init__(self, screen, WIDTH, HEIGHT, SQUARE_SIZE, grid_size, score, font, MOVE_DELAY, running):
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SQUARE_SIZE = SQUARE_SIZE
        self.score = score
        self.font = font
        self.running = running
        self.MOVE_DELAY = MOVE_DELAY
        self.grid_size = grid_size
        self.last_move = pygame.time.get_ticks()
        self.max_x = self.WIDTH - self.SQUARE_SIZE
        self.max_y = self.HEIGHT - self.SQUARE_SIZE
        self.snake_pos = (20 // 2 * SQUARE_SIZE, 15 // 2 * SQUARE_SIZE)
        self.fruit_pos = (random.randrange(0, self.grid_size[0])*SQUARE_SIZE, random.randrange(0, self.grid_size[1])*SQUARE_SIZE)
        self.snake = Snake(body=[self.snake_pos,
               (self.snake_pos[0]-self.SQUARE_SIZE, self.snake_pos[1])
               ],
              direction=(1, 0)
              )
        self.fruit = Fruit(self.fruit_pos)
    
    def draw_grid(self):
        """Draws a grid background"""
        self.screen.fill((0,0,0))
        # Draw the horizontal lines
        for i in range(self.WIDTH):
            x_pos = i * self.SQUARE_SIZE
            pygame.draw.line(self.screen, (102, 102, 102), (x_pos, 0), (x_pos, self.HEIGHT))
        # Draw the vertical lines
        for i in range(self.HEIGHT):
            y_pos = i * self.SQUARE_SIZE
            pygame.draw.line(self.screen, (102, 102, 102), (0, y_pos), (self.WIDTH, y_pos))
    
    def display_score(self):
        """Create a score rect to be displayed on screen"""
        score_surface = self.font.render(f"Score: {self.score}", True, "white")
        score_rect = score_surface.get_rect()
        score_rect.center = (self.WIDTH // 8, 20)
        return score_surface, score_rect
        
    def get_positions(self):
        """Returns the current straight, left and right positions of the snake"""
        x = self.snake.body[0][0]
        y = self.snake.body[0][1]
        if self.snake.direction == (1, 0):
            straight_position = (x+self.SQUARE_SIZE, y)
            left_position = (x, y-self.SQUARE_SIZE)
            right_position = (x, y+self.SQUARE_SIZE)
        elif self.snake.direction == (-1, 0):
            straight_position = (x-self.SQUARE_SIZE, y)
            left_position = (x, y+self.SQUARE_SIZE)
            right_position = (x, y-self.SQUARE_SIZE)
        elif self.snake.direction == (0, -1):
            straight_position = (x, y-self.SQUARE_SIZE)
            left_position = (x-self.SQUARE_SIZE, y)
            right_position = (x+self.SQUARE_SIZE, y)
        elif self.snake.direction == (0, 1):
            straight_position = (x, y+self.SQUARE_SIZE)
            left_position = (x+self.SQUARE_SIZE, y)
            right_position = (x-self.SQUARE_SIZE, y)
            
        return straight_position, left_position, right_position 

    def is_dangerous_position(self, position):
        """Returns true if the position is outside of the boundary or in the snakes body otherwise it returns false"""
        if position in self.snake.body[1:]:
            return 1
        elif position[0] < 0 or position[0] > self.max_x or position[1] < 0 or position[1] >self.max_y:
            return 1
        else:
            return 0
                
    def get_danger_state(self):
        """Returns a tuple of three elements representing danger"""
        straight_position, left_position, right_position = self.get_positions()
        danger_straight = self.is_dangerous_position(straight_position)
        danger_left = self.is_dangerous_position(left_position)
        danger_right = self.is_dangerous_position(right_position)
        return (danger_straight, danger_left, danger_right)
                
    def get_abs_direction(self):
        """Returns the absolute position of the fruit"""
        snake_x = self.snake.body[0][0]
        snake_y = self.snake.body[0][1]
        fruit_x = self.fruit.fruit_pos[0]
        fruit_y = self.fruit.fruit_pos[1]
        
        horizontal_distance = abs(fruit_x - snake_x)
        vertical_distance = abs(fruit_y - snake_y)
        
        if horizontal_distance >= vertical_distance:
            if fruit_x > snake_x:
                absolute_direction = "RIGHT"
            else:
                absolute_direction = "LEFT"
        else:
            if fruit_y > snake_y:
                absolute_direction = "DOWN"
            else:
                absolute_direction = "UP"
        
        return absolute_direction

    def get_relative_direction(self):
        """Returns the direction of the fruit relative to the snake"""
        absolute_direction = self. get_abs_direction()
        
        relative_directions = {
            (1, 0): {
                "RIGHT": "straight",
                "UP": "left",
                "DOWN": "right",
                "LEFT": "behind"
            },
            (-1, 0): {
                "RIGHT": "behind",
                "UP": "right",
                "DOWN": "left",
                "LEFT": "straight"
            },
            (0, -1): {
                "RIGHT": "right",
                "UP": "straight",
                "DOWN": "behind",
                "LEFT": "left"
            },
            (0, 1): {
                "RIGHT": "left",
                "UP": "behind",
                "DOWN": "straight",
                "LEFT": "right"
            }
        }
        
        relative_direction = relative_directions[self.snake.direction][absolute_direction]
        
        return relative_direction

    def get_food_state(self):
        """Returns a tuple of 4 elements representing the position of the food relative to the snake"""
        relative_direction = self.get_relative_direction()
        
        if relative_direction == "left":
            state =  (1, 0, 0, 0)
        elif relative_direction == "right":
            state = (0, 1, 0, 0)
        elif relative_direction == "straight":
            state = (0, 0, 1, 0)
        else:
            state = (0, 0, 0, 1)
            
        return state

    def get_state(self):
        """Returns the current state of the game"""
        state = ()
        if self.snake.direction == (-1, 0):
            state = state + (1, 0, 0, 0)
        elif self.snake.direction == (1, 0):
            state = state + (0, 1, 0, 0)
        elif self.snake.direction == (0, -1):
            state = state + (0, 0, 1, 0)
        else:
            state = state + (0, 0, 0, 1)
            
        danger_state = self.get_danger_state()
        food_state = self.get_food_state()
        
        state = state + danger_state + food_state
        return state
    
    def detect_collisions(self):
        """Ends the game if a collision is detected"""
        # check if the snake collides with any wall
        if self.snake.body[0][0] < 0 or self.snake.body[0][0] > self.max_x:
            return True
        elif self.snake.body[0][1] < 0 or self.snake.body[0][1] > self.max_y:
            return True
        # Check if the snake collides with itself
        elif self.snake.body[0] in self.snake.body[1:]:
            return True
        else:
            return False
            
        return done 
    
    def spawn_fruit(self):
        """Returns a random position for the fruit to spawn at"""
        fruit_x = random.randrange(0, self.grid_size[0])*self.SQUARE_SIZE
        fruit_y = random.randrange(0, self.grid_size[1])*self.SQUARE_SIZE
        fruit_pos = (fruit_x, fruit_y)
                    
        while fruit_pos in self.snake.body:
            fruit_x = random.randrange(0, self.grid_size[0])*self.SQUARE_SIZE
            fruit_y = random.randrange(0, self.grid_size[1])*self.SQUARE_SIZE
            fruit_pos = (fruit_x, fruit_y)
        
        return fruit_pos
            
    def fruit_eaten(self):
        """Checks if the fruit has been eaten"""
        if self.snake.body[0] == self.fruit.fruit_pos:
            self.score += 1
            self.snake.grow()
            self.fruit.fruit_pos = self.spawn_fruit()
            self.snake.moves = 0
            return True
            
    def handle_events(self):
        """Handles events from user input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
    
    def draw(self):
        """Draws the current game state"""
        score_surface, score_rect = self.display_score()
        self.draw_grid()  
        self.screen.blit(score_surface, score_rect) 
            
        self.fruit.draw(self.screen, self.SQUARE_SIZE)
        
        self.snake.draw(self.screen, self.SQUARE_SIZE)
    
    def reset(self):
        self.score = 0

        snake_pos = (20 // 2 * self.SQUARE_SIZE, 15 // 2 * self.SQUARE_SIZE)
        fruit_pos = self.spawn_fruit()
        self.snake.body = [snake_pos,
               (snake_pos[0]-self.SQUARE_SIZE, snake_pos[1])
               ]
        self.snake.direction = (1, 0)
        
        self.fruit.fruit_pos = fruit_pos
        done  = False
        self.snake.moves = 0
        state = self.get_state()
        
        return state
            
    def step(self, action):
        self.snake.change_direction(action)
        
        self.snake.move(self.SQUARE_SIZE)
        
        if self.detect_collisions():
            reward = -10
            done = True
            return self.get_state(), reward, done
        
        if self.fruit_eaten():
            reward = 10
            self.spawn_fruit()
        else:
            reward = 0
            if self.snake.moves > 1000:
                return self.get_state(), reward, True
            
        state = self.get_state()
        return state, reward, False