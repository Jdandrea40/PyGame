import pygame
import Vector
import Constants

from Vector import Vector

class Agent(object):

    def __init__(self, position, size, speed, color):
        self.position = position
<<<<<<< Updated upstream
        self.speed = speed
        self.size = size
        self.color = color
        self.ogColor = self.color
=======
        self.currentSpeed = speed
        self.maxSpeed = speed
        self.size = Vector(size.x, size.y)
        self.image = image  
        self.imageOG = image
        self.velocity = Vector(0, 0)
        self.target = Vector(0,0)
>>>>>>> Stashed changes

        self.centerX = (self.position.x + self.size) / 2 
        self.centerY = (self.position.y + self.size) / 2
        self.center = Vector(self.centerX, self.centerY)

<<<<<<< Updated upstream
        self.velocity = Vector(0, 0)
        self.lineColor = Constants.LINE_COLOR 

        self.time = 0.0
        self.flashTime = 0.0        
=======
        # Used for line drawing
        self.sheepVelLine = False
        self.dogForceLine = False
        self.boundForceLine = False
        self.neighborLine = False
        self.boundingBox = False
>>>>>>> Stashed changes

    def draw(self, screen):
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)
        myRect = pygame.draw.rect(screen, self.color, self.rect)
        #self.center = myRect.center

        self.centerX = (self.position.x + (self.size / 2)) 
        self.centerY = (self.position.y + (self.size / 2))
        self.center = Vector(self.centerX, self.centerY)

        myLine = pygame.draw.line(screen, self.lineColor, (self.center.x, self.center.y), (self.centerX + (self.velocity.x * self.size), self.centerY + (self.velocity.y * self.size)), 3)

        pygame.display.update(myLine)        
        pygame.display.update(myRect)
        
    def drawToPoint(self, screen, playerVect):
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)
        myRect = pygame.draw.rect(screen, self.color, self.rect)
        self.center = myRect.center
        
        if (self.attacking == True):
            #myLine = pygame.draw.line(screen, self.lineColor, self.center, (point.rect.centerx, point.rect.centery), 3)
            myLine = pygame.draw.line(screen, self.lineColor, self.center, (playerVect.x, playerVect.y), 3)
            pygame.display.update(myLine)        
        pygame.display.update(myRect) 

    def update(self):
        self.velocity = self.velocity.normalize()

        # SCREEN BOUNDS
        if(self.position.y + (self.velocity.y * self.speed) <= 0 or self.position.y + (self.velocity.y * self.speed) > float(Constants.WORLD_HEIGHT - Constants.PLAYER_SIZE)):
            self.velocity = Vector(self.velocity.x, 0)            
        if(self.position.x + (self.velocity.x * self.speed) <= 0 or self.position.x + (self.velocity.x * self.speed) > float(Constants.WORLD_WIDTH - Constants.PLAYER_SIZE)):
            self.velocity = Vector(0, self.velocity.y)

        self.position += (self.velocity * self.speed)

    def collisionCheck(self, player):
        currentTime = pygame.time.get_ticks()
        cooldown = Constants.ENEMY_NO_TAG_BACK

        if((currentTime - self.time > cooldown and self.rect.colliderect(player.rect)) or (self.rect.colliderect(player.rect) and self.firstTag == True)):
            self.firstTag = False
            self.iT = not self.iT
            self.time = currentTime
        
        # Color Flashing           
        if (currentTime < self.time + Constants.ENEMY_NO_TAG_BACK and self.time != 0 and currentTime > self.flashTime + 5):
            self.flashTime = pygame.time.get_ticks()
            if (self.color == self.ogColor):
                self.color = Constants.COLOR_WHITE           
            else: 
                self.color = self.ogColor   
        else:
            self.color = self.ogColor     
       







