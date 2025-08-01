import pygame
import random

def main():
    #Setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Pong')

    #PADDLES
    paddle_1_rect = pygame.Rect(30, 0, 7, 100)
    paddle_2_rect = pygame.Rect(SCREEN_WIDTH - 50, 0, 7, 100)

    paddle_1_move = 0
    paddle_2_move = 0

    #BALL
    ball_rect = ptgame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 25, 25)

    ball_accel_x = random.randint(2, 4) * 0.1
    ball_accel_x = random.randint(2, 4) * 0.1

    if random.randint(1, 2) == 1:
        ball_accel_x *= -1
    elif random.randint(1, 2) ==1:
        ball_accel_y *= -1

    # Loop
    while True:
        screen.fill(COLOR_BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.draw.rect(screen, COLOR_PURPLE, paddle_1_rect)
        pygame.draw.rect(screen, COLOR_PURPLE, paddle_2_rect)
        pygame.draw.rect(screen, COLOR_PURPLE, ball_rect)

        pygame.display.update()

if __name__ == '__main__':
    main()
 

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

COLOR_BLACK = (0, 0, 0)
COLOR_PURPLE = (96, 73, 100)