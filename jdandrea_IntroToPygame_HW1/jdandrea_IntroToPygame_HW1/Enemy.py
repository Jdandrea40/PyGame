import pygame
import Constants
import math

from Vector import Vector
from Agent import Agent

class Enemy(Agent):
    def __init__(self, position, size, speed ,color):
        super().__init__(position, size, speed, color)
        self.color = Constants.ENEMY_COLOR
        self.ogColor = self.color
        self.isInSeek = True
        self.firstTag = True
        self.followingPlayer = False
        self.yourIT = pygame.time.get_ticks()
          
    def __str__(self):
        super().__str__()
        #print("Enemy (" + str(self.x) + ", " + str(self.y) + ")")

    def draw(self, screen, player):        
        if (self.isInSeek == True):
            x = (player.position.x + (player.size  / 2))
            y = (player.position.y + (player.size  / 2))
            playerVect = Vector(x, y)
            super().drawToPoint(screen, playerVect)
        else:
            super().draw(screen)

    def update(self, player):
        if (self.isInSeek == True):
            attackVector = player.position - self.position                    
        else:
            attackVector = self.position - player.position        
        
        attackRange = attackVector.length()     
        
        if (attackRange < Constants.ENEMY_ATTACK_RANGE):
            self.velocity = attackVector.normalize()
            if (self.isInSeek == True):
                self.lineColor = Constants.ENEMY_LINE_CHASE_COLOR
                self.followingPlayer = True
            else:
                self.lineColor = Constants.LINE_COLOR
                self.followingPlayer = False                
        else:
            self.velocity = Vector(0,0)
            self.lineColor = Constants.LINE_COLOR
            self.followingPlayer = False

        super().collisionCheck(player)
        super().update() 
        
           
                

