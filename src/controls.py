import pygame

class Controls():
    def __init__(self):
        pass
    
    def isPressQuit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
                print("pressed quit")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
        return False