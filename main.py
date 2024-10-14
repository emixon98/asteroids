# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    
    print("Starting asteroids!")
    print("Screen width: {}".format(SCREEN_WIDTH))
    print("Screen height: {}".format(SCREEN_HEIGHT))
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()
    
    
    while True:
        screen.fill((0, 0, 0))
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
                
        
    
if __name__ == "__main__":
    main()