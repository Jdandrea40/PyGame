import pygame
import Constants

from Agent import Agent
from Vector import Vector

class Dog(Agent):
    def __init__(self, image, position, size, color, speed, angularSpeed):
        super().__init__(image, position, size, color, speed, angularSpeed)
        self.isSearching = False
        self.sheepToChase = 100
        self.pathToSheep = []

    def update(self, bounds, graph, herd, gates):
        super().update(bounds, graph, herd, gates)
        runSearchKey = pygame.key.get_pressed()
        if (self.isSearching == False):

            self.isSearching = True
            closestSheepDist = 1000
            for sheep in herd:
                distanceToSheep = sheep.center - self.center
                if (distanceToSheep.length() < closestSheepDist):
                    sheepToChase = sheep

            if (runSearchKey[pygame.K_a]):
                self.pathToSheep = graph.findPath_AStar(graph.getNodeFromPoint(self.center), graph.getNodeFromPoint(sheepToChase.center))
            elif (runSearchKey[pygame.K_s]):
                self.pathToSheep = graph.findPath_BestFirst(graph.getNodeFromPoint(self.center), graph.getNodeFromPoint(sheepToChase.center))
            elif (runSearchKey[pygame.K_d]):
                self.pathToSheep = graph.findPath_Djikstra(graph.getNodeFromPoint(self.center), graph.getNodeFromPoint(sheepToChase.center))
            elif (runSearchKey[pygame.K_f]):
                self.pathToSheep = graph.findPath_Breadth(graph.getNodeFromPoint(self.center), graph.getNodeFromPoint(sheepToChase.center))
        
        # Once a path is found, move along that path
        if (len(self.pathToSheep) > 0 and self.isSearching == True):
            if (graph.getNodeFromPoint(self.center) == self.pathToSheep[0]):
                self.pathToSheep.pop(0)
                if (len(self.pathToSheep) > 0):
                    self.velocity = (self.pathToSheep[0].center - self.center).normalize()
        else:
            self.velocity = Vector(0,0)
            self.isSearching = False
               

    # draws the dog and its velocity line
    def draw(self, screen):
        screen.blit(self.image, [self.position.x, self.position.y])
        super().draw(screen)
        if (self.dogForceLine == True):
            myLine = pygame.draw.line(screen, Constants.LINE_COLOR, (self.center.x, self.center.y), (self.center.x + self.velocity.x * self.size.x, self.center.y + self.velocity.y * self.size.y), 3)
            pygame.display.update(myLine)
            

