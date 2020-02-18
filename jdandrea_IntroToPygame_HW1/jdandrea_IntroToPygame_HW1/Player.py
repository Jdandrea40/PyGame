import pygame
import Vector
import Constants

from Agent import Agent
from Vector import Vector

class Player(Agent):
    def __init__(self, position, size, speed, color):
        super().__init__(position, size, speed, color)

    def draw(self, screen):

        super().draw(screen)
        #eRect = pygame.draw.rect(screen, ((0, 255, 0)),  [100, 100, self.size, self.size], 0)
        #pygame.display.update(eRect)
        
        #if (pRect.colliderect(eRect)):
            #self.color = ((50, 50, 50))
        #else:
            #self.color = (0, 255, 0)

        
    def update(self, pressedKey):
        super().updatePlayer(pressedKey)
        #self.velocity.__str__()
        #self.position.__str__()            

