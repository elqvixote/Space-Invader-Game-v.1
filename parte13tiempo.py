import pygame,sys
from pygame.locals import *

pygame.init()
#TIEMPO
ventana = pygame.display.set_mode((700,600))
pygame.display.set_caption('Texto en Pygame')
fuente = pygame.font.SysFont('Arial',30)
aux = 1
while True:
    ventana.fill((255,255,255))
    tiempo = pygame.time.get_ticks()//1000 #da el tiempo en milisegundos desde que
#    print(tiempo)                                       #inició init tiempo/1000 para convertir a segundos
    
    if aux == tiempo:
        aux+=1
        print(tiempo)
    for evento in pygame.event.get(): #Lista de eventos de pygame
        if evento.type == QUIT:
            pygame.quit
            sys.exit()

    contador = fuente.render('tiempo: '+str(tiempo),0,(120,70,0))
    ventana.blit(contador,(100,100))
    pygame.display.update()
