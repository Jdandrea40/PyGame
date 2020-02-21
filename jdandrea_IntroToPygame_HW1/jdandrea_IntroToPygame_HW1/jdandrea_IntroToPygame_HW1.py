import pygame
import Constants
import random

from Vector import Vector
from Player import Player
from Enemy import Enemy
from EnemyHunter import EnemyHunter

pygame.init()
screen = pygame.display.set_mode((Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT))
done = False

playerPosition = Vector((Constants.WORLD_WIDTH / 2), (Constants.WORLD_HEIGHT / 2))
player = Player(playerPosition, Constants.PLAYER_SIZE, Constants.PLAYER_SPEED, Constants.PLAYER_COLOR)

#enemy = Enemy(enemyPosition, Constants.ENEMY_SIZE, Constants.ENEMY_SPEED, Constants.ENEMY_COLOR)
enemies = []

enemyHunters = []
#enemyHunter = EnemyHunter(enemyHunterPos, Constants.ENEMY_SIZE, Constants.ENEMY_SPEED, Constants.ENEMY_HUNTER_COLOR)
for x in range(0,10):    
    enemyHunters.append(EnemyHunter(Vector(random.randrange(Constants.WORLD_WIDTH),random.randrange(Constants.WORLD_HEIGHT)), Constants.ENEMY_SIZE, Constants.ENEMY_SPEED, Constants.ENEMY_HUNTER_COLOR))
    enemies.append(Enemy(Vector(random.randrange(Constants.WORLD_WIDTH),random.randrange(Constants.WORLD_HEIGHT)), Constants.ENEMY_SIZE, Constants.ENEMY_SPEED, Constants.ENEMY_COLOR))

# frame rate object
fps = pygame.time.Clock()
  
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        pygame.display.flip()

        fps.tick(Constants.FRAME_RATE)
        screen.fill(Constants.BACKGROUND_COLOR)
        player.draw(screen)       
        player.update(pygame.key.get_pressed())

        
        for x in enemies:
            x.draw(screen, player)
            x.update(player)

        for x in enemyHunters:
            x.draw(screen, player)
            x.update(player)
        
            
        
