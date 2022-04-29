import pygame,sys
from pygame.locals import *

#pygame.font.init() otra forma de inicializar fuente    
pygame.init()
#TEXTO
fonts = pygame.font.get_fonts()
#print(len(fonts))
#for f in fonts:
#    print(f)

miFuente = pygame.font.SysFont('elephant', 72)
#miFuente = pygame.font.Font(None,30)
miText = miFuente.render("Prueba fuente",0,(200,60,80)) #texto, ¿antialias?, color

ventana = pygame.display.set_mode((700,600))
pygame.display.set_caption('Texto en Pygame')


while True:


    for evento in pygame.event.get(): #Lista de eventos de pygame
        if evento.type == QUIT:
            pygame.quit
            sys.exit()

    ventana.blit(miText,(100,100))    

    pygame.display.update()
