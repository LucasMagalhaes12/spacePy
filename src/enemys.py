import pygame
from random import randint

class Enemys:
    def __init__(self):
        self._skin = [pygame.image.load("res/enemy.png"), pygame.image.load("res/enemy.png")]
        for i, image in enumerate(self._skin):
            self._skin[i] = pygame.transform.scale(image, (100, 100))
        
        self._positions = []
        self._SPEED = 6
        self._timeCreation = 30
        self._time = 0
        self._isCreation = False

    def skin(self):
        return self._skin
    

    def new(self, screenSize):
        if self._isCreation:
            self._positions.append([randint(0, screenSize[0] - self._skin[0].get_width()), -self._skin[0].get_height()])
    
    def update(self, screenSize):
        # print(self._positions)
        self._time += 1
        self._time %= 1 + self._timeCreation
        self._isCreation = True if self._time == self._timeCreation else False

        for i, position in enumerate(self._positions):
            self._positions[i][1] += self._SPEED
            if position[1] > screenSize[1] - self._skin[0].get_height():
                self._positions.pop(i)



    def positions(self):
        return self._positions