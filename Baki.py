import pygame
import time


caminar_izq = [pygame.image.load("Imagenes/Personajes/Baki/caminar/caminar1.png"),
              pygame.image.load("Imagenes/Personajes/Baki/caminar/caminar2.png"),
              pygame.image.load("Imagenes/Personajes/Baki/caminar/caminar3.png"),
              pygame.image.load("Imagenes/Personajes/Baki/caminar/caminar4.png"),
              pygame.image.load("Imagenes/Personajes/Baki/caminar/caminar5.png"),
              pygame.image.load("Imagenes/Personajes/Baki/caminar/caminar6.png"),
              pygame.image.load("Imagenes/Personajes/Baki/caminar/caminar7.png"),
              pygame.image.load("Imagenes/Personajes/Baki/caminar/caminar8.png")]
caminar_derecha = [pygame.transform.flip(imagen, True, False) for imagen in caminar_izq]
quieto = [pygame.image.load("Imagenes/Personajes/Baki/quieto/quieto1.png"),
          pygame.image.load("Imagenes/Personajes/Baki/quieto/quieto2.png"),
          pygame.image.load("Imagenes/Personajes/Baki/quieto/quieto3.png"),
          pygame.image.load("Imagenes/Personajes/Baki/quieto/quieto4.png"),
          pygame.image.load("Imagenes/Personajes/Baki/quieto/quieto5.png"),
          pygame.image.load("Imagenes/Personajes/Baki/quieto/quieto6.png")]
quieto_izq = [pygame.transform.flip(imagen, True, False)for imagen in quieto]
saltar = [pygame.image.load("Imagenes/Personajes/Baki/saltar/saltar1.png")]
saltar_izq = [pygame.transform.flip(imagen, True, False)for imagen in saltar]
ataque_basico = [pygame.image.load("Imagenes/Personajes/Baki/ataque_basico/ataque1.png"),
                 pygame.image.load("Imagenes/Personajes/Baki/ataque_basico/ataque2.png"),
                 pygame.image.load("Imagenes/Personajes/Baki/ataque_basico/ataque3.png"),
                 pygame.image.load("Imagenes/Personajes/Baki/ataque_basico/ataque4.png")]
ataque_basico_izq = [pygame.transform.flip(imagen, True, False)for imagen in ataque_basico]
ataque_sec = [pygame.image.load("Imagenes/Personajes/Baki/ataque_sec/ataque1.png"),
              pygame.image.load("Imagenes/Personajes/Baki/ataque_sec/ataque2.png")]
ataque_sec_izq = [pygame.transform.flip(imagen, True, False)for imagen in ataque_sec]
barras_baki = [pygame.image.load('Imagenes/Personajes/Baki/barras/vida1.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida2.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida3.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida4.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida5.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida6.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida7.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida8.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida9.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida10.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida11.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida12.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida13.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida14.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida15.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida16.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida17.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida18.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida19.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida20.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida21.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida22.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida23.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida24.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida25.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida26.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida27.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida28.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida29.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida30.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida31.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida32.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida33.png'),
                pygame.image.load('Imagenes/Personajes/Baki/barras/vida34.png')]
barras_baki_izq = [pygame.transform.flip(imagen, True, False)for imagen in barras_baki]

#cambiar tamaño de los sprites
nuevo_ancho = 125
nuevo_alto = 175

