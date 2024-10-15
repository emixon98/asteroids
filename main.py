# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    print("Starting asteroids!")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Shot.containers = (shots, updatable, drawable)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable: 
            obj.update(dt)
            
        for a in asteroids:
            if a.collision(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if a.collision(shot):
                    a.split()
                    shot.kill()
                           
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
                
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
              

                
        
    
if __name__ == "__main__":
    main()