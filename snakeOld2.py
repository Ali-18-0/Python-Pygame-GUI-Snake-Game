import pygame
from pygame.locals import *
import time
from random import randint

sizeX = 40
sizeY = 40

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("apple2.jpg").convert()
        self.x = sizeX * 3
        self.y = sizeY * 3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))    
        pygame.display.flip()

    def move(self):
        self.x = randint(1, 34) * sizeX    
        self.y = randint(1, 18) * sizeY  # Corrected: Ensure y-coordinate is set correctly

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
        self.parent_screen.fill((52, 232, 235))  # Clears the screen with a background color
        
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
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        
    def play(self):
        self.snake.walk()
        self.apple.draw()
        
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()
            
        for i in range(3,self.snake.length):
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                print("GAME OVER!! ")
                exit(0)    
    
    def is_collision(self, x1, y1, x2, y2):
        if (x1 >= x2 and x1 < x2 + sizeX):  # Adjusted collision logic
            if (y1 >= y2 and y1 < y2 + sizeY):  # Adjusted collision logic
                return True
        return False    
              
                
    def run(self):
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
            time.sleep(0.1)  # Reduced delay to 0.1 seconds for faster updates

  
if __name__ == "__main__":
    game = Game()
    game.run()