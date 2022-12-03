import sys
import pygame
import numpy as np
import src.uppgift2 as u2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def run(initial_distance, lead_car_velocity, time_multiplier = 1):
    (time_axis, graphs) = u2.calculate_positions(initial_distance, lead_car_velocity)

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

        pygame.draw.rect(window, WHITE, (0, 400, 800, 200))

        for points in graphs:
            x = points[current_index]
            pygame.draw.circle(window, WHITE, (x, 400), 10)

        pygame.display.update()







