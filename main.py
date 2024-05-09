import pygame
pygame.init()
from Baki import Baki
from Garou import Garou

# Pantalla
Ancho_pantalla = 1000
Alto_pantalla = 650

evento = "inicio"
idioma = "español"

#saber si es el p1 o el p2
garou = "null"
baki = "null"

#Pantalla
SCREEN = pygame.display.set_mode((Ancho_pantalla, Alto_pantalla))
pygame.display.set_caption('Mortal cumbia')


#FPS
reloj = pygame.time.Clock()
FPS = 23

# ---------------------------------------------------------------------------------
#pista predeterminada
pista = True

#Musica
def Musica(pista):
    #reproduce
    if pista:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("pistas/undertale.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1, 0.0, 5000)
    #detiene
    else:
        pygame.mixer.music.stop()

Musica(pista)
#Pantalla principal
def Inicio():

    fondo = pygame.image.load("Imagenes/Inicio/Fondo.png").convert_alpha()
    fondo = pygame.transform.scale(fondo, (Ancho_pantalla, Alto_pantalla))
    SCREEN.blit(fondo, (0, 0))


    if idioma == "español":
        jugar = pygame.image.load("Imagenes/Inicio/Botones/Jugar.png").convert_alpha()
        menu = pygame.image.load("Imagenes/Inicio/Botones/Menu.png").convert_alpha()
        salir = pygame.image.load("Imagenes/Inicio/Botones/Salir.png")
    elif idioma == "ingles":
        jugar = pygame.image.load("Imagenes/Inicio/Botones/Ingles/Play.png")
        menu = pygame.image.load("Imagenes/Inicio/Botones/Ingles/Menu.png")
        salir = pygame.image.load("Imagenes/Inicio/Botones/Ingles/Exit.png")

    jugar = pygame.transform.scale(jugar, (300, 300))
    SCREEN.blit(jugar, (320, 240))

    menu = pygame.transform.scale(menu, (300, 300))
    SCREEN.blit(menu, (320, 300))

    salir = pygame.transform.scale(salir, (300, 300))
    SCREEN.blit(salir, (320, 360))



def Menu():

    fondo_menu = pygame.image.load("Imagenes/Menu/Fondo_menu.png")
    fondo_menu = pygame.transform.scale(fondo_menu, (Ancho_pantalla, Alto_pantalla))
    SCREEN.blit(fondo_menu, (0, 0))

    idioma = pygame.image.load("Imagenes/Menu/Botones/Idioma.png")
    idioma = pygame.transform.scale(idioma, (300, 300))
    SCREEN.blit(idioma, (320, 160))

    if pista:
        musica = pygame.image.load("Imagenes/Menu/Botones/Musica.png")
        musica = pygame.transform.scale(musica, (300, 300))
        SCREEN.blit(musica, (320, 240))
    else:
        musica_desactivado = pygame.image.load("Imagenes/Menu/Botones/Musica_desactivado.png")
        musica_desactivado = pygame.transform.scale(musica_desactivado, (300, 300))
        SCREEN.blit(musica_desactivado, (320, 240))


def Escenario():
    fondo_Esecenario = pygame.image.load("Imagenes/Escenario/fondo_invierno.png")
    fondo_Esecenario = pygame.transform.scale(fondo_Esecenario, (Ancho_pantalla, Alto_pantalla))
    SCREEN.blit(fondo_Esecenario, (0,0))

    # movimiento de los personajes
    Personaje_1.move(Ancho_pantalla, Alto_pantalla, SCREEN, Personaje_2)
    Personaje_2.move(Ancho_pantalla, Alto_pantalla, SCREEN, Personaje_1)

    # mostrar los personajes
    Personaje_1.draw(SCREEN)
    Personaje_2.draw(SCREEN)

    # Mostrar vida
    Personaje_1.barras_de_vida(SCREEN)
    Personaje_2.barras_de_vida(SCREEN)

def Select_personaje():

    fondo_jugar = pygame.image.load("Imagenes/Seleccion/Fondo.gif")
    fondo_jugar = pygame.transform.scale(fondo_jugar, (Ancho_pantalla, Alto_pantalla))
    SCREEN.blit(fondo_jugar, (0, 0))

    if idioma == "español":
        volver = pygame.image.load("Imagenes/Seleccion/Botones/Volver.png")
        volver = pygame.transform.scale(volver, (400, 400))
        SCREEN.blit(volver, (0, 350))

        jugar = pygame.image.load("Imagenes/Seleccion/Botones/Jugar.png")
        jugar = pygame.transform.scale(jugar, (400, 400))
        SCREEN.blit(jugar, (600, 350))

    else:
        back = pygame.image.load("Imagenes/Seleccion/Botones/ingles/Back.png")
        back = pygame.transform.scale(back, (400, 400))
        SCREEN.blit(back, (0, 350))

        play = pygame.image.load("Imagenes/Seleccion/Botones/ingles/Play.png")
        play = pygame.transform.scale(play, (400, 400))
        SCREEN.blit(play, (600, 350))



    if garou == "null":

        boton_garou = pygame.image.load("Imagenes/Seleccion/Botones/boton_garou.png")
        boton_garou = pygame.transform.scale(boton_garou, (380, 360))
        SCREEN.blit(boton_garou, (230, 100))
    elif garou != "null":

        boton_garou_bloqueado = pygame.image.load("Imagenes/Seleccion/Botones/Garou X.png")
        boton_garou_bloqueado = pygame.transform.scale(boton_garou_bloqueado, (380, 360))
        SCREEN.blit(boton_garou_bloqueado, (230, 100))

    if baki == "null":

        boton_baki = pygame.image.load("Imagenes/Seleccion/Botones/boton_baki.png")
        boton_baki = pygame.transform.scale(boton_baki, (300, 300))
        SCREEN.blit(boton_baki, (390, 130))
    elif baki != "null":

        boton_baki_bloqueado = pygame.image.load("Imagenes/Seleccion/Botones/Baki X.png")
        boton_baki_bloqueado = pygame.transform.scale(boton_baki_bloqueado, (300, 300))
        SCREEN.blit(boton_baki_bloqueado, (390, 130))


    pygame.display.update()

def Select_idioma():

    fondo_menu = pygame.image.load("Imagenes/Menu/Fondo_menu.png")
    fondo_menu = pygame.transform.scale(fondo_menu, (Ancho_pantalla, Alto_pantalla))
    SCREEN.blit(fondo_menu, (0, 0))

    spanish = pygame.image.load("Imagenes/Menu/Botones/Ingles/Español.png")
    spanish = pygame.transform.scale(spanish, (300, 300))
    SCREEN.blit(spanish, (320, 160))

    english = pygame.image.load("Imagenes/Menu/Botones/Ingles/English.png")
    english = pygame.transform.scale(english, (300, 300))
    SCREEN.blit(english, (320, 240))

#Botones inicio
boton_jugar = pygame.Rect(385, 350, 165, 50)
boton_menu = pygame.Rect(385,410, 165, 50)
boton_salir = pygame.Rect(385, 470, 165, 50)

#botones menu
boton_idioma = pygame.Rect(385, 270, 165, 50)
boton_musica = pygame.Rect(385, 350, 165, 50)

#Botones seleccion idioma
boton_Español = pygame.Rect(385, 270, 165, 50)
boton_Ingles = pygame.Rect(385, 365, 165, 50)

#Botones seleccion personaje
boton_garou = pygame.Rect(387, 250, 67, 60)
boton_baki = pygame.Rect(505, 250, 70, 60)

boton_volver = pygame.Rect(118, 530, 152, 31)
boton_pelear = pygame.Rect(718, 533, 152, 31)



#Posiciones (x, y) personajes
Personaje_1 = Garou(200, 310)
Personaje_2 = Baki(700, 310)



#ciclo ejecucion juego
ejecuta = True
while ejecuta:

    reloj.tick(FPS)

    #Actualizar pantallas
    if evento == "inicio":
        Inicio()
    elif evento == "menu":
        Menu()
    elif evento == "escenario":
        Escenario()
    elif evento == "select_p":
        Select_personaje()


    # ciclo ejecucion ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                #Interfaz de Inicio
                if evento == "inicio":

                    if boton_jugar.collidepoint(event.pos):
                        evento = "select_p"
                        Select_personaje()

                    elif boton_menu.collidepoint(event.pos):
                        evento = "menu"
                        Menu()

                    elif boton_salir.collidepoint(event.pos):
                        ejecuta = False
                #Interfaz de Menu
                elif evento == "menu":

                    if boton_idioma.collidepoint(event.pos):
                        evento = "Select_idioma"
                        Select_idioma()

                    elif boton_musica.collidepoint(event.pos):
                        if pista:
                            pista = False
                        else:
                            pista = True
                #Interfaz seleccion idioma
                elif evento == "Select_idioma":

                    if boton_Ingles.collidepoint(event.pos):
                        idioma = "ingles"
                        evento = "inicio"
                        Inicio()

                    elif boton_Español.collidepoint(event.pos):
                        idioma = "español"
                        evento = "inicio"
                        Inicio()
                #Interfaz seleccion de personaje
                elif evento == "select_p":

                    if boton_garou.collidepoint(event.pos):
                        if garou == "null" and baki == "null":
                            garou = "p1"
                        elif garou == "null" and baki != "null":
                            garou = "p2"

                    elif boton_baki.collidepoint(event.pos):
                        if baki == "null" and garou == "null":
                            baki = "p1"
                        elif baki == "null" and garou != "null":
                            baki = "p2"

                    elif boton_volver.collidepoint(event.pos):
                        evento = "inicio"
                        Inicio()

                    elif boton_pelear.collidepoint(event.pos):
                        evento = "escenario"
                        Escenario()

    Musica(pista)
    #actualizar pantalla
    pygame.display.update()

pygame.mixer.music.stop()
pygame.quit()