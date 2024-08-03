from random import randint
import pygame

class PowerUps:
    def __init__(self, screenSize:tuple):
        self._skins = [pygame.image.load("res/speed2x.png"), 
                       pygame.image.load("res/speed3x.png"),
                       pygame.image.load("res/tripleShot.png"),
                       pygame.image.load("res/overPower.png")]
        
        for i, image in enumerate(self._skins):
            self._skins[i] = pygame.transform.scale(image, (40, 40))
        
        self._screenSize = screenSize
        self._SPEED = 5
        self._positions = []
        self._density = 300
        self._lucky = 300 ## essa variavel define o nivel de dificuldade

        self._updateTimeCreation = 0
        self._duration = 0
        self._LIMITDURATION = 400

        self.SPEED2x = 0
        self.SPEED3x = 1
        self.TRIPLESHOOT = 2
        self.OVERPOWER = 3


    def _drop(self):
        if self._updateTimeCreation == 0:
            sorted = randint(0, self._lucky)
            if sorted == 0:
                self._positions.append([randint(0, self._screenSize[0] - self._skins[0].get_width()), -self._skins[0].get_height(), randint(0, 3)])
                self._updateTimeCreation = self._density
        else:
            if self._updateTimeCreation > 0:
                self._updateTimeCreation -= 1


    def update(self):
        self._drop()
        for i, position in enumerate(self._positions):
            self._positions[i][1] += self._SPEED
            if position[1] > self._screenSize[1] + self._skins[0].get_height():
                self._positions.pop(i)


    def get_positions(self):
        """
        Return list of positions.
        """
        return self._positions


    def get_skin(self, numSkin=0):
        """
        Return skin lifes.
        """
        return self._skins[numSkin]
    

    def get_size(self):
        """
        Return laser size.
        """
        return self._skins[0].get_size()
    

    def take(self, index:int):
        self._duration = self._LIMITDURATION
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
        

    def set_screenSize(self, screenSize:tuple):
        """
        Set Screen Size
        """
        self._screenSize = screenSize