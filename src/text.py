import pygame

class Text():
    def __init__(self):
        self.fontText = pygame.font.Font(None, 24)
        # self.textMenu = ('Start', 'Options', 'Exit')

    def textinDictionary(self, screen,  optionsAndPos, color=(255, 255, 255)):
        for name in optionsAndPos:
            renderText = self.fontText.render(name, True, color)
            screen.blit(renderText, optionsAndPos[name])