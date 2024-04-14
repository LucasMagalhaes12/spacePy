from random import randint
import pygame

class PowerUps:
    def __init__(self):
        self._skins = [pygame.image.load("res/speed2x.png"), 
                       pygame.image.load("res/speed3x.png"),
                       pygame.image.load("res/tripleShot.png"),
                       pygame.image.load("res/overPower.png")]
        
        for i, image in enumerate(self._skins):
            self._skins[i] = pygame.transform.scale(image, (40, 40))
        self._SPEED = 5
        self._positions = []
        self._density = 300
        self._lucky = 300

        self._timeCreation = 0

        self._duration = 0
        self.LIMITDURATION = 400
        self.SPEED2x = 0
        self.SPEED3x = 1
        self.TRIPLESHOOT = 2
        self.OVERPOWER = 3


    def update(self, screenSize:tuple):
        if self._timeCreation == 0:
            sorted = randint(0, self._lucky)
            if sorted == 0:
                self._positions.append([randint(0, screenSize[0] - self._skins[0].get_width()), -self._skins[0].get_height(), randint(0, 3)])
                self._timeCreation = self._density
        else:
            if self._timeCreation > 0:
                self._timeCreation -= 1

        for i, position in enumerate(self._positions):
            self._positions[i][1] += self._SPEED
            if position[1] > screenSize[1] + self._skins[0].get_height():
                self._positions.pop(i)


    def positions(self):
        return self._positions

    def skin(self, numSkin=0):
        return self._skins[numSkin]
    

    def size(self):
        return self._skins[0].get_size()
    

    def take(self, index:int):
        self._duration = self.LIMITDURATION
        if len(self._positions) != 0 and len(self._positions) > index:
            self._positions.pop(index)


    def duration(self):
        return self._duration


    def isWithPowerUP(self):
        if self._duration == 0:
            return False
        if self._duration > 0:
            self._duration -= 1
        return True
        