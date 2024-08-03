import pygame
from random import randint

class Particles:
    def __init__(self, limitsScreen, posX:int=0, posY:int=-1, speed:int=5, density:int=2, direction:int=-1, color:str="white"):
        """
        Init:
        limitScreen = limit area
        posX = start X
        posY = start Y
        speed = particles speed
        density = particles density
        direction = particles direction (UP, DOWN)
        color = string ("white", "black", "green", "blue", "red"...)
        """
        
        self._skin = pygame.Surface((1, 1))
        self._skin.fill(pygame.Color(color))
        self._positions = []
        self._updateTimeCreation = 0
        
        self._limitScreen = limitsScreen
        self._posX = posX
        self._posY = posY
        self._speed = speed
        self._density = 2
        self._direction = -1
        self._color = color

        self.UP = 1
        self.DOWN = -1


    def set_config(self, limitScreen, posX:int=0, posY:int=-1, speed:int=5, density:int=2, direction:int=-1, color:str="white"):
        """
        Update particles configuration:
        limitScreen = limit area
        posX = start X
        posY = start Y
        speed = particles speed
        density = particles density
        direction = particles direction (UP, DOWN)
        color = string ("white", "black", "green", "blue", "red"...)
        """
        self._limitScreen = limitScreen
        self._posX = posX
        self._posY = posY
        self._speed = speed
        self._density = 2
        self._direction = -1
        self._color = color


    def update(self):
        """
        Create Particles in the limits.
        Directions:
        UP = 1
        DOWN = -1
        """
        self._updateTimeCreation += 1
        self._updateTimeCreation %= 1 + self._density
        if self._updateTimeCreation == 0:
            self._positions.append([randint(self._posX, self._limitScreen[0]), self._posY])

        for i, position in enumerate(self._positions):
            self._positions[i][1] += self._speed
            if position[1] > self._limitScreen[1] + 1:
                self._positions.pop(i)


    def splash(self, screenSize, density:int=30):
        """
        Randomly draws particles on the screen.
        """
        for i in range(density):
            self._positions.append([randint(0, screenSize[0]), randint(0, screenSize[1])])


    def get_skin(self):
        """
        Return particle skin.
        """
        return self._skin


    def get_positions(self):
        """
        Returns the list of particle positions.
        """
        return self._positions
