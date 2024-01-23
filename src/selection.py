import pygame


class Selection:
    def __init__(self) -> None:
        self.contPosition = 0
        self.positions = []

    def updatePositions(self, positions:list):
        self.positions = positions
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

        self.contPosition %= len(self.positions)
        

    def resetPositionRect(self):
        self.contPosition = 0


    def showContPosition(self):
        return self.contPosition

    def showCurrentPosition(self):
        if (len(self.positions) > 0):
            return self.positions[self.contPosition]