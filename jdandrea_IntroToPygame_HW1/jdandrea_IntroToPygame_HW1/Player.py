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
        

        if pressedKey[pygame.K_w]:
            self.velocity.y = -1
        elif pressedKey[pygame.K_s]:
            self.velocity.y = 1
        else:
            self.velocity.y = 0

        if pressedKey[pygame.K_a]:
            self.velocity.x = -1
        elif pressedKey[pygame.K_d]:
            self.velocity.x = 1
        else:
            self.velocity.x = 0
        self.velocity = self.velocity.normalize()
        super().updatePlayer()
        #self.velocity.__str__()
        #self.position.__str__()            

