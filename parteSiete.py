import pygame,sys
from pygame.locals import *
from random import randint

#CARGAR IMAGENES
#Formas de crear color
#Color = (0,140,60) # Tupla RGB Rojo, Verde y azul
ColorDos = pygame.Color(255,120,9)

pygame.init()

ventana = pygame.display.set_mode((700,600))
pygame.display.set_caption('Hola mundo')

Mi_Imagen = pygame.image.load("C:/Users/rober/OneDrive/Documentos/ROBERTO/knocker3.jpeg")

posX = 200
posY = 100

ventana.blit(Mi_Imagen,(posX,posY))
velocidad = 5 #velocidad 5 pixeles
while True:
    ventana.blit(Mi_Imagen,(posX,posY))
    for evento in pygame.event.get(): #Lista de eventos de pygame
        if evento.type == QUIT:
            pygame.quit
            sys.exit()
    if posX < 500:
        posX+=velocidad
    else:
        posX-=velocidad

    pygame.display.update()
