import pygame
import Vector
import Constants
import math

from Vector import Vector

class Enemy(object):
    def __init__(self, position, speed, size):
        self.position = position
        self.speed = speed
        self.size = size

        self.velocity = Vector(0,0)
        self.color = Constants.ENEMY_COLOR
    
    def __str__(self):
        print("Enemy (" + str(self.x) + ", " + str(self.y) + ")")

    def draw(self, screen):
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)
        pRect = pygame.draw.rect(screen, self.color, self.rect)
        pLine = pygame.draw.line(screen, (0, 0, 255), pRect.center, (pRect.centerx + self.velocity.x * (self.size), pRect.centery + self.velocity.y * (self.size)), 3)
        
        pygame.display.update(pLine)        
        pygame.display.update(pRect)

    def update(self, player):
        attackVector = player.position - self.position
        attackRange = attackVector.length()        

        if (attackRange < Constants.ENEMY_ATTACK_RANGE):
            self.velocity = attackVector.normalize()            
        else:
            self.velocity = Vector(0,0)

        self.position = self.position + (self.velocity * self.speed)

