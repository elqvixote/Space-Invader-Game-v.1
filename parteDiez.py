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
        elif evento.type == pygame.KEYDOWN:
            if evento.key == K_LEFT:
                posX-=velocidad
            elif evento.key == K_RIGHT:
                posX+=velocidad
        elif evento.type == pygame.KEYUP:
            if evento.type == K_LEFT:
                print('Tecla izquierda liberada')
            elif evento.type == K_RIGHT:
                print('Tecla derecha liberada')    
    #Para uso del mouse. Indica la posición del cursor
    posX,posY = pygame.mouse.get_pos()
    #Para centrar el mouse en la imagen
    posX = posX - 250
    posY = posY - 130

    pygame.display.update()
