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
        self.centerX = self.position.x / 2 
        self.centerY = self.position.y / 2

        self.velocity = Vector(0, 0)
        self.lineColor = Constants.LINE_COLOR 
        self.time = pygame.time.get_ticks()
        self.flashTime = pygame.time.get_ticks()

    def draw(self, screen):
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)
        myRect = pygame.draw.rect(screen, self.color, self.rect)
        self.center = myRect.center
        
        myLine = pygame.draw.line(screen, self.lineColor, self.center, (myRect.centerx + self.velocity.x * (self.size), myRect.centery + self.velocity.y * (self.size)), 3)
        
        pygame.display.update(myLine)        
        pygame.display.update(myRect)
        
    def drawToPoint(self, screen, point):
        x = point.position.x
        y = point.position.y
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size, self.size)
        myRect = pygame.draw.rect(screen, self.color, self.rect)
        self.center = myRect.center
        if (self.attacking == True):
            #myLine = pygame.draw.line(screen, self.lineColor, self.center, (point.rect.centerx, point.rect.centery), 3)
            myLine = pygame.draw.line(screen, self.lineColor, self.center, (x, y), 3)
            pygame.display.update(myLine)        
        pygame.display.update(myRect) 

    def updatePlayer(self, pressedKey):
        # player movement
        if pressedKey[pygame.K_w]:
            self.velocity.y = -1
        elif pressedKey[pygame.K_s]:
            self.velocity.y = 1
        else:
            self.velocity.y = 0

        if pressedKey[pygame.K_a]:
            self.velocity.x = -1
        elif pressedKey[pygame.K_d]:
            self.velocity.x = 1
        else:
            self.velocity.x = 0

        self.velocity = self.velocity.normalize()

        # SCREEN BOUNDS
        if(self.position.y + (self.velocity.y * self.speed) <= 0 or self.position.y + (self.velocity.y * self.speed) > float(Constants.WORLD_HEIGHT - Constants.PLAYER_SIZE)):
            self.velocity = Vector(self.velocity.x, 0)            
        if(self.position.x + (self.velocity.x * self.speed) <= 0 or self.position.x + (self.velocity.x * self.speed) > float(Constants.WORLD_WIDTH - Constants.PLAYER_SIZE)):
            self.velocity = Vector(0, self.velocity.y)

        self.position +=(self.velocity * self.speed)

    def collisionCheck(self, player):
        currentTime = pygame.time.get_ticks()
        cooldown = Constants.ENEMY_NO_TAG_BACK
        if((currentTime - self.time > cooldown and self.rect.colliderect(player.rect)) or (self.rect.colliderect(player.rect) and self.firstTag == True)):
            self.firstTag = False
            #self.blink()
            self.iT = not self.iT
            print(str(currentTime) + '-' + str(cooldown) + '-' + str(self.iT))
            self.time = currentTime
            
                 
    def blink(self):
        currentTime = pygame.time.get_ticks()
        while(currentTime - self.flashTime > Constants.ENEMY_NO_TAG_BACK):
            if (currentTime - self.flashTime > 5):
                self.color = Constants.COLOR_WHITE           
            else:
                self.flashTime = currentTime
                self.color = Constants.ENEMY_COLOR

        self.color = Constants.ENEMY_COLOR
        
       
    def updateEnemy(self, player):        
        if (self.iT == True):
            attackVector = player.position - self.position                    
        else:
            attackVector = self.position - player.position        
        
        attackRange = attackVector.length()     
        
        if (attackRange < Constants.ENEMY_ATTACK_RANGE):
            self.velocity = attackVector.normalize()
            if (self.iT == True):
                self.lineColor = Constants.ENEMY_LINE_CHASE_COLOR
            else:
                self.lineColor = Constants.LINE_COLOR
            self.attacking = True
        else:
            self.velocity = Vector(0,0)
            self.lineColor = Constants.LINE_COLOR
            self.attacking = False

        # SCREEN BOUNDS
        if(self.position.y + (self.velocity.y * self.speed) <= 0 or self.position.y + (self.velocity.y * self.speed) > float(Constants.WORLD_HEIGHT - Constants.ENEMY_SIZE)):
            self.velocity = Vector(self.velocity.x, 0)  
        if(self.position.x + (self.velocity.x * self.speed) <= 0 or self.position.x + (self.velocity.x * self.speed) > float(Constants.WORLD_WIDTH - Constants.ENEMY_SIZE)):
            self.velocity = Vector(0, self.velocity.y)

        self.position +=(self.velocity * self.speed)





