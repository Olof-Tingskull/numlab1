import numpy as np
from src.euler_iterations import euler_iterations, time_step
from src.plot import plot

v_max = 25
d = 75
k = time_step * v_max / d

def f(x):
    return min(max(x / d, 0), 1) * 25

def fixed_backward_euler(current_pos, front_pos, front_new_pos, iterations=1000, tolerans=10^-10):
    diff = abs(current_pos - (current_pos + time_step * f(front_new_pos - current_pos)))
    x = current_pos

    i = 0
    while (diff > tolerans and i < iterations):
        x = current_pos + time_step * f(front_new_pos - x)
        i += 1

        diff = abs(x - (current_pos + time_step * f(front_new_pos - x)))

    return x


def explicit_backward_euler(current_pos, front_pos, front_new_pos):
    return current_pos + k * min((front_new_pos - current_pos)/(1+k), d)


def run():
    (time_axis, graphs) = euler_iterations(explicit_backward_euler)

    plot(time_axis, graphs)
