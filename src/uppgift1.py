import matplotlib.pyplot as plt
import numpy as np

def f(x):    
    return min(max(x / 75, 0), 1) * 25

def run():
    x = np.array([-25, 0, 75, 100])

    y = np.vectorize(f)(x)

    fig, ax = plt.subplots()

    ax.plot(x, y, linewidth=2.0)

    ax.set(xlim=(-25, 100),  ylim=(-10, 50))

    plt.show()
