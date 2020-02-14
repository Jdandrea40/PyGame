import pygame
import Vector
import Player

from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False

playerVector = Vector.Vector(50, 50)
playerVel = Vector.Vector(0,0)
player = Player.Player(playerVector, playerVel, 25, [255, 0, 0])

# frame rate object
fps = pygame.time.Clock()
  
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        # sets the framerate
        fps.tick(60)
        # redraws the screen (stops the "paint" feature)
        screen.fill((100, 149, 237))
        pygame.display.flip()

        player.draw(screen)
        player.playerMove(pygame.key.get_pressed())


        
            
        
