import pygame

class Draw():
    def __init__(self):
        self.FONTOPTIONS = pygame.font.Font(None, 24)
        self.FONTTITLE = pygame.font.Font(None, 32)



    def image(self, screen, image, position:tuple):
        screen.blit(image, position)


    def multiNames(self, screen,  namesPositions:tuple, color=(255, 255, 255)):
        for name in namesPositions:
            renderText = self.FONTOPTIONS.render(name[0], True, color)
            screen.blit(renderText, name[1])
    

    def name(self, screen, font:pygame.font.Font, namesPositions:tuple, incrementX:int=0, incrementY:int=0, color=(255, 255, 255)):
        renderText = font.render(namesPositions[0], True, color)
        screen.blit(renderText, (namesPositions[1][0] + incrementX, namesPositions[1][1] + incrementY))
