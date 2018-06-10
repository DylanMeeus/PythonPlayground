import pygame
import sys

WIDTH = 320 
HEIGHT = 200 

""" implement a linear feedback shift register """
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    random = 1
    fizzling = True
    while fizzling:
        y = random & 0x000FF
        x = (random & 0x1FF00) >> 8
        lsb = random & 1
        random >>= 1
        if (lsb == 0):
            random ^= 0x0012000
        if x < 320 and y < 200:
            pygame.draw.rect(screen, (255,0,0), (x,y,1,1))
        if random == 1:
            fizzling = False
        pygame.display.update()
    while True:
        pygame.display.update()





