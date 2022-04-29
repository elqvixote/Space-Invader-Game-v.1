import pygame,sys
from pygame.locals import *
from random import randint
#Variables Globales
ancho = 900
alto = 480
listaEnemigo = []

class naveEspacial(pygame.sprite.Sprite):
    '''Clase para las naves'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenNave = pygame.image.load('recursos/nave.jpg')

        self.rect = self.ImagenNave.get_rect()
        self.rect.centerx = ancho/2
        self.rect.centery = alto -30

        self.listaDisparo = []
        self.Vida = True
        self.Vida = True
        self.velocidad = 4

        self.sonidoDisparo = pygame.mixer.Sound('recursos/shoot.wav')

    def movimientoDerecha(self):
        self.rect.right += self.velocidad
        self.movimiento

    def movimientoIzquierda(self):
        self.rect.right -= self.velocidad
        self.movimiento

    def movimiento(self):
        if self.Vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > 900:
                self.rect.right = 890

    def dispara(self,x,y):
        miProyectil = Proyectil(x,y,'recursos/disparoa.jpg',True)
        self.listaDisparo.append(miProyectil)    
        self.sonidoDisparo.play()


    def dibujar(self,superficie):
        superficie.blit(self.ImagenNave, self.rect)

class Proyectil(pygame.sprite.Sprite):
    def __init__(self,posx,posy,ruta,personaje) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.imageProyectil = pygame.image.load(ruta)

        self.rect = self.imageProyectil.get_rect()
        self.velocidadDisparo = 2

        self.rect.top = posy
        self.rect.left = posx

        self.disparoPersonaje = personaje

    def trayectoria(self):
        if self.disparoPersonaje == True:
            self.rect.top = self.rect.top - self.velocidadDisparo
        else:
            self.rect.top = self.rect.top + self.velocidadDisparo

    def dibujar(self,superficie):
        superficie.blit(self.imageProyectil, self.rect)

class Invasor(pygame.sprite.Sprite):
    def __init__(self,posx,posy) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.imagenA = pygame.image.load('recursos/MarcianoA.jpg')
        self.imagenB = pygame.image.load('recursos/MarcianoB.jpg')
        
        self.listaImagenes = [self.imagenA,self.imagenB]
        self.posImagen = 0

        self.imagenInvasor = self.listaImagenes[self.posImagen]
        self.rect = self.imagenInvasor.get_rect()
        
        
        self.listaDisparo = []
        self.velocidad = 3
        self.rect.top = posy
        self.rect.left = posx

        self.rangoDisparo = 5
        self.tiempoCambio = 3

        self.derecha = True
        self.contador = 0
        self.Maxdescenso = self.rect.top +40

#        self.limiteDerecha = posx+ distancia
#        self.limiteIzquierda = posx- distancia        


    def dibujar(self,superficie):
        self.imagenInvasor = self.listaImagenes[self.posImagen]
        superficie.blit(self.imagenInvasor, self.rect)

    def comportamiento(self, tiempo):
        self.__movimientos()
        
        self.__ataque()
        if self.tiempoCambio == tiempo:
            self.posImagen +=1
            self.tiempoCambio +=1

            if self.posImagen > len(self.listaImagenes)-1:
                self.posImagen = 0

    def __ataque(self):
        if (randint(0,100)<self.rangoDisparo):
            self.__disparo()

    def __movimientos(self):
        if self.contador <3:
            self.__movimientoLateral()
        else:
            self.__descenso()

    def __descenso(self):
        if self.Maxdescenso==self.rect.top:
            self.contador = 0
            self.Maxdescenso = self.rect.top+40
        else:
            self.rect.top+=1

    def __movimientoLateral(self):
        if self.derecha == True:
            self.rect.left = self.rect.left + self.velocidad
            if self.rect.left > 500: #self.limiteDerecha:
                self.derecha = False
                self.contador +=1
        else:
            self.rect.left = self.rect.left - self.velocidad
            if self.rect.left < 0: #self.limiteIzquierda:
                self.derecha = True 


    def __disparo(self):
        x,y = self.rect.center
        miProyectil = Proyectil(x,y,'recursos/disparob.jpg',False)
        self.listaDisparo.append(miProyectil)

#def cargarEnemigos():
#    enemigo = Invasor(100,100,400,'recursos/MarcianoA.jpg','recursos/MarcianoB.jpg')
#    listaEnemigo.append(enemigo)

def SpaceInvader():
    pygame.init()
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption('Space Invader')

    ImagenFondo = pygame.image.load('recursos/Fondo.jpg')

    jugador = naveEspacial()
#    cargarEnemigos()
    enemigo = Invasor(100,100)
    enJuego = True
    reloj = pygame.time.Clock()
    while True:
        reloj.tick(60) #Regula los frames por segundo
 
        tiempo = pygame.time.get_ticks()//1000

        for evento in pygame.event.get(): #Lista de eventos de pygame
            if evento.type == QUIT:
                pygame.quit
                sys.exit()
        if enJuego == True:
            if evento.type == pygame.KEYDOWN:
                if evento.key == K_LEFT:
                    jugador.movimientoIzquierda()

                elif evento.key == K_RIGHT:
                    jugador.movimientoDerecha()

                elif evento.key == K_UP:
                    x,y = jugador.rect.center
                    jugador.dispara(x,y)

        ventana.blit(ImagenFondo,(0,0))
 
        enemigo.comportamiento(tiempo)
        jugador.dibujar(ventana)
        enemigo.dibujar(ventana)
#        cargarEnemigos()

        if len(jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()

                if x.rect.top <- 10:
                    jugador.listaDisparo.remove(x)       
#        if len(listaEnemigo)>0:
#            for enemigo in listaEnemigo:
#                enemigo.comportamiento(tiempo)
#                enemigo.dibujar(ventana)

            if len(enemigo.listaDisparo)>0:
                for x in enemigo.listaDisparo:
                    x.dibujar(ventana)
                    x.trayectoria()

                    if x.rect.top > 900:
                        enemigo.listaDisparo.remove(x)
     
     
      
        pygame.display.update()

SpaceInvader()