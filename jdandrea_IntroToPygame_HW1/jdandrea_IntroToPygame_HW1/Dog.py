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
                
            if pressedKey[pygame.K_s]:
                self.velocity.y = 1
                self.currentSpeed = self.maxSpeed
                

            if pressedKey[pygame.K_a]:
                self.velocity.x = -1
                self.currentSpeed = self.maxSpeed
                
            if pressedKey[pygame.K_d]:
                self.velocity.x = 1
                self.currentSpeed = self.maxSpeed
            elif not pressedKey[pygame.K_w] and not pressedKey[pygame.K_s] and not pressedKey[pygame.K_a]:
                self.currentSpeed = 0

        self.updateVelocity(self.velocity)
        super().update()

    def draw(self, screen):
        screen.blit(self.image, [self.position.x, self.position.y])
        super().draw(screen)
        if (self.dogForceLine == True):
            myLine = pygame.draw.line(screen, Constants.LINE_COLOR, (self.center.x, self.center.y), (self.center.x + self.velocity.x * self.size.x, self.center.y + self.velocity.y * self.size.y), 3)
            pygame.display.update(myLine)
            

