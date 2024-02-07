import pygame


class Bullets:
    def __init__(self):
        self._skin = pygame.image.load("res/bullet.png")
        self._skin = pygame.transform.scale(self._skin, (20, 25))
        self._positions = []
        self._SPEED = 11
        self._timeCreation = 30
        self._auxTimeCreation = self._timeCreation 
        self._isCreation = False
        self._time = 0

        self.NORMALSPEED = 1
        self.DOUBLESPEED = 2
        self.TRIPLESPEED = 3
        self.OVERPOWERSPEED = 5


    def new(self, position):
        if self._isCreation:
            self._positions.append(list(position))


    def update(self):
        # print("---", self._positions)
        self._time += 1
        self._time %= 1 + self._timeCreation
        self._isCreation = True if self._time == self._timeCreation else False
        for i, position in enumerate(self._positions):
            self._positions[i][1] -= self._SPEED
            if position[1] < -self._skin.get_height():
                self._positions.pop(i)



    def positions(self):
        return self._positions
    

    def skin(self):
        return self._skin
   
   
    # def acelleration(self, UP, DOWN):
    #     if UP:
    #         for i, position in enumerate(self._positions):
    #             self._positions[i][1] += self._SPEED
    #     if DOWN:
    #         for i, position in enumerate(self._positions):
    #             self._positions[i][1] -= self._SPEED

    
    def setSpeed(self, setSpeed:int):
        """
        Select Speed:
            1 = Normal Speed
            2 = 2x Speed
            3 = 3x Speed
        """
        self._timeCreation = self._auxTimeCreation // setSpeed