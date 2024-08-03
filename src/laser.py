import pygame


class Laser:
    def __init__(self):
        self._skin = pygame.image.load("res/laser.png")
        self._skin = pygame.transform.scale(self._skin, (10, 25))
        self._positions = []
        self._SPEED = 11
        self._incrementSpeed = 0
        self._limitTimeCreation = 30
        self._updateTimeCreation = 0

        self._isTripleShoot = False
        self.SPEED2x = 0
        self.SPEED3x = 1
        self.TRIPLESHOOT = 2
        self.OVERPOWER = 3
        self.NORMAL = 4


    def _createLaser(self, posLeft:list, posCenter:list, posRight:list):
        self._updateTimeCreation += 1
        self._updateTimeCreation %= self._limitTimeCreation
        if self._updateTimeCreation == 0:
            self._positions.append(list(posLeft))
            self._positions.append(list(posRight))
            if self._isTripleShoot:
                self._positions.append(list(posCenter))


    def update(self, posLeft:list, posCenter:list, posRight:list):
        """
        DEFINE LASER POSITIONS:
        LEFT, CENTER, RIGHT.
        """
        
        self._createLaser(posLeft, posCenter, posRight)
 
        for i, position in enumerate(self._positions):
            self._positions[i][1] -= self._SPEED + self._incrementSpeed
            if position[1] < - self._skin.get_height():
                self._positions.pop(i)


    def get_positions(self):
        """
        Return list of positions.
        """
        return self._positions
    

    def get_skin(self):
        """
        Return skin Laser.
        """
        return self._skin


    def get_size(self):
        """
        Return laser size.
        """
        return self._skin.get_size()

    
    def pop(self, index:int):
        """
        Pass an index to remove from the list of positions.
        """
        if len(self._positions) != 0 and len(self._positions) > index:
            self._positions.pop(index)


    def set_laser(self, setPower:int):
        """
        Set Laser State:
        NORMAL, SPEED2x, SPEED3x, TRIPLESHOOT, OVERPOWER.
        """
        match setPower:
            case self.NORMAL:
                self._incrementSpeed = 0
                self._isTripleShoot = False
                self._limitTimeCreation = 30

            case self.SPEED2x:
                self._incrementSpeed = 10
                self._limitTimeCreation = 15
                
            case self.SPEED3x:
                self._incrementSpeed = 10
                self._limitTimeCreation = 10
            
            case self.TRIPLESHOOT:
                self._isTripleShoot = True

            case self.OVERPOWER:
                self._isTripleShoot = True
                self._incrementSpeed = 10
                self._limitTimeCreation = 10
            
            case _:
                pass
