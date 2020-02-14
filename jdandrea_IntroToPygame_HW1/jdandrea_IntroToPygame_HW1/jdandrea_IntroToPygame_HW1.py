import pygame
import Vector
import Player
import Constants

from pygame.locals import *
from Vector import Vector
from Player import Player

pygame.init()
screen = pygame.display.set_mode((Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT))
done = False

playerVector = Vector(Constants.WORLD_WIDTH / 2, Constants.WORLD_HEIGHT / 2)
playerVel = Vector(0,0)
player = Player(playerVector, playerVel, 25, [255, 0, 0])

enemyVector = Vector(700, 300)
enemyVel = Vector(0,0)
enemy = Player(enemyVector, enemyVel, 25, [0, 255, 0, 0])

# frame rate object
fps = pygame.time.Clock()
  
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        # sets the framerate
        fps.tick(Constants.FRAME_RATE)
        # redraws the screen (stops the "paint" feature)
        screen.fill(Constants.BACKGROUND_COLOR)
        pygame.display.flip()

        player.draw(screen)
        enemy.draw(screen)


        player.playerMove(pygame.key.get_pressed())


        
            
        