quieto = [pygame.transform.scale(img, (nuevo_ancho, nuevo_alto)) for img in quieto]
quieto_izq = [pygame.transform.scale(img, (nuevo_ancho, nuevo_alto)) for img in quieto_izq]
caminar_derecha = [pygame.transform.scale(img, (nuevo_ancho, nuevo_alto)) for img in caminar_derecha]
caminar_izq = [pygame.transform.scale(img, (nuevo_ancho, nuevo_alto)) for img in caminar_izq]
saltar = [pygame.transform.scale(img, (nuevo_ancho, nuevo_alto)) for img in saltar]
saltar_izq = [pygame.transform.scale(img, (nuevo_ancho, nuevo_alto)) for img in saltar_izq]
ataque_basico = [pygame.transform.scale(img, (nuevo_ancho, nuevo_alto)) for img in ataque_basico]
ataque_basico_izq = [pygame.transform.scale(img, (nuevo_ancho, nuevo_alto)) for img in ataque_basico_izq]
ataque_sec = [pygame.transform.scale(img, (nuevo_ancho, nuevo_alto)) for img in ataque_sec]
ataque_sec_izq = [pygame.transform.scale(img, (nuevo_ancho, nuevo_alto)) for img in ataque_sec_izq]
barras_baki = [pygame.transform.scale(img, (nuevo_ancho, nuevo_alto)) for img in barras_baki]
barras_baki_izq = [pygame.transform.scale(img, (nuevo_ancho, nuevo_alto)) for img in barras_baki_izq]
class Baki():
    def __init__(self, x, y):
        self.flip = False
        self.image_index = 0  # permite que el índice de la lista no se salga de los límites
        self.image = quieto[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y + 100)
        self.vel_y = 0
        self.attacking = False
        self.attack_type = 0
        self.health = 102
        self.stop = True
        self.moving = False
        self.moving_left = False
        self.jump = False
        self.jump_right = False
        self.jump_left = False
        self.cooldown = 0
        self.enfriamiento = False
        self.indice = 0
        self.barras_p1 = barras_baki
        self.barras_p2 = barras_baki_izq
        self.last_move = "derecha"
        self.animation_speed = {
            'caminar_derecha': 20,
            'caminar_izquierda': 20,
            'ataque_basico': 50,
            'ataque_sec': 120,
            'quieto': 50,
        }
        self.current_animation = 'quieto'

        # Movimiento del personaje
    def move(self, Ancho_pantalla, Alto_pantalla, surface, target):
         Speed = 20
         gravedad = 10
         dx = 0
         dy = 0

         if self.attacking == False:
            # Controles
            key = pygame.key.get_pressed()
            # izquierda
            if key[pygame.K_LEFT]:
                dx = -Speed
                self.moving = False
                self.moving_left = True
                self.last_move = "izquierda"
                self.current_animation = 'caminar_izquierda'
                if self.jump and self.moving_left:
                    self.jump_left = True
                    self.moving_left = True
            # derecha
            elif key[pygame.K_RIGHT]:
                dx = Speed
                self.moving_left = False
                self.moving = True
                self.last_move = "derecha"
                self.current_animation = 'caminar_derecha'
                if self.jump and self.moving:
                    self.jump_right = True
                    self.moving = True
            # salto
            elif key[pygame.K_UP] and self.jump == False:
                self.vel_y = -60
                self.moving = False
                self.moving_left = False
                self.stop = False
                self.jump = True
            # quieto
            else:
                self.moving = False
                self.moving_left = False
                self.current_animation = 'quieto'

            # gravedad
            self.vel_y += gravedad
            dy += self.vel_y

            # Ataques
            if key[pygame.K_KP1] or key[pygame.K_KP2]:
                self.attack(surface, target)
                # Saber qué ataque se usó
                if key[pygame.K_KP1]:
                    self.attack_type = 1
                    self.attacking = True
                    self.current_animation = 'ataque_basico'
                # ataque 2
                if key[pygame.K_KP2]:
                    self.attack_type = 2
                    self.attacking = True
                    self.current_animation = 'ataque_sec'

        # hacer que el personaje se mantenga en la pantalla
         if self.rect.left + dx < 0:
            dx = -self.rect.left
         if self.rect.right + dx > Ancho_pantalla:
            dx = Ancho_pantalla - self.rect.right

         if self.last_move == "izquierda":
             self.flip = True
         else:
             self.flip = False

         # Requisitos para el salto
         if self.rect.bottom + dy > Alto_pantalla - 47:
            self.vel_y = 0
            self.jump = False
            dy = Alto_pantalla - 47 - self.rect.bottom

         self.rect.x += dx
         self.rect.y += dy

         animation_speed = self.animation_speed[self.current_animation]

         # Animacion a la derecha
         if self.moving and self.jump == False:
             self.image_index = (self.image_index + 1) % len(caminar_derecha)
             self.image = caminar_derecha[self.image_index]
         # Animacion salto a la derecha
         elif self.moving and self.jump:
             self.image_index = (self.image_index) % len(saltar)
             self.image = saltar[self.image_index]
         # Animacion a la izquierda
         elif self.moving_left and self.jump == False:
             self.image_index = (self.image_index + 1) % len(caminar_izq)
             self.image = caminar_izq[self.image_index]
         # Animacion salto a la izquierda
         elif self.moving_left and self.jump:
             self.image_index = (self.image_index) % len(saltar_izq)
             self.image = saltar_izq[self.image_index]
         # Animacion al saltar
         elif self.jump:
             self.image_index = (self.image_index) % len(saltar)
             self.image = saltar[self.image_index]
         # Animacion ataque
         elif self.attacking:
             self.moving = False
             self.moving_left = False
             self.stop = False
             self.jump = False
             # ataque basico
             if self.attack_type == 1:
                 if self.last_move == "derecha":
                     self.image_index = (self.image_index + 1) % len(ataque_basico)
                     self.image = ataque_basico[self.image_index]
                 else:
                     self.image_index = (self.image_index + 1) % len(ataque_basico_izq)
                     self.image = ataque_basico_izq[self.image_index]
                 self.attacking = False
                 self.stop = True
             # Ataque secundario
             else:
                 if self.last_move == "derecha":
                     self.image_index = (self.image_index + 1) % len(ataque_sec)
                     self.image = ataque_sec[self.image_index]
                 else:
                     self.image_index = (self.image_index + 1) % len(ataque_sec_izq)
                     self.image = ataque_sec_izq[self.image_index]
                 self.attacking = False
                 self.stop = True
         # Animacion al estar quieto
         else:
             if self.last_move == "derecha":
                 self.image_index = (self.image_index + 1) % len(quieto)
                 self.image = quieto[self.image_index]
             else:
                 self.image_index = (self.image_index + 1) % len(quieto_izq)
                 self.image = quieto_izq[self.image_index]

         pygame.time.delay(animation_speed)

    def barras_de_vida(self, SCREEN):
        vida = pygame.transform.scale(self.barras_p2[self.indice], (507, 450))  # evitar error al acabar la vida
        SCREEN.blit(vida, (500, 15))

    # Restar vida al enemigo al acertar un golpe
    def attack(self, surface, target):
        if self.last_move == "derecha":
            attacking_rect = pygame.Rect(self.rect.right - 0.5 * self.rect.width, self.rect.top + self.rect.height * 0.2, 0.5 * self.rect.width, 0.3 * self.rect.height)
        else:
            attacking_rect = pygame.Rect(self.rect.left + 0 * self.rect.width, self.rect.top + self.rect.height * 0.2, 0.5 * self.rect.width, 0.3 * self.rect.height)

        if attacking_rect.colliderect(target.rect):
            tiempo = time.time()
            if tiempo - self.cooldown >= 1:
                target.health -= 3
                self.cooldown = tiempo

        pygame.draw.rect(surface, (250, 75, 255), attacking_rect)

    # Dibuja el personaje
    def draw(self, surface):
        surface.blit(self.image, self.rect)

baki = Baki(100, 200)
