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
        
    def draw(self, screen):
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)
        myRect = pygame.draw.rect(screen, self.color, self.rect)
        self.center = myRect.center
        myLine = pygame.draw.line(screen, self.lineColor, self.center, (myRect.centerx + self.velocity.x * (self.size), myRect.centery + self.velocity.y * (self.size)), 3)
        
        pygame.display.update(myLine)        
        pygame.display.update(myRect)
     
    def collisionCheck(self, player):        
        return self.rect.colliderect(player)            
    
    def updatePlayer(self):                     
        if(self.position.y <= 0 or self.position.y >= Constants.WORLD_HEIGHT):
            self.position.y = self.position.y
            self.position.x += (self.velocity.x * self.speed)
        elif(self.position.x <= 0 or self.position.x >= Constants.WORLD_WIDTH):
            self.position.x = self.position.x
            self.position.y +=(self.velocity.y * self.speed)
        else:
            self.position +=(self.velocity * self.speed)
        
        
        #self.velocity.__str__()
        #self.position.__str__()  

    def updateEnemy(self, player):             
        self.position += self.velocity * self.speed




