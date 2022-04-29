import pygame,sys
from pygame.locals import *


#Formas de crear color
#Color = (0,140,60) # Tupla RGB Rojo, Verde y azul
ColorDos = pygame.Color(255,120,9)

pygame.init()

ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hola mundo')

#Dibujamos un circulo (lienzo,color, ubicacion en X y Y,radio)
pygame.draw.circle(ventana,(80,70,120),(89,90),20)


#dibujamos un rectangulo
pygame.draw.rect(ventana,(140,90,90),(0,0,200,50))  #0,0 es la esquina superior izquierda

ColorTres = pygame.Color(70,80,150)
#Dibuja linea
pygame.draw.line(ventana,ColorTres,(60,80),(160,100),8)#(x,y)inicial y final
while True:
#    ventana.fill(ColorDos) #Color del lienzo
    for evento in pygame.event.get(): #Lista de eventos de pygame
        if evento.type == QUIT:
            pygame.quit
            sys.exit()
    pygame.display.update()
