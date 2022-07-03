import pygame
from sys import exit
from pygame.locals import *

def animar_rampa(animacao):
    pygame.init()

    # informações da tela
    SCREEN_SIZE = (320, 320)
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    black = (0,0,0)

    # informações da bola
    bola = pygame.Surface((10, 10))
    bola.fill((255, 0, 0))

    # loop da animação
    for pos in animacao:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()

        pygame.time.wait(500)
        screen.fill(black)
        screen.blit(bola, (pos[0], pos[1]))

        pygame.display.update()