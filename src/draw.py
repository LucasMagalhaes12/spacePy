import pygame

class Draw():
    def __init__(self):
        self.fontTextOptions = pygame.font.Font(None, 24)
        self.fontTextTitles = pygame.font.Font(None, 32)
        self.skinBackgroundMenu = pygame.image.load("res/backgroundMenu.png")
        self.contPositionRect = 0
        # self.rectPositions = []


    def backgroundMenu(self, screen):
        screen.blit(self.skinBackgroundMenu, (0, 0))

    def resetPositionRect(self):
        self.contPositionRect = 0

    def nextPositionRect(self):
        self.contPositionRect += 1

    def previusPositionRect(self):
        self.contPositionRect -= 1

    def rect(self, screen, positions:dict):
        print(len(positions))
        self.contPositionRect =  self.contPositionRect % len(positions)
        pygame.draw.rect(screen, (255, 255, 255), (positions[self.contPositionRect][0]-5, positions[self.contPositionRect][1]-5, 80, 30), 2)

    def textOptions(self, screen,  optionsAndPos, color=(255, 255, 255)):
        for name in optionsAndPos:
            renderText = self.fontTextOptions.render(name, True, color)
            screen.blit(renderText, optionsAndPos[name])
        
    def textTitle(self, screen, name, pos:tuple, color=(255, 255, 255)):
        renderText = self.fontTextTitles.render(name, True, color)
        screen.blit(renderText, pos)