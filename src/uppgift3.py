import sys
import pygame
import numpy as np
from src.euler_iterations import euler_iterations
from src.uppgift2 import iteration_function

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


time_multiplier = 5

def run():
    (time_axis, graphs) = euler_iterations(iteration_function)

    window_width, window_height = 800, 600
    pygame.init()
    window = pygame.display.set_mode((window_width, window_height))

    current_index = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        time = pygame.time.get_ticks() * float(time_multiplier) / 1000

        for i in range(current_index, len(time_axis)):
            if time_axis[i] > time: break
            current_index = i

        window.fill(BLACK)

        pygame.draw.rect(window, WHITE, (0, window_height - 200, window_width, 200))

        for points in graphs:
            x = points[current_index]
            pygame.draw.circle(window, WHITE, (x, window_height - 200), 10)

        pygame.display.update()







