
from controls import Controls
from draw import Draw
from selections import Selections
from names import Names
from window import Window


import pygame
from random import randint

pygame.init()

NEXT = 1
PREVIUS = -1
WINDOW = False
FULLSCREEN = pygame.FULLSCREEN

# currentScreenResolution = pygame.display.Info().current_w, pygame.display.Info().current_h
CURRENTRESOLUTION = (1366, 768)

#criar arquivo de configuração
resolutions = {"640x480":(640, 480), "1366x768":(1366, 768), "1920x1080":(1920, 1080)}
screen = pygame.display.set_mode()
pygame.display.set_caption('Shooter')
clock = pygame.time.Clock()

window = Window(CURRENTRESOLUTION)
window.updateResolution(screen, 0, False)

currentLanguage = "PTBR"
names = Names(currentLanguage)


#Images
backgroundMenu = pygame.image.load("res/backgroundMenu.png")
backgroundMenu = pygame.transform.scale(backgroundMenu, window.returnCurrentResolution())


selections = Selections((100, 25))
controls = Controls()
draw = Draw()


def game():
    runningConfig = True
    while runningConfig:
        clock.tick(60)
        controls.update()
        runningConfig = not controls.keys["QUIT"]
        
        screen.fill(pygame.Color('black'))
        pygame.display.update()


def configuration():
    runningConfig = True
    selections.resetPos("configuration")
    while runningConfig:
        clock.tick(60)
        
        # Draw Configuration
        print(selections.pos("configuration"), selections.pos("configuration"), controls.keys)
        screen.fill(pygame.Color('black'))
        draw.title(screen, ("Configuration", (300, 20)))
        draw.multiWords(screen, names.items("config"))
        
        draw.name(screen, names.items("window")[selections.pos("window")])
        draw.name(screen, names.items("resolutions")[selections.pos("resolutions")])
        draw.name(screen, names.items("langSelection")[selections.pos("lang")])
 
        draw.image(screen, selections.skin(), (names.positions("config")[selections.pos("configuration")][0]-5, names.positions("config")[selections.pos("configuration")][1]-5))
        pygame.display.update()

        # Controls
        controls.update()
        runningConfig = not controls.keys["QUIT"]
        
        if controls.keyStatus("UP"):
            selections.moveSelection("configuration", PREVIUS)
            controls.setKey("UP", False)

        elif controls.keyStatus("DOWN"):
            selections.moveSelection("configuration", NEXT)
            controls.setKey("DOWN", False)

        elif controls.keyStatus("LEFT") or controls.keyStatus("RIGHT"):
            if selections.pos("configuration") == 0:
                if controls.keyStatus("LEFT"):
                    selections.moveSelection("window", PREVIUS)
                    controls.setKey("LEFT", False)
                elif controls.keyStatus("RIGHT"):
                    selections.moveSelection("window", NEXT)
                    controls.setKey("RIGHT", False)

            elif selections.pos("configuration") == 1:
                if controls.keyStatus("LEFT"):
                    selections.moveSelection("resolutions", PREVIUS)
                    controls.setKey("LEFT", False)
                elif controls.keyStatus("RIGHT"):
                    selections.moveSelection("resolutions", NEXT)
                    controls.setKey("RIGHT", False)

            elif selections.pos("configuration") == 2:
                if controls.keyStatus("LEFT"):
                    selections.moveSelection("lang", PREVIUS)
                    controls.setKey("LEFT", False)

                elif controls.keyStatus("RIGHT"):
                    selections.moveSelection("lang", NEXT)
                    controls.setKey("RIGHT", False)


        if controls.keyStatus("ACTION"):
            if selections.pos("configuration") == 3:
                window.updateResolution(screen, selections.pos("resolutions"), not selections.pos("window"))
                global backgroundMenu
                backgroundMenu = pygame.transform.scale(backgroundMenu, window.returnCurrentResolution())

            if  selections.pos("configuration") == 4:
                runningConfig = False
                controls.setKey("ACTION", False)
            
        


def mainMenu():
    running = True
    while running:
        clock.tick(60)
        controls.update()
        running = not controls.keys["QUIT"]
        # print(names.names("menu")[selections.pos("menu")], selections.pos("menu"), controls.keys)
        if controls.keys["UP"]:
            selections.moveSelection("menu", PREVIUS)
            controls.keys["UP"] = False

        elif controls.keys["DOWN"]:
            selections.moveSelection("menu", NEXT)
            controls.keys["DOWN"] = False

        if controls.keys["ACTION"]:
            if selections.pos("menu") == 0:
                game()
                selections.resetPos("menu")
            
            elif selections.pos("menu") == 1:
                configuration()
                selections.resetPos("menu")
            
            elif selections.pos("menu") == 2:
                controls.keys["QUIT"] = True

        draw.image(screen, backgroundMenu, (0, 0))
        draw.image(screen, selections.skin(), (names.positions("menu")[selections.pos("menu")][0]-5, names.positions("menu")[selections.pos("menu")][1]-5))
        draw.multiWords(screen, names.items("menu"))
        pygame.display.update()


mainMenu()
pygame.quit()
