import pygame
import Vector
import Constants

from Vector import Vector

class Agent(object):

    def __init__(self, position, size, speed, color):
        self.position = position
        self.speed = speed
        self.size = size
        self.color = color
        self.velocity = Vector(0, 0)
        self.lineColor = Constants.LINE_COLOR 
        self.currentTime = pygame.time.get_ticks()
        

    def draw(self, screen):
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)
        myRect = pygame.draw.rect(screen, self.color, self.rect)
        self.center = myRect.center
        myLine = pygame.draw.line(screen, self.lineColor, self.center, (myRect.centerx + self.velocity.x * (self.size), myRect.centery + self.velocity.y * (self.size)), 3)
        
        pygame.display.update(myLine)        
        pygame.display.update(myRect)
     
    def collisionCheck(self, player):  
        self.currentTime = pygame.time.get_ticks()

        if(self.currentTime > self.currentTime + Constants.ENEMY_NO_TAG_BACK):        
            return self.rect.colliderect(player)            
    
    def updatePlayer(self):                     
        if(self.position.y + (self.velocity.y * self.speed) <= 0 or self.position.y + (self.velocity.y * self.speed) > float(Constants.WORLD_HEIGHT - Constants.PLAYER_SIZE)):
            self.velocity = Vector(self.velocity.x, 0)            
        if(self.position.x + (self.velocity.x * self.speed) <= 0 or self.position.x + (self.velocity.x * self.speed) > float(Constants.WORLD_WIDTH - Constants.PLAYER_SIZE)):
            self.velocity = Vector(0, self.velocity.y)

        self.position +=(self.velocity * self.speed)


    def updateEnemy(self, player):

        if(self.position.y + (self.velocity.y * self.speed) <= 0 or self.position.y + (self.velocity.y * self.speed) > float(Constants.WORLD_HEIGHT - Constants.ENEMY_SIZE)):
            self.velocity = Vector(self.velocity.x, 0)  
        if(self.position.x + (self.velocity.x * self.speed) <= 0 or self.position.x + (self.velocity.x * self.speed) > float(Constants.WORLD_WIDTH - Constants.ENEMY_SIZE)):
            self.velocity = Vector(0, self.velocity.y)

        self.position +=(self.velocity * self.speed)





