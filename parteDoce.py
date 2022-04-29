import pygame,sys
from pygame.locals import *
from random import randint
#COLISIONES POR MEDIO DE RECTÁNGULOS
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

velocidad = 1 #velocidad 5 pixeles
derecha = True
rectangulo = pygame.Rect(0,0,100,50)
rectangulo_dos = pygame.Rect(200,200,100,50)
while True:
    ventana.fill(Blanco)
    
    pygame.draw.rect(ventana,(100,70,70),rectangulo)
    pygame.draw.rect(ventana,(100,70,70),rectangulo_dos)
    rectangulo.left, rectangulo.top = pygame.mouse.get_pos()

    if rectangulo.colliderect(rectangulo_dos):
        velocidad = 0

    for evento in pygame.event.get(): #Lista de eventos de pygame
        if evento.type == QUIT:
            pygame.quit
            sys.exit()
    if derecha == True:
        if posX < 500:
            posX+=velocidad
            rectangulo_dos.left = posX
        else:
            derecha = False
    else:
        if posX>1:
            posX-=velocidad
            rectangulo_dos.left = posX
        else:
            derecha = True
    

    pygame.display.update()
