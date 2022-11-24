import sys
import pygame
import numpy as np
from functions import f, g

window_width, window_height = 800, 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def game_loop(initial_positions):
    pygame.init()

    clock = pygame.time.Clock()
    window = pygame.display.set_mode((window_width, window_height))
    positions = initial_positions

    ticks = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        t = pygame.time.get_ticks()
        dt = (t-ticks) / 1000.0
        ticks = t

        distances = np.diff(positions)
        last = positions[distances.size:]
        velocities = np.concatenate((np.vectorize(f)(distances), np.vectorize(g)(last)))
        
        positions = positions + velocities * dt

        window.fill(BLACK)

        pygame.draw.rect(window, WHITE, (0, 400, 800, 200))

        for x in positions:
            pygame.draw.circle(window, WHITE, (x, 400), 10)

        clock.tick(60)
        pygame.display.update()
