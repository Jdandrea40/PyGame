import pygame
import Constants
import math

from Vector import Vector
from Agent import Agent

class Enemy(Agent):
    def __init__(self, position, size, speed ,color):
        super().__init__(position, size, speed, color)
        self.iT = True
        self.firstTag = True
        self.attacking = False
        self.yourIT = pygame.time.get_ticks()
      
    
    def __str__(self):
        super().__str__()
        #print("Enemy (" + str(self.x) + ", " + str(self.y) + ")")

    def draw(self, screen, player):        
        if (self.iT == True):
            #playerCenter = (player.rect.centerx, player.rect.centery)
            super().drawToPoint(screen, player)
        else:
            #normalEndPoint = (self.rect.centerx + self.velocity.x * (self.size), self.rect.centery + self.velocity.y * (self.size))
            super().draw(screen)

    def update(self, player):
        super().collisionCheck(player)
        super().updateEnemy(player) 
        
           
                

