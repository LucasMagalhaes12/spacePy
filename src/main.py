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
backgroundMenu = pygame.transform.scale(backgroundMenu, window.resolution())

rocket = Rocket(window.resolution())
enemys = Enemys()
lasers = Laser()
selections = Selections()
controls = Controls()
draw = Draw()
powerUps = PowerUps()
particles = Particles()
lifes = Lifes()


def game():
    particles.splash(window.resolution())
    runningGame = True
    while runningGame:
        clock.tick(60)
        controls.update()
        runningGame = not controls.keyStatus()["QUIT"]

        lasers.update(rocket.position(incrementX=6, incrementY=35), rocket.position(45, 20), rocket.position(85, 35))
        enemys.update(window.resolution())
        particles.update(window.resolution())
        rocket.update(controls.keyStatus(), window.resolution())
        powerUps.update(window.resolution())
        lifes.update(window.resolution())
        
        for enemyIndex, enemyPos in enumerate(enemys.positions()):
            for bulletIndex, bulletPos in enumerate(lasers.positions()):
                if collision(enemyPos, enemys.size(), bulletPos, lasers.size()): 
                    enemys.pop(enemyIndex)
                    lasers.pop(bulletIndex)
            if collision(enemyPos, enemys.size(), rocket.position(), rocket.size()):
                enemys.pop(enemyIndex)
                lifes.set(lifes.LOSELIFE)


        for powerupIndex, powerupsPos in enumerate(powerUps.positions()):
            if collision(powerupsPos, powerUps.size(), rocket.position(), rocket.size()):
                lasers.set(powerupsPos[2])
                powerUps.take(powerupIndex)
        

        for lifesIndex, lifesPos in enumerate(lifes.positions()):
            if collision(lifesPos, lifes.size(), rocket.position(), rocket.size()):
                lifes.pop(lifesIndex)
                lifes.set(lifes.WINLIFE)


        screen.fill(pygame.Color('black'))
        draw.name(screen, draw.FONTTITLE, names.items("game")[0])
        draw.name(screen, draw.FONTTITLE, (str(lifes.lifes()), names.items("game")[0][1]), 70)
        

        for bulletPos in lasers.positions():
            draw.image(screen, lasers.skin(), bulletPos)      

        for enemyPos in enemys.positions():
            draw.image(screen, enemys.skin(), enemyPos)
            
        for particlesPos in particles.positions():
            draw.image(screen, particles.skin(), particlesPos)

        for powerupsPos in powerUps.positions():
            draw.image(screen, powerUps.skin(powerupsPos[2]), powerupsPos)

        for lifesPos in lifes.positions():
            draw.image(screen, lifes.skin(), lifesPos)

        draw.image(screen, rocket.skin(), rocket.position())

        if powerUps.isWithPowerUP():
            rect = (20, window.resolution()[1] - 40, 150, 20)
            porcent = (rect[2] - rect[0]) * powerUps.duration() // powerUps.LIMITDURATION
            draw.bar(screen, rect, porcent)
        else:
            lasers.set(lasers.NORMAL)

        pygame.display.update()


def configuration():
    runningConfig = True
    selections.resetPos("configuration")
    while runningConfig:
        clock.tick(60)
              
        screen.fill(pygame.Color('black'))
        draw.name(screen, draw.FONTTITLE, ("Configuration", (300, 20)))
        draw.multiNames(screen, names.items("config"))
        
        draw.name(screen, draw.FONTOPTIONS, names.items("window")[selections.pos("window")])
        draw.name(screen, draw.FONTOPTIONS, names.items("resolutions")[selections.pos("resolutions")])
        draw.name(screen, draw.FONTOPTIONS, names.items("langSelection")[selections.pos("language")])
        draw.image(screen, selections.skin(), (names.positions("config")[selections.pos("configuration")][0]-5, names.positions("config")[selections.pos("configuration")][1]-5))
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
            if selections.pos("configuration") == 0:
                if controls.keyStatus("LEFT"):
                    selections.moveSelection("window", selections.PREVIUS)
                    controls.setKey("LEFT", False)
                elif controls.keyStatus("RIGHT"):
                    selections.moveSelection("window", selections.NEXT)
                    controls.setKey("RIGHT", False)

            elif selections.pos("configuration") == 1:
                if controls.keyStatus("LEFT"):
                    selections.moveSelection("resolutions", selections.PREVIUS)
                    controls.setKey("LEFT", False)
                elif controls.keyStatus("RIGHT"):
                    selections.moveSelection("resolutions", selections.NEXT)
                    controls.setKey("RIGHT", False)

            elif selections.pos("configuration") == 2:
                if controls.keyStatus("LEFT"):
                    selections.moveSelection("language", selections.PREVIUS)
                    controls.setKey("LEFT", False)

                elif controls.keyStatus("RIGHT"):
                    selections.moveSelection("language", selections.NEXT)
                    controls.setKey("RIGHT", False)


        if controls.keyStatus("ACTION"):
            if selections.pos("configuration") == 3:
                window.updateResolution(screen, selections.pos("resolutions"), not selections.pos("window"))
                rocket.updateScreenSize(window.resolution())
                if selections.pos("language") == 0:
                    names.set("EN")
                if selections.pos("language") == 1:
                    names.set("PTBR")
                global backgroundMenu
                backgroundMenu = pygame.transform.scale(backgroundMenu, window.resolution())

            if  selections.pos("configuration") == 4:
                runningConfig = False
                controls.setKey("ACTION", False)
            

def mainMenu():
    running = True
    while running:
        clock.tick(60)
        controls.update()
        running = not controls._keys["QUIT"]

        draw.image(screen, backgroundMenu, (0, 0))
        draw.image(screen, selections.skin(), (names.positions("menu")[selections.pos("menu")][0]-5, names.positions("menu")[selections.pos("menu")][1]-5))
        draw.multiNames(screen, names.items("menu"))
        
        if controls._keys["UP"]:
            selections.moveSelection("menu", selections.PREVIUS)
            controls._keys["UP"] = False

        elif controls._keys["DOWN"]:
            selections.moveSelection("menu", selections.NEXT)
            controls._keys["DOWN"] = False

        if controls._keys["ACTION"]:
            if selections.pos("menu") == 0:
                game()
                selections.resetPos("menu")
            
            elif selections.pos("menu") == 1:
                configuration()
                selections.resetPos("menu")
            
            elif selections.pos("menu") == 2:
                controls._keys["QUIT"] = True

        pygame.display.update()


mainMenu()
pygame.quit()
