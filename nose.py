import pygame
#Para el desplasamiento del fondo

#shift de fondo
shift = 0
#velocidad de fondo actual
speed = 0
background_picture = "image.jpg"
win_windth = 700
win_height = 500
window = (win_windth, win_height)

#Procesamiento de eventos
for event in pygame.event.get():
  if event.type == pygame.QUIT:
    run = False
  #flecha presionada
  if event.type == pygame.KEYDOWN:
    shift += speed
    local_shift = shift % win_windth
    #Dibujar el fondo a la derecha del shift
    window.blit(background_picture, (local_shift, 0))
    #Dibujar el fondo a la izquierda del shift
    if local_shift != 0:
      window.blit(background_picture, (local_shift, 0))
    if event.key == pygame.K_LEFT:
      speed = -5
    elif event.key == pygame.K_RIGHT:
      speed = 5
  #flecha liberada
  elif event.type == pygame.KEYUP:
    if event.key == pygame.K_LEFT:
      speed = 0
    elif event.key == pygame.K_RIGHT:
      speed = 0
