import pygame
import Constants
import math

from Vector import Vector
from Agent import Agent
from Enemy import Enemy

class EnemyHunter(Enemy):
    """description of class"""
    def __init__(self, position, size, speed ,color):
        super().__init__(position, size, speed, color)
        self.iT = True
        self.attacking = True
        self.firstTag = True
        self.yourIT = pygame.time.get_ticks()      
    
    def __str__(self):
        super().__str__()
        #print("Enemy (" + str(self.x) + ", " + str(self.y) + ")")

    def draw(self, screen, player):
        pointToMove = self.calcPlayerPosition(player)
        if (self.iT == True):
            #playerCenter = (player.rect.centerx, player.rect.centery)
            super().drawToPoint(screen, pointToMove)
        else:
            #normalEndPoint = (self.rect.centerx + self.velocity.x * (self.size), self.rect.centery + self.velocity.y * (self.size))
            super().drawToPoint(screen, pointToMove)
    
    def calcPlayerPosition(self, player):
        if (self.iT == True):
            # Chase
            attackVectorX = (player.position.x + (player.velocity.x * player.speed)) - self.position.x
            attackVectorY = (player.position.y + (player.velocity.y * player.speed)) - self.position.y
        else:
            # Flee
            attackVectorX = self.position.x - (player.position.x + (player.velocity.x * player.speed))
            attackVectorY = self.position.y- (player.position.y + (player.velocity.y * player.speed))
        attackVector = Vector(attackVectorX, attackVectorY)
        attackRange = attackVector.length() 
        return attackVector
        
    def update(self, player):
        super().collisionCheck(player)
        super().updateEnemy(player) 

