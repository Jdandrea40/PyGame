import pygame
import Vector
import Constants
import math

from Vector import Vector

class Agent(object):
    "An agent class that is parented to moveable game objects"\
    # Object stat initializer
    def __init__(self, image, position, size, color, speed, angularSpeed):
        self.position = position
        self.currentSpeed = speed
        self.maxSpeed = speed
        self.size = Vector(size.x, size.y)
        self.image = image  
        self.imageOG = image
        self.velocity = Vector(0, 0)
        self.target = Vector(0,0)

        self.updateRect()
        self.updateCenter()
        self.updateAngle()

        # Used for line drawing
        self.sheepVelLine = True
        self.dogForceLine = True
        self.boundForceLine = True
        self.neighborLine = True
        self.boundingBox = True


    # Draws the bounding box around the child
    def draw(self, screen):
        if (self.boundingBox == True):
            boundingRect = pygame.draw.rect(screen, [0,0,255], self.rect, 3)
            pygame.display.update(boundingRect)
    
    # updates the rotation of the sprite
    def updateAngle(self):
        # converts the radians into degrees and corrects the offset (90 degrees)
        self.angle = math.degrees(math.atan2(-self.velocity.y, self.velocity.x)) - 90
        self.image = pygame.transform.rotate(self.imageOG, self.angle)  
      
    # gets the number 1 - 0 to toggle Lines and Forces
    # not the best way to handle but certainly an easy way to do it
    def updateLineDraws(self, key):
        if key is not None:
            if (key[pygame.K_1]):
                self.sheepVelLine = not self.sheepVelLine
            if (key[pygame.K_2]):
                self.dogForceLine = not self.dogForceLine
            if (key[pygame.K_3]):
                self.boundForceLine = not self.boundForceLine
            if (key[pygame.K_4]):
                self.neighborLine = not self.neighborLine
            if (key[pygame.K_5]):
                self.boundingBox = not self.boundingBox
            if (key[pygame.K_6]):
                if(Constants.SHEEP_DOG_INFLUENCE_WEIGHT > 0):
                    Constants.SHEEP_DOG_INFLUENCE_WEIGHT = 0
                else:
                    Constants.SHEEP_DOG_INFLUENCE_WEIGHT = 0.3
            if (key[pygame.K_7]):
                if (Constants.SHEEP_ALIGNMENT_WEIGHT > 0):
                    Constants.SHEEP_ALIGNMENT_WEIGHT = 0
                else:
                    Constants.SHEEP_ALIGNMENT_WEIGHT = 0.3
            if (key[pygame.K_8]):
               if (Constants.SHEEP_SEPARATION_WEIGHT > 0):
                    Constants.SHEEP_SEPARATION_WEIGHT = 0
               else:
                    Constants.SHEEP_SEPARATION_WEIGHT = .325
            if (key[pygame.K_9]):
                if (Constants.SHEEP_COHESION_WEIGHT > 0):
                    Constants.SHEEP_COHESION_WEIGHT = 0
                else:
                    Constants.SHEEP_COHESION_WEIGHT = .3
            if (key[pygame.K_0]):
                if (Constants.SHEEP_BOUNDARY_INFLUENCE_WEIGHT > 0):
                    Constants.SHEEP_BOUNDARY_INFLUENCE_WEIGHT = 0
                else:
                   Constants.SHEEP_BOUNDARY_INFLUENCE_WEIGHT = .5

    def update(self, bounds, graph, herd, gates):
        # SCREEN BOUNDS
        if(self.position.y + (self.velocity.y * self.currentSpeed) <= 0 or self.position.y + (self.velocity.y * self.currentSpeed) > float(Constants.WORLD_HEIGHT - self.size.y)):
            self.velocity = Vector(self.velocity.x, 0)            
        if(self.position.x + (self.velocity.x * self.currentSpeed) <= 0 or self.position.x + (self.velocity.x * self.currentSpeed) > float(Constants.WORLD_WIDTH - self.size.x)):
            self.velocity = Vector(0, self.velocity.y)

        self.position += self.velocity * self.currentSpeed
        self.updateRect()
        self.updateCenter()
        self.updateAngle()
        
    # used for proper rotation by getting the bounding rect  
    def updateRect(self):
        self.rect = self.image.get_bounding_rect()
        
    # updates the center while rotating
    def updateCenter(self):
        self.center = Vector(self.position.x + (self.size.x / 2), self.position.y + (self.size.y/ 2))
        self.rect = self.rect.move(self.center.x - self.size.x / 2, self.center.y - self.size.y / 2)
        self.center = Vector(self.rect.centerx, self.rect.centery)
    
    # child velocity normalization
    def updateVelocity(self, velocity):
         self.velocity = velocity.normalize()
    
    # checks for collision
    def isInCollision(self, agent):
        if (self.rect.colliderrect(agent.rect)):
            return True
        return False
       







