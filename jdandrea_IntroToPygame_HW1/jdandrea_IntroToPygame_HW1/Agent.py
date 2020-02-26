import pygame
import Vector
import Constants
import math

from Vector import Vector

class Agent(object):

    def __init__(self, position, size, speed, image):
        self.position = position
        self.currentSpeed = 0
        self.maxSpeed = speed
        self.size = Vector(size.x, size.y)
        self.image = image  
        self.imageOG = image
        self.velocity = Vector(0, 0)
        self.target = Vector(0,0)
        self.updateRect()
        self.updateCenter()
        self.updateAngle()
        self.angle = math.atan2(-self.velocity.y, self.velocity.x)

        # Used for line drawing
        self.sheepVelLine = True
        self.dogForceLine = True
        self.boundForceLine = True
        self.neighborLine = True
        self.boundingBox = True
        self.dogForces = True
        self.alignForces = True
        self.sepForces = True
        self.cohensionForces = True
        self.boundForces = True

        self.time = 0.0
        self.flashTime = 0.0        

    def draw(self, screen):
        myLine = pygame.draw.line(screen, Constants.ENEMY_LINE_CHASE_COLOR, (self.center.x, self.center.y), (self.center.x + self.velocity.x * self.size.x, self.center.y + self.velocity.y * self.size.y), 3)
        pygame.display.update(myLine)

        if (self.boundingBox == True):
            boundingRect = pygame.draw.rect(screen, [0,0,255], self.rect, 3)
            pygame.display.update(boundingRect)


    def updateAngle(self):
        self.angle = math.degrees(math.atan2(-self.velocity.y, self.velocity.x)) - 90
        self.image = pygame.transform.rotate(self.imageOG, self.angle)  
        
    def updateLineDraws(self, key):
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
             self.dogForces = not self.dogForces
        if (key[pygame.K_7]):
            self.alignForces = not self.alignForces
        if (key[pygame.K_8]):
           self.sepForces = not self.sepForces
        if (key[pygame.K_9]):
            self.cohensionForces = not self.cohensionForces
        if (key[pygame.K_0]):
            self.boundForces = not self.boundForces

    def update(self):
        # SCREEN BOUNDS
        if(self.position.y + (self.velocity.y * self.currentSpeed) <= 0 or self.position.y + (self.velocity.y * self.currentSpeed) > float(Constants.WORLD_HEIGHT - self.size.y)):
            self.velocity = Vector(self.velocity.x, 0)            
        if(self.position.x + (self.velocity.x * self.currentSpeed) <= 0 or self.position.x + (self.velocity.x * self.currentSpeed) > float(Constants.WORLD_WIDTH - self.size.x)):
            self.velocity = Vector(0, self.velocity.y)
               
        self.updateRect()
        self.updateCenter()
        self.updateAngle()
        self.position += self.velocity * self.currentSpeed
        
    def updateRect(self):
        #self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)
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

    def collisionCheck(self, agent):
        currentTime = pygame.time.get_ticks()
        cooldown = Constants.ENEMY_NO_TAG_BACK

        if((currentTime - self.time > cooldown and self.rect.colliderect(agent.rect)) or (self.rect.colliderect(agent.rect))):
            self.firstTag = False
            self.isInSeek = not self.isInSeek
            self.time = currentTime
        
        # Color Flashing           
        #if (currentTime < self.time + Constants.ENEMY_NO_TAG_BACK and self.time != 0 and currentTime > self.flashTime + 5):
        #    self.flashTime = pygame.time.get_ticks()
        #    if (self.color == self.ogColor):
        #        self.color = Constants.COLOR_WHITE           
        #    else: 
        #        self.color = self.ogColor   
        #else:
        #    self.color = self.ogColor     
       







