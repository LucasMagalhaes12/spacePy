import pygame

class Selections:
    def __init__(self):
        self._skinSelection = pygame.image.load("res/selection.png")
        self._skinSelection = pygame.transform.scale(self._skinSelection, (100, 25))
        self._selections = {
            "menu":[0, 3],
            "configuration":[0, 5],
            "window":[0, 2],
            "resolutions":[0, 3],
            "language":[0, 2]
        }

        self.NEXT = 1
        self.PREVIUS = -1


    def moveSelection(self, menu:str, move:int):
        """
        Moves:
        Next = 1
        Previus = -1
        """
        if move > 0:
            self._selections[menu][0] += 1
        if move < 0:
            self._selections[menu][0] -= 1

        self._selections[menu][0] %= self._selections[menu][1]
        

    def resetPos(self, menu:str):
        self._selections[menu][0] = 0


    def get_pos(self, menu):
        return int(self._selections[menu][0])


    def get_skin(self):
        return self._skinSelection
    

    def set_size(self, size:tuple):
        self._skinSelection = pygame.transform.scale(self._skinSelection, size)