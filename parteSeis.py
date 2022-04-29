import pygame,sys
from pygame.locals import *


#CARGAR IMAGENES
#Formas de crear color
#Color = (0,140,60) # Tupla RGB Rojo, Verde y azul
ColorDos = pygame.Color(255,120,9)

pygame.init()

ventana = pygame.display.set_mode((700,600))
pygame.display.set_caption('Hola mundo')

Mi_Imagen = pygame.image.load("C:/Users/rober/OneDrive/Documentos/ROBERTO/knocker3.jpeg")
posX,posY = 100,90

ventana.blit(Mi_Imagen,(posX,posY))

while True:

    for evento in pygame.event.get(): #Lista de eventos de pygame
        if evento.type == QUIT:
            pygame.quit
            sys.exit()
    pygame.display.update()
