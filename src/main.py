
from controls import Controls
# from text import *
from draw import Draw
# from namesAndPositions import NamesAndPositions

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
# text = Text()
draw = Draw()
namesPositionsMenu = {'Start':(50, 50), 'Options':(50, 100), 'Exit':(50, 200)}
namesPositionsConfiguration = {'Resolution':(50, 50), 'Language':(50, 100), 'Back':(50, 200)}
# if currentScreenResolution != (1920, 1080):
#     print("transform")
#     backgroundMenu = pygame.transform.scale(backgroundMenu, currentScreenResolution)


def game():
    print("Gamer")
    pass


def configuration():
    print(configuration)
    runningConfig = True
    draw.resetPositionRect()
    while runningConfig:
        clock.tick(60)
        controls.update()
        runningConfig = not controls.updates["QUIT"]
        print(draw.contPositionRect, controls.updates)
        
        if controls.updates["UP"]:
            draw.previusPositionRect()
            controls.updates["UP"] = False

        elif controls.updates["DOWN"]:
            draw.nextPositionRect()
            controls.updates["DOWN"] = False

        if controls.updates["ACTION"]:
            result = tuple(namesPositionsConfiguration.keys())[draw.contPositionRect]
            if  result == "Back":
                runningConfig = False
                controls.updates["ACTION"] = False
            

        screen.fill(pygame.Color('black'))
        # draw.backgroundMenu(screen)
        draw.textTitle(screen, "Configuration", (currentScreenResolution[0]/2-60, 20))
        draw.textOptions(screen, namesPositionsConfiguration)
        draw.rect(screen, tuple(namesPositionsConfiguration.values()))
        pygame.display.update()


def mainMenu():
    running = True
    while running:
        clock.tick(60)
        controls.update()
        running = not controls.updates["QUIT"]
        print(draw.contPositionRect, controls.updates)
        
        if controls.updates["UP"]:
            draw.previusPositionRect()
            controls.updates["UP"] = False

        elif controls.updates["DOWN"]:
            draw.nextPositionRect()
            controls.updates["DOWN"] = False

        if controls.updates["ACTION"]:
            result = tuple(namesPositionsMenu.keys())[draw.contPositionRect]
            if  result == "Start":
                game()
            elif  result == "Options":
                configuration()
                draw.resetPositionRect()
            elif result == "Exit":
                controls.updates["QUIT"] = True
            

        # screen.fill(pygame.Color('black'))
        draw.backgroundMenu(screen)
        draw.textOptions(screen, namesPositionsMenu)
        draw.rect(screen, tuple(namesPositionsMenu.values()))
        pygame.display.update()


mainMenu()
pygame.quit()