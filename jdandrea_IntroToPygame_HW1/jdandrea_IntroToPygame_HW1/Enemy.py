import pygame
import Constants
import math

from Vector import Vector
from Agent import Agent

class Enemy(Agent):
    def __init__(self, position, size, speed ,color):
        super().__init__(position, size, speed, color)
        self.iT = True
        self.chasing = False

        self.yourIT = pygame.time.get_ticks()
        
    
    def __str__(self):
        super().__str__()
        #print("Enemy (" + str(self.x) + ", " + str(self.y) + ")")

    def draw(self, screen, player):        
        if (self.chasing == True):
            super().draw(screen)
            myLine = pygame.draw.line(screen, self.lineColor, self.center, (player.rect.centerx, player.rect.centery), 3)
        else:
            super().draw(screen)

    def update(self, player):
        super().updateEnemy(player)
        
        if (self.iT == True):
            attackVector = player.position - self.position
            attackRange = attackVector.length()         
            
            if (attackRange < Constants.ENEMY_ATTACK_RANGE):
                self.velocity = attackVector.normalize()
                self.lineColor = Constants.ENEMY_LINE_CHASE_COLOR
                self.chasing = True
            else:
                self.velocity = Vector(0,0)
                self.lineColor = Constants.LINE_COLOR
                self.chasing = False
        else:
            attackVector = self.position - player.position
            attackRange = attackVector.length()         
            
            if (attackRange < Constants.ENEMY_ATTACK_RANGE):
                self.velocity = attackVector.normalize()
                self.lineColor = Constants.LINE_COLOR
                self.chasing = True
            else:
                self.velocity = Vector(0,0)
                self.lineColor = Constants.LINE_COLOR
                self.chasing = False

            
            if (super().collisionCheck(player)):
                if (self.iT == True):
                    self.iT = False
                    self.chasing = False
                else:
                    self.iT = True
                

