import pygame
import Constants

from Agent import Agent
from Vector import Vector

class Player(Agent):
    def __init__(self, position, size, speed, color):
        super().__init__(position, size, speed, color)

    def draw(self, screen):
        super().draw(screen)
        
    def update(self, pressedKey):
        # player movement
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

        super().update()

