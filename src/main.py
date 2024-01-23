
from controls import Controls
from draw import Draw
from selection import Selection
# from namesAndPositions import NamesAndPositions

import pygame
from random import randint

pygame.init()

# currentScreenResolution = pygame.display.Info().current_w, pygame.display.Info().current_h
currentResolution = "1920x1080"
#criar arquivo de configuração
resolutions = {"640x480":(640, 480), "1366x768":(1366, 768), "1920x1080":(1920, 1080)}
stateWindow = {"Window":False, "Full Screen":pygame.FULLSCREEN}
screen = pygame.display.set_mode(resolutions["640x480"], stateWindow["Window"])
pygame.display.set_caption('Shooter')
clock = pygame.time.Clock()





#Positions Names
namesPositionsMenu = {'Start':(50, 50), 'Options':(50, 100), 'Exit':(50, 200)}
namesPositionsConfiguration = {'Resolution':(50, 50), 'Language':(50, 100), 'Back':(50, 200)}
namesPositionsConfigurarionResolution = {}

#Images
backgroundMenu = pygame.image.load("res/backgroundMenu.png")
selectionImage = pygame.image.load("res/selection.png")

controls = Controls()
draw = Draw()

selectionMenu = Selection()
selectionMenu.updatePositions(tuple(namesPositionsMenu.values()))

selectionConfiguration = Selection()
selectionConfiguration.updatePositions(tuple(namesPositionsConfiguration.values()))

selectionImage = pygame.transform.scale(selectionImage, (80, 25))

# if currentScreenResolution != (1920, 1080):
#     print("transform")
    # backgroundMenu = pygame.transform.scale(backgroundMenu, currentScreenResolution)

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
        print(selectionConfiguration.showCurrentPosition(), selectionConfiguration.showContPosition(), controls.keys)
        
        if controls.keyStatus("UP"):
            selectionConfiguration.moveSelection(-1)
            controls.setKey("UP", False)

        elif controls.keyStatus("DOWN"):
            selectionConfiguration.moveSelection(1)
            controls.setKey("DOWN", False)

        
        if controls.keyStatus("RIGHT"):
            pass

        elif controls.keyStatus("LEFT"):
            pass

        if controls.keyStatus("ACTION"):
            if  selectionConfiguration.showContPosition() == 2:
                runningConfig = False
                controls.setKey("ACTION", False)
            

        screen.fill(pygame.Color('black'))
        # draw.backgroundMenu(screen)
        draw.singleWord(screen, "Configuration", (resolutions[currentResolution][0]/2-60, 20))
        # draw.singleWord(screen, )
        draw.multiWords(screen, namesPositionsConfiguration)
        draw.image(screen, selectionImage, (selectionConfiguration.showCurrentPosition()[0]-5, selectionConfiguration.showCurrentPosition()[1]-5))
        pygame.display.update()


menu = True


def mainMenu():
    running = True
    while running:
        clock.tick(60)
        controls.update()
        running = not controls.keys["QUIT"]
        
        print(selectionMenu.showCurrentPosition(), selectionMenu.showContPosition(), controls.keys)
        if controls.keys["UP"]:
            selectionMenu.moveSelection(-1)
            controls.keys["UP"] = False

        elif controls.keys["DOWN"]:
            selectionMenu.moveSelection(1)
            controls.keys["DOWN"] = False

        if controls.keys["ACTION"]:
            if selectionMenu.showContPosition() == 0:
                game()
            
            elif selectionMenu.showContPosition() == 1:
                configuration()
                selectionMenu.resetPositionRect()
            
            elif selectionMenu.showContPosition() == 2:
                controls.keys["QUIT"] = True

        # screen.fill(pygame.Color('black')) 
        
        draw.background(screen, backgroundMenu)
        draw.multiWords(screen, namesPositionsMenu)
        print(selectionMenu.showCurrentPosition(), selectionMenu.showContPosition())
        draw.image(screen, selectionImage, (selectionMenu.showCurrentPosition()[0]-5, selectionMenu.showCurrentPosition()[1]-5))

        pygame.display.update()


mainMenu()
pygame.quit()
