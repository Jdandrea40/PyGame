import pygame
import Constants
import math
import random
from Vector import Vector
from Agent import Agent

class Sheep(Agent):
    "A sheep class that handles hearding behavior"
    def __init__(self, image, position, size, color, speed, angularSpeed):
        # initializes all Sheep stats
        super().__init__(image, position, size, color, speed, angularSpeed)
        self.followingPlayer = False
        self.target = Vector(0,0)
        self.lineToTarg = None

        self.velocity = Vector(random.randrange(-1,1), random.randrange(-1,1))
        self.updateVelocity(self.velocity)
        self.neighbors = []

        self.forces = Vector(0,0)
        self.dogForce = Vector(0,0)
        self.alignment = Vector(0,0)
        self.cohesion = Vector(0,0)
        self.separation = Vector(0,0)
        self.bounds = Vector(0,0)
        self.obsVector = Vector(0,0)
        
        #self.linearAccel = 0
        #self.angularVel = Vector(0,0)
        
    def __str__(self):
        super().__str__()
    
    # a state swithcing method
    def switchMode(self):
        self.isInSeek = not self.isInSeek
    
    # used to check if the player (dog) is within its force range
    def isPlayerClose(self, target):
        # dtermines the vector from dog to sheep
        attackVector = target.position - self.position                    
        # gets the length of the vector
        attackRange = attackVector.length()           
        # checks the distance in comparision to the force range
        if (attackRange <= Constants.ENEMY_ATTACK_RANGE):
            self.followingPlayer = True
            return True
        self.followingPlayer = False
        return False

    # used to get the center of the dog
    def calcTrackingVelocity(self, target):
        self.target = target.center

    # the main update method of the sheep
    def update(self, bounds, graph, dog, herd, gates):
        # initialize the starting force to 0
        self.forces = Vector(0,0)
        self.obsVector = Vector(0,0)
        self.calcTrackingVelocity(dog)

        # gets the vector to the dog and uses it to check its closeness
        vectToPlayer = dog.position - self.position

        if (self.isPlayerClose(dog) == True):
            self.dogForce = vectToPlayer * -1
        else:
            self.dogForce = Vector(0,0)

        self.dogForce = self.dogForce.normalize()
        # gets the total numbers of neighbors for neighbor alignment
        totalNeighbors = len(self.neighbors)

        # makes sure the sheep has neighbors to group with
        if (totalNeighbors > 0):
            # loops through the list of neighbors so that all neighbored sheep stay groupped properly
            for sheep in self.neighbors:
                self.alignment += sheep.velocity
                self.cohesion += sheep.position
                self.separation += (sheep.position - self.position)

            self.sheepAlignment(totalNeighbors)
            self.sheepCohesion(totalNeighbors)
            self.sheepSeparation(totalNeighbors)
    

        if ((self.position - Vector(0,self.position.y)).length() < Constants.SHEEP_BOUNDARY_RADIUS):
            self.bounds.x = 1
        elif (Vector(Constants.WORLD_WIDTH, self.position.y) - Vector(self.position.x + self.rect.w, self.position.y)).length() < Constants.SHEEP_BOUNDARY_RADIUS:
            self.bounds.x = -1
        else:
            self.bounds.x = 0
        if (self.position - Vector(self.position.x,0)).length() < Constants.SHEEP_BOUNDARY_RADIUS:
            self.bounds.y = 1
        elif (Vector(self.position.x,Constants.WORLD_HEIGHT) - Vector(self.position.x, self.position.y + self.rect.h)).length() < Constants.SHEEP_BOUNDARY_RADIUS:
            self.bounds.y = -1
        else:
            self.bounds.y = 0
        self.bounds = self.bounds.normalize()

        for o in graph.obstacles:
            if (o.center - self.center).length() < Constants.SHEEP_OBSTACLE_RADIUS:
                self.obsVector += (self.center - o.center)               
        self.obsVector = self.obsVector.normalize()

        self.forces += self.alignment * Constants.SHEEP_ALIGNMENT_WEIGHT \
            + self.cohesion * Constants.SHEEP_COHESION_WEIGHT \
                + self.separation * Constants.SHEEP_SEPARATION_WEIGHT \
                    + self.bounds * Constants.SHEEP_BOUNDARY_INFLUENCE_WEIGHT \
                        + self.dogForce * Constants.SHEEP_DOG_INFLUENCE_WEIGHT \
                         + self.obsVector * Constants.SHEEP_OBSTACLE_INFLUENCE_WEIGHT
        
        self.forces *= Constants.SHEEP_ANGULAR_SPEED
        self.updateVelocity(self.forces)

        super().update(bounds, graph, herd, gates)

    def sheepAlignment(self, totNeighs):
        # SHEEP ALIGNMENT
        self.alignment *= 1/totNeighs
        self.alignment = self.alignment.normalize()

    def sheepCohesion(self, totNeighs):
        # SHEEP COHESION
        self.cohesion *= 1/totNeighs
        self.cohesion = Vector(self.cohesion.x - self.position.x, self.cohesion.y - self.position.y)
        self.cohesion = self.cohesion.normalize()

    def sheepSeparation(self, totNeighs):
        # SHEEP SEPERATION
        self.separation *= 1/totNeighs
        self.separation *= -1
        self.separation = self.separation.normalize() 
       
    # handles the drawing og the sheeps visual lines
    def draw(self, screen):
        # draws sheep PNG
        screen.blit(self.image, [self.position.x, self.position.y])
        super().draw(screen)
        
        # used for sheep velocity line toggling and direction
        if(self.sheepVelLine == True):                            
            if (self.followingPlayer == True):
                if self.lineToTarg == None:
                    # draws the lines
                    self.lineToTarg = pygame.draw.line(screen, Constants.ENEMY_LINE_CHASE_COLOR, (self.center.x, self.center.y), (self.target.x, self.target.y), 3)            
            pygame.display.update(self.lineToTarg)
            drawLine = pygame.draw.line(screen, [0,0,255], (self.center.x,self.center.y), (self.center.x + self.velocity.x * self.size.x, self.center.y + self.velocity.y * self.size.y) ,3)
        self.lineToTarg = None
                    
        # neighbor lines drawing
        if (self.neighborLine == True):
            for sheep in self.neighbors:
                drawNeighborLine = pygame.draw.line(screen,[0,255,0],(self.center.x, self.center.y),(sheep.center.x, sheep.center.y),1)
                pygame.display.update(drawNeighborLine)
        
        # dog force affect line drawing
        if (self.dogForceLine == True):
            drawDogLine = pygame.draw.line(screen,[0,0,255],(self.center.x,self.center.y),(self.center.x + self.dogForce.x, self.center.y + self.dogForce.y),1)
            pygame.display.update(drawDogLine)
        
        # bound force line drawing
        if self.boundForceLine == True:
            drawBoundLine = pygame.draw.line(screen, [255,0,255],(self.center.x,self.center.y),(self.center.x + self.bounds.x, self.center.y + self.bounds.y),1)
            pygame.display.update(drawBoundLine)
    
    # handles the adding of neighbors to the sheep
    def getNeighbors(self, sheepHerd):
        self.neighbors = []
        for sheep in sheepHerd:
            if sheep is not self:
                sheepVect = sheep.position - self.position
                # checks the sheeps distance to determine if the are neighbors
                if (sheepVect.length() < Constants.SHEEP_NEIGHBOR_RADIUS):
                    self.neighbors.append(sheep)
                    

     

     


