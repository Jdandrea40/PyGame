import pygame
import Vector
import Constants
import math

from Vector import Vector

class Agent(object):

    def __init__(self, position, size, speed, image):
        self.position = position
        self.currentSpeed = 1
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


    def draw(self, screen):
        if (self.boundingBox == True):
            boundingRect = pygame.draw.rect(screen, [0,0,255], self.rect, 3)
            pygame.display.update(boundingRect)

    def updateAngle(self):
        self.angle = math.degrees(math.atan2(-self.velocity.y, self.velocity.x)) - 90
        self.image = pygame.transform.rotate(self.imageOG, self.angle)  
        
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
                if(Constants.DOG_FORCE > 0):
                    Constants.DOG_FORCE = 0
                else:
                    Constants.DOG_FORCE = 1
            if (key[pygame.K_7]):
                if (Constants.ALIGNMENT_FORCE > 0):
                    Constants.ALIGNMENT_FORCE = 0
                else:
                    Constants.ALIGNMENT_FORCE = 1
            if (key[pygame.K_8]):
               if (Constants.SEPARATION_FORCE > 0):
                    Constants.SEPARATION_FORCE = 0
               else:
                    Constants.SEPARATION_FORCE = .8
            if (key[pygame.K_9]):
                if (Constants.COHESION_FORCE > 0):
                    Constants.COHESION_FORCE = 0
                else:
                    Constants.COHESION_FORCE = .8
            if (key[pygame.K_0]):
                if (Constants.BOUNDARY_FORCE > 0):
                    Constants.BOUNDARY_FORCE = 0
                else:
                   Constants.BOUNDARY_FORCE = 1.2

    def update(self):
        # SCREEN BOUNDS
        if(self.position.y + (self.velocity.y * self.currentSpeed) <= 0 or self.position.y + (self.velocity.y * self.currentSpeed) > float(Constants.WORLD_HEIGHT - self.size.y)):
            self.velocity = Vector(self.velocity.x, 0)            
        if(self.position.x + (self.velocity.x * self.currentSpeed) <= 0 or self.position.x + (self.velocity.x * self.currentSpeed) > float(Constants.WORLD_WIDTH - self.size.x)):
            self.velocity = Vector(0, self.velocity.y)

        self.position += self.velocity * self.currentSpeed
        self.updateRect()
        self.updateCenter()
        self.updateAngle()
        
        
    def updateRect(self):
        self.rect = self.image.get_bounding_rect()
            
    def updateCenter(self):
        self.center = Vector(self.position.x + (self.size.x / 2), self.position.y + (self.size.y/ 2))
        self.rect = self.rect.move(self.center.x - self.size.x / 2, self.center.y - self.size.y / 2)
        self.center = Vector(self.rect.centerx, self.rect.centery)
    
    def updateVelocity(self, velocity):
         self.velocity = velocity.normalize()
    
    def isInCollision(self, agent):
        if (self.rect.colliderrect(agent.rect)):
            return True
        return False
       







