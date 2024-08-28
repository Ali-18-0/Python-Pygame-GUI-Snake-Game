import pygame
from pygame.locals import *
import time
from random import randint

sizeX = 40
sizeY = 40

class Apple:
    def __init__(self, parent_screen, snake):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("apple2.jpg").convert()
        self.snake = snake
        self.move()

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        while True:
            self.x = randint(1, 34) * sizeX
            self.y = randint(1, 18) * sizeY
            # Check if the new position is not on the snake
            if (self.x, self.y) not in zip(self.snake.x, self.snake.y):
                break

class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("block.jpg").convert()
        self.length = length
        self.x = [sizeX * i for i in range(length)]  # Correctly spaced initial positions
        self.y = [sizeY] * length
        self.direction = "right"

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        self.parent_screen.fill((46, 2, 168))  # Clears the screen with a background color
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))  # Draws the block image at (self.x, self.y)
        pygame.display.flip()  # Updates the display to show the changes

    def moveup(self):
        if self.direction != "down":  # Prevent reversing direction
            self.direction = "up"

    def movedown(self):
        if self.direction != "up":  # Prevent reversing direction
            self.direction = "down"

    def moveright(self):
        if self.direction != "left":  # Prevent reversing direction
            self.direction = "right"

    def moveleft(self):
        if self.direction != "right":  # Prevent reversing direction
            self.direction = "left"

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == "up":
            self.y[0] -= sizeY  # Use the same spacing as initialization
        elif self.direction == "down":
            self.y[0] += sizeY  # Use the same spacing as initialization
        elif self.direction == "right":
            self.x[0] += sizeX  # Use the same spacing as initialization
        elif self.direction == "left":
            self.x[0] -= sizeX  # Use the same spacing as initialization

        self.draw()

class Game:
    def __init__(self):
        pygame.init()  # Initializes Pygame
        self.surface = pygame.display.set_mode((1400, 750))  # Creates a display surface
        pygame.display.set_caption("Snake Game 69")  # Sets the window title
        self.snake = Snake(self.surface, 2)
        self.apple = Apple(self.surface, self.snake)
        self.speed = 0.1

    def show_menu(self):
        font = pygame.font.SysFont('arial', 40)
        self.surface.fill((46, 2, 168))
        options = ["1. New Game", "2. Set Speed Level", "3. Exit"]
        for i, option in enumerate(options):
            text = font.render(option, True, (0, 0, 0))
            self.surface.blit(text, (500, 300 + i * 50))
        pygame.display.flip()
        
        menu_option = None
        while menu_option is None:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_1:
                        menu_option = "new_game"
                    elif event.key == K_2:
                        menu_option = "set_speed"
                    elif event.key == K_3:
                        menu_option = "exit"
                elif event.type == QUIT:
                    menu_option = "exit"
        return menu_option

    def set_speed(self):
        font = pygame.font.SysFont('arial', 40)
        self.surface.fill((52, 232, 235))
        options = ["1. Slow", "2. Medium", "3. Fast"]
        for i, option in enumerate(options):
            text = font.render(option, True, (0, 0, 0))
            self.surface.blit(text, (500, 300 + i * 50))
        pygame.display.flip()
        
        speed_option = None
        while speed_option is None:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_1:
                        speed_option = 0.3
                    elif event.key == K_2:
                        speed_option = 0.1
                    elif event.key == K_3:
                        speed_option = 0.05
                elif event.type == QUIT:
                    speed_option = 0.1
        self.speed = speed_option

    def play(self):
        self.snake.walk()
        self.apple.draw()
        
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()
            
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.show_game_over_menu()
    
    def is_collision(self, x1, y1, x2, y2):
        if (x1 >= x2 and x1 < x2 + sizeX) and (y1 >= y2 and y1 < y2 + sizeY):
            return True
        # Check if snake's head is outside the playable area
        if x1 < 0 or x1 >= 1400 or y1 < 0 or y1 >= 750:
            return True
        return False


    def show_game_over_menu(self):
        font = pygame.font.SysFont('arial', 40)
        self.surface.fill((52, 232, 235))
        options = ["GAME OVER!", "1. Play Again", "2. Exit"]
        for i, option in enumerate(options):
            text = font.render(option, True, (0, 0, 0))
            self.surface.blit(text, (500, 300 + i * 50))
        pygame.display.flip()

        game_over_option = None
        while game_over_option is None:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_1:
                        game_over_option = "play_again"
                    elif event.key == K_2:
                        game_over_option = "exit"
                elif event.type == QUIT:
                    game_over_option = "exit"
        if game_over_option == "play_again":
            self.snake = Snake(self.surface, 2)
            self.apple = Apple(self.surface, self.snake)
            self.run()
        else:
            exit(0)
                
    def run(self):
        menu_option = self.show_menu()
        if menu_option == "exit":
            exit(0)
        elif menu_option == "set_speed":
            self.set_speed()

        running = True  # Flag to control the main loop
        while running:
            for event in pygame.event.get():  # Iterates over events detected by Pygame
                if (event.type == KEYDOWN): 
                    if (event.key == K_ESCAPE):
                        running = False  
                    elif (event.key == K_UP):  
                        self.snake.moveup()
                    elif (event.key == K_DOWN):  
                        self.snake.movedown()
                    elif (event.key == K_RIGHT):  
                        self.snake.moveright()
                    elif (event.key == K_LEFT):  
                        self.snake.moveleft()
                elif (event.type == QUIT): 
                    running = False
            
            self.play()
            time.sleep(self.speed)  # Adjusted speed for game

  
if __name__ == "__main__":
    game = Game()
    game.run()
