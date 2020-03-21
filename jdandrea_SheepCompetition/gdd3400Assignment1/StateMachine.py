from Constants import *
from pygame import *
from random import *
from Vector import *
from Agent import *
from Sheep import *
from Dog import *
from Graph import *
from Node import *
from GameState import *

class StateMachine:
	""" Machine that manages the set of states and their transitions """

	def __init__(self, startState):
		""" Initialize the state machine and its start state"""
		self.__currentState = startState
		self.__currentState.enter()

	def getCurrentState(self):
		""" Get the current state """
		return self.__currentState

	def update(self, gameState):
		""" Run the update on the current state and determine if we should transition """
		nextState = self.__currentState.update(gameState)

		# If the nextState that is returned by current state's update is not the same
		# state, then transition to that new state
		if nextState != None and type(nextState) != type(self.__currentState):
			self.transitionTo(nextState)

	def transitionTo(self, nextState):
		""" Transition to the next state """
		self.__currentState.exit()
		self.__currentState = nextState
		self.__currentState.enter()

	def draw(self, screen):
		""" Draw any debugging information associated with the states """
		self.__currentState.draw(screen)

class State:
	def enter(self):
		""" Enter this state, perform any setup required """
		print("Entering " + self.__class__.__name__)
				
	def exit(self):
		""" Exit this state, perform any shutdown or cleanup required """
		print("Exiting " + self.__class__.__name__)

	def update(self, gameState):
		""" Update this state, before leaving update, return the next state """
		print("Updating " + self.__class__.__name__)

	def draw(self, screen):
		""" Draw any debugging info required by this state """
		pass

class Idle(State):
	""" This is an idle state where the dog does nothing """

	def update(self, gameState):
		super().update(gameState)
		
		# Do nothing
		return Idle()
			   
class FindSheepState(State):
	""" This is an example state that simply picks the first sheep to target """

	def update(self, gameState):
		""" Update this state using the current gameState """
		super().update(gameState)
		dog = gameState.getDog()

		# Pick a random sheep
		dog.setTargetSheep(gameState.getHerd()[0])
		herd = gameState.getHerd()
		# You could add some logic here to pick which state to go to next
		# depending on the gameState
		if (len(herd) > 0):
			return CalcChaseOffset()
		else:
			return Idle()


class CalcChaseOffset(State):
	def update(self, gameState):
		super().update(gameState)
		dog = gameState.getDog()
		sheep = dog.getTargetSheep()
		graph = gameState.getGraph()
		pen = gameState.getPenBounds()
		gate = pen[0]

		gateCent = Vector(gate.centerx, gate.centery)

		sheepVect = sheep.center - gateCent
		sheepVect = sheepVect.normalize()
		sheepVect = sheepVect * (Constants.SHEEP_MIN_FLEE_DIST * (2/3))

		pointToMove = sheep.center + sheepVect

		# Keeps offset inbounds of the screen
		if (pointToMove.x > Constants.WORLD_WIDTH):
			pointToMove.x = Constants.WORLD_WIDTH
		if (pointToMove.x < 0):
			pointToMove.x = 0
		if (pointToMove.y > Constants.WORLD_HEIGHT):
			pointToMove.y = Constants.WORLD_HEIGHT
		if (pointToMove.y < 0):
			pointToMove.y = 0
		
		# checks if offset is inside an obstacle
		if (graph.getNodeFromPoint(pointToMove).isWalkable == False):
			while (graph.getNodeFromPoint(pointToMove).isWalkable == False):
				pointToMove.x += Constants.GRID_SIZE
				pointToMove.y += Constants.GRID_SIZE

		dog.calculatePathToNewTarget(pointToMove)

		return Chase()

class Chase(State):
	def update(self, gameState):
		super().update(gameState)
		dog = gameState.getDog() 
		if (dog.getPathLength() < 1):
			return FindSheepState()
		

