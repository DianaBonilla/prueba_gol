import pygame
from pygame.locals import*
pygame.init()
v = pygame.display.set_mode((1500,700)) ## crea la ventana
arco = pygame.image.load("arco.jpg") ## la imagen
balon = pygame.image.load("balon.jpg")
posXbalon = 950 # posicion inicial del balon en x
posYbalon = 150 # posicion inicial del balon en y
posXarco = 100  # posicion del arco en x
posYarco = 100  # posicion del arco y
posXbalon1 = posXbalon
movimiento = 30 ## "velocidad a la que se mueve"
Blanco = (253,254,254) ## color de fondo
##derecha=True
while True:
    v.fill(Blanco)
    v.blit(arco,(posXarco,posYarco))
    v.blit(balon,(posXbalon,posYbalon))   
    for event in pygame.event.get():
          if event.type == pygame.KEYDOWN: ## movimientos con las flechas
              if event.key == K_LEFT: ## movimiento a la izquierda
                  posXbalon -= movimiento
                  posXbalon1 = posXbalon
                  print(posXbalon1 + posYbalon)
              elif event.key == K_RIGHT:  ## movimiento a la derecha
                  posXbalon += movimiento
                  posXbalon1 = posXbalon
                  print(posXbalon1,posYbalon) 
          if posXbalon1 and posYbalon == posXarco and posYarco:
              print("gol")
          pygame.display.update()
