import pygame
import random

def main():
    pygame.init()
    screen = pygame.display.set_model((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Pong')

    # Loop
    while True:
        screen.fill(COLOR_BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == '__main__':
    main()
 

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

COLOR_BLACK = (0, 0, 0)
COLOR_PURPLE = (96, 73, 100)