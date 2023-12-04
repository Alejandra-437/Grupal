from typing import Any
import pygame
import random
from random import *
from pygame import *
from pygame.sprite import _Group


idle_images = [transform.scale(image.load("a/assets/player/idle/idle_0.png"), (76, 75)),
               transform.scale(image.load("a/assets/player/idle/idle_1.png"), (76, 75))]
move_images = [transform.scale(image.load("a/assets/player/move/move_1.png"), (76, 75)),
               transform.scale(image.load("a/assets/player/move/move_0.png"), (76, 75))]
sit_images = [transform.scale(image.load("a/assets/player/sit/sit_0.png"), (76, 75)),
              transform.scale(image.load("a/assets/player/sit/sit_1.png"), (76, 75)),
              transform.scale(image.load("a/assets/player/sit/sit_2.png"), (76, 75))]
class Superior(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        sprite.Sprite.__init__(self)
    
        self.image = player_image
        self.speed = player_speed
        self.rect.x = player_x
        self.rect.y = player_y
        
        
    def reset(self):
       window.blit(self.image,(self.rect.x, self.rect.y))

class Player(Superior):
    def __init__(self, player_image, player_x, player_y, player_speed):
        sprite.Sprite.__init__(player_image, player_x, player_y, player_speed)
        self.gravity = 9.8
        self.jump = 12
        self.jumping = False
        self.jumps_left = 2
        self.bullets_left = []
        self.player_image =  idle_images  
        self.facing_left = False
        self.current_frame = 0        
        self.frame_delay= 300
        self.x = 360
        self.y = 290 - window_height - 3
        self.speed = 5
        self.frame = 0  
        self.state = "idle"  
        self.ctrl_pressed = False 
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < window_width -80:
            self.rect.x += self.speed
#Restablecer el numero de saltos disponibles cuando toque el suelo.
        if self.rect.y  >= window_height -80:
            self.jumps_left = 2
        
        if self.jumps_left >0: #Permitir saltar si quedan saltos disponibles
            
            if  keys[K_SPACE]:
                self.jumping = True 
                #Si tocamos el espacio entonces el self.jumping va a ser el poder de nuestro salto.
                self.jump = 12
                self.jumps_left -= 1
        if self.jumping:
            self.rect.y -= self.jump
            self.jump -= self.gravity
        if self.rect.y >= window_height - 80:
            self.jumping = False
            self.rect.y = window_height - 80
        
        if keys[K_SPACE]:
            self.jumping = True
            self.jump_power = 10
            self.jumps_left -= 1

        if keys[K_LSHIFT]:  # Detectar si se presiona la tecla SHIFT izquierda para disparar
            self.shoot()
        
        #Actualizacion de proyectiles
        for bullet in self.bullets_left: 
            bullet.update()
        #click para tirotear
        #ctrl o c para agacharse
        #shift para correr
    def shoot(self):
        #Creando el objeto bala
        bullet = Bullet(self.rect.centerx, self.rect.centery)
        self.bullets_left.append(bullet)

        #el personaje va a ser mauricio, el va a ser la skin, skin desbloquiable de soyapaneco
        #el nivel oculto va a ser la casa de mauricio
        #la curacion son panes mataniños
        #La princesa va a ser la miss
        #Los enemigos van a ser los migueles
class Enemy(Superior):
    def __init__(self, platforms, player, *groups):
        super().__init__(*groups)
        self.platforms = platforms #creacion de plataformas
        self.player = player 
        self.rect.x = randint(0, window_width - 80)
        self.rect.y = 0
        self.speed = 2

    def update(self):
        self.rect.y += window_height
        self.check_collissions()

        # Desaparece si alcanza el borde de la pantalla
        if self.rect.y > window_height:
            self.rect.x = randint(0, window_width - 80)
            self.rect.y = 0
            global lost
            lost = lost + 1
    
    def check_collissions():
        #como hago para que el enemigo colisione con el jugador
        #plataformas
        pass
    
class Bullet(sprite.Sprite):
    def __init__(self, x, y) :
        super().__init__(self)
        self.speed = 20 #velocidad de la bala
        self.image = Surface((15,15))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
    def update(self):
        self.rect.x += self.speed

        #Eliminar la bala si esta sale de la pantalla
        if self.rect.right > window_width:
            self.kill()

class Platform(sprite.Sprite):
    def _init_(self, x, y, width, height, is_movable=False, move_speed=0):
        super()._init_()
        self.is_movable= is_movable
        self.move_speed = move_speed
        self.image = Surface((width, height))
        self.image.fill((40,0,80)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 1

    def update(self):
        if self.is_movable:
            self.rect.x += self.move_speed
        if self.rect.left < 600 or self.rect.right > 200 :
            self.direction *= -1


window_height = 700
window_width = 500
window = pygame.display.set_mode((window_width, window_height), pygame.SCALED + pygame.RESIZABLE)
pygame.display.set_caption("TilinShooter")

#intente hacer de tarea los objetos
enemy = sprite.Group
#investigar como poner en un grupo un objeto
for i in range(1,12):
    monster = Enemy(idle_images, randint(80, window_width -80), -40, 80,50,randint(1,5))
    #como poner en grupo un objeto
    enemy.add(monster)

mauricio = Player(idle_images, 360, 290 - window_height - 3, 5)
platforms = sprite.Group()
platforms.add(Platform(0, 600, 500, 100))
platforms.add(Platform(0, 400, 300, 100))
platforms.add(Platform(0, 200, 100, 100))

bullets_left = sprite.Group()
finish = False

run = True
while run:
    for e in event.get():
        if e.type==QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_LSHIFT:
                mauricio.shoot()
        if not finish:
            window.blit(background, (0,0))



