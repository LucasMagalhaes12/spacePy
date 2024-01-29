import pygame

class Window():
    def __init__(self, currentResolution:tuple):
        self.currentResolution = currentResolution


    def updateResolution(self, screen, newResolution:tuple, isFullScreen:bool=True):
        self.currentResolution = newResolution
        if isFullScreen:
            screen = pygame.display.set_mode(self.currentResolution, pygame.FULLSCREEN)
        else:
            screen = pygame.display.set_mode(self.currentResolution)


    def margin(self, percentMargin:int=50):
        result = (self.currentResolution[0] * percentMargin) // 1080
        # print(result)
        return result
    