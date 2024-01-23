import pygame


class Selection:
    def __init__(self, limitMoves:int):
        self.contPosition = 0
        self.limitMoves = limitMoves
        # self.positions = positions

    # def updatePositions(self, positions:list):
    #     self.positions = positions
        # pygame.draw.rect(screen, (255, 255, 255), (positions[self.currentPositionSelection][0]-5, positions[self.currentPositionSelection][1]-5, 80, 30), 2)
    

    def moveSelection(self, move:int):
        """
        Moves:
        Next = 1
        Previus = -1
        """
        if move > 0:
            self.contPosition += 1
        if move < 0:
            self.contPosition -= 1

        self.contPosition %= self.limitMoves
        

    def resetPositionRect(self):
        self.contPosition = 0


    def showCont(self):
        return self.contPosition

    # def showCurrentPosition(self):
    #     if (len(self.positions) > 0):
    #         return self.positions[self.contPosition]