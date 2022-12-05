import numpy as np
from src.plot import plot

def f(x):    
    return min(max(x / 75, 0), 1) * 25

def run():
    x = np.array([-25, 0, 75, 100])
    y = np.vectorize(f)(x)

    plot(x, [y])