import pygame

class Selections:
    def __init__(self):

        # MENU : [currentPosition, moveLimit]
        self.selections = {
            "menu":[0, 3],
            "configuration":[0, 5],
            "window":[0, 2],
            "resolutions":[0, 3],
            "lang":[0, 2]
        }
        

    def moveSelection(self, menu:str, move:int):
        """
        Moves:
        Next = 1
        Previus = -1
        """
        if move > 0:
            self.selections[menu][0] += 1
        if move < 0:
            self.selections[menu][0] -= 1

        self.selections[menu][0] %= self.selections[menu][1]
        

    def resetPos(self, menu:str):
        self.selections[menu][0] = 0


    def pos(self, menu):
        return int(self.selections[menu][0])


    # def showCurrentPosition(self):
    #     if (len(self.positions) > 0):
    #         return self.positions[self.contPosition]