import pygame

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

class Rocket:
    def __init__(self):
        self._skin = [pygame.image.load("res/planeUp.png"),\
                          pygame.image.load("res/planeDown.png"),\
                          pygame.image.load("res/planeLeft.png"),\
                          pygame.image.load("res/planeRight.png")]
        
        for i, image in enumerate(self._skin):
            self._skin[i] = pygame.transform.scale(image, (100, 100))

        self._position = [200, 380]
        self._SPEED = 10

   
    def update(self, move:tuple, screenSize):
        ## TODO Ajeitar movimentação diagonal, e movimentações de lados opostos, aceleração no movimento
        """
        move = (UP, DOWN, LEFT, RIGHT)
        """
        if move[0] and self._position[1] > 0:
            self._position[1] -= self._SPEED

        if move[1] and self._position[1] < screenSize[1] - self._skin[0].get_height():
            self._position[1] += self._SPEED

        if move[2] and self._position[0] > 0:
            self._position[0] -= self._SPEED
        
        if move[3] and self._position[0] < screenSize[0] - self._skin[0]. get_width():
            self._position[0] += self._SPEED


    def position(self, incrementX:int=0, incrementY:int=0):
        return self._position[0] + incrementX, self._position[1] + incrementY
    

    def size(self):
        return self._skin[0].get_size()


    def skin(self):
        return self._skin