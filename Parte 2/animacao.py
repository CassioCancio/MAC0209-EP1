import pygame
import math
from sys import exit
from pygame.locals import *

def animar_rampa(animacao, radianos):
    pygame.init()

    graus = radianos / (math.pi/180)

    # informações da tela
    SCREEN_SIZE = (720, 540)
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    black = (0,0,0)

    # informações triangulo
    rampa = pygame.image.load('rampa.png')
    rampa = pygame.transform.scale(rampa, (1001, 423.2))

    # informações da bloco
    bloco = pygame.image.load('bloco.png')
    bloco = pygame.transform.scale(bloco, (68.1, 49.9))

    # loop da animação
    indice = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or indice >= len(animacao): 
                pygame.quit()
                sys.exit()

        pygame.time.wait(50)
        screen.fill(black)
        screen.blit(rampa, (0, 27))
        screen.blit(bloco, (animacao[indice][0]*100, animacao[indice][1]*100))
        pygame.display.update()
        indice += 1