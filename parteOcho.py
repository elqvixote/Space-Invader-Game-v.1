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

Mi_Imagen = pygame.image.load("./ovni.png")

posX = 200
posY = 100
Blanco = (255,255,255)
ventana.blit(Mi_Imagen,(posX,posY))
velocidad = 5 #velocidad 5 pixeles
derecha = True
while True:
    ventana.fill(Blanco)
    ventana.blit(Mi_Imagen,(posX,posY))
    for evento in pygame.event.get(): #Lista de eventos de pygame
        if evento.type == QUIT:
            pygame.quit
            sys.exit()
    
    if derecha == True:
        if posX < 500:
            posX+=velocidad
        else:
            derecha = False
    else:
        if posX>1:
            posX-=velocidad
        else:
            derecha = True

    pygame.display.update()
