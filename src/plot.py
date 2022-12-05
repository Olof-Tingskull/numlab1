import numpy as np
import matplotlib.pyplot as plt

def plot(horizontal, graphs):
    fig, ax = plt.subplots()

    for graph in graphs:
        ax.plot(horizontal, graph, linewidth=2.0)

    ax.set(xlim=(0, np.max(horizontal)),  ylim=(0, np.max(graphs)))

    plt.show()