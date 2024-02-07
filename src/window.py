import pygame

class Window():
    def __init__(self, screen, resolutionSelection:int, isFullScreen:bool=False):
        ## TODO Melhorar o Input do resolution Selection
        """
        Select Resolution:
        0 = 1920x1080
        1 = 1366x768
        2 = 640x480
        """
        self._resolutions = (1920, 1080), (1366, 768), (640, 480)
        self._currentResolution = self._resolutions[resolutionSelection]
        self.updateResolution(screen, resolutionSelection, isFullScreen)


    def updateResolution(self, screen, newResolution:int, isFullScreen:bool=True):
        """
        Select Resolution:
        0 = 1920x1080
        1 = 1366x768
        2 = 640x480
        """
        self._currentResolution = self._resolutions[newResolution]
        if isFullScreen:
            screen = pygame.display.set_mode(self._currentResolution, pygame.FULLSCREEN)
        else:
            screen = pygame.display.set_mode(self._currentResolution)


    def margin(self, percentMargin:int=50):
        result = (self._currentResolution[0] * percentMargin) // 1080
        # print(result)
        return result
    

    def resolution(self):
        return self._currentResolution