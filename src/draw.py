import pygame

class Draw():
    def __init__(self):
        self.FONTOPTIONS = pygame.font.Font(None, 24)
        self.FONTTITLE = pygame.font.Font(None, 32)
        self._timeBar = 100

    def image(self, screen, image, position:tuple):
        """
        Draw image in the screen
        """
        screen.blit(image, position[:2])


    def name(self, screen, font:pygame.font.Font, namesPositions:tuple, incrementX:int=0, incrementY:int=0, color=(255, 255, 255)):
        renderText = font.render(namesPositions[0], True, color)
        screen.blit(renderText, (namesPositions[1][0] + incrementX, namesPositions[1][1] + incrementY))


    def multiNames(self, screen,  namesPositions:tuple, color=(255, 255, 255)):
        for name in namesPositions:
            renderText = self.FONTOPTIONS.render(name[0], True, color)
            screen.blit(renderText, name[1])
    

    def bar(self, screen, rectValues:tuple, porcent:int, colorInside:tuple=(255, 0, 0), colorOutSide:tuple=(255, 255, 255)):
        x, y, w, h = rectValues
        pygame.draw.rect(screen, colorOutSide, rectValues)
        pygame.draw.rect(screen, colorInside, (x+2, y+2, porcent-4, h-4))