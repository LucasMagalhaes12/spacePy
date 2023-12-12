import pygame
from random import randint

pygame.init()

print()

currentScreenResolution = pygame.display.Info().current_w, pygame.display.Info().current_h
#criar arquivo de configuração
screen = pygame.display.set_mode(currentScreenResolution)
pygame.display.set_caption('Shooter')

clock = pygame.time.Clock()

running = True


def controls():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


def game():
    while running:
        clock.tick(60)
        screen.fill(pygame.Color('black'))
        controls()
        pygame.display.update()

game()
pygame.quit()