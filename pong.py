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

    clock = pygame.time.Clock()
    started = False

    # Loop
    while True:
        screen.fill(COLOR_BLACK)

        if not started:
            font = pygame.font.SysFont('Consolas', 30)

            text = font.render('Press Space to Start', True, COLOR_WHITE)
            text_rect = text.get_rect() 
            text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            screen.blit(text, text_rect)

            pygame.display.flip()

            clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    started = True
        
        if ball_rect.left <= 0 or ball_rect.left >= SCREEN_WIDTH:
            return

        pygame.draw.rect(screen, COLOR_PURPLE, paddle_1_rect)
        pygame.draw.rect(screen, COLOR_PURPLE, paddle_2_rect)
        pygame.draw.rect(screen, COLOR_WHITE, ball_rect)

        pygame.display.update()

        delts_time = clock.tick(60)

if __name__ == '__main__':
    main()
 

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

COLOR_BLACK = (0, 0, 0)
COLOR_PURPLE = (96, 73, 100)
COLOR_WHITE = (100, 98, 94)