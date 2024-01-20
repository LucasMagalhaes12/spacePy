from controls import Controls
from text import *

import pygame
from random import randint

pygame.init()

# currentScreenResolution = pygame.display.Info().current_w, pygame.display.Info().current_h
currentScreenResolution = (640, 480)
#criar arquivo de configuração
screen = pygame.display.set_mode(currentScreenResolution)
pygame.display.set_caption('Shooter')
clock = pygame.time.Clock()



controls = Controls()
text = Text()

backgroundMenu = pygame.image.load("res/backgroundMenu.png")
if currentScreenResolution != (1920, 1080):
    print("transform")
    backgroundMenu = pygame.transform.scale(backgroundMenu, currentScreenResolution)


def mainMenu():
    running = True
    while running:
        if controls.isPressQuit():
            running = False
        clock.tick(60)
        # screen.fill(pygame.Color('black'))
        #classe para desenhar o menu
        screen.blit(backgroundMenu, (0, 0))
        text.drawTextMenu(screen)
        pygame.display.update()

mainMenu()
pygame.quit()