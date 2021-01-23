import pygame
import sys
from ctypes  import *

def game():
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                pygame.draw.circle(screen, (0, 0, 255), event.pos, 5)
        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    pygame.init()
    size = width, height = windll.user32.GetSystemMetrics(0), windll.user32.GetSystemMetrics(1) - 40
    screen = pygame.display.set_mode(size)
    clock, fps = pygame.time.Clock(), 30
    game()