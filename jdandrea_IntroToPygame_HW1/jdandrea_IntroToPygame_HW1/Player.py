import pygame
import Vector
import Constants

from Vector import Vector

class Player(object):
    def __init__(self, position, size, speed):
        self.position = position
        self.speed = speed
        self.size = size

        self.velocity = Vector(0, 0)
        self.color = Constants.PLAYER_COLOR

    def draw(self, screen):
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)
        pRect = pygame.draw.rect(screen, self.color, self.rect)
        pLine = pygame.draw.line(screen, (0, 0, 255), pRect.center, (pRect.centerx + self.velocity.x * (self.size), pRect.centery + self.velocity.y * (self.size)), 3)
        
        pygame.display.update(pLine)        
        pygame.display.update(pRect)
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
        self.position = self.position + (self.velocity * self.speed)
        #self.velocity.__str__()
        #self.position.__str__()            

