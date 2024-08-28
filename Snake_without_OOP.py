import pygame
from pygame.locals import *

def draw_block(block,block_x,block_y):
    surface.fill((52, 232, 235))
    surface.blit(block,(block_x,block_y))
    pygame.display.flip()

if __name__=="__main__":
    pygame.init()
    
    surface = pygame.display.set_mode((1400,750))
    pygame.display.set_caption("Snake Game 69")
    surface.fill((52, 232, 235))
    
    block = pygame.image.load("Capture3.png").convert()
    
    block_x = 500
    block_y = 500
    surface.blit(block,(block_x,block_y))
    
    pygame.display.flip()
    running = True
    
    while running:
        for event in pygame.event.get():
            if (event.type == KEYDOWN):
                if (event.key == K_ESCAPE):
                    running = False
                elif (event.key == K_UP):
                    block_y = block_y - 10
                    draw_block(block,block_x,block_y)
                elif (event.key == K_DOWN):
                    block_y = block_y + 10
                    draw_block(block,block_x,block_y)
                elif (event.key == K_RIGHT):
                     block_x = block_x + 10 
                     draw_block(block,block_x,block_y)      
                elif (event.key == K_LEFT):
                    block_x = block_x - 10
                    draw_block(block,block_x,block_y)      
            elif (event.type == QUIT):
                running = False