import pygame


class Laser:
    def __init__(self):
        self._skin = pygame.image.load("res/laser.png")
        self._skin = pygame.transform.scale(self._skin, (10, 25))
        self._positions = []
        self._SPEED = 11
        self._sumSpeed = 0
        self._density = 30
        self._step = 0
        
        self._isTripleShoot = False
        self.SPEED2x = 0
        self.SPEED3x = 1
        self.TRIPLESHOOT = 2
        self.OVERPOWER = 3
        self.NORMAL = 4


    def update(self,posLeftBullets:tuple, posCenterBullets:tuple, posRightBullets:tuple):
        self._step += 1
        self._step %= self._density
        if self._step == 0:
            if self._isTripleShoot:
                self._positions.append(list(posCenterBullets))
            self._positions.append(list(posLeftBullets))
            self._positions.append(list(posRightBullets))
           
        for i, position in enumerate(self._positions):
            self._positions[i][1] -= self._SPEED + self._sumSpeed
            if position[1] < -self._skin.get_height():
                self._positions.pop(i)


    def positions(self):
        return self._positions
    

    def skin(self):
        return self._skin


    def size(self):
        return self._skin.get_size()

    
    def pop(self, index:int):
        if len(self._positions) != 0 and len(self._positions) > index:
            self._positions.pop(index)


    def set(self, setPower:int):
        match setPower:
            case self.NORMAL:
                self._sumSpeed = 0
                self._isTripleShoot = False
                self._density = 30

            case self.SPEED2x:
                self._sumSpeed = 10
                self._density = 15
                
            case self.SPEED3x:
                self._sumSpeed = 10
                self._density = 10
            
            case self.TRIPLESHOOT:
                self._isTripleShoot = True

            case self.OVERPOWER:
                self._isTripleShoot = True
                self._sumSpeed = 10
                self._density = 10
            
            case _:
                pass
