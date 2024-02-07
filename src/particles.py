import pygame
from random import randint

class Particles:
    def __init__(self):
        self._skin = pygame.Surface((1, 1))
        self._skin.fill(pygame.Color('white'))
        self._positions = []
        self._SPEED = 5
        self._time = 0
        self.density = 2 
        self._isCreation = False


    def new(self, screenSize):
        if self._isCreation:
            self._positions.append([randint(0, screenSize[0]), -1])


    def update(self, screenSize):
        # print("---", self._positions)
        self._time += 1
        self._time %= 1 + self.density
        self._isCreation = True if self.density == self._time else False
        for i, position in enumerate(self._positions):
            self._positions[i][1] += self._SPEED
            if position[1] > screenSize[1] + 1:
                self._positions.pop(i)

    
    def skin(self):
        return self._skin
    
    def positions(self):
        return self._positions