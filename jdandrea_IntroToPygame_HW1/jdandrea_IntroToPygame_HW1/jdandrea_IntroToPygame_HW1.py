import pygame
import Constants
import random

from Vector import Vector
from Player import Player
from Enemy import Enemy
from EnemyHunter import EnemyHunter
from Sheep import Sheep
from Dog import Dog

pygame.init()
screen = pygame.display.set_mode((Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT))
done = False

dogImage = pygame.image.load("collie.png")
dogPosition = Vector((Constants.WORLD_WIDTH / 2), (Constants.WORLD_HEIGHT / 2))
dog = Dog(dogPosition,Vector(Constants.DOG_WIDTH, Constants.DOG_HEIGHT), Constants.PLAYER_SPEED, dogImage)

sheepImage = pygame.image.load("sheep.png")
herdOfSheep = []

for x in range(0,50):    
    herdOfSheep.append(Sheep(Vector(random.randrange(Constants.WORLD_WIDTH),random.randrange(Constants.WORLD_HEIGHT)), Vector(Constants.SHEEP_WIDTH, Constants.SHEEP_HEIGHT), Constants.ENEMY_SPEED, sheepImage))

# frame rate object
fps = pygame.time.Clock()
  
while not done:
        lineKey = None
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN:
                        lineKey = pygame.key.get_pressed()
        pygame.display.flip()
        key = pygame.key.get_pressed()
        fps.tick(Constants.FRAME_RATE)
        screen.fill(Constants.BACKGROUND_COLOR)

        dog.updateLineDraws(lineKey)        
        dog.draw(screen)       
        dog.update(key)

        for x in herdOfSheep:
            x.updateLineDraws(lineKey)
            x.getNeighbors(herdOfSheep)
            x.draw(screen)
            x.update(dog)
            
