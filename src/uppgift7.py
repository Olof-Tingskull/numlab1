import numpy as np
from src.euler_iterations import euler_iterations, time_step
from src.plot import plot

v_max = 25
d = 75
k = time_step * v_max / d

def f(x):
    return min(max(x / d, 0), 1) * v_max

def fixed_backward_euler(current_pos, front_pos, front_new_pos, iterations=100, tolerans=10^-10):
    calculate_error = lambda x: abs(x - (current_pos + time_step * f(front_new_pos - x)))

    x = current_pos

    for _ in range(iterations):
        if calculate_error(x) < tolerans: break

        x = current_pos + time_step * f(front_new_pos - x)

    return x


def explicit_backward_euler(current_pos, front_pos, front_new_pos):
    return current_pos + k * min((front_new_pos - current_pos) / (1 + k), d)


def run():
    (time_axis, graphs) = euler_iterations(fixed_backward_euler)

    plot(time_axis, graphs)
