from controls import Controls
from draw import Draw
from selections import Selections
from names import Names
from window import Window
from rocket import Rocket
from laser import Laser
from enemys import Enemys
from particles import Particles
from collision import collision
from powerUps import PowerUps
from lifes import Lifes

import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode()
pygame.display.set_caption('Shooter')
clock = pygame.time.Clock()

window = Window(screen, 1)
names = Names("PTBR")

backgroundMenu = pygame.image.load("res/backgroundMenu.png")
backgroundMenu = pygame.transform.scale(backgroundMenu, window.get_resolution())

rocket = Rocket(window.get_resolution())
enemys = Enemys()
lasers = Laser()
selections = Selections()
controls = Controls()
draw = Draw()
powerUps = PowerUps(window.get_resolution())
particles = Particles(window.get_resolution())
lifes = Lifes(window.get_resolution())


def game():
    particles.splash(window.get_resolution())
    runningGame = True
    while runningGame:
        clock.tick(60)
        controls.update()
        runningGame = not controls.keyStatus()["QUIT"]

        lasers.update(rocket.get_position(incrementX=6, incrementY=35), rocket.get_position(45, 20), rocket.get_position(85, 35))
        enemys.update(window.get_resolution())
        particles.update()
        rocket.update(controls.keyStatus())
        powerUps.update()
        lifes.update()
        
        for enemyIndex, enemyPos in enumerate(enemys.positions()):
            for bulletIndex, bulletPos in enumerate(lasers.get_positions()):
                if collision(enemyPos, enemys.size(), bulletPos, lasers.get_size()): 
                    enemys.pop(enemyIndex)
                    lasers.pop(bulletIndex)
            if collision(enemyPos, enemys.size(), rocket.get_position(), rocket.get_size()):
                enemys.pop(enemyIndex)
                lifes.set_nlifes(lifes.LOSELIFE)


        for powerupIndex, powerupsPos in enumerate(powerUps.get_positions()):
            if collision(powerupsPos, powerUps.get_size(), rocket.get_position(), rocket.get_size()):
                lasers.set_laser(powerupsPos[2])
                powerUps.take(powerupIndex)
        

        for lifesIndex, lifesPos in enumerate(lifes.get_positions()):
            if collision(lifesPos, lifes.get_size(), rocket.get_position(), rocket.get_size()):
                lifes.pop(lifesIndex)
                lifes.set_nlifes(lifes.WINLIFE)


        screen.fill(pygame.Color('black'))
        draw.name(screen, draw.FONTTITLE, names.items("game")[0])
        draw.name(screen, draw.FONTTITLE, (str(lifes.get_nlifes()), names.items("game")[0][1]), 70)
        

        for bulletPos in lasers.get_positions():
            draw.image(screen, lasers.get_skin(), bulletPos)      

        for enemyPos in enemys.positions():
            draw.image(screen, enemys.get_skin(), enemyPos)
            
        for particlesPos in particles.get_positions():
            draw.image(screen, particles.get_skin(), particlesPos)

        for powerupsPos in powerUps.get_positions():
            draw.image(screen, powerUps.get_skin(powerupsPos[2]), powerupsPos)

        for lifesPos in lifes.get_positions():
            draw.image(screen, lifes.get_skin(), lifesPos)

        draw.image(screen, rocket.get_skin(), rocket.get_position())

        if powerUps.isWithPowerUP():
            rect = (20, window.get_resolution()[1] - 40, 150, 20)
            porcent = (rect[2] - rect[0]) * powerUps.duration() // powerUps._LIMITDURATION
            draw.bar(screen, rect, porcent)
        else:
            lasers.set_laser(lasers.NORMAL)

        pygame.display.update()


