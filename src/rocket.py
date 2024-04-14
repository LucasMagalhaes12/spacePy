import pygame


class Rocket:
    def __init__(self, screenSize):
        self._skin = pygame.image.load("res/rocket.png")
        self._skin = pygame.transform.scale(self._skin, (110, 100))
        
        self._position = {'x':screenSize[0]//2-self._skin.get_width()//2, 'y':screenSize[1]//2+self._skin.get_height()}
        self._MAXSPEED = 15
        self._INCREMENTSPEED = 1
        self._speed = 3
        self._limitWidth = screenSize[0] - self._skin. get_width()
        self._limitHeigth = screenSize[1] - self._skin.get_height()

   
    def update(self, keysPresseds:dict, screenSize):
        """
        Update rocket with buttons presseds
        """
        if (keysPresseds["UP"] or keysPresseds["DOWN"]) and (keysPresseds["LEFT"] or keysPresseds["RIGHT"]):
            self._speed = self._MAXSPEED // 2 + 3

        else:
            if True in keysPresseds.values() and self._speed < self._MAXSPEED:
                self._speed += self._INCREMENTSPEED
            elif self._speed > 3:
                self._speed -= self._INCREMENTSPEED
        
        if keysPresseds["UP"]:
            if self._position['y'] - self._speed > 0:
                self._position['y'] -= self._speed
            else:
                 self._position['y'] = 0

        if keysPresseds["DOWN"]:
            if self._position['y'] < self._limitHeigth:
                self._position['y'] += self._speed
            else:
                self._position['y'] = self._limitHeigth
        
        if keysPresseds["LEFT"]:
            if self._position['x'] - self._speed > 0:
                self._position['x'] -= self._speed
            else:
                self._position['x'] = 0
        
        if keysPresseds["RIGHT"]:
            if self._position['x'] < self._limitWidth:
                self._position['x'] += self._speed
            else:
                self._position['x'] = self._limitWidth


    def position(self, incrementX:int=0, incrementY:int=0):
        """
        Returns the position of the rocket
        """
        return self._position['x'] + incrementX, self._position['y'] + incrementY
    

    def size(self):
        """
        Returns the size of the rocket
        """
        return self._skin.get_size()


    def updateScreenSize(self, screenSize):
        self._position = {'x':screenSize[0]//2-self._skin.get_width()//2, 'y':screenSize[1]//2+self._skin.get_height()}
        self._limitWidth = screenSize[0] - self._skin. get_width()
        self._limitHeigth = screenSize[1] - self._skin.get_height()


    def skin(self):
        """
        Returns the skin of the rocket
        """
        return self._skin
