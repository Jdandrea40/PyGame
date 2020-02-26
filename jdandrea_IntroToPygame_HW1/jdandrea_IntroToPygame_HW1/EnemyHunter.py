import pygame
import Constants
import math

from Vector import Vector
from Agent import Agent
from Enemy import Enemy

class EnemyHunter(Enemy):
    def __init__(self, position, size, speed ,color):
        super().__init__(position, size, speed, color)
    
    def draw(self, screen, player):         
        self.vectToPlayer = player.position - self.position
        self.distToPlayer = self.vectToPlayer.length()
        self.timeToPlaya = self.distToPlayer / self.currentSpeed
        self.playaPosition = player.position + (player.velocity * self.timeToPlaya)
        
        if (self.followingPlayer == True):
            super().drawToPoint(screen, self.playaPosition)
        else:
            super().draw(screen, player)

    def update(self, player):
        
        self.velocity = (self.playaPosition - self.position).normalize()
        super().update(player)

