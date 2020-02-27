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
        self.target = Vector(0,0)
        self.lineToTarg = None

        self.velocity = Vector(random.randrange(-1,1), random.randrange(-1,1))
        self.updateVelocity(self.velocity)
        self.neighbors = []

        self.forces = Vector(0,0)
        self.dog = Vector(0,0)
        self.alignment = Vector(0,0)
        self.cohesion = Vector(0,0)
        self.separation = Vector(0,0)
        self.bounds = Vector(0,0)
        
        #self.linearAccel = 0
        #self.angularVel = Vector(0,0)
        
    def __str__(self):
        super().__str__()
    
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
        self.forces = Vector(0,0)
        self.calcTrackingVelocity(target)
        vectToPlayer = target.position - self.position

        if (self.isPlayerClose(target) == True):
            self.dog = vectToPlayer * -1
        else:
            self.dog = Vector(0,0)

        totalNeighbors = len(self.neighbors)

        if (totalNeighbors > 0):
            for sheep in self.neighbors:
                self.alignment += sheep.velocity
                self.cohesion += sheep.position
                self.separation += (sheep.position - self.position)
            self.alignment *= 1/totalNeighbors
            self.alignment = self.alignment.normalize()

            self.cohesion *= 1/totalNeighbors
            self.cohesion = Vector(self.cohesion.x - self.position.x, self.cohesion.y - self.position.y)
            self.cohesion = self.cohesion.normalize()

            self.separation *= 1/totalNeighbors
            self.separation *= -1
            self.separation = self.separation.normalize()       

        if (self.position - Vector(0,self.position.y)).length() < Constants.BOUNDS_DIST:
            self.bounds.x = 1
        elif (Vector(Constants.WORLD_WIDTH, self.position.y) - Vector(self.position.x + self.rect.w, self.position.y)).length() < Constants.BOUNDS_DIST:
            self.bounds.x = -1
        else:
            self.bounds.x = 0
        if (self.position - Vector(self.position.x,0)).length() < Constants.BOUNDS_DIST:
            self.bounds.y = 1
        elif (Vector(self.position.x,Constants.WORLD_HEIGHT) - Vector(self.position.x, self.position.y + self.rect.h)).length() < Constants.BOUNDS_DIST:
            self.bounds.y = -1
        else:
            self.bounds.y = 0
        self.bounds = self.bounds.normalize()

        self.forces += self.alignment * Constants.ALIGNMENT_FORCE \
            + self.cohesion * Constants.COHESION_FORCE \
                + self.separation * Constants.SEPARATION_FORCE \
                    + self.bounds * Constants.BOUNDARY_FORCE \
                        + self.dog * Constants.DOG_FORCE
        

        self.updateVelocity(self.forces)
        super().update()

    def draw(self, screen):        
        screen.blit(self.image, [self.position.x, self.position.y])
        super().draw(screen)
        
        if(self.sheepVelLine == True):                            
            if (self.followingPlayer == True):
                if self.lineToTarg == None:
                    self.lineToTarg = pygame.draw.line(screen, Constants.ENEMY_LINE_CHASE_COLOR, (self.center.x, self.center.y), (self.target.x, self.target.y), 3)            
            pygame.display.update(self.lineToTarg)
            drawLine = pygame.draw.line(screen, [0,0,255], (self.center.x,self.center.y), (self.center.x + self.velocity.x * self.size.x, self.center.y + self.velocity.y * self.size.y) ,3)
        self.lineToTarg = None
                    
        if (self.neighborLine == True):
            for sheep in self.neighbors:
                drawNeighborLine = pygame.draw.line(screen,[0,255,0],(self.center.x, self.center.y),(sheep.center.x, sheep.center.y),1)
                pygame.display.update(drawNeighborLine)

        if (self.dogForceLine == True):
            drawDogLine = pygame.draw.line(screen,[0,0,255],(self.center.x,self.center.y),(self.center.x + self.dog.x, self.center.y + self.dog.y),1)
            pygame.display.update(drawDogLine)

        if self.boundForceLine == True:
            drawBoundLine = pygame.draw.line(screen, [255,0,255],(self.center.x,self.center.y),(self.center.x + self.bounds.x, self.center.y + self.bounds.y),1)
            pygame.display.update(drawBoundLine)

    def getNeighbors(self, sheepHerd):
        self.neighbors = []
        for sheep in sheepHerd:
            if sheep is not self:
                sheepVect = sheep.position - self.position
                if (sheepVect.length() < Constants.NEIGHBOR_DIST):
                    self.neighbors.append(sheep)
                    

     

     


