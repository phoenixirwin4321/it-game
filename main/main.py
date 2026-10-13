
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
#-----

def render():
  pass



def turn:
  if running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
        break
    
    screen.fill("white")
    update_player_stats()
    render()
    


pygame.quit()
