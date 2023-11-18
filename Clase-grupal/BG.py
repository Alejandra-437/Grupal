import pygame
from pygame import *
"""
import sys
import math
import random

import os
"""





mainClock = pygame.time.Clock()
pygame.init()
main = pygame.display.set_mode((900, 600), pygame.SCALED + pygame.RESIZABLE)
pygame.display.set_caption("Burrow Game")
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()


idle_images = [transform.scale(image.load("assets/player/idle/idle_0.png"), (76, 75)),
               transform.scale(image.load("assets/player/idle/idle_1.png"), (76, 75))]
move_images = [transform.scale(image.load("assets/player/move/move_1.png"), (76, 75)),
               transform.scale(image.load("assets/player/move/move_0.png"), (76, 75))]
sit_images = [transform.scale(image.load("assets/player/sit/sit_0.png"), (76, 75)),
              transform.scale(image.load("assets/player/sit/sit_1.png"), (76, 75)),
              transform.scale(image.load("assets/player/sit/sit_2.png"), (76, 75))]


current_images = idle_images  
facing_left = False
current_frame = 0        
frame_delay = 300
last_frame_time = pygame.time.get_ticks()
height = -0
width = 0
x = 360
y = 290 - height - 3
speed = 5

true = True
frame = 0  
state = "idle"  
ctrl_pressed = False 


while true:
    time.delay(30)
    main.fill((5, 18, 24))

    for key in event.get():
        if key.type == QUIT:
            true = False
        if key.type == KEYDOWN:
            if key.key == K_LEFT:
                x -= speed
                current_images = move_images
                facing_left = True  
            elif key.key == K_RIGHT:
                x += speed
                current_images = move_images
                facing_left = False  
            elif key.key == K_UP:
                y -= speed
                current_images = move_images
            elif key.key == K_DOWN:
                y += speed
                current_images = move_images
        elif key.type == KEYUP and state != "sit": 
            current_images = idle_images

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        x -= speed
        facing_left = True
        state = "move"
    if keys[K_RIGHT]:
        x += speed
        facing_left = False
        state = "move"
    if keys[K_UP]:
        y -= speed
        state = "move"
    if keys[K_DOWN]:
        y += speed
        state = "move"
    if keys[K_LCTRL]:
        ctrl_pressed = True
    else:
        ctrl_pressed = False
    if state == "idle":
        current_images = idle_images
        if ctrl_pressed:
            current_images = sit_images
            state = "sit"
    elif state == "move":
        if ctrl_pressed:
            current_images = sit_images
            state = "sit"

    if state == "sit" and not ctrl_pressed:
        current_images = [sit_images[-1]] 
        if keys[K_LCTRL]:
            state = "down"
        if keys[K_LEFT] or keys[K_RIGHT] or keys[K_UP] or keys[K_DOWN]:
            state = "move"    
    

    if frame >= len(move_images) * 10:
        frame = 0
    
    if len(current_images) > 0:
        if frame >= len(current_images) * 10:
            frame = 0
        if facing_left:
            img = transform.flip(current_images[frame // 10], True, False)
        else:
            img = current_images[frame // 10]

    frame += 1
    if frame >= 30:  
        frame = 0
        


    main.blit(img, (x, y))
    display.update()