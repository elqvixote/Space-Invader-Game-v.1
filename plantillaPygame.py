import pygame,sys
from pygame.locals import *

pygame.init()
#TIEMPO
ventana = pygame.display.set_mode((400,400))
pygame.display.set_caption('Space Invader')


while True:

    for evento in pygame.event.get(): #Lista de eventos de pygame
        if evento.type == QUIT:
            pygame.quit
            sys.exit()

    pygame.display.update()
