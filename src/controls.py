import pygame

class Controls():
    """
    return bool list with values:
    ["Quit", "UP", "Down", "Left", "Right", "Action"]
    """
    def __init__(self):
        self.keys = {"QUIT":False, "UP":False, "DOWN":False, "LEFT":False, "RIGHT":False, "ACTION":False}
        self.configKeys = {"QUIT":pygame.K_ESCAPE, "UP":pygame.K_w, "DOWN":pygame.K_s, "LEFT":pygame.K_a, "RIGHT":pygame.K_d, "ACTION":pygame.K_SPACE}
    
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.keys["QUIT"] = True
            if event.type == pygame.KEYDOWN:
                for keyPressed in self.configKeys:
                    if event.key == self.configKeys[keyPressed]:
                        self.keys[keyPressed] = True
            
            if event.type == pygame.KEYUP:
                for keyPressed in self.configKeys:
                    if event.key == self.configKeys[keyPressed]:
                        self.keys[keyPressed] = False

    def keyStatus(self, key:str):
        return self.keys[key]
    
    def setKey(self, key:str, setStatus:bool):
        self.keys[key] = setStatus