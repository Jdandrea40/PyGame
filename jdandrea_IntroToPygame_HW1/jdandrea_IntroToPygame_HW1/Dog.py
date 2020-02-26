import pygame
import Constants

from Agent import Agent
from Vector import Vector

class Dog(Agent):
    def update(self, pressedKey):
        
        if (pressedKey is not None):
            # player movement
            if pressedKey[pygame.K_w]:
                self.velocity.y = -1
                self.currentSpeed = self.maxSpeed
                
            elif pressedKey[pygame.K_s]:
                self.velocity.y = 1
                self.currentSpeed = self.maxSpeed
                

            if pressedKey[pygame.K_a]:
                self.velocity.x = -1
                self.currentSpeed = self.maxSpeed
                
            elif pressedKey[pygame.K_d]:
                self.velocity.x = 1
                self.currentSpeed = self.maxSpeed
                
        else:
            self.currentSpeed = 0

        self.updateVelocity(Vector(self.velocity.x, self.velocity.y))
        super().update()

    def draw(self, screen):
        screen.blit(self.image, [self.position.x, self.position.y])

        if (self.dogForceLine == True):
            super().draw(screen)

