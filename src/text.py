import pygame

class Text():
    def __init__(self):
        self.fontText = pygame.font.Font(None, 24)
        self.textMenu = {'Start':(50, 50), 'Options':(50, 100), 'Exit':(50, 200)}
        # self.textMenu = ('Start', 'Options', 'Exit')

    def drawTextMenu(self, screen):
        for name in self.textMenu:
            text = self.fontText.render(name, True, (255, 255, 255))
            screen.blit(text, self.textMenu[name])