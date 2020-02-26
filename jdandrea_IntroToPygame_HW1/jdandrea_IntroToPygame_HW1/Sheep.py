import pygame
import Constants
import math
import random
from Vector import Vector
from Agent import Agent

class Sheep(Agent):
    def __init__(self, position, size, speed, image):
        super().__init__(position, size, speed, image)
        self.followingPlayer = False
        #self.isInSeek = True
        self.target = Vector(0,0)
        self.lineToTarg = None
        self.yourIT = pygame.time.get_ticks()

        self.linearAccel = 0
        self.angularVel = Vector(0,0)

        self.velocity = Vector(random.randrange(-1,1), random.randrange(-1,1))
        
                  
    def __str__(self):
        super().__str__()
    #print("Enemy (" + str(self.x) + ", " + str(self.y) + ")")
    
    def switchMode(self):
        self.isInSeek = not self.isInSeek
    
    def isPlayerClose(self, target):
        attackVector = target.position - self.position                    
        attackRange = attackVector.length()           
        if (attackRange <= Constants.ENEMY_ATTACK_RANGE):
            self.followingPlayer = True
            return True
        self.followingPlayer = False
        return False

    def calcTrackingVelocity(self, target):
        self.target = target.center

    def update(self, target):
        self.calcTrackingVelocity(target)
        vectToPlayer = target.position - self.position
        if (self.isPlayerClose(target) == True):
            self.updateVelocity(vectToPlayer * -1)
        else:
            self.updateVelocity(Vector(0,0))

        super().update()

    def draw(self, screen):        
        screen.blit(self.image, [self.position.x, self.position.y])
        if(self.sheepVelLine == True):
            super().draw(screen)                
            if (self.followingPlayer == True):
                self.lineToTarg = pygame.draw.line(screen, Constants.ENEMY_LINE_CHASE_COLOR, (self.center.x, self.center.y), (self.target.x, self.target.y), 3)
            pygame.display.update(self.lineToTarg)
            self.lineToTarg = None

     


