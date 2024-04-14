import pygame
from random import randint

class Particles:
    def __init__(self, color:str="white"):
        self._skin = pygame.Surface((1, 1))
        self._skin.fill(pygame.Color(color))
        self._positions = []
        self._time = 0


    def update(self, limitsScreen, posX:int=0, posY:int=-1, speed:int=5, density:int=2, direction:int=-1):
        """
        Create Particles in the limits.
        Directions:
        UP = 1
        DOWN = -1
        """
        self._time += 1
        self._time %= 1 + density
        if self._time == 0:
            self._positions.append([randint(posX, limitsScreen[0]), posY])

        for i, position in enumerate(self._positions):
            self._positions[i][1] += speed
            if position[1] > limitsScreen[1] + 1:
                self._positions.pop(i)


    def splash(self, screenSize, density:int=30):
        """
        Randomly draws particles on the screen.
        """
        for i in range(density):
            self._positions.append([randint(0, screenSize[0]), randint(0, screenSize[1])])


    def skin(self):
        """
        Return particle skin.
        """
        return self._skin


    def positions(self):
        """
        Returns the list of particle positions.
        """
        return self._positions
