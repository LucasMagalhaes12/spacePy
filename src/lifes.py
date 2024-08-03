import pygame
from random import randint

class Lifes():
    def __init__(self, screenSize:tuple):
        self._screenSize = screenSize
        self._skin = pygame.image.load("res/heart.png")
        self._skin = pygame.transform.scale(self._skin, (40, 40))
        self._SPEED = 5
        self._positions = []
        self._nlifes = 3
        self._MAXLIFES = 3
        self._limitTimeCreation = 200
        self._updateTimeCreation = 1
        self._dropLucky = 300 ## essa variavel define o nivel de dificuldade

        self.LOSELIFE = -1
        self.WINLIFE = 1


    def _drop(self):
        if self._nlifes < self._MAXLIFES:
            if self._updateTimeCreation > 0:
                self._updateTimeCreation -= 1
            else:
                sorted = randint(0, self._dropLucky)
                if sorted == 0:
                    self._positions.append([randint(0, self._screenSize[0] - self._skin.get_width()), -1])
                    self._updateTimeCreation = self._limitTimeCreation



    def update(self):
        self._drop()

        for i, position in enumerate(self._positions):
            self._positions[i][1] += self._SPEED
            if position[1] > self._screenSize[1] + 1:
                self._positions.pop(i)


    def pop(self, index:int):
        """
        Pass an index to remove from the list of positions.
        """
        if len(self._positions) != 0 and len(self._positions) > index:
            self._positions.pop(index)


    def set_nlifes(self, setState:int):
        """
        Set Number of Lifes:
        LOSELIFE, WINLIFE.
        """
        self._nlifes += setState


    def get_positions(self):
        """
        Return list of positions.
        """
        return self._positions


    def get_skin(self):
        """
        Return skin lifes.
        """
        return self._skin
    

    def get_nlifes(self):
        return self._nlifes


    def get_size(self):
        """
        Return life size.
        """
        return self._skin.get_size()
    

    def set_screenSize(self, screenSize:tuple):
        """
        Set Screen Size
        """
        self._screenSize = screenSize

    