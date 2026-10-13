
#imports
import pygame
import random, time
import math as maths

#-----

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

running = True
delta = 0

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  screen.fill("white")
  #render
  pygame.display.flip()
  delta = clock.tick(60) / 1000
