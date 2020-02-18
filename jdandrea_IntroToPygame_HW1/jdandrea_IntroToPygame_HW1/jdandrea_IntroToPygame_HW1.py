import pygame
import Constants

from Vector import Vector
from Player import Player
from Enemy import Enemy
from EnemyHunter import EnemyHunter

pygame.init()
screen = pygame.display.set_mode((Constants.WORLD_WIDTH, Constants.WORLD_HEIGHT))
done = False

playerPosition = Vector((Constants.WORLD_WIDTH / 2), (Constants.WORLD_HEIGHT / 2))
player = Player(playerPosition, Constants.PLAYER_SIZE, Constants.PLAYER_SPEED, Constants.PLAYER_COLOR)

enemyPosition = Vector(100, 100)
enemy = Enemy(enemyPosition, Constants.ENEMY_SIZE, Constants.ENEMY_SPEED, Constants.ENEMY_COLOR)

enemyHunterPos = Vector(300, 300)
enemyHunter = EnemyHunter(enemyHunterPos, Constants.ENEMY_SIZE, Constants.ENEMY_SPEED, Constants.ENEMY_HUNTER_COLOR)

# frame rate object
fps = pygame.time.Clock()
  
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        pygame.display.flip()

        # sets the framerate
        fps.tick(Constants.FRAME_RATE)
        # redraws the screen (stops the "paint" feature)
        screen.fill(Constants.BACKGROUND_COLOR)
        
        player.draw(screen)       
        player.update(pygame.key.get_pressed())

        enemy.draw(screen, player)
        enemy.update(player)

        enemyHunter.draw(screen, player)
        enemyHunter.update(player)


        
            
        
