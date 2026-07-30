import pygame

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
    
    def display_score(self, WIDTH):
        """Create a score rect to be displayed on screen"""
        score_surface = self.font.render(f"Score: {self.score}", True, "white")
        score_rect = score_surface.get_rect()
        score_rect.center = (WIDTH // 8, 20)
        return score_surface, score_rect
    
    def detect_collisions(self, snake_body, WIDTH, HEIGHT, SQUARE_SIZE):
        """Ends the game if a collision is detected"""
        # check if the snake collides with any wall
        if snake_body[0][0] < 0 or snake_body[0][0] > WIDTH - SQUARE_SIZE:
            self.running = False
        if snake_body[0][1] < 0 or snake_body[0][1] > HEIGHT - SQUARE_SIZE:
            self.running = False
            
        # Check if the snake collides with itself
        if snake_body[0] in snake_body[1:]:
            self.running = False
    
    def fruit_eaten(self, snake, fruit, grid_size, SQUARE_SIZE):
        """Checks if the fruit has been eaten"""
        if snake.body[0] == fruit.fruit_pos:
            self.score += 1
            snake.grow()
            fruit.respawn(grid_size, SQUARE_SIZE)
            
    def handle_events(self, snake):
        """Handles events from user input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and snake.current_direction != "UP":
                    snake.next_direction ="DOWN"
                elif event.key == pygame.K_UP and snake.current_direction != "DOWN":
                    snake.next_direction = "UP"
                elif event.key == pygame.K_RIGHT and snake.current_direction != "LEFT":
                    snake.next_direction = "RIGHT"
                elif event.key == pygame.K_LEFT and snake.current_direction != "RIGHT":
                    snake.next_direction = "LEFT"
    
    def update(self, snake, fruit):
        """Updates the game state"""
        current_time = pygame.time.get_ticks()  
            
        if current_time - self.last_move >= self.MOVE_DELAY:
            snake.move(self.SQUARE_SIZE)
            self.last_move = current_time
        
        self.fruit_eaten(snake, fruit, self.grid_size, self.SQUARE_SIZE)
            
        running = self.detect_collisions(snake.body, self.WIDTH, self.HEIGHT, self.SQUARE_SIZE)
    
    def draw(self, snake, fruit):
        """Draws the current game state"""
        score_surface, score_rect = self.display_score(self.WIDTH)
        self.draw_grid()  
        self.screen.blit(score_surface, score_rect) 
            
        if fruit.fruit_pos in snake.body:
            fruit.respawn(self.grid_size, self.SQUARE_SIZE)
        else:
            fruit.draw(self.screen, self.SQUARE_SIZE)
        
        snake.draw(self.screen, self.SQUARE_SIZE)
            
        