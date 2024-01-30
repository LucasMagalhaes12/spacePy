import pygame

class Window():
    def __init__(self, currentResolution:tuple):
        self.currentResolution = currentResolution
        self.resolutions = (1920, 1080), (1366, 768), (640, 480)


    def updateResolution(self, screen, newResolution:int, isFullScreen:bool=True):
        """
        Select Resolution:
        0 = 1920x1080
        1 = 1366x768
        2 = 640x480
        """
        print(type(self.resolutions), self.resolutions)
        self.currentResolution = self.resolutions[1]
        if isFullScreen:
            screen = pygame.display.set_mode(self.currentResolution, pygame.FULLSCREEN)
        else:
            screen = pygame.display.set_mode(self.currentResolution)


    def margin(self, percentMargin:int=50):
        result = (self.currentResolution[0] * percentMargin) // 1080
        # print(result)
        return result
    