def configuration():
    runningConfig = True
    selections.resetPos("configuration")
    while runningConfig:
        clock.tick(60)
              
        screen.fill(pygame.Color('black'))
        draw.name(screen, draw.FONTTITLE, ("Configuration", (300, 20)))
        draw.multiNames(screen, names.items("config"))
        
        draw.name(screen, draw.FONTOPTIONS, names.items("window")[selections.get_pos("window")])
        draw.name(screen, draw.FONTOPTIONS, names.items("resolutions")[selections.get_pos("resolutions")])
        draw.name(screen, draw.FONTOPTIONS, names.items("langSelection")[selections.get_pos("language")])
        draw.image(screen, selections.get_skin(), (names.positions("config")[selections.get_pos("configuration")][0]-5, names.positions("config")[selections.get_pos("configuration")][1]-5))
        pygame.display.update()

        controls.update()
        runningConfig = not controls._keys["QUIT"]

        if controls.keyStatus("UP"):
            selections.moveSelection("configuration", selections.PREVIUS)
            controls.setKey("UP", False)

        elif controls.keyStatus("DOWN"):
            selections.moveSelection("configuration", selections.NEXT)
            controls.setKey("DOWN", False)

        elif controls.keyStatus("LEFT") or controls.keyStatus("RIGHT"):
            if selections.get_pos("configuration") == 0:
                if controls.keyStatus("LEFT"):
                    selections.moveSelection("window", selections.PREVIUS)
                    controls.setKey("LEFT", False)
                elif controls.keyStatus("RIGHT"):
                    selections.moveSelection("window", selections.NEXT)
                    controls.setKey("RIGHT", False)

            elif selections.get_pos("configuration") == 1:
                if controls.keyStatus("LEFT"):
                    selections.moveSelection("resolutions", selections.PREVIUS)
                    controls.setKey("LEFT", False)
                elif controls.keyStatus("RIGHT"):
                    selections.moveSelection("resolutions", selections.NEXT)
                    controls.setKey("RIGHT", False)

            elif selections.get_pos("configuration") == 2:
                if controls.keyStatus("LEFT"):
                    selections.moveSelection("language", selections.PREVIUS)
                    controls.setKey("LEFT", False)

                elif controls.keyStatus("RIGHT"):
                    selections.moveSelection("language", selections.NEXT)
                    controls.setKey("RIGHT", False)


        if controls.keyStatus("ACTION"):
            if selections.get_pos("configuration") == 3:
                window.updateResolution(screen, selections.get_pos("resolutions"), not selections.get_pos("window"))
                rocket.set_screenSize(window.get_resolution())
                if selections.get_pos("language") == 0:
                    names.set("EN")
                if selections.get_pos("language") == 1:
                    names.set("PTBR")
                global backgroundMenu
                backgroundMenu = pygame.transform.scale(backgroundMenu, window.get_resolution())

            if  selections.get_pos("configuration") == 4:
                runningConfig = False
                controls.setKey("ACTION", False)
            

def mainMenu():
    running = True
    while running:
        clock.tick(60)
        controls.update()
        running = not controls._keys["QUIT"]

        draw.image(screen, backgroundMenu, (0, 0))
        draw.image(screen, selections.get_skin(), (names.positions("menu")[selections.get_pos("menu")][0]-5, names.positions("menu")[selections.get_pos("menu")][1]-5))
        draw.multiNames(screen, names.items("menu"))
        
        if controls._keys["UP"]:
            selections.moveSelection("menu", selections.PREVIUS)
            controls._keys["UP"] = False

        elif controls._keys["DOWN"]:
            selections.moveSelection("menu", selections.NEXT)
            controls._keys["DOWN"] = False

        if controls._keys["ACTION"]:
            if selections.get_pos("menu") == 0:
                game()
                selections.resetPos("menu")
            
            elif selections.get_pos("menu") == 1:
                configuration()
                selections.resetPos("menu")
            
            elif selections.get_pos("menu") == 2:
                controls._keys["QUIT"] = True

        pygame.display.update()


mainMenu()
pygame.quit()
