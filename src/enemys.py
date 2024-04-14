import pygame
from random import randint

class Enemys:
    def __init__(self):
        self._skin = pygame.image.load("res/enemy.png")
        self._skin = pygame.transform.scale(self._skin, (100, 100))
        
        self._positions = []
        self._SPEED = 6
        self._density = 60
        self._lucky = 100
        self._time = 0
        self._size = {"WIDTH": self._skin.get_width(), "HEIGHT":self._skin.get_height(), "SIZE":self._skin.get_size()}


    def update(self, screenSize):
        """
        Creates an enemy in a random position and removes them if they go beyond the edge of the screen.
        """
        if self._time == 0:
            sorted = randint(0, self._lucky)
            if sorted == 0:
                self._positions.append([randint(0, screenSize[0] - self._size["WIDTH"]), -self._size["HEIGHT"]])
                self._time = self._density
        else:
            if self._time > 0:
                self._time -= 1
            
        for i, position in enumerate(self._positions):
            self._positions[i][1] += self._SPEED
            if position[1] > screenSize[1] + self._size["HEIGHT"]:
                self._positions.pop(i)


    def difficulty(self):
        pass


    def positions(self):
        """
        return positions list.
        """
        return self._positions

    
    def size(self):
        """
        Return enemy size.
        """
        return self._size["SIZE"]
    

    def skin(self):
        """
        Return enemy skin.
        """
        return self._skin


    def pop(self, index:int):
        """
        Remove enemy index from positions list.
        """
        if index < len(self._positions) != 0:
            self._positions.pop(index)
