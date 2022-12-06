import matplotlib.pyplot as plt 
import numpy as np 
from src.uppgift7 import explicit_backward_euler, fixed_backward_euler
from src.euler_iterations import euler_iterations
from src.plot import plot

min_iter = 1
max_iter = 20

def run(): 
    (_, explicit_cars) = euler_iterations(explicit_backward_euler)

    explicit_last_pos = np.ones(max_iter - min_iter + 1, dtype=np.float128) * explicit_cars[0][-1]
    iterations = np.arange(min_iter, max_iter + 1)
    fixed_last_post = np.zeros(max_iter - min_iter + 1, dtype=np.float128)

    for i in iterations: 
        (_, fixed_cars) = euler_iterations(lambda car, front, front_new: fixed_backward_euler(car, front, front_new, i, 0))
        fixed_last_post[i - min_iter] = fixed_cars[0][-1] 
        print(str(int((i**2 - min_iter**2) / (max_iter**2 - min_iter**2) * 1000)/10) + "%")

    log_errors = np.log(np.absolute(fixed_last_post - explicit_last_pos))
    
    plot(iterations, [log_errors])





















































