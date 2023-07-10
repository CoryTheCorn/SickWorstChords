import pygame, sys
from pygame.locals import *

#1.
pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)

#2.
clock = pygame.time.Clock()

color = (3, 86, 252)

#3.
def main():
  while True:
    clock.tick(60)
    

    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
        
    pygame.display.flip()
    screen.fill(color)

if __name__ == '__main__':
    main()