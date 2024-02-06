import pygame

class Controls():
    """
    return bool list with values:
    ["Quit", "UP", "Down", "Left", "Right", "Action"]
    """
    def __init__(self):
        self._keys = {"UP":False, "DOWN":False, "LEFT":False, "RIGHT":False, "ACTION":False, "QUIT":False}
        self._configKeys = {"UP":pygame.K_w, "DOWN":pygame.K_s, "LEFT":pygame.K_a, "RIGHT":pygame.K_d, "ACTION":pygame.K_SPACE, "QUIT":pygame.K_ESCAPE}
    
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._keys["QUIT"] = True
            if event.type == pygame.KEYDOWN:
                for keyPressed in self._configKeys:
                    if event.key == self._configKeys[keyPressed]:
                        self._keys[keyPressed] = True
            
            if event.type == pygame.KEYUP:
                for keyPressed in self._configKeys:
                    if event.key == self._configKeys[keyPressed]:
                        self._keys[keyPressed] = False


    def keyStatus(self, key:str):
        """
        Return state Key:
        key = UP, DOWN, LEFT, RIGHT, ACTION, QUIT or ALL(Return all keys)
        """
        if key == "ALL":
            return tuple(self._keys.values())
        return self._keys[key]


    def setKey(self, key:str, setStatus:bool):
        if key == "ALL":
            self._keys["UP"] = setStatus
            self._keys["DOWN"] = setStatus
            self._keys["LEFT"] = setStatus
            self._keys["RIGHT"] = setStatus
        self._keys[key] = setStatus
        