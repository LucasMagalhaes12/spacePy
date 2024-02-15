import pygame
from random import randint

class Enemys:
    def __init__(self):
        self._skin = [pygame.image.load("res/enemy.png"), pygame.image.load("res/enemy.png")]
        for i, image in enumerate(self._skin):
            self._skin[i] = pygame.transform.scale(image, (100, 100))
        
        self._positions = []
        self._SPEED = 6
        self._density = 60
        self._step = 0
        self._isCreation = False
    

    def new(self, screenSize):
        self._step += 1
        self._step %= self._density
        if self._step == 0:
            self._positions.append([randint(0, screenSize[0] - self._skin[0].get_width()), -self._skin[0].get_height()])
    

    def update(self, screenSize):
        for i, position in enumerate(self._positions):
            self._positions[i][1] += self._SPEED
            if position[1] > screenSize[1] + self._skin[0].get_height():
                self._positions.pop(i)


    def positions(self):
        return self._positions

    
    def size(self):
        return self._skin[0].get_size()
    

    def skin(self):
        return self._skin


    def pop(self, index:int):
        if len(self._positions) != 0 and len(self._positions) > index:
            self._positions.pop(index)
