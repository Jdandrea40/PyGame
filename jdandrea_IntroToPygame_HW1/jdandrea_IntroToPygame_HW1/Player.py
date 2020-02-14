import pygame
import Vector

class Player(object):
    def __init__(self, position, velocity, size, color):
        self.position = position
        self.velocity = velocity
        self.size = size
        self.color = color

    def draw(self, screen):
        pRect = pygame.draw.rect(screen, self.color,  [self.position.x, self.position.y, self.size, self.size], 0)
        pygame.display.update(pRect)
        pygame.display.update(pygame.draw.line(screen, (0, 0, 255), pRect.center, (pRect.centerx + self.velocity.x * self.size, pRect.centery + self.velocity.y * self.size), 3))        
    
    def playerMove(self, pressedKey):
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
            

        self.position += self.velocity


