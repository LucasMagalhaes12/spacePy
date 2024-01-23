
from controls import Controls
from draw import Draw
from selection import Selection
from namesandPositions import NamesandPositions
from window import Window
# from namesAndPositions import NamesAndPositions

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
# resolutions = {"640x480":(640, 480), "1366x768":(1366, 768), "1920x1080":(1920, 1080)}
# screen = pygame.display.set_mode((1920, 1080), stateWindow["Full Screen"])
screen = pygame.display.set_mode()
pygame.display.set_caption('Shooter')
clock = pygame.time.Clock()

window = Window(CURRENTRESOLUTION)
window.updateResolution(screen, CURRENTRESOLUTION, False)

#Positions Names
namesMenu = NamesandPositions({'Start':(50, 50), 'Options':(50, 100), '[ Exit ]':(50, 200)})
namesConfig = NamesandPositions({'Screen':(50, 80), 'Resolution:':(50, 130), 'Language:':(50, 180), 'Accept':(50, 230), '[ Back ]':(50, 400)})
namesWindow = NamesandPositions({"< Full Screen >":(150, 80), "< Window >":(0, 0)})
resolutions = (1920, 1080), (1366, 768), (640, 480)
namesResolution = NamesandPositions({"< 1920x1080 >":(150, 130), "< 1366x768 >":(0, 0), "< 640x480 >":(0, 0)})
namesLanguage = NamesandPositions({"< English >":(150, 180), "< Portugues >":(0, 0)})

#Images
backgroundMenu = pygame.image.load("res/backgroundMenu.png")
selectionImage = pygame.image.load("res/selection.png")

controls = Controls()
draw = Draw()

selectionMenu = Selection(namesMenu.showLength())
selectionConfiguration = Selection(namesConfig.showLength())
selectionWindow = Selection(namesWindow.showLength())
selectionResolution = Selection(namesResolution.showLength())
selectionLanguage = Selection(namesLanguage.showLength())


selectionImage = pygame.transform.scale(selectionImage, (80, 25))


def game():
    print("Gamer")
    pass


def configuration():
    runningConfig = True
    selectionConfiguration.resetPositionRect()
    while runningConfig:
        clock.tick(60)
        controls.update()
        runningConfig = not controls.keys["QUIT"]
        # print(namesConfig.showPos(selectionConfiguration.showCont()), selectionConfiguration.showCont(), controls.keys)
        
        if controls.keyStatus("UP"):
            selectionConfiguration.moveSelection(PREVIUS)
            controls.setKey("UP", False)

        elif controls.keyStatus("DOWN"):
            selectionConfiguration.moveSelection(NEXT)
            controls.setKey("DOWN", False)

        elif controls.keyStatus("LEFT") or controls.keyStatus("RIGHT"):
            if selectionConfiguration.showCont() == 0:
                if controls.keyStatus("LEFT"):
                    selectionWindow.moveSelection(PREVIUS)
                    controls.setKey("LEFT", False)
                elif controls.keyStatus("RIGHT"):
                    selectionWindow.moveSelection(NEXT)
                    controls.setKey("RIGHT", False)

            elif selectionConfiguration.showCont() == 1:
                if controls.keyStatus("LEFT"):
                    selectionResolution.moveSelection(PREVIUS)
                    controls.setKey("LEFT", False)
                elif controls.keyStatus("RIGHT"):
                    selectionResolution.moveSelection(NEXT)
                    controls.setKey("RIGHT", False)

            elif selectionConfiguration.showCont() == 2:
                if controls.keyStatus("LEFT"):
                    selectionLanguage.moveSelection(PREVIUS)
                    controls.setKey("LEFT", False)
                elif controls.keyStatus("RIGHT"):
                    selectionLanguage.moveSelection(NEXT)
                    controls.setKey("RIGHT", False)


        if controls.keyStatus("ACTION"):
            if selectionConfiguration.showCont() == 3:
                window.updateResolution(screen, resolutions[selectionResolution.showCont()], not selectionWindow.showCont())

            if  selectionConfiguration.showCont() == 4:
                runningConfig = False
                controls.setKey("ACTION", False)
            

        screen.fill(pygame.Color('black'))
        draw.title(screen, "Configuration", (300, 20))
        draw.multiWords(screen, namesConfig.showDictionary())
        draw.selectionsNames(screen, namesWindow.showNames(), selectionWindow.showCont(), namesWindow.showPos(0))
        draw.selectionsNames(screen, namesResolution.showNames(), selectionResolution.showCont(), namesResolution.showPos(0))
        draw.selectionsNames(screen, namesLanguage.showNames(), selectionLanguage.showCont(), namesLanguage.showPos(0))
        draw.image(screen, selectionImage, (namesConfig.showPos(selectionConfiguration.showCont())[0]-5, namesConfig.showPos(selectionConfiguration.showCont())[1]-5))
        pygame.display.update()


# menu = True


def mainMenu():
    running = True
    while running:
        clock.tick(60)
        controls.update()
        running = not controls.keys["QUIT"]
        # print(namesMenu.showPos(selectionMenu.showCont()), selectionMenu.showCont(), controls.keys)
        if controls.keys["UP"]:
            selectionMenu.moveSelection(PREVIUS)
            controls.keys["UP"] = False

        elif controls.keys["DOWN"]:
            selectionMenu.moveSelection(NEXT)
            controls.keys["DOWN"] = False

        if controls.keys["ACTION"]:
            if selectionMenu.showCont() == 0:
                game()
            
            elif selectionMenu.showCont() == 1:
                configuration()
                selectionMenu.resetPositionRect()
            
            elif selectionMenu.showCont() == 2:
                controls.keys["QUIT"] = True

        # screen.fill(pygame.Color('black')) 
        
        draw.background(screen, backgroundMenu)
        draw.image(screen, selectionImage, (namesMenu.showPos(selectionMenu.showCont())[0]-5, namesMenu.showPos(selectionMenu.showCont())[1]-5))
        draw.multiWords(screen, namesMenu.showDictionary())

        pygame.display.update()


mainMenu()
pygame.quit()
