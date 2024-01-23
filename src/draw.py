import pygame

class Draw():
    def __init__(self):
        self.fontTextOptions = pygame.font.Font(None, 24)
        self.fontTextTitles = pygame.font.Font(None, 32)



    def background(self, screen, background):
        screen.blit(background, (0, 0))


    def multiWords(self, screen,  optionsAndPos:dict, color=(255, 255, 255)):
        for name in optionsAndPos:
            renderText = self.fontTextOptions.render(name, True, color)
            screen.blit(renderText, optionsAndPos[name])
    

    def singleWord(self, screen, name, pos:tuple, color=(255, 255, 255)):
        renderText = self.fontTextTitles.render(name, True, color)
        screen.blit(renderText, pos)

    def image(self, screen, image, position:tuple):
        screen.blit(image, position)