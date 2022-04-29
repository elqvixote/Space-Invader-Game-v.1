import pygame,sys
from pygame.locals import *
#Variables Globales
ancho = 900
alto = 480

class naveEspacial(pygame.sprite.Sprite):
    '''Clase para las naves'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenNave = pygame.image.load('imagenes_pygame-master/nave.jpg')

        self.rect = self.ImagenNave.get_rect()
        self.rect.centerx = ancho/2
        self.rect.centery = alto -30

        self.listaDisparo = []
        self.Vida = True
        self.velocidad = 1

    def movimiento(self):
        if self.Vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > 900:
                self.rect.right = 890

    def dispara(self,x,y):
        miProyectil = Proyectil(x,y)
        self.listaDisparo.append(miProyectil)    

    def dibujar(self,superficie):
        superficie.blit(self.ImagenNave, self.rect)

class Proyectil(pygame.sprite.Sprite):
    def __init__(self,posx,posy) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.imageProyectil = pygame.image.load('imagenes_pygame-master/disparoa.jpg')

        self.rect = self.imageProyectil.get_rect()
        self.velocidadDisparo = 2

        self.rect.top = posy
        self.rect.left = posx
    def trayectoria(self):
        self.rect.top = self.rect.top - self.velocidadDisparo

    def dibujar(self,superficie):
        superficie.blit(self.imageProyectil, self.rect)

def SpaceInvader():
    pygame.init()
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption('Space Invader')

    ImagenFondo = pygame.image.load('imagenes_pygame-master/Fondo.jpg')

    jugador = naveEspacial()

    DemoProyectil = Proyectil(ancho/2,alto-30)

    enJuego = True
    
    while True:
        jugador.movimiento()
        DemoProyectil.trayectoria()
        for evento in pygame.event.get(): #Lista de eventos de pygame
            if evento.type == QUIT:
                pygame.quit
                sys.exit()
        if enJuego == True:
            if evento.type == pygame.KEYDOWN:
                if evento.key == K_LEFT:
                    jugador.rect.left -= jugador.velocidad

                elif evento.key == K_RIGHT:
                    jugador.rect.right += jugador.velocidad

                elif evento.key == K_UP:
                    x,y = jugador.rect.center
                    jugador.dispara(x,y)

        ventana.blit(ImagenFondo,(0,0))
        DemoProyectil.dibujar(ventana)
        jugador.dibujar(ventana) 
        
        if len(jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()

                if x.rect.top < 100:
                    jugador.listaDisparo.remove(x)       
        pygame.display.update()

SpaceInvader()