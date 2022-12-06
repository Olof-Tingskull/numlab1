import numpy as np
from src.euler_iterations import euler_iterations, time_step
from src.plot import plot

num_cars = 10
total_time = 10

def f(x):    
    return min(max(x / 75, 0), 1) * 25

def iteration_function(current, front):
    return current + time_step * f(front - current)

def run():
    (time_axis, graphs) = euler_iterations(iteration_function)

    plot(time_axis, graphs)
