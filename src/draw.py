import pygame

class Draw():
    def __init__(self):
        self.fontTextOptions = pygame.font.Font(None, 24)
        self.fontTextTitles = pygame.font.Font(None, 32)



    def background(self, screen, background):
        screen.blit(background, (0, 0))


    def multiWords(self, screen,  optionsAndPos:dict, color=(255, 255, 255)):
        for name in optionsAndPos:
            # print(name)
            renderText = self.fontTextOptions.render(name, True, color)
            screen.blit(renderText, optionsAndPos[name])
    

    def name(self, screen, nameandPosition:tuple, incrementX:int=0, incrementY:int=0,color=(255, 255, 255)):
        renderText = self.fontTextTitles.render(nameandPosition[0], True, color)
        screen.blit(renderText, (nameandPosition[1][0] + incrementX, nameandPosition[1][1] + incrementY))


    def title(self, screen, nameandPosition:tuple, incrementX:int=0, incrementY:int=0,color=(255, 255, 255)):
        renderText = self.fontTextTitles.render(nameandPosition[0], True, color)
        screen.blit(renderText, (nameandPosition[1][0] + incrementX, nameandPosition[1][1] + incrementY))


    def selectionsNames(self, screen, names:tuple, indexName:int, position:tuple, incrementX:int=0, incrementY:int=0, color:tuple=(255, 255, 255)):
        renderText = self.fontTextOptions.render(names[indexName], True, color)
        screen.blit(renderText, (position[0] + incrementX, position[1] + incrementY))


    def image(self, screen, image, position:tuple):
        screen.blit(image, position)