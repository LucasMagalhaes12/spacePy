
from controls import Controls
from draw import Draw
from selections import Selections
from names import Names
from window import Window
from rocket import Rocket
from bullets import Bullets
from enemys import Enemys
from particles import Particles
from collision import collision
from powerUps import PowerUps

import pygame
from random import randint
"""
> Documentar cada função
> criar sprites de outros inimigos
> adicionar animação de fogo
> Criar arquivo de configuração
"""

pygame.init()
screen = pygame.display.set_mode()
pygame.display.set_caption('Shooter')
clock = pygame.time.Clock()

window = Window(screen, 1)
names = Names("PTBR")


#Images
backgroundMenu = pygame.image.load("res/backgroundMenu.png")
backgroundMenu = pygame.transform.scale(backgroundMenu, window.resolution())

rocket = Rocket()
enemys = Enemys()
bullets = Bullets()
selections = Selections((100, 25))
controls = Controls()
draw = Draw()
powerUps = PowerUps()
particles = Particles()

def game():
    particles.splash(window.resolution())
    runningGame = True
    while runningGame:
        clock.tick(60)
        controls.update()
        runningGame = not controls._keys["QUIT"]

        bullets.new(rocket.position(incrementY=35), rocket.position(40, 20), rocket.position(80, 35))
        enemys.new(window.resolution())
        particles.new(window.resolution())
        
        rocket.update(controls.keyStatus("ALL")[:4], window.resolution())   
        bullets.update()
        enemys.update(window.resolution())
        particles.update(window.resolution())
        powerUps.update(window.resolution())
        

        for enemyIndex, enemyPos in enumerate(enemys.positions()):
            for bulletIndex, bulletPos in enumerate(bullets.positions()):
                if collision(enemyPos, enemys.size(), bulletPos, bullets.size()): 
                    enemys.pop(enemyIndex)
                    bullets.pop(bulletIndex)


        for powerupIndex, powerupsPos in enumerate(powerUps.positions()):
            if collision(powerupsPos, powerUps.size(), rocket.position(), rocket.size()):
                bullets.set(powerupsPos[2])
                powerUps.pop(powerupIndex)
            

        screen.fill(pygame.Color('black'))
        
        for bulletPos in bullets.positions():
            draw.image(screen, bullets.skin(), bulletPos)
            # draw.name(screen, draw.FONTOPTIONS, (str(bulletPos), bulletPos), 10, 5)

        for enemyPos in enemys.positions():
            draw.image(screen, enemys.skin()[0], enemyPos)
            # draw.name(screen, draw.FONTOPTIONS, (str(enemyPos), enemyPos), 15, -10)

        for particlesPos in particles.positions():
            draw.image(screen, particles.skin(), particlesPos)

        for powerupsPos in powerUps.positions():
            draw.image(screen, powerUps.skin(powerupsPos[2]), powerupsPos)

        draw.image(screen, rocket.skin()[0], rocket.position())

        # draw.name(screen, draw.FONTOPTIONS, ("enemys: "+ str(len(enemys.positions())), (200, 10)))
        # draw.name(screen, draw.FONTOPTIONS, ("bullets: " + str(len(bullets.positions())), (400, 10)))
        # draw.name(screen, draw.FONTOPTIONS, (str(int(clock.get_fps())), (10, 10)))

        pygame.display.update()


def configuration():
    runningConfig = True
    selections.resetPos("configuration")
    while runningConfig:
        clock.tick(60)

        # Draw Configuration
        # print(selections.pos("configuration"), selections.pos("configuration"), controls._keys)
              
        screen.fill(pygame.Color('black'))
        draw.name(screen, draw.FONTTITLE, ("Configuration", (300, 20)))
        draw.multiNames(screen, names.items("config"))
        
        draw.name(screen, draw.FONTOPTIONS, names.items("window")[selections.pos("window")])
        draw.name(screen, draw.FONTOPTIONS, names.items("resolutions")[selections.pos("resolutions")])
        draw.name(screen, draw.FONTOPTIONS, names.items("langSelection")[selections.pos("lang")])
        draw.image(screen, selections.skin(), (names.positions("config")[selections.pos("configuration")][0]-5, names.positions("config")[selections.pos("configuration")][1]-5))
        pygame.display.update()

        # Controls
        controls.update()
        runningConfig = not controls._keys["QUIT"]
        ## TODO Melhorar esses inputs 
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
                    selections.moveSelection("lang", selections.PREVIUS)
                    controls.setKey("LEFT", False)

                elif controls.keyStatus("RIGHT"):
                    selections.moveSelection("lang", selections.NEXT)
                    controls.setKey("RIGHT", False)


        if controls.keyStatus("ACTION"):
            if selections.pos("configuration") == 3:
                window.updateResolution(screen, selections.pos("resolutions"), not selections.pos("window"))
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
        # print(names.names("menu")[selections.pos("menu")], selections.pos("menu"), controls.keys)

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
            ## TODO Definir o que significa o "0".
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
