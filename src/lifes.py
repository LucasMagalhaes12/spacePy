import pygame
from random import randint

class Lifes():
    def __init__(self):
        self._skin = pygame.image.load("res/heart.png")
        self._skin = pygame.transform.scale(self._skin, (40, 40))
        self._SPEED = 5
        self._positions = []
        self._lifes = 3
        self._MAXLIFES = 3
        self._density = 200
        self._lucky = 200

        self._time = 1
        self.LOSELIFE = -1
        self.WINLIFE = 1


    def update(self, screenSize:tuple):
        if self._lifes < self._MAXLIFES and self._time == 0:
                sorted = randint(0, self._lucky)
                if sorted == 0:
                    self._positions.append([randint(0, screenSize[0] - self._skin.get_width()), -1])
                    self._time = self._density
        else:
            if self._time > 0:
                self._time -= 1


        for i, position in enumerate(self._positions):
            self._positions[i][1] += self._SPEED
            if position[1] > screenSize[1] + 1:
                self._positions.pop(i)


    def pop(self, index:int):
        if len(self._positions) != 0 and len(self._positions) > index:
            self._positions.pop(index)


    def set(self, setState:int):
        self._lifes += setState


    def positions(self):
        return self._positions


    def skin(self):
        return self._skin
    

    def lifes(self):
        return self._lifes


    def size(self):
        return self._skin.get_size()


    